import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Practise')
window.setGeometry(100,100,400,100)
window.move(830,500)
helloMSG  = QLabel('<p style="color:red;">My name is nesh. Welcome to my brain.</p>', parent=window)
helloMSG.move(926,100)
window.show()
sys.exit(app.exec_())