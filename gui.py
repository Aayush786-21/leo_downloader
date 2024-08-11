from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QComboBox
from downloader import download_video

class LeoDownLoaderApp:
    def __init__(self):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.window.setWindowTitle("YouTube Video Downloader")
        self.window.setGeometry(300, 300, 400, 300)  # Adjusted height for additional controls

        self.url_label = QLabel("YouTube Video URL:")
        self.url_input = QLineEdit()

        self.quality_label = QLabel("Select Quality:")
        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["best", "highest", "lowest", "144p", "360p", "720p", "1080p"])

        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.start_download)  # Connect button to download method

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.quality_label)
        layout.addWidget(self.quality_combo)
        layout.addWidget(self.download_button)

        container = QWidget()
        container.setLayout(layout)
        self.window.setCentralWidget(container)

    def start_download(self):
        url = self.url_input.text()
        quality = self.quality_combo.currentText()
        if url:
            download_video(url, quality)  # Pass quality preference to download function

    def run(self):
        self.window.show()
        self.app.exec_()
