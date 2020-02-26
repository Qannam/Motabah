from django.urls import path, include

from . import views

app_name = 'eval'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:child_id>/', views.childDetails, name='detail'),
    path('<int:child_id>/UGFyZW50IFBhZ2UgKE9ubHkgUGFyZW50KQ==', views.childDetails, name='detail_parent'),
    path('<int:child_id>/UGFyZW50IFBhZ2UgKE9ubHkgUGFyZW50KQ==/evaluation', views.evaluation, name='evaluation'),
    path('<int:evaluation_id>/UGFyZW50IFBhZ2UgKE9ubHkgUGFyZW50KQ==/delete', views.evaluationDelete, name='evaluation_delete'),
    path('UGFyZW50IFBhZ2UgKE9ubHkgUGFyZW50KQ==', views.parentIndex, name='parent index'),
    
    path('<int:child_id>/UGFyZW50IFBhZ2UgKE9ubHkgUGFyZW50KQ==/evaluation/<str:message>', views.evaluation, name='evaluation_message'),
    path('<int:child_id>/UGFyZW50IFBhZ2UgKE9ubHkgUGFyZW50KQ==/<str:message>', views.childDetails, name='detail_parent_message'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('setLang/', views.setLanguage, name='set_language'),
]