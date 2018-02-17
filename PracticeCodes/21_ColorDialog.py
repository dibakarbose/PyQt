from PyQt5.QtWidgets import (QWidget,QPushButton,QFrame,QColorDialog,QApplication)
from PyQt5.QtGui import QColor
import sys

#The Application example shows a push button and QFrame. The widget background is set to black
#colour. Using the QColorDialog, we can change its background

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		col=QColor(0,0,0)			#This is an initial colour of the QFrame background
		self.btn=QPushButton('Dialog',self)
		self.btn.move(20,20)

		self.btn.clicked.connect(self.showDialog)

		self.frm=QFrame(self)
		self.frm.setStyleSheet("QWidget { background-color: %s}" %col.name())
		self.frm.setGeometry(130,22,100,100)

		self.setGeometry(300,300,250,180)
		self.setWindowTitle('Color Dialog')
		self.show()

	def showDialog(self):
		col=QColorDialog.getColor()		#This line pops up the QColorDialog
		if col.isValid():
			self.frm.setStyleSheet("QWidget { background-color: %s}" %col.name())

		#We check if the colour is valid. if we click on the Cancel button, no valid colour is returned. If the 
		#colour is valid, we change the background colour using style sheets
if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())