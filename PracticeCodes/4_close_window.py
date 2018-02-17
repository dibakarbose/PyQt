import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		qbtn=QPushButton('Quit',self)
		#We create a push button. The button is an instance of the QPushButton class. The first parameter
		#of the constructor is the label of the button. The second parameter is the parent widget. The parent
		#widget is the Example widget, which is QWidget by inheritance

		qbtn.clicked.connect(QCoreApplication.instance().quit)
		#The event processing system in PyQt5 is built with the signal & slot mechanism. If we click on the button, the signal
		#clicked is emitted. The slot can be a Qt slot or any Python callable. The QCoreApplication contains the main event loop;
		#it processes and dispatches all events. The instance() method gives us its current instance. Note that QCoreApplication 
		#is created with the QApplication. The clicked signal is connected to the quit() method which terminates the application.
		#The communication is done between the two objects: the sender and the receiver. The sender is the push button, the receiver 
		#is the application object.
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(50,50)

		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Quit button')
		self.show()


if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())