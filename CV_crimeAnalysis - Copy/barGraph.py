import numpy as np #pip install numpy
import matplotlib.pyplot as plt #pip install matplotlib

#create arrays for plotting crime types for 4 cities
#murder cases for 4 cities: Virginia Beach,Chesapeake, Norfolk, Portsmouth
murder = (4555, 7678, 3960, 9234)
rape = (5012, 6875, 8096, 3124) #rape cases in order by of cities
robbery = (2618, 9270, 1056, 7722)
thief = (6018, 2803, 4960, 8037)

#var city and store array of cities name corresponding to to 4 array data numbers with type of crimes
city = ["St.Louis-Miss", "Oakland-Cal", "Memphis-Tenn","Detroit-Mich"]
index = np.arange(4)#specify index elements number
#create 4 bar charts and specify the with, label and assign each bar to the var arrays that defined above
plt.bar(index, murder, width =0.2, label = "Murder")
plt.bar(index + 0.2, rape, width =0.2, label = "Rape")
plt.bar(index + 0.4, robbery, width =0.2, label = "Robbery")
plt.bar(index + 0.6, thief, width =0.2, label = "Thief")


#load the array on the graph and define a scale range
plt.title("Crimes Comparison: Virginia Beach,Chesapeake,Norfolk,Porsmouth\n")
plt.xlabel("Dangerous Cities with High Crime Rate")
plt.ylabel("Number of Cases")
plt.xticks(index + 0.2, city)
plt.legend(loc = 'upper left')
plt.ylim(1000,10000)
plt.show()#show graph