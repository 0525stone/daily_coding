from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint

class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        # Set the mouse tracking flag to track mouse movements
        self.setMouseTracking(True)

        # Initialize the list of lines to be drawn
        self.lines = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        for line in self.lines:
            painter.drawLine(line[0], line[1])

    def mousePressEvent(self, event):
        self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        new_point = event.pos()
        self.lines.append((self.last_point, new_point))
        self.last_point = new_point
        self.update()

    def mouseReleaseEvent(self, event):
        new_point = event.pos()
        self.lines.append((self.last_point, new_point))
        self.last_point = None
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a canvas for drawing
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)

if __name__ == '__main__':
    # Create a PySide6 application instance
    app = QApplication()

    # Create a main window instance
    main_window = MainWindow()
    main_window.show()

    # Run the application
    app.exec()
