"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
	url(r'^$', 'blog.views.index'), # post list
	url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail'), #post content
	url(r'^(?P<pk>\d+)/comments/new/$', 'blog.views.comment_new'), #new commnet create
	url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'blog.views.comment_edit'), #commnet
	url(r'^new/$', 'blog.views.post_new'), # Now Posting
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
