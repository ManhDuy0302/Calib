# Dự án Hiệu chỉnh Camera với PyQt5
# Tổng quan
Dự án này là một ứng dụng hiệu chỉnh camera sử dụng OpenCV và giao diện người dùng đồ họa (GUI) được xây dựng bằng PyQt5. Ứng dụng cho phép người dùng thực hiện hiệu chỉnh camera từ các ảnh bàn cờ (chessboard), lưu tham số hiệu chỉnh, và áp dụng chúng để sửa méo ảnh hoặc video. Giao diện PyQt5 cung cấp cách tương tác dễ dàng để tải ảnh, video, và xem kết quả.
# Tính năng

Hiệu chỉnh camera:
Xử lý ảnh bàn cờ để tính ma trận nội tại, hệ số méo, và tham số tối ưu.
Lưu tham số hiệu chỉnh vào file .npz.


Sửa méo:
Áp dụng tham số hiệu chỉnh để sửa méo cho ảnh hoặc video.
Tùy chỉnh vùng quan tâm (ROI) để cắt ảnh/video sau khi sửa méo.


Giao diện người dùng (GUI):
Tải thư mục ảnh để hiệu chỉnh camera.
Tải file tham số hiệu chỉnh.
Tải và hiển thị ảnh đã sửa méo.
Tải và phát video đã sửa méo.


Tham số được lưu dưới dạng file .npz.

# Kiến thức cần thiết
OpenCV: Quen thuộc với xử lý ảnh, hiệu chỉnh camera, và các hàm như calibrateCamera, undistort.
PyQt5: Kiến thức về cách tạo ứng dụng GUI, bố cục, widget và xử lý sự kiện.
NumPy: Hiểu cách làm việc với mảng và ma trận.

Hướng dẫn cài đặt
Cài đặt các thư viện phụ thuộc:
pip install -r requirements.txt

Lệnh này sẽ cài đặt OpenCV, NumPy và PyQt5.

Chạy ứng dụng:
python main.py

Giao diện PyQt5 sẽ mở trong một cửa sổ mới.


# Hướng dẫn sử dụng

Giao diện người dùng (GUI):

Nhấn Calibrate Camera để chọn thư mục chứa ảnh bàn cờ (định dạng .jpg hoặc .png) và thực hiện hiệu chỉnh. Kết quả và lỗi tái chiếu sẽ được hiển thị.
Nhấn Load Calibration Parameters để tải file .npz chứa tham số hiệu chỉnh (ví dụ: calib_params.npz).
Nhấn Load Image để chọn một ảnh (.jpg hoặc .png) và hiển thị phiên bản đã sửa méo.
Nhấn Load Video để chọn một video (.mp4 hoặc .avi) và phát phiên bản đã sửa méo.
Kết quả (ảnh hoặc video) được hiển thị trong cửa sổ GUI.


# Lưu ý:

Cần tải tham số hiệu chỉnh trước khi xử lý ảnh hoặc video.
Đảm bảo các ảnh bàn cờ có kích thước bàn cờ đúng (mặc định: 8x6) và được chụp ở nhiều góc độ.
Video sẽ phát liên tục cho đến khi hết hoặc nhấn phím 'q' (nếu cần thoát sớm).



# Lưu ý kỹ thuật

File tham số hiệu chỉnh (calib_params.npz) được tạo tự động sau khi hiệu chỉnh thành công.
Ứng dụng sử dụng ma trận nội tại và hệ số méo từ OpenCV để sửa méo ảnh/video.
ROI được điều chỉnh thủ công trong code (mở rộng 65 pixel lên trên, 120 pixel xuống dưới, 40 pixel trái, 37 pixel phải) để đảm bảo vùng quan tâm hợp lý.


# Giấy phép
Dự án này được tạo với mục đích học tập và không được cấp phép để sử dụng trong môi trường sản xuất.
