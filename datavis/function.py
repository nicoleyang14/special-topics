# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import sys
  
path = sys.path[0]
endpath = input("Please enter the name of your data file here (without the file extension): ")
path2 = path + "\\" + endpath + ".csv"

# Initialize the lists for X and Y
data = pd.read_csv(path2)       
  
df = pd.DataFrame(data)
  
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
  
# Plot the data using bar() method
cinput = input('Please enter the desired bar chart color (enter "info" for a list of possible colors): ')

if (cinput == "info"):
        print('enter "b" for blue');
        print('enter "c" for cyan');
        print('enter "k" for black');
        print('enter "g" for green');
        print('enter "m" for purple');
        print('enter "w" for white');
        print('enter "r" for red');
        print('enter "y" for yellow');
        cinput = input("Please enter the desired bar chart color: ")
plt.bar(X, Y, color=cinput)
dinput = input('Please enter the title: ')
#Students over 11 Years
plt.title(dinput)
einput = input('Please enter the x-axis label: ')
#Years
plt.xlabel(einput)
finput = input('Please enter the y-axis label: ')
#Number of Students
plt.ylabel(finput)
  
# Show the plot
plt.show()
<<<<<<< HEAD
input("Type enter to exit")
=======
input('Press enter to end program.')
>>>>>>> ebe04d1d39aac72bef029bdfe8856016860d9f2c
sys.exit()