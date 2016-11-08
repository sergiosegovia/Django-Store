from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='store_home'),
    url(r'^products/(?P<slug>[\w-]+)/$', views.ProductDetail.as_view(), name='product_detail'),
    url(r'^products/create', views.create_product, name='create_product'),
    url(r'^login', views.login_view, name='login_view'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
]
