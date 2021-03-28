from matplotlib import pyplot as plt

GDP=[7.8,15.4,11.8]
Population=[1.814,1.845,2.083]
StateNames=['Kosovo','Albania','North Macedonia']

plt.scatter(GDP,Population)

for GDP,Population,StateNames in zip(GDP,Population,StateNames):
    plt.annotate(StateNames, xy=(GDP,Population),xytext=(5,-5),textcoords='offset points')

plt.title("Numri i banoreve dhe GDP")
plt.xlabel("GDP")
plt.ylabel("Numri i banoreve (Milion)")
plt.show()

# 1.814.894
# 1.845.553
# 2.083.000


#
# 3.GDP, POPULLSIA SHTETI DHE ermrat e shtetit profi tha e keni leht se osht
# njejt me fig3-7 fq77 veq zevendsim te vlerave ka