"""
GUI templete 도 필요함.  230404
"""
import sys
from PySide6 import QtWidgets, QtCore, QtGui


class ExampleGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Create a graphics scene and view
        # TODO : window를 만들어준 듯
        self.scene = QtWidgets.QGraphicsScene()
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setFixedSize(400, 400)

        # Create a rectangle item on the scene
        self.rect = QtWidgets.QGraphicsRectItem(QtCore.QRectF(50, 50, 100, 100))
        self.rect.setBrush(QtGui.QBrush(QtCore.Qt.green))
        self.scene.addItem(self.rect)

        # Enable drag and drop on the rectangle item
        self.rect.setAcceptedMouseButtons(QtCore.Qt.LeftButton)
        self.rect.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)

        # Create a layout for the view
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.view)

        # Add buttons to the layout
        button_layout = QtWidgets.QHBoxLayout()
        button1 = QtWidgets.QPushButton("Button 1")
        button2 = QtWidgets.QPushButton("Button 2")
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        layout.addLayout(button_layout)

        # Connect buttons to slots
        button1.clicked.connect(self.on_button1_clicked)
        button2.clicked.connect(self.on_button2_clicked)

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

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton and self.rect.contains(event.pos()):
            self.drag_start_pos = event.pos() - self.rect.pos()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.buttons() & QtCore.Qt.LeftButton and hasattr(self, 'drag_start_pos'):
            new_pos = event.pos() - self.drag_start_pos
            self.rect.setPos(new_pos)

    def on_button1_clicked(self):
        print("Button 1 clicked")

    def on_button2_clicked(self):
        print("Button 2 clicked")


# Create an application instance and run the main event loop
app = QtWidgets.QApplication(sys.argv)
gui = ExampleGUI()
gui.show()
sys.exit(app.exec_())