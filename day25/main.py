import pandas
# colors = ['Gray', 'Cinnamon','Black']
# gr_num = 0
# re_num = 0
# bl_num = 0
# other_num = 0


# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# fur_list = data['Primary Fur Color'].to_list()

# for coat in fur_list:
#     if coat == 'Gray':
#         gr_num += 1
#     elif coat == 'Cinnamon':
#         re_num += 1
#     elif coat == 'Black':
#         bl_num += 1
#     else:
#         other_num += 0
# fur_dict = { 
#     'Color' : ['Gray', 'Red', 'Black'],
#     'Count' : [gr_num, re_num, bl_num]
    
# }
# out_file = pandas.DataFrame(fur_dict) 
# out_file.to_csv('Furcount.csv')
# print(f'Red : {re_num}\n Grey: {gr_num}\n Black: {bl_num}')



data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_count = len(data[data['Primary Fur Color'] == 'Grey'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = { 
    'Color' : ['Gray', 'Red', 'Black'],
    'Count' : [grey_count, red_count, black_count]
    
}

df =  pandas.DataFrame(data_dict) 
df.to_csv('Squirrel_Count.csv')
