from django . urls import path
from .views import index, myForm

urlpatterns = [
    path('', index, name='home'),
    # path('user', user, name ='user')
    #path('MyForm', myForm, name='login')
]