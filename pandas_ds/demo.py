import pandas as pd
import numpy as np
#
# l = [1,2,3]
# print("List to panda :: ", pd.Series(l))
#
# print("List with custom index..  ", pd.Series(data=l, index=['a','b','c']))
#
# d = {"a":1, "b":2, "c":3}
# print(pd.Series(d))
#
# ##
#
# label = ['a', 'b','c']
# my_list = [10,20,30]
# arr = np.array([10,20,30])
# d= {'a':10, 'b':20, 'c':30}
#
#
# pd_s = pd.Series(my_list)
#
# print("Without custom index :: ",pd_s)
#
#
# pd_s_1 = pd.Series(my_list, label)
#
# print("With custom index :: ",pd_s_1)
#
#
# pd_s_2 = pd.Series(d)
#
# print("With custom index :: ",pd_s_2)
#
#
#
# print(type(pd_s_1))
#
# print(pd_s_1 + pd_s_2)
#
#
# df = pd.DataFrame({'length': [1.5, 0.5, 1.2, 0.9, 3],'width': [0.7, 0.2, 0.15, 0.2, 1.1]} , index= ['pig', 'rabbit', 'duck', 'chicken', 'horse'])
#
#
# print(df)
#
#
# from numpy.random import randn
#
# np.random.seed(101)
#
#
# print(randn(5,4))
# df = pd.DataFrame(randn(5,4), ['R1','R2','R3','R4','R5'], ['C1','C2','C3','C4'])
#
# print(df)
#
# print(df["C1"])
# print(type(df["C1"]))
# print(df[["C1", "C2"]])
# print(df.loc["R1"])
#
#
# print(df["C1"] > 0)
# print(df[df["C1"] > 0])
#
# print(df[(df['C1'] > 0) & (df['C2'] > 0)])
# print(df[(df['C1'] > 0) | (df['C2'] > 0)])
#
# print(df.reset_index())
# # print(df.reset_index(inplace=True))
# #
# states = ['CA', 'USA', 'IND', 'ITALY', 'FR']
#
# df['States'] = states
#
# print(df)
#
# print(df.set_index('States'))
# print(df)
#
# group_names = ['R1', 'R1', 'R1', 'R2', 'R2', 'R2']
# row_names = ['C1', 'C2', 'C3', 'C1', 'C2', 'C3']
#
# print(zip(group_names, row_names))
# index = list(zip(group_names, row_names))
#
# m_index = pd.MultiIndex.from_tuples(index)
#
#
# df = pd.DataFrame(data=randn(6,2), index= m_index, columns=['A', 'B'])
# print(df)
#
#
# # print(df.loc['R1'].loc['C1'])
# # df.index.names = ['Groups', 'Num']
# # print(df.index.names)
# #
# print(df.loc['R1'].loc['C2']['B'])
# # cross section column selection
# print(df.xs('R1'))
# # print(df.xs('C1', level='Num'))
#
# #
# #
# d = {"R1":["a","v","s","d","s", "s"],"Company":['ab','cd','ef','ab','cd','ef' ],"R3":[2,3,4,2,3,4],}
#
# df = pd.DataFrame(d)
#
# print(df)
# gp = df.groupby('Company')
#
# print(gp.sum())
#
# print(gp.describe().transpose())

#
# df = pd.read_csv('a.csv')
# df.to_excel('a.xlsx', sheet_name='a')

# print(df)
#
# df = pd.read_excel('a.xlsx', sheet_name='a')
#
# print(df)


import matplotlib.pyplot as plt

df = pd.DataFrame({'length': [1.5, 0.5, 1.2, 0.9, 3],'width': [0.7, 0.2, 0.15, 0.2, 1.1]} , index= ['pig', 'rabbit', 'duck', 'chicken', 'horse'])
hist = df.hist(bins=20)
plt.show()

#df.plot.hist()

# df.plot(kind='hist')
# df.plot.area(alpha=0.4)
# df.plot.bar(stacked=True)
# df.plot.hist(bins=50)
# df.plot.line()
# df.plot.scatter(x='length', y = 'width')
# df.plot.box()



#openpyxl and sqlalchemy

from sqlalchemy import create_engine

engine= create_engine('sqlite:///:memory:')


df.to_sql('my_table', engine)

df = pd.read_sql('my_table', engine)

print(df)