import sys
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


#Objects created from a QObject can emit signals.

class Communicate(QObject):
	closeApp=pyqtSignal()
	#We have created a new signal called closeApp. This signal is emitted during a mouse press event.The signal
	#is connected to the close() slot of the QMainWindow
	#A Signal is created with the pyqtSignal() as a class attribute of the external Communicate class
class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.c=Communicate()
		self.c.closeApp.connect(self.close)
		#The custom closeApp signal is connected to the close() slot of the QMainWindow

		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Emit Signal')
		self.show()

	def mousePressEvent(self,event):
		self.c.closeApp.emit()
		#When we click on the window with a mouse pointer, the closeApp signal is emitted. The application
		#terminates

if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())