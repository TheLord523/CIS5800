from website import create_app
#from . import db
app = create_app()
#need secret key otherwise the session is unavailable when you use flash
#app.secret_key = 'yurr'

if __name__ == '__main__':
    #If this doesn't work, change the Python interpreter to 3.7.4 or 3.8
    #You get an error with 3.9
    app.run(debug=True, port=5001)
