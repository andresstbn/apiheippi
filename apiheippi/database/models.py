from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from .db import db
from dataclasses import dataclass


@dataclass
class User(db.Model):
    """ Abstracción del usuario base. De él derivan los otros tipos 
    de usurio existentes. """
    id: int
    username: str
    email: str
    phone: str
    address: str
    type: str

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=False, nullable=True)
    address = db.Column(db.String(120), unique=False, nullable=True)
    type = db.Column(db.String(20))
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }


@dataclass
class HospitalUser(db.Model):
    id: int
    __tablename__ = 'hospital_user'
    id = Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    services = relationship("MedicalService")
    __mapper_args__ = {
        'polymorphic_identity': 'hospital',
    }


@dataclass
class PatientUser(db.Model):
    id: int
    clinic_history: ClinicHistory
    __tablename__ = 'patient_user'
    id = Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    birthdate = db.Column(db.Date)
    clinic_history_id = db.Column(db.Integer, ForeignKey('clinic_history.id'))
    __mapper_args__ = {
        'polymorphic_identity': 'patient',
    }


@dataclass
class DoctorUser(db.Model):
    id: int
    __tablename__ = 'doctor_user'
    id = Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'doctor',
    }


@dataclass
class MedicalService(db.Model):
    id: int
    name: str
    hospital_id: int
    hospital: HospitalUser

    __tablename__ = 'medical_service'

    """ Abstracción de los servicios médicos que brinda un HospitalUser """
    # Este podría ser un Many To Many Field pero agregaría complejidad innecesaria.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    hospital_id = db.Column(db.Integer, ForeignKey('hospital_user.id'))


@dataclass
class ClinicHistory(db.Model):
    id: int
    patient: str
    registers: ClinicHistoryRegister

    __tablename__ = 'clinic_history'
    id = db.Column(db.Integer, primary_key=True)
    patient = relationship("PatientUser")
    registers = relationship("ClinicHistoryRegister")


@dataclass
class ClinicHistoryRegister(db.Model):
    id: int
    date: str
    content: str

    __tablename__ = 'clinic_history_register'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    clinic_history_id = db.Column(db.Integer, ForeignKey('clinic_history.id'))
    content = db.Column(db.String(500), nullable=False)
