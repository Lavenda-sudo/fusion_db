"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from myapp import views
from myproject import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new-products/', views.add, name='add'),
    path('delete-products/<int:id>', views.delete_products, name='delete'),
    path('edit-products/<int:id>', views.edit_products, name='edit'),
    path('details/<int:id>', views.details, name='details'),
    path('accounts/login', views.signin, name='login'),
    path('accounts/signup', views.signup, name='register'),
    path('accounts/logout', views.signout, name='sign-out'),
    path('accounts/', include('django.contrib.auth.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# /delete-products/100