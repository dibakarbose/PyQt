import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		#Here we create a simple Toolbar. The toolbar has one tool action, an exit action
		#which terminates the application when triggered
		exitAction=QAction(QIcon('exit.png'),'Exit',self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.triggered.connect(qApp.quit)


		#Similar to menubar example we create an action object. The object has a label icon, and
		#a shortcut. A quit() method of the QtGui.QMainWinWindow is connected to the triggered signal
		self.toolbar=self.addToolBar('Exit')
		self.toolbar.addAction(exitAction)

		self.setGeometry(300,300,300,200)
		self.setWindowTitle('Toolbar')
		self.show()

if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())