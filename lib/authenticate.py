#This is all about AUTHENTICATION ******Work in Progress.   I don't know what I'm doing here?????
#We used functools.

from flask import Flask
app = Flask(__name__)

def authenticate(func):
    def wrapper(*args, **kwargs):
        if authenticated:
            return func(*args, **kwargs)
        
        else:
            return "Unauthorized", 401
        
    return wrapper

@app.route('/')
@authenticate
def protected_route():
    return 

if __name__ == '__main':
    app.run