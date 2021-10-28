from django.shortcuts import render

# Create your views here.


def become_vendor(request):
    return render(request, 'vendor/become_vendor.html')

