import cv2
import numpy as np

def undistort_image(img, params):
    if not params:
        return None, "Tham số hiệu chỉnh không hợp lệ."
    
    mtx, dist, newcameramtx, roi = params['mtx'], params['dist'], params['newcameramtx'], params['roi']
    h, w = img.shape[:2]
    
    # Sửa méo
    undistorted = cv2.undistort(img, mtx, dist, None, newcameramtx)
    
    # Cắt theo ROI với điều chỉnh
    x, y, w, h = roi
    y = max(0, y - 65)
    h = max(0, h + 120)
    x = max(0, x - 40)
    w = min(w + 2 * 37, undistorted.shape[1] - x)
    undistorted = undistorted[y:y+h, x:x+w]
    
    return undistorted, None

def process_video(video_path, params, display_callback=None):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return False, f"Không thể mở video: {video_path}"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        undistorted, error = undistort_image(frame, params)
        if error:
            cap.release()
            return False, error

        if display_callback:
            display_callback(undistorted)

    cap.release()
    return True, None