"""TpDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from askit.views.index import IndexView
from askit.views.register import RegisterFormView
from django.contrib.auth import views as auth_views
from askit.views.question.list import QuestionListView
from askit.views.question.create import QuestionFormView
from askit.views.question.detail import QuestionDetailView
from askit.views.question.update import QuestionUpdateView
from askit.views.question.search import QuestionSearchView, QuestionSearchByTopicView
from askit.views.answer.create import AnswerFormView
from askit.views.answer.delete import AnswerDeleteView
from askit.views.answer.update import AnswerUpdateView
from askit.views.profile import ProfileView
from askit.views.profile_update import ProfileUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('register', RegisterFormView.as_view(), name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('question/list', QuestionListView.as_view(), name='question_list'),
    path('question/create', QuestionFormView.as_view(), name='question_create'),
    path('question/detail/<int:pk>', QuestionDetailView.as_view(), name='question_detail'),
    path('question/update/<int:pk>', QuestionUpdateView.as_view(), name='question_update'),
    path('question/search/<str:search>', QuestionSearchView.as_view(), name='question_search'),
    path('question/searchbytopic/<int:topic_id>', QuestionSearchByTopicView.as_view(), name='question_search_by_topic'),
    path('answer/<int:question_id>', AnswerFormView.as_view(), name='question_answer'),
    path('answer/<int:question_id>/<int:answer_id>', AnswerFormView.as_view(), name='answer_answer'),
    path('answer/delete/<int:pk>', AnswerDeleteView.as_view(), name='answer_delete'),
    path('answer/update/<int:pk>', AnswerUpdateView.as_view(), name='answer_update'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),
]
