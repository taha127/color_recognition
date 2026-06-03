import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

import resources.resources_rc
from widgets.app_window import AppWindow


def main():
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(":icons/favicon256.ico"))
    app.setApplicationName("Color Recognition App")

    window = AppWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
