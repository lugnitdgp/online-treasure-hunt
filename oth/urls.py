from django.conf.urls import url

from oth import views


urlpatterns = [
    #url(r'^$', views.landing, name='landing'),
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='index'),
    url(r'^answer/$', views.answer , name='answer'),
    url(r'^lboard/$', views.lboard , name='lboard'),
    url(r'^rules/$', views.rules , name='rules'),
    url(r'^story/$', views.story , name='story'),
    url(r'^story2/$', views.story2 , name='story2'),
    url(r'^story3/$', views.story3 , name='story3'),
    url(r'^api/scoreboard/$',views.leaderboard_api,name='leaderboard_api'),
]

