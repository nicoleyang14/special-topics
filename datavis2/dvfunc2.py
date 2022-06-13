from idna import package_data
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os

path = sys.path[0]
endpath = "Database\covid19_confirmed.csv"
path2 = os.path.join(path, endpath)


covid1_dataset_csv = pd.read_csv(path2)
print(covid1_dataset_csv.head(10))
print(covid1_dataset_csv.shape)
input('The dataset has been loaded. Please press enter to remove unnecessary columns.')
covid1_dataset_csv.drop(['Lat','Long'], axis = 1, inplace = True)
print(covid1_dataset_csv.head(10))
input('The dataset has been cleaned. Please press enter to sort the dataset.')
covid1_dataset_country = covid1_dataset_csv.groupby("Country").sum()
print(covid1_dataset_country.head(10))
print(covid1_dataset_country.shape)
input('The dataset has been consolidated into rows by country. Please press enter to begin a demo of a single country analysis.')
covid1_dataset_country.loc['US'].plot()
plt.legend()
plt.show()
country1 = input('Please enter a country to compare (or enter "list" for a list of countries): ')
if(country1 == "list"):
    print("Afghanistan,	Albania, Algeria, Andorra, Angola, Antigua and Barbuda, Argentina, Armenia, Australia, Austria, Azerbaijan,	Bahamas, Bahrain, Bangladesh, Barbados,	Belarus, Belgium, Belize, Benin, Bhutan, Bolivia, Bosnia and Herzegovina, Botswana,	Brazil,	Brunei,	Bulgaria, Burkina Faso,	Burma, Burundi,	Cabo Verde,	Cambodia, Cameroon,	Canada,	Central African Republic, Chad,	Chile, China, Colombia,	Comoros, Congo (Brazzaville), Congo (Kinshasa),	Costa Rica,	Cote d'Ivoire, Croatia,	Cuba, Cyprus, Czechia, Denmark,	Diamond Princess, Djibouti,	Dominica, Dominican Republic, Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia,	Eswatini, Ethiopia,	Fiji, Finland, France, Gabon, Gambia, Georgia, Germany,	Ghana, Greece, Grenada,	Guatemala, Guinea, Guinea-Bissau, Guyana, Haiti, Holy See, Honduras, Hungary, Iceland, India, Indonesia, Iran, Iraq, Ireland, Israel, Italy, Jamaica, Japan, Jordan, Kazakhstan, Kenya,	South Korea, Kosovo, Kuwait, Kyrgyzstan, Laos, Latvia, Lebanon,	Liberia, Libya,	Liechtenstein, Lithuania, Luxembourg, Madagascar, Malawi, Malaysia,	Maldives, Mali,	Malta, Mauritania, Mauritius, Mexico, Moldova, Monaco, Mongolia, Montenegro, Morocco, Mozambique, MS Zaandam, Namibia, Nepal, Netherlands, New Zealand, Nicaragua, Niger, Nigeria, North Macedonia,	Norway,	Oman, Pakistan,	Panama,	Papua New Guinea, Paraguay,	Peru, Philippines, Poland, Portugal, Qatar,	Romania, Russia, Rwanda, Saint Kitts and Nevis,	Saint Lucia, Saint Vincent and the Grenadines, San Marino, Sao Tome and Principe, Saudi Arabia,	Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Slovakia,	Slovenia, Somalia, South Africa, South Sudan, Spain, Sri Lanka,	Sudan, Suriname, Sweden, Switzerland, Syria, Taiwan, Tajikistan, Tanzania, Thailand, Timor-Leste, Togo, Trinidad and Tobago, Tunisia, Turkey, Uganda, Ukraine, United Arab Emirates, United Kingdom, Uruguay, US, Uzbekistan, Venezuela, Vietnam, West Bank and Gaza, Western Sahara, Yemen, Zambia, Zimbabwe")
    country1 = input('Please enter a country to compare the US to: ')
covid1_dataset_country.loc['US'].plot()
covid1_dataset_country.loc[country1].plot()
plt.legend()
plt.show()
input('Comparison is complete. Please click enter to compute the graph of the derivative of the United States\' COVID infection rate.')
covid1_dataset_country.loc['US'].diff().plot()
plt.show()
input('Please press enter to continue to Maximum Infection Rates. The maximum infection rate is defined as the amount of new infections on the day with the most new infections throughout the data set.')
print('Maximum Infection Rate for US:')
print(covid1_dataset_country.loc['US'].diff().max())
country1 = input('Please enter a country to find the maximum infection rate (or enter "list" for a list of countries): ')
if(country1 == "list"):
    print("Afghanistan,	Albania, Algeria, Andorra, Angola, Antigua and Barbuda, Argentina, Armenia, Australia, Austria, Azerbaijan,	Bahamas, Bahrain, Bangladesh, Barbados,	Belarus, Belgium, Belize, Benin, Bhutan, Bolivia, Bosnia and Herzegovina, Botswana,	Brazil,	Brunei,	Bulgaria, Burkina Faso,	Burma, Burundi,	Cabo Verde,	Cambodia, Cameroon,	Canada,	Central African Republic, Chad,	Chile, China, Colombia,	Comoros, Congo (Brazzaville), Congo (Kinshasa),	Costa Rica,	Cote d'Ivoire, Croatia,	Cuba, Cyprus, Czechia, Denmark,	Diamond Princess, Djibouti,	Dominica, Dominican Republic, Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia,	Eswatini, Ethiopia,	Fiji, Finland, France, Gabon, Gambia, Georgia, Germany,	Ghana, Greece, Grenada,	Guatemala, Guinea, Guinea-Bissau, Guyana, Haiti, Holy See, Honduras, Hungary, Iceland, India, Indonesia, Iran, Iraq, Ireland, Israel, Italy, Jamaica, Japan, Jordan, Kazakhstan, Kenya,	South Korea, Kosovo, Kuwait, Kyrgyzstan, Laos, Latvia, Lebanon,	Liberia, Libya,	Liechtenstein, Lithuania, Luxembourg, Madagascar, Malawi, Malaysia,	Maldives, Mali,	Malta, Mauritania, Mauritius, Mexico, Moldova, Monaco, Mongolia, Montenegro, Morocco, Mozambique, MS Zaandam, Namibia, Nepal, Netherlands, New Zealand, Nicaragua, Niger, Nigeria, North Macedonia,	Norway,	Oman, Pakistan,	Panama,	Papua New Guinea, Paraguay,	Peru, Philippines, Poland, Portugal, Qatar,	Romania, Russia, Rwanda, Saint Kitts and Nevis,	Saint Lucia, Saint Vincent and the Grenadines, San Marino, Sao Tome and Principe, Saudi Arabia,	Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Slovakia,	Slovenia, Somalia, South Africa, South Sudan, Spain, Sri Lanka,	Sudan, Suriname, Sweden, Switzerland, Syria, Taiwan, Tajikistan, Tanzania, Thailand, Timor-Leste, Togo, Trinidad and Tobago, Tunisia, Turkey, Uganda, Ukraine, United Arab Emirates, United Kingdom, Uruguay, US, Uzbekistan, Venezuela, Vietnam, West Bank and Gaza, Western Sahara, Yemen, Zambia, Zimbabwe")
    country = input('Please enter a country to find the maximum infection rate: ')
print(covid1_dataset_country.loc[country1].diff().max())
input('Please press enter to begin the process of adding a column for Maximum Infection Rate to the data set.')
countries = list(covid1_dataset_country.index)
max_infection_rates = []
for country in countries :
    max_infection_rates.append(covid1_dataset_country.loc[country].diff().max())
covid1_dataset_country['Maximum Infection Rate'] = max_infection_rates
print('New Table')
print(covid1_dataset_country.head())
input('Please press enter to continue.')
infection_data = pd.DataFrame(covid1_dataset_country['Maximum Infection Rate'])
print('Required Comparison Data')
print(infection_data.head())
input('The data set has been cleaned for comparison with another data set. Press enter to initiate the importing of the other data set.')

endpath2 = "Database\covid_other_factors.csv"
path3 = os.path.join(path, endpath2)
other_factors = pd.read_csv(path3)
print(other_factors.head())
input('Press enter to clean the new data set.')

columns_to_remove = ['Overall rank', 'Score', 'Generosity', 'Perceptions of corruption']
## Will change as we use more columns, however for now we are keeping it simple.
other_factors.drop(columns_to_remove, axis = 1, inplace = True)
other_factors.set_index(['Country'], inplace = True)
print('Simplified data:')
print(other_factors.head())
input('Press enter to combine the data sets.')

fulldata = other_factors.join(infection_data).copy()
print('Combined Data:')
print(fulldata.head())
input('Press enter to find the correlation index of each factor pair.')

print('Correlation Index:')
print(fulldata.corr())
input('Press enter to compare the columns on a graph.')

x = fulldata['Freedom to make life choices']
y = fulldata['Maximum Infection Rate']
sns.scatterplot(x,np.log(y))
plt.show()
input('Press enter to establish a line of best fit on the graph.')
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))
plt.show()
input('Thank you. Press enter to convert existing data to per capita.')


endpath3 = "Database\population.csv"
path4 = os.path.join(path, endpath3)
pop = pd.read_csv(path4)
columns_to_remove2 = ['Yearly Change', 'Net Change', 'Density', 'Land Area', 'Migrants (net)', 'Fert. Rate', 'Med. Age', 'Urban Pop %', 'World Share']
pop.drop(columns_to_remove2, axis = 1, inplace = True)
pop.set_index(['Country'], inplace = True)
pcdata = fulldata.join(pop).copy()
pcdata.to_csv(index=False)
print('Unnecessary columns removed and population database adjoined.')
pcdata["Max Infection Rate Per 10,000 Pop"] = pcdata["Maximum Infection Rate"].div(pcdata['Population'])
print('Per Capita Infection Rate calculated.')
pcdata['Max Infection Rate Per 10,000 Pop'] = 10000 * pcdata['Max Infection Rate Per 10,000 Pop']
print('Per Capita data convered to Per 10,000')
columns_to_remove3 = ['Population']
pop.drop(columns_to_remove3, axis = 1, inplace = True)
print('Raw Population Data removed.')
factorn1 = input('Choose the first factor to compare. Enter 1 for GDP per capita, Enter 2 for Social Support, Enter 3 for Healthy Life Expectancy, Enter 4 for Freedom to Make Life Choices, or Enter 5 for Maximum Infection Rate per capita. ')
if(factorn1 == "1"):
    factorn2 = input('Choose the second factor to compare. Enter 2 for Social Support, Enter 3 for Healthy Life Expectancy, Enter 4 for Freedom to Make Life Choices, or Enter 5 for Maximum Infection Rate per capita. ')
    factorn1 = "GDP per capita"
if(factorn1 == "2"):
    factorn2 = input('Choose the second factor to compare. Enter 1 for GDP per capita, Enter 3 for Healthy Life Expectancy, Enter 4 for Freedom to Make Life Choices, or Enter 5 for Maximum Infection Rate per capita. ')
    factorn1 = "Social support"
if(factorn1 == "3"):
    factorn2 = input('Choose the second factor to compare. Enter 1 for GDP per capita, Enter 2 for Social Support, Enter 4 for Freedom to Make Life Choices, or Enter 5 for Maximum Infection Rate per capita. ')
    factorn1 = "Healthy life expectancy"
if(factorn1 == "4"):
    factorn1 = "Freedom to make life choices"
    factorn2 = input('Choose the second factor to compare. Enter 1 for GDP per capita, Enter 2 for Social Support, Enter 3 for Healthy Life Expectancy, or Enter 5 for Maximum Infection Rate per capita. ')
if(factorn1 == "5"):
    factorn1 = "Max Infection Rate Per 10,000 Pop"
    factorn2 = input('Choose the second factor to compare. Enter 1 for GDP per capita, Enter 2 for Social Support, Enter 3 for Healthy Life Expectancy, or Enter 4 for Freedom to Make Life Choices. ')

if(factorn2 == "1"):
    factorn2 = "GDP per capita"
if(factorn2 == "2"):
    factorn2 = "Social support"
if(factorn2 == "3"):
    factorn2 = "Healthy life expectancy"
if(factorn2 == "4"):
    factorn2 = "Freedom to make life choices"
if(factorn2 == "5"):
    factorn2 = "Max Infection Rate Per 10,000 Pop"


x = pcdata[factorn1]
y = pcdata[factorn2]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))
plt.show()
input('Please press enter to end the function.')









print('Function Complete.')

