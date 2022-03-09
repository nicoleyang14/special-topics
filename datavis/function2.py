import pandas as pd
import sys
  
def main():
    path = sys.path[0]
    endpath = input("Please enter the name of your data file here (without the file extension): ")
    path2 = path + "\\" + endpath + ".csv"

    data = pd.read_csv(path2)

    find = input("Please enter the first column value: ")
    # potentially unnecessary
    find = int(find)
    # from earlier attempts, potentially useful in future
    ##data2 = data.where(data == find)
    ##bool_series = pd.notnull(data2["Area Code"])
    print(data.query('`Area Code` == @find')['Region'])

while True:
    main()
    if input("Repeat? (y/n): ") != 'y':
        break
