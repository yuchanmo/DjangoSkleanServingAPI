from django.urls import path
import Test.views as views
app_name = 'Test'

urlpatterns = [
    path('test1/',views.test1,name='test'),
]
