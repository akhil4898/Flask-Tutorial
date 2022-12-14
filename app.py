# # Flask Tutorial...


# from flask import Flask, render_template        # Import the Flask module from flask...

# # Here, __name__ is the name of current module...

# # Here Flask is a constructor & __name__ as the argument into the Flask constructor....

# #An object (app) of the Flask class is considered as the WSGI application.

# app = Flask(__name__)               #Creating the Flask class object...So, Here app is the object...

# # The route() function of the Flask class defines the URL mapping of the associated (related) function.

# # @app.route('/home/<int:age>')                     # decorator defines the
# # def home(age):                 
#     # return "Your age is: " + str(age)
#     # return 'Hello world! This is Akhil Upadhyay'
    
# @app.route("/")
# def home():
#     return render_template('index.html')                   # render_template always used with return statement.

# @app.route('/products')
# def product():
#     return "This is my product's hi page"


# # Finally, the run method of the Flask class is used to run the flask application on the local development server.
# if __name__ == '__main__':
#         app.run(debug=True, port=8000)









# from flask import redirect
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

def about():
    return "This is about page..."

def viewThis():
    return "This is very good city..."

# # Another approach to perform routing for the flask web application
app.add_url_rule('/viewThis', "city", viewThis)
app.add_url_rule('/about', "about", about)






# @app.route('/')
# def home():
#     return "Welcome to my first page!"

# @app.route('/admin')
# def admin():
#     return "admin"

# @app.route('/librarian')
# def librarian():
#     return "librarian"

# @app.route('/student')
# def student():
#     return "student"

# @app.route('/user/<string:name>')
# def user(name):
#     if name == 'admin':
# # There is a specific function named user() which recognizes the user the redirect the user to the exact function which contains the implementation for this particular function.
#         return redirect(url_for('admin'))                      
#     if name == 'librarian':
#        return redirect(url_for('librarian'))
#     if name == 'student':
#        return redirect(url_for('student'))







# Databasde connection..

# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy  
# from datetime import datetime

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///akhil.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
# db = SQLAlchemy(app)

 
# class Todo(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     desc = db.Column(db.String(500), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)


#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.title}"


# @app.route('/')
# def home():
#     todo = Todo(title="First todo", desc="Start investing in stock market...")
#     db.session.add(todo)
#     db.session.commit()
#     return render_template('index.html')







# from flask import Flask
# from flask import request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     val = request.args.get("var")
#     return f"Hello World! {val}"




if __name__ == '__main__':
    app.run(debug=True)