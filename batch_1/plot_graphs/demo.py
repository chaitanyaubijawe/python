import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,6, 12)
print(type(x), x)

y = x ** 2

print(y)

# functional
# plt.plot(x,y,'g')
# plt.xlabel("time")
# plt.ylabel("distance in km")
# plt.title("distance covered in time,...")

#
# p1 = plt.subplot(3,2,1)
# p1.plot(x,y, 'r')
#
#
# p2 = plt.subplot(3,2,2)
# p2.plot(y, x, 'g')
#
# p3 = plt.subplot(3,2,3)
# p3.plot(y, x, 'g')
#
# p4 = plt.subplot(3,2,4)
# p4.plot(x,y, 'r')
#
# p5 = plt.subplot(3,2,5)
# p5.plot(x,y, 'r')
#
# plt.show()




# OO
#
figure = plt.figure()

axis = figure.add_axes([0.1,0.1,0.8,0.8])
axis2 = figure.add_axes([0.1,0.1,0.8,0.8])
axis3 = figure.add_axes([0.1,0.1,0.8,0.8])
axis4 = figure.add_axes([0.1,0.1,0.8,0.8])
axis.plot(x,y)

l = []

l.append(axis)
l.append(axis2)
l.append(axis3)
l.append(axis4)


for axs in l:
    axs.plot(x,y)



# axis.set_xlabel("thisdfsd")
#
# axis2 = figure.add_axes([0.2,0.6,0.2,0.2])
# axis2.plot([1,2,3,4],[1,2,3,4])
#
# figure.show()




fig, axis = plt.subplots(nrows=5,ncols=5)

print(type(axis))


# axis[0,1].plot(x,y)
# for a in np.ndi
#[[]]
for a in axis:
    print("Row: ", type(a))

    for aa in a:
        print(aa)
        aa.plot(x,y)


plt.show()