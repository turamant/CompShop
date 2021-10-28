from django.urls import path

from vendor.views import become_vendor

urlpatterns = [
    path('become-vendor/', become_vendor, name='become_vendor'),

]