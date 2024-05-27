from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent

class TestWidget(QWidget):
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Z:
            print("Key Z pressed")
        elif event.key() == Qt.Key_Space:
            print("Space key pressed")

app = QApplication([])
window = TestWidget()
window.show()
app.exec_()
