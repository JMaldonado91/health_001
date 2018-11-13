# Project Name: health_001

Question I analyzed:
Does having fast food restaurants in your county increase chance of physical inactivity?
Is there a relationship between fast-food restaurant growth and physical inactivity in these selected 20 counties?

Used: 
- MYSQL 8.0 Database
- Python 3.7
- Anaconda3-Jupyter Notebook
- CSV file to fetch data to MySQL 8.0 is MySQL_Schema.csv

Resources:
1. Source where I gathered data for county statistics on leisure-time physical inactivity in 2014. Once you go to page, select U.S. report with county data bubble, and then click on the Risk Factors tab.
Select Leisure-Time Physical Inactivity	bubble and then click on Show Results. I used the top 20 counties with the highest percentage of leisure-time physical inactivity.
- [Centers for Disease Control and Prevention](https://nccd.cdc.gov/DHDSPAtlas/Reports.aspx)


2. Sources where I gathered data on fast food restaurants change in 2014 for U.S. counties. I selected counties from source #1 and used the Fast-Food restaurants 2014 number and percent change.

- [United States Department of Agriculture](https://www.ers.usda.gov/data-products/food-environment-atlas/go-to-the-atlas)
- [County Health Rankings and Roadmaps](http://www.countyhealthrankings.org/app/mississippi/2013/measure/factors/84/data)

3. Sources where I gathered data on county population in 2014. I googled the county, state population 2014. Example 'Sevier TN population 2014'.
- [Google](https://www.google.com)
- [United States Census Bureau](https://www.census.gov)

I created 2 graphs in Matplotlib. The graph shows how the growth of fast-food restaurants in different counties have an impact on physical activity.

In conclusion, Arkansas and Mississippi have the highest percentage of physical inactivity, but do not have the most fast food restaurants in comparison. However, Prentiss, MS county and St. Francis, AR county had the highest ratio of fast food restaurants to population. Number of fast food restaurants growth in 2014, Prentiss 16 (population 1,014), St. Francis 10 (population 239). Prentiss, MS county ranked number 2 in physical inactivity.
