import numpy as np
import numpy.random as r
import matplotlib.pyplot as plot

target = 250
beta = 0.5

Y = np.random.exponential(beta, 50)

print(Y)


# np_arr_1 = np.array(([1,2,3], [1,2,3]))
# np_arr_2 = np.array(([1,2,3], [1,2,3]))
#
# # arithmatic operations.
# print(np_arr_1  + np_arr_2)
# print(np_arr_1  - np_arr_2)
# print(np_arr_1  / np_arr_2)
#
#
# print("Random::", r.random(10))
#
#
# np_arr_3 = np.array(([1,2,2], [1,2,3]))
# print("Shape of numpy arr :: ", np_arr_3.shape)
#
# np_arr_3 = np.array(([1,2,2], [1,2,3]))
# print("Ravel ", np_arr_3.ravel())
#
#
# np_arr_3 = np.array(([1,2,3], [4,5,6]))
#
# print("Accessing via index.. :: ", np_arr_3[0,1], np_arr_3[1,1])
#
# print("Standard deviation :: ", np_arr_3.std())
#
# a = np.arange(5,100)
#
# print("Arange:: ", a)
#
# print("Square :: ", np.sqrt(a))
#
# a = np.array([2,3,4, 10, 100])
#
# print("Log ", np.log10(a))
#
# print("Natural Log ", np.log(a))
#
#
#
# x = np.array([2,3,5,7])
# y = np.array([2,3,5,7])
#
# print (" Sin function :: ", np.sin(x))
# print (" Sin function return type  :: ", type(np.sin(x)), np.sin(y))
#
# #plot.plot(x,y)
# plot.plot(np.tan(np.arange(100)))
#
#
# plot.show()
# #
# import plotly.plotly as py
# import plotly.tools as tls
#
# import matplotlib.pyplot as plt
#
#
# y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
# N = len(y)
# x = range(N)
# width = 1/1.5
# plt.bar(x, y, width, color="blue")
#
#
# fig = plt.gcf()
# plotly_fig = tls.mpl_to_plotly(fig)
# py.iplot(plotly_fig, filename='mpl-basic-bar')
#
# import matplotlib.pyplot as plt
#
#
# y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
# N = len(y)
# x = range(N)
# width = 1/1.5
# plt.bar(x, y, width, color="blue")
#
#
# fig = plt.gcf()
# plotly_fig = tls.mpl_to_plotly(fig)
# py.iplot(plotly_fig, filename='mpl-basic-bar')