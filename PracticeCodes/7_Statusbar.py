import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		#The statusbar is created with the help of the QMainWindow widget
		#To get the statusbar we call the statusbar() method of the QtGui.QMainWindow class. The first call of the
		#method creates a status bar. Subsequent calls return the statusbar object. The showMessage() displaysa message
		#on the statusbar
		
		self.statusBar().showMessage('Ready')
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Statusbar')
		self.show()

if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())