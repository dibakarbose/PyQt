import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
def window():
	app=QApplication(sys.argv)			#Creating Application Object. Sys.argv parameter is a list of Arguments from command line
	
	#The QWidget is the base class of all user interface objects.
	#We provide the default constructor for QWidget. The default constructor
	#has no parent. A Widget with no parent is called a window
	w=QWidget()
	b=QLabel(w)
	b.setText("Hello World")
	w.resize(250,150)					#Resize widget of 250px wide and 150px high
	w.move(300,300)						#Moves the widget to position on the Screen at x=300,y=300 coordinates
	b.move(100,20)
	w.setWindowTitle("Simple")			#Title for our window
	w.show()							#Displays Widget on screen. Widget first created in the memory and later shown on screen
	
	#We enter the mainloop of the application. The event handling starts from this point.
	#The mainloop receives events from the window system and dispatches them 
	#to the application widgets. The mainloop ends if we call the exit() method or the main
	#widget is destroyed. The sys.exit() method ensures clean exit. The environment will be informed how the application ended.
	#The exec_() method has an underscore since it is a Python keyword.
	sys.exit(app.exec_())
if __name__=='__main__':
	window()