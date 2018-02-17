import sys
from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication
class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		btn1=QPushButton("Button 1",self)
		btn1.move(30,50)

		btn2=QPushButton("Button 2",self)
		btn2.move(150,50)

		#In buttonClicked() method we determine which button we have clicked by calling the sender() method
		btn1.clicked.connect(self.buttonClicked)
		btn2.clicked.connect(self.buttonClicked)
		#Both Buttons are connected to the same slot

		self.statusBar()

		self.setGeometry(300,300,290,150)
		self.setWindowTitle('Event sender')
		self.show()

		#We determine the signal source by calling the sender() method. In the statusbar of the application,
		#we show the label of the button being pressed.
	def buttonClicked(self):
		sender=self.sender()
		self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())