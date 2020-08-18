from distutils.command.install_data import install_data

import pandas as pd
dataFram=pd.DataFrame({'User_id': ["154", "155","165"], 'TimeStamp': ["2020-10-8 10:55:22", "2020-10-8 11:22:32","2020-8-10 12:45:23"]})
print(dataFram)
# to get data using index as array (0 -> n-1)
print(dataFram._get_column_array(1)[0]," ",type(dataFram._get_column_array(1)[0]))
# # Data Frame is like dictionary means we get data from key
print("Time Stamp \n",dataFram.__getitem__("TimeStamp"))
# # to get specific element from index
# k=dataFram.__getitem__("TimeStamp")[0]
# print(k)
#
# # to declaration index of datafram using index attribute
# dateframAttend=pd.DataFrame({'User_id': ["154", "155","156"], 'TimeStamp': ["2020-10-8 10:55:22", "2020-10-8 11:22:32","2020-8-10 12:45:23"]},index=['Eng.Ahmed','Eng.ِAhmed','Eng.abbas'])
# print(dateframAttend)
#
# # to write DataFram in CSV Files
dateframAttend.to_csv (r'attendanceFram.csv',index=0, header=True)
#
# '''
# Series
# A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list.
# And in fact you can create one with nothing more than a list
# '''
#
# sdatafram=pd.Series(["2020-10-8 10:55:22", "2020-10-8 11:22:32","2020-8-10 12:45:23"],index=["154","155","156"],name="Attendaces ")
# print(sdatafram)

attend_obj = pd.read_csv("attendacne.csv")
# print("(r,c) ",attend_obj.shape," ",type(attend_obj.shape))
# print("Nmuber of row ",attend_obj.shape[0], " number of Columns ",attend_obj.shape[1])
#
# # to print the First 5 rows

#print(attend_obj.head())

# to use the index not default in odoo
attend_obj_1 = pd.read_csv("attendanceFram.csv",index_col=0)
print(attend_obj_1)
print("(r,c) ",attend_obj_1.shape," ",type(attend_obj_1.shape))
print("Nmuber of row ",attend_obj_1.shape[0], " number of Columns ",attend_obj_1.shape[1])

# to print the First 5 rows

#print(attend_obj_1.head())

'''  Second Lesson Indexing Selecting     '''
# we can selecting elements from index is attribute is label of datafram
print(attend_obj_1.User_id) #print(attend_obj_1['User_id'])

# select specific element using index operator []
print(attend_obj_1.User_id[2]) #print(attend_obj_1['User_id'][0])

'''
pandas has its own accessor operators, loc and iloc. For more advanced operations, 
these are the ones you're supposed to be using.
'''
'''
Pandas indexing works in one of two paradigms. The first is index-based selection: 
selecting data based on its numerical position in the data. iloc follows this paradigm.
'''
print("\n",attend_obj_1.iloc[0].User_id)

print("\n",attend_obj_1.iloc[:].User_id)
#return data the first row
print("\n",attend_obj_1.iloc[0])
#select specific element using operator [:,0] datafram as matrix 0->r-1  , 0->c-1
print("\n",attend_obj_1.iloc[0:2,0])

print("\n",attend_obj_1.iloc[[0,1,2],0])