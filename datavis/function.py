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
plt.bar(X, Y, color='g')
plt.title("Students over 11 Years")
plt.xlabel("Years")
plt.ylabel("Number of Students")
  
# Show the plot
plt.show()
input()
sys.exit()