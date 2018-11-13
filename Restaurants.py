import numpy as np
import matplotlib.pyplot as plt
 
# Data
percentage = [42, 60, 50, 50, 33, 59, 39, 27, 40, 57, 33, 48, 67, 55, 37, 67, 38, 71, 58, 60]

county = ["Cleburne, AR", "Prentiss, MS", "Jasper, MS", "Holmes, MS", "Coal, OK", "Ashley, AR", "St Francis, AR",
          "Lawrence, AR", "Lafayette, AR", "Mississippi, AR", "Haskell, OK", "Randolph, AR", "Poinsett, AR",
          "Lawrence, MS", "Sevier, TN", "Claiborne, MS", "Cocke, TN", "Bell, KY", "Yazoo, MS", "Quitman, MS"]

restaurants = [15, 15, 5, 5, 1, 13, 11, 4, 2, 32, 4, 10, 20, 6, 83, 4, 18, 27, 11, 3]


positions = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38]
positions2 = [0.8,2.8,4.8,6.8,8.8,10.8,12.8,14.8,16.8,18.8,20.8,22.8,24.8,26.8,28.8,30.8,32.8,34.8,36.8,38.8]
positions3= [0.4,2.4,4.4,6.4,8.4,10.4,12.4,14.4,16.4,18.4,20.4,22.4,24.4,26.4,28.4,30.4,32.4,34.4,36.4,38.4]

# Bars
barWidth = 0.5
plt.bar(positions, percentage, color = (0.3,0.1,0.4,0.6), label='% of Fast Food Restaurants in 2014')
plt.bar(positions2, restaurants, color= (0.3,0.5,0.4,0.6), label='# of Fast Food Restaurants in 2014')

# Rotation of the bars names
plt.xticks(positions3, county, rotation=90, color='orange')
plt.xlabel('County', fontweight='bold', color = (0.3,0.9,0.4,0.6), fontsize='18')
plt.yticks(color='orange')


plt.subplots_adjust(bottom=0.4, top=0.99)

plt.legend()
 

plt.show()
