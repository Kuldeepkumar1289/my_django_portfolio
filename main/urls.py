from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_portfolio_dashboard, name='portfolio_root'),
]