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
         views.delete_record, name='contact-delete'),
    path('show_contacts/<int:pk>/delete_phone',
         views.delete_phone, name='delete-phone'),
    path('show_contacts/add_phone/<int:id>',
         views.add_phone, name='add_phone'),
    path('search_contact/', views.search, name='search-contact'),
    path('search_contact/<int:pk>', views.search),
    path('show_contacts/<int:id>/daystobth',
         views.days_to_birthday, name='bithday'),
    path('show_contacts/days_to/<int:day>',
         views.filtered_by_day, name='by-day-to-birthday'),

    #path('<str:filepath>/', views.download_file),
]
