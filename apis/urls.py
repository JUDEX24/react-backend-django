from django.urls import path
from apis import views

urlpatterns = [
    path("api/customers/", views.customers, name="customers"),
    path("api/customers/<int:id>", views.customer, name="customer"),
]
