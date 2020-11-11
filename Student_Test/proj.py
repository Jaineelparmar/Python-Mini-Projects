import pandas as pd

data = pd.read_csv('test.csv')
print(data)


#Pandas Series.fillna() function is used to fill NA/NaN values using the specified method.
# data = data.fillna(0)


# #Total of 'MATHS', 'PHYSICS', 'CHEMISTRY'.
# data['Total'] = data['Maths'] + data['Physics'] + data['Chemistry']
# print(data)
# print('-'*20)
# #print(data[['Total']])
# #print('-'*20)


# #print(data[data['Total'] > 200])
# #print('-'*20)
# total_more_than_200 = data[data['Total']>200]
# print(total_more_than_200)
# print('-'*20)


# #'Student ID' of students who scored 'greater than 80' in 'MATHS' and 'PHYSICS'

# #print(data[(data['Maths']>80) & (data['Physics']>80)][['Student ID','Total']])
# #print('-'*20)
# more_than_80_in_maths_phy = data[(data['Maths']>80) & (data['Physics']>80)]
# print(more_than_80_in_maths_phy[['Student ID','Total']])
# print('-'*20)


# #Gives the list of Student ID
# print(data['Student ID'].tolist())
# print('-'*20)


# #The drop() function is used to drop the colums by using axix = 1 or name of the columns as columns = 'name of the column'
# data = data.drop(['Physics', 'Maths'], axis = 1)
# print(data)
# print('-'*20)


# #The sum() function adds the elements of an iterable and returns the sum
# print(data['Total'].sum())
# print('-'*20)

# #To print the length of the column 'Total'
# print(len(data['Total']))
# print('-'*20)



# #apply() calls the passed lambda function for each row and passes each row contents as series to this lambda function.
# #Finally it returns a modified copy of dataframe constructed with rows returned by lambda functions, instead of altering original dataframe.

# data['Chemistry_result'] = data['Chemistry'].apply(lambda x: 'Pass' if x>35 else 'Fail')
# print(data)


# #Converts and saves into a new CSV file
# data.to_csv('abc.csv')
