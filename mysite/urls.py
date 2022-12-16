from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('polls/',views.index,name='index'),                                #/polls/
    path('polls/<int:question_id>/',views.detail,name='detail'),            #/polls/5/
    path('polls/<int:question_id>/results/',views.results,name='results'),  #/polls/5/results/
    path('polls/<int:question_id>/vote/',views.vote,name='vote'),           #/polls/5/vote/
]