import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):
	def __init__(self):
 		super().__init__()
 		self.initUI()
	def initUI(self):

 		self.resize(250,150)

 		#The QtGui.QDesktopWidget class provides information about the user's desktop, including screen size
 		#The code that will center the windowsd is placed in the custom center() method
 		self.center()
 		self.setWindowTitle('Center')
 		self.show()

	def center(self):
		#We get a rectangle specifying the geometry of the main window. This includes any window frame.
 		qr=self.frameGeometry()
 		
 		#We figure out the screen resolution of our monitor. And from this resolution, we get the center point.
 		cp=QDesktopWidget().availableGeometry().center()

 		#Our rectangle has already its width and height. now we set the center of the rectangle to the center
 		#of the screen. The rectangle's size is unchanged
 		qr.moveCenter(cp)

 		#We move the top-left point of the application window to the top-left point of the qr Rectangle, thus
 		#centering the window on our screen.
 		self.move(qr.topLeft())

if __name__=='__main__':
 	app=QApplication(sys.argv)
 	ex=Example()
 	sys.exit(app.exec_())