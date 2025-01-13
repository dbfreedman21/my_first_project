# Chart creation test

import matplotlib.pyplot as plt

plt.bar(["easy", "medium", "hard"], [5, 3, 2], color=["purple", "orange", "red"])
plt.title("Matplotlib Test Chart")
plt.xlabel("Difficulty")
plt.ylabel("Number of Missions")
plt.show()
