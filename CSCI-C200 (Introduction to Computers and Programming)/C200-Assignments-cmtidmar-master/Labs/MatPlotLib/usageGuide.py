import matplotlib.pyplot as plt
import numpy as np 


fig = plt.figure() # an empty figure with no axes
fig.suptitle('no axes on this figure') #title of the empty figure
fig, ax_lst = plt.subplots(2,2) #a figure with a 2x2 grid of axes

# -----------------Objects that need to be converted into an array---------------------------------
# a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde')) # taking a data object (pandas.DataFrame) and turning it into an array, 
#                                                                    #use np (numpy) and generate an array with random values
#                                                                    # store the array in the variable 'a'
# a_asarray = a.values # This is the conversion to an array for a's values

# b = np.maxtrix([1,2], [3,4]) #for the values in the variable 'b', you need to convert the values into an array, like pandas.
# b_asarray = np.asarray(b) # This is the conversion to an array for b's values
# # -------------------------------------------------------------------------------------------------

x = np.linspace(0, 2, 100) #Returns evenly spaced numbers over a specified interval, in this case the
                           #the interval is (0, 2, 100)

plt.plot(x, x, label = 'linear') #this is the type of line being plotted
plt.plot(x, x**2, label='quadratic') #this is the type of line being plotted
plt.plot(x, x**3, label='cubic') #this is the type of line being plotted

plt.xlabel('x label') #just labelling the graph (x-axis)
plt.ylabel('y label') #just labelling the graph (y-axis)
plt.title("Simple Plot") #just labelling the graph (top title)

# plt.legend()
# plt.show()

x = np.arange(0, 10, 0.2) # create an array with the given (0, 10, 0.2) and store it in 'x' (x-value of pt)
y = np.sin(x) # once you have the array, substitute for x and store the answer in 'y' (y-value of pt)
fig, ax = plt.subplots()
ax.plot(x, y) #plotting the x and the y that you found
plt.show() #visual representation

#Plotting in the data with markers
def my_plotter(ax, data1, data2, param_dict): 
    out = ax.plot(data1, data2, **param_dict)
    return out
#----------------------------either/or--------------------------------
#Using one subplot
data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1,1)
my_plotter(ax, data1, data2, {'marker': 'x'})

#Using two subplots
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
#---------------------------------------------------------------------
plt.legend()
plt.show()



