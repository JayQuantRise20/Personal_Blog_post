from flask import Flask,jsonify,request
from app import db
import uuid

class User:


    def signup(self):

        print(request.form)

        User = {
            "_id":uuid.uuid4().hex,
            "name":request.form.get('name'),
            "email":request.form.get('email'),
            "password":request.form.get('password')
        
        }

        db.users.insert_one(User)

        return jsonify(User), 200


      
