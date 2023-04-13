import sys
from PySide6 import QtWidgets, QtCore, QtGui


class ExampleGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create a graphics scene and view
        self.scene = QtWidgets.QGraphicsScene()
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setFixedSize(400, 400)

        # Create a rectangle item on the scene
        self.rect = QtWidgets.QGraphicsRectItem(QtCore.QRectF(50, 50, 100, 100))
        self.rect.setBrush(QtGui.QBrush(QtCore.Qt.blue))
        self.scene.addItem(self.rect)

        # Enable drag and drop on the rectangle item
        self.rect.setAcceptedMouseButtons(QtCore.Qt.LeftButton)
        self.rect.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)

        # Create buttons
        self.button1 = QtWidgets.QPushButton("Button 1")
        self.button2 = QtWidgets.QPushButton("Button 2")

        # Create a layout for the view and buttons
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.view)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        layout.addLayout(button_layout)

        # Connect button signals to slots
        self.button1.clicked.connect(self.show_popup)

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.rect.isSelected():
            # Change the fill color of the rectangle when double clicked
            self.rect.setBrush(QtGui.QBrush(QtCore.Qt.red))

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton and self.rect.contains(event.pos()):
            self.drag_start_pos = event.pos() - self.rect.pos()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.buttons() & QtCore.Qt.LeftButton and hasattr(self, 'drag_start_pos'):
            new_pos = event.pos() - self.drag_start_pos
            self.rect.setPos(new_pos)

    def show_popup(self):
        # Create and show a message box when Button1 is clicked
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText("Button1 was clicked!")
        msg_box.exec_()


# Create an application instance and run the main event loop
app = QtWidgets.QApplication(sys.argv)
gui = ExampleGUI()
gui.show()
sys.exit(app.exec_())
