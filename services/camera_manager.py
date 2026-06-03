from PySide6.QtWidgets import QWidget, QGraphicsView, QGraphicsScene, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtMultimedia import QCamera, QMediaCaptureSession, QVideoSink


class CameraManager:
    def __init__(self):
        self.camera = None

    def start(self, device):
        if self.camera:
            self.camera.stop()

        self.camera = QCamera(device)
        self.camera.start()

    def get_camera(self):
        return self.camera


class CameraWidget(QWidget):
    def __init__(self, camera, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.view = QGraphicsView()
        layout.addWidget(self.view)

        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        self.pixmap_item = self.scene.addPixmap(QPixmap())

        # Multimedia
        self.session = QMediaCaptureSession()
        self.sink = QVideoSink()

        self.session.setCamera(camera)
        self.session.setVideoSink(self.sink)
        self.sink.videoFrameChanged.connect(self.update_frame)

        # state
        self.last_frame = None
        self.live_mode = True
        self.captured_pixmap = None

    # ---------- start camera ----------
    def start_camera(self, device):
        if self.camera:
            self.camera.stop()
        self.camera = QCamera(device)
        self.session.setCamera(self.camera)
        self.camera.start()

    # ---------- update frame ----------
    def update_frame(self, frame):
        if not frame.isValid() or not self.live_mode:
            return
        img = frame.toImage()
        self.last_frame = img
        pix = QPixmap.fromImage(img)
        self.pixmap_item.setPixmap(pix)
        self.scene.setSceneRect(self.pixmap_item.boundingRect())
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    # ---------- take snapshot ----------
    def take_photo(self):
        if self.last_frame is None:
            return
        self.live_mode = False
        pix = QPixmap.fromImage(self.last_frame)
        self.captured_pixmap = pix
        self.pixmap_item.setPixmap(pix)
        return pix

    # ---------- resume live ----------
    def resume_live(self):
        self.captured_pixmap = None
        self.live_mode = True
