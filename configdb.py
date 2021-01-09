from apiheippi import db, create_app
from apiheippi.models import User, HospitalUser, PatientUser
app = create_app()
db.create_all(app=app)

with app.app_context():
    admin = User(username='admin', email='admin@fooheippi.com')
    guest = User(username='guest', email='guest@fooheippi.com')
    # hospital1 = HospitalUser()
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

