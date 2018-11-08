import numpy as np
import matplotlib.pyplot as plt
 
# Data
restaurants = [16, 16, 4, 4, 1, 15, 10, 6, 3, 32, 4, 8, 17, 6, 97, 5, 16, 24, 10, 4]

county = ["Cleburne, AR", "Prentiss, MS", "Jasper, MS", "Holmes, MS", "Coal, OK", "Ashley, AR", "St Francis, AR",
          "Lawrence, AR", "Lafayette, AR", "Mississippi, AR", "Haskell, OK", "Randolph, AR", "Poinsett, AR",
          "Lawrence, MS", "Sevier, TN", "Claiborne, MS", "Cocke, TN", "Bell, KY", "Yazoo, MS", "Quitman, MS"]

physical_inactivity = [42.1, 41.3, 40.8, 39.7, 39.5, 39.2, 38.9, 38.8, 38.8, 38.8, 38.7, 38.6, 38.5, 38.4, 38.3, 38.2, 38.1, 38, 38, 38]

positions = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38]
positions2 = [0.8,2.8,4.8,6.8,8.8,10.8,12.8,14.8,16.8,18.8,20.8,22.8,24.8,26.8,28.8,30.8,32.8,34.8,36.8,38.8]
positions3= [0.4,2.4,4.4,6.4,8.4,10.4,12.4,14.4,16.4,18.4,20.4,22.4,24.4,26.4,28.4,30.4,32.4,34.4,36.4,38.4]

# Bars
barWidth = 0.5
plt.bar(positions, restaurants, color = (0.3,0.1,0.4,0.6), label='Fast Food Restaurant growth in 2014')
plt.bar(positions2, physical_inactivity, color= (0.3,0.5,0.4,0.6), label='% of Physical Inactivity in 2014')
 
# Rotation of the bars names
plt.xticks(positions3, county, rotation=90, color='orange')
plt.xlabel('County', fontweight='bold', color = (0.3,0.9,0.4,0.6), fontsize='18')
plt.yticks(color='orange')


plt.subplots_adjust(bottom=0.4, top=0.99)

plt.legend()
 

plt.show()

