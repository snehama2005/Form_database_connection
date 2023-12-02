
from django.db import models

# class Login(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.TextField()

#     def __str__(self):
#         return self.name
# import the standard Django Model 
# from built-in library 
# from django.db import models 

# # declare a new model with a name "GeeksModel" 
# class LoginModel(models.Model): 

# 	# fields of the model 
# 	name = models.CharField(max_length = 200) 
# 	password = models.TextField() 

# 	# renames the instances of the model 
# 	# with their title name 
# 	def __str__(self): 
# 		return self.name

class MovieInfo(models.Model):
	title=models.CharField(max_length=250)
	year=models.IntegerField(null=True)
	description=models.TextField()


