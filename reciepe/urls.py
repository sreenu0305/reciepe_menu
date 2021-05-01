from django.urls import path
from . import views

urlpatterns = [
    path('reciepe/',views.reciepe_list,name="reciepe_list"),
    path('<int:Reciepe_id>/detail/',views.detail,name="detail"),
    path('create/',views.create_reciepe,name="create")

]