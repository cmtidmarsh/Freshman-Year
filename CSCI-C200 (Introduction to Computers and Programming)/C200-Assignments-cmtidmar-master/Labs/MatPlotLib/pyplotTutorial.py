import matplotlib.pyplot as plt 

plt.plot([1, 2, 3, 4]) #connecting a list of numbers
plt.ylabel('some numbers') #labelling the y-axis
plt.show() #visualization

plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) #connecting two lists of numbers

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') #plotting the lists in a row
plt.axis([0, 6, 0, 20]) #creates the window of axes with the min and max
plt.show() #visualization

