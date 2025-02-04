from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import Register ,create_blog,upload_img,upload_profile
from django.contrib import messages
from django.core.paginator import Paginator







# Create your views here.
@login_required
def index(request):
    movies =  movie.objects.all()
    paginator = Paginator(movies, 12) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj' : page_obj,
    }
    return render (request, 'index.html' ,context )

    
def landingpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,'landingpage.html')

def about (request):
    return render (request, 'about.html')


def register(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'it was created'+ user)
            return redirect('home')
        else:
            messages.info(request,'invalid username or password')
  
       
    return render (request,'register.html',{'form':form})
   
   
   
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user )
            return redirect('home')
        else:
            messages.info(request,'invalid username or password')        
    return render(request,'login.html')

def logout_user(request):
        logout(request)
        return redirect('landingpage')


@login_required
def blog(request):
    form = create_blog()
    if request.method == 'POST':
        form = create_blog(request.POST)
        if form.is_valid():
            form= form.save(commit=False)
            form.created_by = request.user
            form.save()
            messages.success(request, "blog created successfully!")
            return redirect('home')
        else:
            messages.info(request,'not bad')  
   
    return render (request,'blogs.html',{'form':form})
   
@login_required
def edit_blog(request, pk):
    blog = get_object_or_404(movie, pk=pk) 
    form = create_blog(instance=blog)  

    if request.method == 'POST':
        form = create_blog(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home') 
    return render(request, 'edit.html', {'form': form})
   
            
@login_required
def delete_blog(request,pk):
    edit = movie.objects.get(pk=pk)
    if request.method == 'POST':
        edit.delete()
        return redirect('home')
    
    
def profile_pic(request):
    upload = upload_img (instance=request.user.profile)
    uploadprofile = upload_profile(instance=request.user)
    if request.method == 'POST':
         upload = upload_img(request.POST, request.FILES, instance=request.user.profile)
         uploadprofile = upload_profile(request.POST, instance=request.user)
         if upload.is_valid and uploadprofile.is_valid():
             upload.save()
             uploadprofile.save()
             return redirect('profile')
    
    context={
        'upload':upload,
        'uploadprofile':uploadprofile
       
    }
    
    return render (request,'profile.html',context)
  
  
  
  
  
  
  
        
def image(request):
    return render (request,'image.html')
        