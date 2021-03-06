"""songuard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    #admin line is default and unedited
    url(r'^admin/', admin.site.urls),

    #anything beyond/apart from admin is pushed to urls in the songlist app.
    #url(r'^songlist/', include('songlist.urls'))
    url(r'', include('songlist.urls'))

]

#
# urlpatterns += patterns(
#     # 'django.contrib.auth.views',
#     #
#     # url(r'^login/$, 'login',
#     #     {'template_name': 'login.html'},
#     #     name='songuard_login'),
#     #
#     # url(r'^logout/$, 'logout',
#     #     {'next_page': 'songuard_home'},
#     #     name='songuard_logout'),
#
#
#
# )
