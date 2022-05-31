import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os

print('Module Imported Successfully.')

path = sys.path[0]
endpath = "Database\covid19_confirmed.csv"
path2 = os.path.join(path, endpath)

print(path2)

covid1_dataset_csv = pd.read_csv(path2)
print(covid1_dataset_csv.head(10))
input()
print(covid1_dataset_csv.shape)
covid1_dataset_csv.drop(['Lat','Long'], axis = 1, inplace = True)
print(covid1_dataset_csv.head(10))
input()
covid1_dataset_country = covid1_dataset_csv.groupby("Country").sum()
print(covid1_dataset_country.head(10))
print(covid1_dataset_country.shape)
input()
covid1_dataset_country.loc['US'].plot()
input()
plt.show()
input()
country1 = input('Please enter a country to compare (or enter "list" for a list of countries): ')
if(country1 == "list"):
    print("Afghanistan,	Albania,	Algeria,	Andorra,	Angola,	Antigua and Barbuda,	Argentina,	Armenia,	Australia,	Austria,	Azerbaijan,	Bahamas,	Bahrain,	Bangladesh,	Barbados,	Belarus,	Belgium,	Belize,	Benin,	Bhutan,	Bolivia,	Bosnia and Herzegovina,	Botswana,	Brazil,	Brunei,	Bulgaria,	Burkina Faso,	Burma,	Burundi,	Cabo Verde,	Cambodia,	Cameroon,	Canada,	Central African Republic,	Chad,	Chile,	China,	Colombia,	Comoros,	Congo (Brazzaville),	Congo (Kinshasa),	Costa Rica,	Cote d'Ivoire,	Croatia,	Cuba,	Cyprus,	Czechia,	Denmark,	Diamond Princess,	Djibouti,	Dominica,	Dominican Republic,	Ecuador,	Egypt,	El Salvador,	Equatorial Guinea,	Eritrea,	Estonia,	Eswatini,	Ethiopia,	Fiji,	Finland,	France,	Gabon,	Gambia,	Georgia,	Germany,	Ghana,	Greece,	Grenada,	Guatemala,	Guinea,	Guinea-Bissau,	Guyana,	Haiti,	Holy See,	Honduras,	Hungary,	Iceland,	India,	Indonesia,	Iran,	Iraq,	Ireland,	Israel,	Italy,	Jamaica,	Japan,	Jordan,	Kazakhstan,	Kenya,	Korea, South,	Kosovo,	Kuwait,	Kyrgyzstan,	Laos,	Latvia,	Lebanon,	Liberia,	Libya,	Liechtenstein,	Lithuania,	Luxembourg,	Madagascar,	Malawi,	Malaysia,	Maldives,	Mali,	Malta,	Mauritania,	Mauritius,	Mexico,	Moldova,	Monaco,	Mongolia,	Montenegro,	Morocco,	Mozambique,	MS Zaandam,	Namibia,	Nepal,	Netherlands,	New Zealand,	Nicaragua,	Niger,	Nigeria,	North Macedonia,	Norway,	Oman,	Pakistan,	Panama,	Papua New Guinea,	Paraguay,	Peru,	Philippines,	Poland,	Portugal,	Qatar,	Romania,	Russia,	Rwanda,	Saint Kitts and Nevis,	Saint Lucia,	Saint Vincent and the Grenadines,	San Marino,	Sao Tome and Principe,	Saudi Arabia,	Senegal,	Serbia,	Seychelles,	Sierra Leone,	Singapore,	Slovakia,	Slovenia,	Somalia,	South Africa,	South Sudan,	Spain,	Sri Lanka,	Sudan,	Suriname,	Sweden,	Switzerland,	Syria,	Taiwan*,	Tajikistan,	Tanzania,	Thailand,	Timor-Leste,	Togo,	Trinidad and Tobago,	Tunisia,	Turkey,	Uganda,	Ukraine,	United Arab Emirates,	United Kingdom,	Uruguay,	US,	Uzbekistan,	Venezuela,	Vietnam,	West Bank and Gaza,	Western Sahara,	Yemen,	Zambia,	Zimbabwe")
    country1 = input('Please enter a country to compare the US to: ')
covid1_dataset_country.loc['US'].plot()
covid1_dataset_country.loc[country1].plot()
plt.legend()
plt.show()
input()
covid1_dataset_country.loc['US'].diff().plot()
plt.show()
input()
print('Maximum Infection Rate for US:')
print(covid1_dataset_country.loc['US'].diff().max())
country1 = input('Please enter a country to find the maximum infection rate (or enter "list" for a list of countries): ')
if(country1 == "list"):
    print("Afghanistan,	Albania,	Algeria,	Andorra,	Angola,	Antigua and Barbuda,	Argentina,	Armenia,	Australia,	Austria,	Azerbaijan,	Bahamas,	Bahrain,	Bangladesh,	Barbados,	Belarus,	Belgium,	Belize,	Benin,	Bhutan,	Bolivia,	Bosnia and Herzegovina,	Botswana,	Brazil,	Brunei,	Bulgaria,	Burkina Faso,	Burma,	Burundi,	Cabo Verde,	Cambodia,	Cameroon,	Canada,	Central African Republic,	Chad,	Chile,	China,	Colombia,	Comoros,	Congo (Brazzaville),	Congo (Kinshasa),	Costa Rica,	Cote d'Ivoire,	Croatia,	Cuba,	Cyprus,	Czechia,	Denmark,	Diamond Princess,	Djibouti,	Dominica,	Dominican Republic,	Ecuador,	Egypt,	El Salvador,	Equatorial Guinea,	Eritrea,	Estonia,	Eswatini,	Ethiopia,	Fiji,	Finland,	France,	Gabon,	Gambia,	Georgia,	Germany,	Ghana,	Greece,	Grenada,	Guatemala,	Guinea,	Guinea-Bissau,	Guyana,	Haiti,	Holy See,	Honduras,	Hungary,	Iceland,	India,	Indonesia,	Iran,	Iraq,	Ireland,	Israel,	Italy,	Jamaica,	Japan,	Jordan,	Kazakhstan,	Kenya,	Korea, South,	Kosovo,	Kuwait,	Kyrgyzstan,	Laos,	Latvia,	Lebanon,	Liberia,	Libya,	Liechtenstein,	Lithuania,	Luxembourg,	Madagascar,	Malawi,	Malaysia,	Maldives,	Mali,	Malta,	Mauritania,	Mauritius,	Mexico,	Moldova,	Monaco,	Mongolia,	Montenegro,	Morocco,	Mozambique,	MS Zaandam,	Namibia,	Nepal,	Netherlands,	New Zealand,	Nicaragua,	Niger,	Nigeria,	North Macedonia,	Norway,	Oman,	Pakistan,	Panama,	Papua New Guinea,	Paraguay,	Peru,	Philippines,	Poland,	Portugal,	Qatar,	Romania,	Russia,	Rwanda,	Saint Kitts and Nevis,	Saint Lucia,	Saint Vincent and the Grenadines,	San Marino,	Sao Tome and Principe,	Saudi Arabia,	Senegal,	Serbia,	Seychelles,	Sierra Leone,	Singapore,	Slovakia,	Slovenia,	Somalia,	South Africa,	South Sudan,	Spain,	Sri Lanka,	Sudan,	Suriname,	Sweden,	Switzerland,	Syria,	Taiwan*,	Tajikistan,	Tanzania,	Thailand,	Timor-Leste,	Togo,	Trinidad and Tobago,	Tunisia,	Turkey,	Uganda,	Ukraine,	United Arab Emirates,	United Kingdom,	Uruguay,	US,	Uzbekistan,	Venezuela,	Vietnam,	West Bank and Gaza,	Western Sahara,	Yemen,	Zambia,	Zimbabwe")
    country = input('Please enter a country to find the maximum infection rate: ')
print(covid1_dataset_country.loc[country1].diff().max())
input()
countries = list(covid1_dataset_country.index)
max_infection_rates = []
for country in countries :
    max_infection_rates.append(covid1_dataset_country.loc[country].diff().max())
covid1_dataset_country['Maximum Infection Rate'] = max_infection_rates
print('New Table')
print(covid1_dataset_country.head())
input()
infection_data = pd.DataFrame(covid1_dataset_country['Maximum Infection Rate'])
print('Required Comparison Data')
print(infection_data.head())
input()

endpath2 = "Database\covid_other_factors.csv"
path3 = os.path.join(path, endpath2)
other_factors = pd.read_csv(path3)
print(other_factors.head())
input()

columns_to_remove = ['Overall rank', 'Score', 'Generosity', 'Perceptions of corruption']
## Will change as we use more columns, however for now we are keeping it simple.
other_factors.drop(columns_to_remove, axis = 1, inplace = True)
other_factors.set_index(['Country'], inplace = True)
print('Simplified data:')
print(other_factors.head())
input()

fulldata = other_factors.join(infection_data).copy()
print('Combined Data:')
print(fulldata.head())
input()

print('Correlation Index:')
print(fulldata.corr())
input()

x = fulldata['Freedom to make life choices']
y = fulldata['Maximum Infection Rate']
sns.scatterplot(x,np.log(y))
plt.show()
input()
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))
plt.show()
input()
print('Function Complete.')