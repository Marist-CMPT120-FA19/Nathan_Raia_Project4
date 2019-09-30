#nathan.raia1@marist.edu
#Nathan Raia
#This program is meant to display a traffic light when it is run.
from graphics import *

def main():
	win = GraphWin("Traffic Light", 1000, 1000)
	rec = Rectangle(Point(300 , 100) , Point(700 , 900))
	rec.setFill("white")
	rec.draw(win)
	
	redColor = Circle(Point(500 , 250) , 100)
	redColor.setFill("red")
	redColor.draw(win)

	yellowColor = Circle(Point(500 , 500) , 100)
	yellowColor.setFill("yellow")
	yellowColor.draw(win)
		
	greenColor = Circle(Point(500, 750) , 100)
	greenColor.setFill("green")
	greenColor.draw(win)
		
main()