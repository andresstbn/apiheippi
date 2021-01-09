from apiheippi import create_app
from apiheippi.database.models import User, HospitalUser, PatientUser, DoctorUser, MedicalService, ClinicHistory, ClinicHistoryRegisters
from apiheippi.database.db import db

app = create_app()
db.create_all(app=app)

# with app.app_context():
    # admin = User(username='admin', email='admin@fooheippi.com')
    # patients = PatientUser(username='Pedro', email='admin@fooheippi.com')
    # hospitals = HospitalUser(username='', email='guest@fooheippi.com')
    # doctors = DoctorUser(username='guest', email='guest@fooheippi.com')
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()
