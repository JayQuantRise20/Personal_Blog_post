from flask import Flask,render_template,jsonify,request
import uuid

import pymongo


app = Flask(__name__)


# data base
client = pymongo.MongoClient('localhost',27017)
db = client.user_login


from user import routes


class User:


    def signup(self):

        print(request.form)

        User = {
            "_id":uuid.uuid4().hex,
            "name":request.form.get('name'),
            "email":request.form.get('email'),
            "password":request.form.get('password')
        
        }


        return jsonify(User), 200






@app.route('/')
def home():

    return  render_template('home.html')



@app.route('/dashboard')
def dashboard():
    return  render_template('dashboard.html')



@app.route('/user/signup',methods=['POST'])
def signup():

    return User().signup()




def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
