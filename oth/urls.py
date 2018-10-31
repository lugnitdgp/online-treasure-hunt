from django.conf.urls import url

from oth import views


urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    # url(r'^$', views.index, name='index'),
    # url(r'^home/$', views.index, name='index'),
    # url(r'^answer/$', views.answer , name='answer'),
    # url(r'^lboard/$', views.lboard , name='lboard'),
    # url(r'^rules/$', views.rules , name='rules'),
    # url(r'^story/$', views.story , name='story'),
    url(r'^api/scoreboard/$',views.leaderboard_api,name='leaderboard_api'),
]

