import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon 


'''Here the Example class inherits from the QWidget class. This means that we call
two constructors: the first one for the Example Class and the second one for the inherited
class. The super() method returns the parent object of the Example class and we call its 
constructor '''
class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		#The creation of the GUI is delegated to the initUI() method

	def initUI(self):
		#setGeometry() located the window on the screen and sets its size.
		#First twoo parameters are x and y positions of the window.
		#The third is the width and the fourth is the height of the window.
		#Infact it combines the resize() and move() method in one method.
		self.setGeometry(300,300,300,220)
		self.setWindowTitle('Icon')
		self.setWindowIcon(QIcon('pencil.png'))
		self.show()

if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())