
from email import message
from django.template import Template, Context
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Package, CustomUser, Agent, book ,Travel_mode
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import AgentSignUpForm, PackageForm, UserSignUpForm, AgentSignUpForm, AgentDetailForm
from django.contrib.auth.decorators import login_required
from .decorators import agent_only, customer_only
from django.utils import timezone as tz
from django.db.models import Q


# Create your views here.


def index(request):
    if request.user.is_authenticated and request.user.is_customer:
        return redirect('package')
    elif request.user.is_authenticated and request.user.is_agent:
        return redirect('agent_packages')

    return render(request, 'backpacker/index.html')


def user_signup(request):
    form = UserSignUpForm

    context = {
        'form': form

    }
    if request.method == 'POST':
        form = UserSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            #user.username = user.username.lower()
            #user.save()
            login(request, user)
            return redirect('package')
        else:
            messages.error(request, 'An error occurred during registration')
            return redirect('signup')
    else:
        return render(request, "backpacker/signup.html", context)


def agent_signup(request):
    profile_form = AgentSignUpForm
    detail_form = AgentDetailForm
    context = {
        'profile_form': profile_form,
        'detail_form': detail_form
    }
    if request.method == 'POST':
        profile_form = AgentSignUpForm(request.POST)
        detail_form = AgentDetailForm(request.POST)
        if all((profile_form.is_valid(), detail_form.is_valid())):
            profile = profile_form.save()
            detail = detail_form.save(commit=False)
            detail.User = profile
            detail.save()
            return redirect('agent_packages')
        else:
            messages.error(request, 'An error occurred during registration')
            return redirect('agent_signup')

    return render(request, "backpacker/agent_signup.html", context)


def login_page(request):
    if request.user.is_authenticated:
        if user.is_customer == True:
            return redirect('package')
        elif user.is_agent == True:
            return redirect('agent_packages')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            messages.error(
                request, 'Username OR password is  not correct ,recheck and try again')
            return redirect('login')
        if user.is_customer == True:
            return redirect('package')
        elif user.is_agent == True:
            return redirect('agent_packages')

    return render(request, 'backpacker/login.html')


def logoutUser(request):
    logout(request)
    return redirect('index')


def is_valid_queryparam(param):
    return param != '' and param is not None


@login_required(login_url='login')
@customer_only
def package(request):

    today = tz.localtime(tz.now()).date()

    packages = Package.objects.filter(ddate__gt=today)
    packages=packages.filter(slots__gt=0)
    agents = Agent.objects.all()
    destination = request.GET.get('destination')
    departure = request.GET.get('departure')
    min_cost = request.GET.get('min_cost')
    max_cost = request.GET.get('max_cost')
    min_date = request.GET.get('min_date')
    max_date = request.GET.get('max_date')
    agent = request.GET.get('agent')
    min_dur = request.GET.get('min_dur')
    max_dur = request.GET.get('max_dur')
    type = request.GET.get('type')

    if is_valid_queryparam(destination):
        packages = packages.filter(Location__icontains=destination)

    if is_valid_queryparam(departure):
        packages = packages.filter(dloc__icontains=departure)
    if is_valid_queryparam(min_cost):
        packages = packages.filter(cost__gte=min_cost)
    if is_valid_queryparam(max_cost):
        packages = packages.filter(cost__lte=max_cost)
    if is_valid_queryparam(min_date):
        packages = packages.filter(ddate__gte=min_date)
    if is_valid_queryparam(max_date):
        packages = packages.filter(ddate__lte=max_date)
    if is_valid_queryparam(agent) and agent != 'Choose...':
        packages = packages.filter(agent__name=agent)
    if is_valid_queryparam(min_dur):
        packages = packages.filter(duration__gte=min_dur)
    if is_valid_queryparam(max_dur):
        packages = packages.filter(duration__lte=max_dur)
    if is_valid_queryparam(type) and type != 'Choose...':
         packages = packages.filter(mode__contains = type)
    # # if is_valid_queryparam(type) and type != 'Choose...':
    # #     packages = packages.filter(mode=type)
        
    context = {
        'packages': packages,
        'agents': agents
        
    }
    return render(request, 'backpacker/contents.html', context)


@login_required(login_url='login')
@customer_only
def package_details(request, pk):
    package = Package.objects.get(id=pk)
    context = {'package': package}
    if request.method == "POST":

        nos = int(request.POST.get('nos'))
        bord= request.POST.get('station')
        if nos >= 1:
            price = nos*package.cost
            user = request.user
            package_name = package
            agent_name = package.agent
            books = book.objects.create(user=user, package=package_name, price=price,
                                        nos=nos, agent=agent_name,boarding=bord, status=True)
            package.slots = package.slots-nos
            if request.user not in package.users.all():
                package.users.add(request.user)
            package.save()
            request.session['book_id'] = books.id

            return redirect('booking_success')
        else:
            messages.error(request, 'An error occured')

    return render(request, 'backpacker/package_details.html', context)


@login_required(login_url='login')
@customer_only
def booking_success(request):
    bookid = request.session['book_id']
    order = book.objects.get(id=bookid)
    context = {
        'order': order
    }

    return render(request, 'backpacker/booking_success.html', context)


@login_required(login_url='login')
@customer_only
def bookinglist(request):
    user = request.user
    order = book.objects.filter(user=user)
    # package=Package.objects.filter()
   
    context = {
        'order': order,
       
    }

    return render(request, 'backpacker/bookinglist.html', context)


@login_required(login_url='login')
@customer_only
def cancel_booking(request, pk):
    
    ord = book.objects.get(id=pk)
    package=Package.objects.get(title=ord.package)
    if request.method=='POST':
        nos = int(request.POST.get('nos'))
        package.slots=package.slots+nos
        print(package)
        print(package.slots)
        package.save()
        ord.nos=ord.nos-nos
        print(ord.nos)
        if ord.nos==0:
            ord.status = False
        ord.save()
        return redirect('bookinglist')

    
    
    context = {
        'ord': ord
    }

    return render(request, 'backpacker/bookingcancel.html', context)


@login_required(login_url='login')
@agent_only
def agent_packages(request):
    user = request.user
    age = Agent.objects.get(User=user)
    pack = Package.objects.filter(agent=age)
   

    context = {
        'pack': pack,
       
    }
    return render(request, "backpacker/agent_packages.html", context)

@login_required(login_url='login')
@agent_only
def package_status(request,pk):
    package=Package.objects.get(id=pk)
    ps=package.users.all()
    print(ps)
    
    orders=book.objects.filter(package=package)

    x=0
    for ord in orders:
        x=x+ord.nos

    context={
        'ps':ps,
        'package':package,
        'x':x,
        
    }


    
    return render(request, "backpacker/packagestatus.html",context)


def user_detail(request,uname):
    u=CustomUser.objects.get(username=uname)
   
    context={
        'u':u
    }
    return render(request,"backpacker/userdetail.html",context)



def Agentdetails(request,name):
    u=CustomUser.objects.get(username=name)
   
    context={
        'u':u
    }
    return render(request,"backpacker/Agentdetails.html",context)





@login_required(login_url='login')
@agent_only
def create_package(request):
    form = PackageForm
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PackageForm(request.POST ,request.FILES)
        if form.is_valid():
            p=form.save(commit=False)
            u = request.user
            age = Agent.objects.get(User=u)
            p.agent = age
            
            print (age)
            print(p.agent)
            p.save()
            return redirect('agent_packages')
        else:
            print (form.errors)
            return HttpResponse(form.errors.values())
            

            # messages.error(request, 'An error occurred during registration')
            # return redirect('create')
    return render(request, "backpacker/create_package.html", context)


@login_required(login_url='login')
@agent_only
def package_edit(request, pk):
    package = Package.objects.get(id=pk)
    form = PackageForm(request.POST or None,instance=package)
    
    if request.method == 'POST':
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('agent_packages')
        else:
            messages.error(request, 'An error occurred during editing')
            return redirect('agent_packages')

    context = {
        'package': package,
        'form': form
    }
    return render(request, "backpacker/create_package.html", context)

@login_required(login_url='login')
@agent_only
def bookinglist_agent(request):
    user = request.user
    print(user)
    order = book.objects.filter(agent__User=user)
    # package=Package.objects.filter()
   
    context = {
        'order': order,
       
    }

    return render(request, 'backpacker/bookinglist_agent.html', context)