Dự án Hiệu chỉnh Camera với PyQt5
Tổng quan
Dự án này là một ứng dụng hiệu chỉnh camera sử dụng OpenCV và giao diện người dùng đồ họa (GUI) được xây dựng bằng PyQt5. Ứng dụng cho phép người dùng thực hiện hiệu chỉnh camera từ các ảnh bàn cờ (chessboard), lưu tham số hiệu chỉnh, và áp dụng chúng để sửa méo ảnh hoặc video. Giao diện PyQt5 cung cấp cách tương tác dễ dàng để tải ảnh, video, và xem kết quả.
Tính năng

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


Cơ sở dữ liệu: Không sử dụng, tham số được lưu dưới dạng file .npz.

Cấu trúc dự án
camera_calibration_project/
├── src/
│   ├── __init__.py
│   ├── calibration.py      # Xử lý hiệu chỉnh camera
│   ├── utils.py           # Các hàm tiện ích (đọc ảnh, xử lý video)
│   └── gui.py             # Giao diện PyQt5
├── main.py                # Điểm bắt đầu của ứng dụng
├── requirements.txt       # Các thư viện phụ thuộc
└── README.md              # Tài liệu hướng dẫn

Kiến thức cần thiết
Để hiểu và làm việc với dự án này, bạn cần có kiến thức cơ bản về:

Python: Hiểu cú pháp Python, hàm, lớp và module.
OpenCV: Quen thuộc với xử lý ảnh, hiệu chỉnh camera, và các hàm như calibrateCamera, undistort.
PyQt5: Kiến thức về cách tạo ứng dụng GUI, bố cục, widget và xử lý sự kiện.
NumPy: Hiểu cách làm việc với mảng và ma trận.
Môi trường ảo (Virtual Environment): Quen thuộc với việc tạo và sử dụng môi trường ảo Python để quản lý thư viện.

Hướng dẫn cài đặt

Tạo hoặc sao chép thư mục dự án:

Tạo một thư mục có tên camera_calibration_project và đặt các file dự án theo cấu trúc như trên.
Hoặc sao chép kho lưu trữ (nếu có).


Thiết lập môi trường ảo:
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate


Cài đặt các thư viện phụ thuộc:
pip install -r requirements.txt

Lệnh này sẽ cài đặt OpenCV, NumPy và PyQt5.

Chạy ứng dụng:
python main.py

Giao diện PyQt5 sẽ mở trong một cửa sổ mới.


Hướng dẫn sử dụng

Giao diện người dùng (GUI):

Nhấn Calibrate Camera để chọn thư mục chứa ảnh bàn cờ (định dạng .jpg hoặc .png) và thực hiện hiệu chỉnh. Kết quả và lỗi tái chiếu sẽ được hiển thị.
Nhấn Load Calibration Parameters để tải file .npz chứa tham số hiệu chỉnh (ví dụ: calib_params.npz).
Nhấn Load Image để chọn một ảnh (.jpg hoặc .png) và hiển thị phiên bản đã sửa méo.
Nhấn Load Video để chọn một video (.mp4 hoặc .avi) và phát phiên bản đã sửa méo.
Kết quả (ảnh hoặc video) được hiển thị trong cửa sổ GUI.


Lưu ý:

Cần tải tham số hiệu chỉnh trước khi xử lý ảnh hoặc video.
Đảm bảo các ảnh bàn cờ có kích thước bàn cờ đúng (mặc định: 8x6) và được chụp ở nhiều góc độ.
Video sẽ phát liên tục cho đến khi hết hoặc nhấn phím 'q' (nếu cần thoát sớm).



Lưu ý kỹ thuật

File tham số hiệu chỉnh (calib_params.npz) được tạo tự động sau khi hiệu chỉnh thành công.
Ứng dụng sử dụng ma trận nội tại và hệ số méo từ OpenCV để sửa méo ảnh/video.
GUI không sử dụng QThread vì xử lý video được thực hiện tuần tự và không gây tắc nghẽn giao diện.
ROI được điều chỉnh tự động (mở rộng 65 pixel lên trên, 120 pixel xuống dưới, 40 pixel trái, 37 pixel phải) để đảm bảo vùng quan tâm hợp lý.

Các cải tiến tiềm năng

Thêm QThread để xử lý video nặng hoặc hiệu chỉnh camera trong luồng riêng nếu cần.
Thêm tùy chọn điều chỉnh thủ công ma trận nội tại (fx, fy) trong GUI.
Hỗ trợ lưu video đã sửa méo thành file.
Thêm hiển thị thông tin chi tiết (ma trận nội tại, lỗi tái chiếu) trong GUI.
Tích hợp kiểm tra chất lượng ảnh bàn cờ trước khi hiệu chỉnh.

Giấy phép
Dự án này được tạo với mục đích học tập và không được cấp phép để sử dụng trong môi trường sản xuất.
