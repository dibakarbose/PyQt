import sys
from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		#Here we create a menubar with one menu. This menu will contain one action which will 
		#terminate the application if selected. A statusbar is created as well. The action is 
		#accessible with the Ctrl+Q shortcut.
		#A QAction is an abstraction for actions performed with a menubar, toolbar, or with a 
		#custom keyboard shortcut. In the above three lines, we create an action with a specific
		#icon and an 'Exit' label. Furthermore, a shortcut is defined for this action. The third
		#line creates a status tip which is shown in the statusbar when we hover a mouse pointer
		#over the menu item.
		exitAction=QAction(QIcon('exit.png'),'&Exit',self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit Application')

		#When we select this particular action, a triggered signal is emitted. The signal is 
		#connected to the quit() method of the QApplication widget. This terminates the application.
		exitAction.triggered.connect(qApp.quit)
		
		self.statusBar()

		#The menuBar() method creates a menubar. We create a file menu and append the exit action to it.
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Menubar')
		self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())