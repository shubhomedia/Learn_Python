import matplotlib.pyplot as plt

fig = plt.figure("Histogram")
ax = fig.add_subplot(1,1,1)
ax.hist([21,12,23,35,45,60,33,22,56,34,28,40,41],bins=7, facecolor='r',normed=False)

plt.title("Distribution")
plt.xlabel("Rang")
plt.ylabel("Amount")
plt.show()

fig2 = plt.figure('Box-plot')
ax1 = fig2.add_subplot(1,1,1)
ax1.boxplot([21,12,23,35,45,60,33,22,56,34,28,40,41])
plt.show()

fig3 = plt.figure("Bar")
ax2 = fig3.add_subplot(1,1,1)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title("Bars")
ax2.bar([0,1,2,3],[5,10,15,5],[0.5,1,1.3,1],color=['b','r'])
plt.show()