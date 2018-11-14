
# coding: utf-8

# In[42]:


# define the Location class
class Location:
    def __init__(area, county, restaurants, population, percentage): 
        
        area.county = county
        area.restaurants = restaurants
        area.population = population
        area.percentage = percentage
      
    def description(self):
        desc_str = "In 2014 %s county had %s fast-food restaurants and physical inactivity percentage of %s with population of %s." % (self.county, self.restaurants, self.percentage, self.population)
        return desc_str
        
        area1 = Location()
        area1.county = "Cleburne,AR"
        area1.restaurants = "16"
        area1.population = "25,603"
        area1.percentage = 42.1    

# test code
print(area1.description())


# In[45]:


# define the Location class
class Location:
    def __init__(location, county, restaurants, population, percentage):
        location1 = Location()
        location1.county = "Cleburne,AR"
        location1.restaurants = "16"
        location1.population = "25,603"
        location1.percentage = 42.1


    def description(self):
        desc_str = "In 2014 %s county had %s fast-food restaurants and physical inactivity percentage of %s with population of %s." % (self.county, self.restaurants, self.percentage, self.population)
        return desc_str

       

# test code
print(location1.description())


# In[44]:



class Location:
    def __init__(location, county, restaurants, population, percentage):
        location1 = Location()
        location1.county = "Cleburne,AR"
        location1.restaurants = "16"
        location1.population = "25,603"
        location1.percentage = 42.1


    def description(self):
        desc_str = "In 2014 %s county had %s fast-food restaurants and physical inactivity percentage of %s with population of %s." % (self.county, self.restaurants, self.percentage, self.population)
        return desc_str

       


print(location1.description())

