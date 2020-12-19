from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import DoctorMore, Doctor


def index(request):
    # return HttpResponse("<h1>Home page{form}</h1>",)
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        department = request.POST['txtEmpPhone']
        print(username, password1, password2, email, department)
        if password1 == password2:
            doct_obj = Doctor.objects.create(
                username=username, email=email, password=password1)
            Doctor.save
            DoctorMore.objects.create(
                user=doct_obj, department=department)
            DoctorMore.save
        return render(request, 'wdw-snippet.html')

    else:
        # form = DoctorForm()
        # more = DoctorMoreForm()
        return render(request, 'wdw-snippet.html')
