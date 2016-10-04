
# coding: utf-8

# In[33]:

class animal(object):
    
    def __init__ (self):
        print "Animal has created"
    
    def WhoAmI (self):
        print "Animal"
    
    def eat(self):
        print "Eating"


# In[34]:

class dog(animal):
    
    def __init__ (self):
        animal.__init__(self)
        print "Dog created"
    
    def WhoAmI (self):
        print "Dog"
    
    def bark(self):
        print "bark bark"


# In[35]:

d = animal()


# In[36]:

d.WhoAmI()


# In[37]:

d.eat()


# In[38]:

d2 = dog()


# In[39]:

d2.WhoAmI()


# In[40]:

d2.bark()


# In[41]:

d2.eat()


# In[ ]:



