from flask import Blueprint
from .views import *

def initialize_routes(api):
    api.add_resource(UserListView, '/users/')
    api.add_resource(UserView, '/users/<int:user_id>/')
    api.add_resource(ClinicHistoryListView, '/clinic_history/')
    api.add_resource(ClinicHistoryView, '/clinic_history/<int:clinic_history_id>')
    api.add_resource(HospitaListView, '/hospital/')
    api.add_resource(HospitalView, '/hospital/<int:hospital_id>/'
