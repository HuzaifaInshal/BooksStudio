from distutils.command.upload import upload
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import Books,Music
from .forms import BooksForm
from django.core.files.storage import FileSystemStorage
from django.db.models import Q

# Create your views here.


def splash(request):
    context={}
    return render(request,'base/Splash.html',context)

def land(request):
    context={}
    return render(request,'base/LandingPage.html',context)

def account(request):
    page='login'

    if request.user.is_authenticated:
        return redirect('main',pk=request.user.id)

    if request.method=='POST':

        if request.POST.get('submit') == 'sign_in':

            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                user=User.objects.get(username=username)
            except:
                print(request,'User doesnt exists')

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('main',pk=request.user.id) 
            else:
                print(request,'Username or password wrong mfs')

            context={'page':page}

        elif request.POST.get('submit') == 'sign_up':
            form = UserCreationForm()
            if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.username = user.username
                    user.save()
                    login(request,user)
                    return redirect('main',pk=request.user.id)
                else:
                    print(request,'An error occured during registration!!')

                context={'form':form}
    context={}    
    return render(request,'base/LoginSignup.html',context)



def main(request,pk):


    form=BooksForm()
    if request.GET.get('q')==None:
        abcd=Books.objects.all()
    else:
        q=request.GET.get('q') if request.GET.get('q')!=None else request.user
        abcd = Books.objects.filter(user__exact=q)

    if request.GET.get('p')==None:
        mzk=Music.objects.all()
    else:
        p=request.GET.get('p') if request.GET.get('p')!=None else request.user
        mzk = Music.objects.filter(user__exact=p)    


    # TO BE USED WITH DJANGO_FORMS
    # if request.method == 'POST':
    #     form = BooksForm(request.POST,request.FILES or None)
    #     if form.is_valid:
    #         form.save()
    #         return redirect('main',request.user.id)

    if request.method == 'POST':
        if request.POST.get('submit')=='book-upload':
            if request.FILES['pdf']:
                var1 = request.user
                var2 = request.POST['bookname']
                var3 = request.FILES['pdf']
                Books.objects.create(user=var1,bookname=var2,pdf=var3).save()
                return redirect('main',request.user.id)

        
        elif request.POST.get('submit')=='music-upload':
            if request.FILES['musicpath']:
                var1 = request.user
                var2 = request.POST['musicname']
                var3 = request.FILES['musicpath']
                Music.objects.create(user=var1,musicname=var2,musicpath=var3).save()
                return redirect('main',request.user.id)

    context={'abc':abcd,'form':form,'mzk':mzk}
    return render(request,'base/BSMain.html',context)

def test(request):
    context={}
    return render(request,'base/test.html',context)

def logoutUser(request):
    logout(request)
    return redirect('land')