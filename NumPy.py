# import numpy as np
# my_list = [1,2,3,4,5,6,7,8,9]
# np_array = np.array(my_list)
# print(np_array)
# # Numpy 2x3 array of zeroes
# array_zero=np.zeros((2,3))
# print("Array Zero")
# print(array_zero)

import pandas as pd
# a_list =['Alice','Bob','Charlie']
# pd_serie = pd.Series(a_list)
# print(pd_serie)
#
# my_dict = {'Alice':1,'Bob':2,'Charlie':3}
# pd_dataframe = pd.DataFrame(my_dict,index=['row1','row2'])
# print(pd_dataframe)
#
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ['sepal_length','sepal_width','petal_length','petal_width','species']
dataset = pd.read_csv(url)
frame = pd.DataFrame(list(dataset.values),columns=columns)

import matplotlib.pyplot as plt
# y =[1,2,3,4,5,6,7,8,9]
# plt.plot(y)
# plt.ylabel('Number')
# plt.show()

plt.scatter(frame['sepal_length'],frame['sepal_width'],color='red')
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.show()