from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    url('add_contact/', views.add_contact, name='add-contact'),
    path('show_contacts/', views.show_all, name='show-contacts'),
    path('show_contacts/<int:pk>/',
         views.ContactDetailView.as_view(), name='contact-detail'),
    path('show_contacts/<int:pk>/update',
         views.ContactUpdateView.as_view(), name='contact-update'),
    path('show_contacts/<int:pk>/delete',
         views.ContactDeleteView.as_view(), name='contact-delete'),
    path('show_contacts/<int:pk>/add_phone',
         views.AddPhone.as_view(), name='add-phone'),
    path('show_contacts/add_phone/<int:id>',
         views.add_phone, name='add_phone'),
    path('search_contact/', views.search, name='search-contact'),
    path('search_contact/<int:pk>', views.search),
    path('<str:filepath>/', views.download_file),
]
