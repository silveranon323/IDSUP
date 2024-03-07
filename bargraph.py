from matplotlib import pyplot as plt
movies=["AnnieHall","Ben-Haur","Ben-Hur","Casablanca","Gandhi","West Side Story"]
num_oscars=[5,11,3,8,10,90]
plt.bar(range(len(movies)),num_oscars)
plt.title("My Favourite Movies")
plt.ylabel("# of Academy of Awards")
plt.xticks(range(len(movies)),movies)
plt.show()
