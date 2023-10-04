from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login,logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ContactForm



# Create your views here.
def home(request):
    # return HttpResponse('Hi')
   #paginator starts

    myproduct = Product.objects.all()
    paginator = Paginator(myproduct,3)  # Show 3contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "test1/home.html", {"page_obj": page_obj})

def search(request):
    # query = request.GET['query']
    if request.method == 'POST':
        query = request.POST.get('field1')
        # query = request.GET('field1')
        print(query)
        if len(query) > 0 :
            if Product.objects.filter(title__icontains=query):
                k = Product.objects.filter(title__icontains=query)
                return render(request,"test1/search.html",{'x':k})
            else:
                return HttpResponse('item not found')
        else:
            return redirect("show")
        


def show(request):
    myproducts = Product.objects.all()
    return render(request,"test1/search.html",{'x':myproducts})
     
def contact(request):
    form = ContactForm
    return render(request, 'test1/contact.html',{'form': form})

def add_record(request):
    if request.method=="POST":
        form=ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')



   # paginator ends

   #Filter  starts

def  allproducts(request):
    if request.method == 'GET':
        myproducts = Product.objects.all()
        return render(request,"test1/filter.html",{'x':myproducts})
    else:
        z = request.POST.get('myfood')
        print (z)
        m = float(request.POST.get('price_range'))
        print(m)
        k = Product.objects.filter(category=z, price__lte=m )
        # k = Product.objects.filter(category=z)
        print(k)
        # return HttpResponse('Hello')
        return render(request, "test1/filter.html", {'x': k})
    
    

    
    

def signupuser(request):
    if request.method == 'GET':
        return render(request,'test1/signupuser.html',{'form':UserCreationForm()})
    else:
        if(request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('home')
            except IntegrityError:
                return render(request,'test1/signupuser.html',{'form':UserCreationForm(),'y':'Username already taken'})
            
        else:
            return render(request,'test1/signupuser.html',{'form':UserCreationForm(),'z':'Passwords not matched'})




def loginuser(request):
    if request.method == 'GET':
        return render(request,'test1/loginuser.html',{'form':AuthenticationForm()})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'test1/loginuser.html',{'form':AuthenticationForm(),'k':'Invalid username or password'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')




def myhome(request):
    return render(request,'test1/myhome.html')



# @login_required
def details(request,pid):
    if request.user.is_authenticated:
        myproduct = get_object_or_404(Product,pk=pid)
        return render (request,'test1/details.html',{'z':myproduct})
    else:
        return redirect ('loginuser')
       
    


def aboutus(request):
    return render(request,'test1/aboutus.html')

    
