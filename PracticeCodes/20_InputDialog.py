from PyQt5.QtWidgets import (QWidget,QPushButton,QLineEdit,QInputDialog,QApplication)
import sys

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.btn=QPushButton('Dialog',self)
		self.btn.move(20,20)
		self.btn.clicked.connect(self.showDialog)

		self.le=QLineEdit(self)
		self.le.move(130,22)

		self.setGeometry(300,300,290,150)
		self.setWindowTitle('Input Dialog')
		self.show()

	def showDialog(self):

		#The below line displays the input dialog. The first string is a dialog title, the second one is a message
		#within the dialog.The dialog returns the entered text and a boolean value. If we click the OK Button,
		#the boolean value is true
		text,ok=QInputDialog.getText(self,'Input Dialog','Enter your name')
		if ok:
			self.le.setText(str(text))

		#The text that we have received from the dialog is set to the line edit widget with setText()

if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())