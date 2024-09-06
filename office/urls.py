from django.urls import path
from office.views import AddApointment, DeleteApointment, EditApointment, ViewTransaction, AddService, AppointmentListAPIView

urlpatterns = [
    path('add_appointment/', AddApointment.as_view(), name='add_appointment'),
    path('delete_appointment/<int:pk>/', DeleteApointment.as_view(), name='delete_appointment'),
    path('edit_appointment/<int:pk>/', EditApointment.as_view(), name='edit_appointment'),
    path('view_transaction/', ViewTransaction.as_view(), name='view_transaction'),
    path('add_service/', AddService.as_view(), name='add_service'),
    path('appointment_list/', AppointmentListAPIView.as_view(), name='appointment_list'),
]