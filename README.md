# Data Visualization
Our program will serve as a free and open-source program that allows users to upload data and choose a method of simple visualization. Our program's current form allows users to upload a very basic two-column CSV file and either create a bar chart or to search the file's first column for a specific resulting second column value.

## Prerequisites
- Github Desktop
- Python
** Both Prerequisites can be downloaded from the BSD Software Center.

## Instructions
1. Clone the Github Repository to your computer. More detailed instructions can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
2. Run function.py. When prompted, please type "data" as the file name. A bar chart should appear for the sample data, which was already pre-loaded into the repository.
3. Run function2.py. When prompted, please type "areacodes" as the file name. Then, enter any telephone area code in the second prompt. The program should return an abbreviation of the region the area code you entered corresponds to. If you did not enter a valid area code, the program should return nothing. It should also ask if you would like to repeat the program, and functional the same way if you respond with a "y". 
4. If any of the above same functions did not function as it should have, please create an issue in the link at the bottom of this page, or email one of the project developers.
5. (Optional) Feel free to alter the sample CSV files (also located in datavis folder) or upload your own two-column CSV files to test the program's capabilities with non-sample databases. This testing would be most useful, as the programs sometimes react in unanticipated manners to differing databases. If you run into any problems, please upload your sample CSV file to an issue report on Github and summarize the issue.

## Website
Please visit the website here: https://henryrodgers.github.io to for more information, however the program is not currently hosted online and must be accessed locally.

## Current Features
- Website Shows Project Information
- Two-Column CSV File can be visualized as a bar chart
- CSV File can search one column and retrieve another column's corresponding value

## Primary Modules:
All relevant modules are within the datavis folder.
* function.py - Contains the Bar Chart program.
* function2.py - Contains the Search and Retrieve program.
* areacodes.csv & data.csv - Sample data files to use in respective programs.


Known Issues: https://github.com/nicoleyang14/special-topics/issues
You may also use the link above for any suggestions or bug reports. It will require a GitHub account to create a new Issue, so if you are unable to create or log in to an account, please just email one of us (s-rodgersh@bsd405.org or s-yangn@bsd405.org) with your feedback.