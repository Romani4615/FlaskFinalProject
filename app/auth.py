from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()
@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
@token_auth.verify_token
def verify_token(token): #name of function checking token7   
    user = User.check_token(token)
    if user:
        return user 
    