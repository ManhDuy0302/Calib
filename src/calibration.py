import cv2
import numpy as np
import glob
import os

class CameraCalibrator:
    def __init__(self, checkerboard=(8, 6), square_size=0.025):
        self.checkerboard = checkerboard
        self.square_size = square_size
        self.objp = np.zeros((checkerboard[0] * checkerboard[1], 3), np.float32)
        self.objp[:, :2] = np.mgrid[0:checkerboard[0], 0:checkerboard[1]].T.reshape(-1, 2) * square_size
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    def calibrate(self, image_dir):
        objpoints = []
        imgpoints = []
        images = [f for f in glob.glob(image_dir + "/*") if f.lower().endswith(('.jpg', '.png'))]

        if not images:
            return False, "Không tìm thấy ảnh trong thư mục."

        print(f"Tìm thấy {len(images)} ảnh trong thư mục.")
        for fname in images:
            img = cv2.imread(fname)
            if img is None:
                print(f"Không thể đọc ảnh: {fname}")
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(
                gray, self.checkerboard,
                flags=cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE + cv2.CALIB_CB_FAST_CHECK
            )

            if ret:
                objpoints.append(self.objp)
                corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self.criteria)
                imgpoints.append(corners2)
            else:
                print(f"Không tìm thấy góc bàn cờ trong ảnh: {fname}")

        if len(objpoints) < 10:
            return False, f"Chỉ tìm thấy {len(objpoints)} ảnh hợp lệ. Cần ít nhất 10 ảnh."

        print(f"Tìm thấy {len(objpoints)} ảnh hợp lệ.")
        print("Đang hiệu chỉnh máy ảnh...")
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
            objpoints, imgpoints, gray.shape[::-1], None, None
        )

        # Tính lỗi tái chiếu
        mean_error = 0
        for i in range(len(objpoints)):
            imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
            error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
            mean_error += error
        mean_error /= len(objpoints)
        print(f"Lỗi tái chiếu trung bình: {mean_error:.4f} pixel")

        # Tối ưu ma trận camera
        h, w = img.shape[:2]
        alpha = 1
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), alpha, (w, h))

        # Lưu tham số
        np.savez('calib_params.npz', mtx=mtx, dist=dist, newcameramtx=newcameramtx, roi=roi)
        return True, f"Hiệu chỉnh hoàn tất. Lỗi tái chiếu: {mean_error:.4f} pixel"

    def load_params(self, param_file='calib_params.npz'):
        try:
            with np.load(param_file) as data:
                params = {
                    'mtx': data['mtx'],
                    'dist': data['dist'],
                    'newcameramtx': data['newcameramtx'],
                    'roi': data['roi']
                }
                return params, None
        except Exception as e:
            return None, f"Không thể tải tham số: {str(e)}"