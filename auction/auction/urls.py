from django.conf.urls import patterns, include, url
from auction.views import HomeView, WhoAmIView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',
        include(admin.site.urls),
        name='admin_home'
    ),
    
    url(r'^$',
        HomeView.as_view(),
        name='auction_home'
    ),
    
    url(r'^whoami/$',
        WhoAmIView.as_view(),
        name='auction_whoami'
    ),
)
