from matplotlib import pyplot as plt
from collections import Counter
grade=[87,56,14,88,98,40,86,65,72,91,100]
hg=Counter(min(g//10*10,90)for g in grade)

plt.bar([x for x in hg.keys()], hg.values(), 10, edgecolor="green", color="lightgreen")
plt.axis([-5,105,0,5])
plt.xticks(10*i for i in range(11))
plt.title("Student-Marks")
plt.ylabel("Students")
plt.xlabel("Grdes")
plt.show()
