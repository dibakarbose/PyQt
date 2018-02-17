import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Message Box')
		self.show()
	#If we close a QWidget, the QCloseEvent is generated. To modify the widget Behaviour we need to reimplement
	#the closeEvent() event handler
	def closeEvent(self,event):

	#We show a message box with two buttons: yes and no. The first string appears on the titlebar. The
	#second string is the message displayed by the dialog. the third argument specifies the combination
	#of buttons appearing in the dialog. The last parameter is the default button. it is the button which
	#has initially the keyboard focus. The return value is stored in the reply variable.
		reply=QMessageBox.question(self,'Message',"Are you sure to quit?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
		if reply==QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())