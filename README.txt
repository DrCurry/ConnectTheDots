connectingLines
uses python 3.4.3 and pygame version 1.9.2a0 (windows only)

Creates a bunch for points on screen with random x,y coordinates. Then calculates the distance from the first point to all other point
and if the distance btwn them is less then a preset value a line is drawn connecting them. Then it moves to the second point 
repeating the process so that it look similar to a full mesh network.



08/26/2016:

Issues
When program is running cant close the window to exit. (not a big problem) real pain when there are lots of points
Possible solution, have the window closing event run on a seperate thread

Work in progress
Create a function for the distance formula

