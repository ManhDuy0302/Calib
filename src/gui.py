import cv2
import numpy as np
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QPushButton, 
                             QFileDialog, QLabel, QMessageBox)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from .calibration import CameraCalibrator
from .utils import undistort_image, process_video

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera Calibration and Undistortion")
        self.setGeometry(100, 100, 800, 600)
        self.calibrator = CameraCalibrator()
        self.params = None
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Buttons
        self.calibrate_btn = QPushButton("Calibrate Camera")
        self.calibrate_btn.clicked.connect(self.calibrate_camera)
        layout.addWidget(self.calibrate_btn)

        self.load_params_btn = QPushButton("Load Calibration Parameters")
        self.load_params_btn.clicked.connect(self.load_params)
        layout.addWidget(self.load_params_btn)

        self.load_image_btn = QPushButton("Load Image")
        self.load_image_btn.clicked.connect(self.load_image)
        layout.addWidget(self.load_image_btn)

        self.load_video_btn = QPushButton("Load Video")
        self.load_video_btn.clicked.connect(self.load_video)
        layout.addWidget(self.load_video_btn)

        # Image display
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        central_widget.setLayout(layout)

    def calibrate_camera(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Image Directory")
        if folder:
            success, message = self.calibrator.calibrate(folder)
            QMessageBox.information(self, "Calibration Result", message)
            if success:
                self.params, error = self.calibrator.load_params()
                if error:
                    QMessageBox.critical(self, "Error", error)

    def load_params(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Calibration File", "", "NPZ Files (*.npz)")
        if file:
            self.params, error = self.calibrator.load_params(file)
            if error:
                QMessageBox.critical(self, "Error", error)
            else:
                QMessageBox.information(self, "Success", "Parameters loaded successfully.")

    def load_image(self):
        if not self.params:
            QMessageBox.warning(self, "Warning", "Please load calibration parameters first.")
            return

        file, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg)")
        if file:
            img = cv2.imread(file)
            if img is None:
                QMessageBox.critical(self, "Error", "Cannot load image.")
                return

            undistorted, error = undistort_image(img, self.params)
            if error:
                QMessageBox.critical(self, "Error", error)
                return

            self.display_image(undistorted)

    def load_video(self):
        if not self.params:
            QMessageBox.warning(self, "Warning", "Please load calibration parameters first.")
            return

        file, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Videos (*.mp4 *.avi)")
        if file:
            success, error = process_video(file, self.params, self.display_image)
            if not success:
                QMessageBox.critical(self, "Error", error)

    def display_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img_rgb.shape
        bytes_per_line = ch * w
        q_img = QImage(img_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img).scaled(self.image_label.size(), Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)