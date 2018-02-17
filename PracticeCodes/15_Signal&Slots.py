import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		lcd=QLCDNumber(self)
		sld=QSlider(Qt.Horizontal, self)
		vbox=QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)

		self.setLayout(vbox)

		#Here we display a QtGui.QLCDNumber and a QtGui.QSlider. We Change the lcd number by
		#dragging the slider knob.
		#Here we connect a valueChanged signal of the slider to the display slot of the lcd number
		#The sender is an object that sends a signal. The receiver is the object that receives the signal.
		#The slot is the method that reacts to the signal
		sld.valueChanged.connect(lcd.display)

		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Signal& & Slot')
		self.show()

if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())