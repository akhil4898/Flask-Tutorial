# # # Flask Tutorial...


# # from flask import Flask, render_template        # Import the Flask module from flask...

# # # Here, __name__ is the name of current module...

# # # Here Flask is a constructor & __name__ as the argument into the Flask constructor....

# # #An object (app) of the Flask class is considered as the WSGI application.

# # app = Flask(__name__)               #Creating the Flask class object...So, Here app is the object...

# # # The route() function of the Flask class defines the URL mapping of the associated (related) function.

# # # @app.route('/home/<int:age>')                     # decorator defines the
# # # def home(age):                 
# #     # return "Your age is: " + str(age)
# #     # return 'Hello world! This is Akhil Upadhyay'
    
# # @app.route("/")
# # def home():
# #     return render_template('index.html')                   # render_template always used with return statement.

# # @app.route('/products')
# # def product():
# #     return "This is my product's hi page"


# # # Finally, the run method of the Flask class is used to run the flask application on the local development server.
# # if __name__ == '__main__':
# #         app.run(debug=True, port=8000)









# # from flask import redirect
# from flask import Flask, render_template, redirect, url_for

# app = Flask(__name__)




# # @app.route('/')
# # def home():
# #     return render_template('index.html')




# # def about():
# #     return "This is about page..."

# # def viewThis():
# #     return "This is very good city..."

# # Another approach to perform routing for the flask web application
# # app.add_url_rule('/about', "city", viewThis)
# # app.add_url_rule('/about', "about", about)






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
   


# if __name__ == '__main__':
#     app.run(port=8080, debug=True)