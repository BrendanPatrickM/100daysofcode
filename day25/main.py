import pandas
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_count = len(data[data['Primary Fur Color'] == 'Grey'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Color': ['Gray', 'Red', 'Black'],
    'Count': [grey_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('Squirrel_Count.csv')
