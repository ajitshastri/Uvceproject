from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *


# Create your views here.

def Movies_List(request):
    Latest_Movies = Movie.objects.filter(Movie_Year__startswith=2019)[:6]
    Kannada_Movies = Movie.objects.filter(Movie_Language__startswith="Kannada")[:6]
    Telgu_Movies = Movie.objects.filter(Movie_Language__startswith="Telgu")[:6]
    rate = Movie.objects.filter(Movie_Rating__startswith=8).order_by('Movie_Rating').reverse()[:6]
    return render(request,'Movie/movies_list.html',{'Latest':Latest_Movies,'Kannada':Kannada_Movies,'Telgu':Telgu_Movies,'Rate':rate})


def Movie_Details(request,pk):
    movie = get_object_or_404(Movie,Movie_id=pk)
    try:
        rent = Rent.objects.GET(Movie_id=pk)
    except Rent.DoesNotExist:
        rent = Rent.objects.filter(Movie_id=pk)
    return render(request,'Movie/movie_details.html',{'movie':movie,'rent':rent})


def Home(request):
    return render(request,'Movie/page.html')


def All_Movies(request):
    movies = Movie.objects.all()
    return render(request,'Movie/all_movies.html',{'movies':movies})


def Logout_View(request):
    logout(request)
    return redirect('home')


def User_View(request):
    rent = Rent.objects.filter(user=request.user)
    contact = Contact.objects.filter(user=request.user)
    return render(request,'Movie/user_view.html',{'contact':contact,'rent':rent})


def Sign_Up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')

    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})



def SearchMovies(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        #submitbutton = request.GET.get('submit')
        if query is not None:
            results = Movie.objects.get(Movie_Name__icontains='query') |Movie.objects.get(Movie_Year__icontains='query') | Movie.objects.get(Movie_Language__icontains='query') | Movie.objects.get(Movie_Genre__icontains='query').distinct()
            return render(request,'Movie/search.html',{'results':results,'submitbutton':submitbutton})
        else:
            return render(request,'Movie/search.html',)

    else:
        return render(request,'Movie/search.html')


def Mains(request):
    return render(request,'Movie/main.html')


def Email_View(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            Name = form.cleaned_data['Name']
            From_Email = form.cleaned_data['From_Email']
            Message = form.cleaned_data['Message']
            try:
                send_mail(Name,Message,Form_Email,['ajeetshastri77@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('success')
    return render(request,"Movie/contact.html",{'form':form})

def Success_View(request):
    return render(request,'Movie/success.html')


def Rented(request):
    rent =Rent.objects.filter(user=request.user)
    return render(request,'Movie/rented.html',{'rent':rent})


def Rented_Details(request,pk):
    rented_detail =  get_object_or_404(Movie,movie_id=pk)
    return render(request,'Movie/rented_details.html',{'rented_details':rented_detail})

def Watch(request):
    return render(request,'Movie/watch.html')

def rent(request,pk):
    movie = get_object_or_404(Movie,movie_id=pk)
    if request.method == 'GET':
        form = RentedForm()
    else:
        form = RentedForm(request.POST)
        if form.is_valid():
            rents = form.save(commit=False)
            rent = form.save(commit=False)
            rents.user = request.user
            rent.movie_id = Movie.objects.get(pk=pk)
            rents.save()
            return redirect('rentedsuccess')
    return render(request,'Movie/rented_form.html',{'form':form,'movie':movie})


def RentedSuccessView(request):
    return render(request,'Movie/rented_success.html')
