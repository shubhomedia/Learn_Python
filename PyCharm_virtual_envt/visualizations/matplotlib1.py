import matplotlib.pyplot as plt

fig = plt.figure("Histogram")
ax = fig.add_subplot(1,1,1)
ax.hist([21,12,23,35,45,60,33,22,56,34,28,40,41],bins=7,facecolor ='r',density=True)

plt.title("Distribution")
plt.xlabel("Range")
plt.ylabel("Amount")
plt.show()