"""SummerProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.blogs, name ='root' ),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^blog/(?P<pk>\d*)/$', views.blog_view, name="blog_view"),
    url(r'^blog/create/$', views.blog_create, name = "blog_create"),
    
    url(r'^api/blog/', include('Blog.api.urls', namespace = 'api-blogs')),
]
