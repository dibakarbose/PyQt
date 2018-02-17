import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif',10))
		#This static method sets a font used to render tooltips.We use a 10px Sanserif font

		self.setToolTip("This is a <b>QWidget</b> widget")
		#To create a tooltip, we call the setTooltip() method
		btn=QPushButton('Button',self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		#We create a Push button widget and create a tooltip for it
		btn.resize(btn.sizeHint())
		btn.move(50,50)
		#The button is being resized and moved on the window. The sizeHint() method gives a recommended size
		#for the button

		self.setGeometry(300,300,300,200)
		self.setWindowTitle('Tootips')
		self.show()

if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())