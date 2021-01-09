from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from ..database.models import *
from ..database.db import db


class UserListView(Resource):
    def get(self):
        return jsonify(User.query.all())

    def post(self):
        body = request.get_json()
        user = User(**body)
        db.session.add(user)
        db.session.commit()
        id = user.id
        return {'id': str(id)}, 200


class UserView(Resource):
    def get(self, user_id):
        return jsonify(User.query.get(user_id))

    def put(self):
        return jsonify({"error": "No implementado"})

    def delete(self):
        return jsonify({"error": "No implementado"})


class ClinicHistoryListView(Resource):
    def get(self):
        return jsonify({"error": "No implementado"})

    def post(self):
        return jsonify({"error": "No implementado"})


class ClinicHistoryView(Resource):
    def get(self):
        return jsonify({"error": "No implementado"})

    def put(self):
        return jsonify({"error": "No implementado"})

    def delete(self):
        return jsonify({"error": "No implementado"})


class HospitaListView(Resource):
    def get(self):
        return jsonify({"error": "No implementado"})

    def post(self):
        return jsonify({"error": "No implementado"})


class HospitalView(Resource):
    def get(self):
        return jsonify({"error": "No implementado"})

    def put(self):
        return jsonify({"error": "No implementado"})

    def delete(self):
        return jsonify({"error": "No implementado"})
