from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import contact
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "home.html")


def blogdelhi(request):
    return render(request, "blogdelhi.html")


def blogbangalore(request):
    return render(request, "blogbangalore.html")


def blogchennai(request):
    return render(request, "blogchennai.html")


def bloghyderabad(request):
    return render(request, "bloghyderabad.html")


def blogmumbai(request):
    return render(request, "blogmumbai.html")


def blogpune(request):
    return render(request, "blogpune.html")


def gallery(request):
    return render(request, "gallery.html")


def index1(request):
    return render(request, "home1.html")


def index2(request):
    return render(request, "home2.html")


def index3(request):
    return render(request, "home3.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("signup/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    form1 = AuthenticationForm()
    return render(request=request, template_name="signup.html", context={"login_form": form1, "register_form": form})


@csrf_exempt
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="signup.html", context={"login_form": form})


def message(request):
    msg = contact()
    msg.name = request.POST.get('name')
    msg.mail = request.POST.get('mail')
    msg.subject = request.POST.get('subject')
    msg.message = request.POST.get('message')
    msg.save()

    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def trains(request):
    return render(request, 'trains.html')


def flights(request):
    return render(request, 'flights.html')


def cars(request):
    return render(request, 'cars.html')


def main(request):
    return render(request, 'main.html')


def delhi(request):
    return render(request, 'delhi.html')


def delhi_travel(request):
    return render(request, 'delhi_travel.html')


def delhi_tours(request):
    return render(request, 'delhi_tours.html')


def delhi_security(request):
    return render(request, 'delhi_security.html')


def delhi_hotels(request):
    return render(request, 'delhi_hotels.html')


def jammu(request):
    return render(request, 'jammu.html')


def jammu_travel(request):
    return render(request, 'jammu_travel.html')


def jammu_tours(request):
    return render(request, 'jammu_tours.html')


def jammu_security(request):
    return render(request, 'jammu_security.html')


def jammu_hotels(request):
    return render(request, 'jammu_hotels.html')


def kerala(request):
    return render(request, 'kerala.html')


def kerala_travel(request):
    return render(request, 'kerala_travel.html')


def kerala_tours(request):
    return render(request, 'kerala_tours.html')


def kerala_security(request):
    return render(request, 'kerala_security.html')


def kerala_hotels(request):
    return render(request, 'kerala_hotels.html')


def mumbai(request):
    return render(request, 'mumbai.html')


def mumbai_travel(request):
    return render(request, 'mumbai_travel.html')


def mumbai_tours(request):
    return render(request, 'mumbai_tours.html')


def mumbai_security(request):
    return render(request, 'mumbai_security.html')


def mumbai_hotels(request):
    return render(request, 'mumbai_hotels.html')


def bangalore(request):
    return render(request, 'bangalore.html')


def bangalore_travel(request):
    return render(request, 'bangalore_travel.html')


def bangalore_tours(request):
    return render(request, 'bangalore_tours.html')


def bangalore_security(request):
    return render(request, 'bangalore_security.html')


def bangalore_hotels(request):
    return render(request, 'bangalore_hotels.html')


def chennai(request):
    return render(request, 'chennai.html')


def chennai_travel(request):
    return render(request, 'chennai_travel.html')


def chennai_tours(request):
    return render(request, 'chennai_tours.html')


def chennai_security(request):
    return render(request, 'chennai_security.html')


def chennai_hotels(request):
    return render(request, 'chennai_hotels.html')


def payment(request):
    return render(request, 'payment.html')


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def bot(request):
    return render(request, 'chatbot.html')


def hotel_book(request):
    return render(request, 'hotelsbook.html')


def compare(request):
    return render(request, 'vehicles.html')