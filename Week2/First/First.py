from matplotlib import pyplot as plt

Years=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
Kosovo = [3.31, 4.375, 2.81, 3.44,1.222,4.095,4.071,4.226,3.816,4.172]
Albania = [3.707,2.545,1.418, 1.002,1.774,2.219,3.315,3.802,4.071,2.24 ]
USA = [2.564,1.551,2.25, 1.842,2.526,2.908,1.638,2.37,2.927,2.161]
Russia=[4.5,4.3,4.024,1.755,0.736,-1.973,0.194,1.826,2.536,1.342]
Turkey=[8.427,11.2,4.788,8.468,4.94,6.084,3.323,7.502,2.959,0.917]

plt.plot(Years,Kosovo, color='Red',marker='o', linestyle='dotted')
plt.plot(Years,Albania, color='Black',marker='o', linestyle='dotted')
plt.plot(Years,USA, color='Blue',marker='o', linestyle='dotted')
plt.plot(Years,Russia, color='Green',marker='o', linestyle='dotted')
plt.plot(Years,Turkey, color='Yellow',marker='o', linestyle='dotted')


plt.legend(['[Kosovo','Albania','USA','Russia','Turkey'])
plt.title("GDP Over the years")
plt.ylabel("GDP")
plt.xlabel('Years', color='blue')


plt.show()
