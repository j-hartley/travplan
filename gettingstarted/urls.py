from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^account/', include(('social_django.urls','account'), namespace='social')),
    url(r'^account/', include(('django.contrib.auth.urls','account'), namespace='auth')),
    url(r'^profile/$', hello.views.update_profile),
    url(r'^account/logout/$', hello.views.Logout),
    url(r'^admin/', admin.site.urls),
]
