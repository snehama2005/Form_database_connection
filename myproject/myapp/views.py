
# from django.http import HttpResponse
# from django.template import loader

# def login(request):
#   template = loader.get_template('login.html')
#   return HttpResponse(template.render())
# # views.py
# from django.views.generic.edit import CreateView
# from .models import LoginModel

# class GeeksCreate(CreateView):

# 	# specify the model for create view
# 	model = LoginModel

# 	# specify the fields to be displayed

# 	fields = ['title', 'description']



from django.shortcuts import render 
  
# relative import of forms 
# from .models import LoginModel 
# from .forms import LoginForm 
from .models import MovieInfo
  
  
# def create_view(request): 
#     # dictionary for initial data with  
#     # field names as keys 
#     context ={} 
  
#     # add the dictionary during initialization 
#     form = LoginForm(request.POST or None) 
#     if form.is_valid(): 
#         form.save() 
          
#     context['form']= form 
#     return render(request, "create_view.html", context) 



def create(request):
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        desc=request.POST.get('summary')
        movie_obj=MovieInfo(title=title,year=year,description=desc)
        movie_obj.save()
    return render(request,"create.html")
def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,"list.html",{'movies':movie_set})
def edit(request):
    return render(request,"edit.html")

