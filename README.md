# Data Visualization Project 2.0
This project consists of a demo followed by an input-based program in Python using Pandas, MatPlotLib, and Seaborn to process three data sets, combine them into one single data set, and enable the user to analyze and compare data points.

The three data sets are located in datavis2/Database, and include a COVID-19 Case Count Dataset, an Economist World Database dataset that includes many general factors about all countries, and a Population data set, which was used to make the case data per capita.

The programs are located in datavis2, as dvfunc.py and dvfunc2.py. dvfunc2.py is the working build of our project, however dvfunc.py still exists as a stable build demonstration of the basic functionality we have worked on, though it does not include the interactive features we have built since then, which have had most of their issues ironed out.

Thank you! Other files in this repository can be disregared, unless looking at the information below here on the README page.







---------------------------------------------------------------------------------------------------------
All information below here is for the First Semester project. Please disregard for non-archive purposes.


# Data Visualization
Our program will serve as a free and open-source program that allows users to upload data and choose a method of simple visualization. Our program's current form allows users to upload a very basic two-column CSV file and either create a bar chart or to search the file's first column for a specific resulting second column value.

## Prerequisites
- Github Desktop
- Python
- *Both Prerequisites can be downloaded from the BSD Software Center, however if the program is being run on replit, neither are necessary.*

## Instructions
1. If you are running the program on Replit, please skip to Step 4
2. Clone the Github Repository to your computer. More detailed instructions can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
3. Run function.py. When prompted, please type "data" as the file name. A bar chart should appear for the sample data, which was already pre-loaded into the repository.
4. Run function2.py. When prompted, please type "areacodes" as the file name. Then, enter any telephone area code in the second prompt. The program should return an abbreviation of the region the area code you entered corresponds to. If you did not enter a valid area code, the program should return nothing. It should also ask if you would like to repeat the program, and functional the same way if you respond with a "y". 
5. If any of the above same functions did not function as it should have, please create an issue in the link at the bottom of this page, or email one of the project developers.
6. (Optional) Feel free to alter the sample CSV files (also located in datavis folder) or upload your own two-column CSV files to test the program's capabilities with non-sample databases. This testing would be most useful, as the programs sometimes react in unanticipated manners to differing databases. If you run into any problems, please upload your sample CSV file to an issue report on Github and summarize the issue.

## Website
Please visit the website here: https://henryrodgers.github.io to for more information, however the program is not currently hosted online and must be accessed locally.

## Current Features
- Website Shows Project Information
- Two-Column CSV File can be visualized as a bar chart (only works on Github)
- CSV File can search one column and retrieve another column's corresponding value

## Primary Modules:
All relevant modules are within the datavis folder.
* function.py - Contains the Bar Chart program.
* function2.py - Contains the Search and Retrieve program.
* areacodes.csv, countrycodes.csv & data.csv - Sample data files to use in respective programs.


Known Issues: https://github.com/nicoleyang14/special-topics/issues
You may also use the link above for any suggestions or bug reports. It will require a GitHub account to create a new Issue, so if you are unable to create or log in to an account, please just email one of us (s-rodgersh@bsd405.org or s-yangn@bsd405.org) with your feedback.