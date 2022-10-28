# Flask Tutorial...


from flask import Flask, render_template        # Import the Flask module from flask...

# Here, __name__ is the name of current module...

# Here Flask is a constructor & __name__ as the argument into the Flask constructor....

#An object (app) of the Flask class is considered as the WSGI application.

app = Flask(__name__)               #Creating the Flask class object...So, Here app is the object...

# The route() function of the Flask class defines the URL mapping of the associated (related) function.

@app.route('/home/<int:age>')                     # decorator defines the
def home(age):                 
    # return render_template('index.html')                   # render_template always used with return statement.
    # return 'Hello world! This is Akhil Upadhyay'
    return "Your age is: " + str(age)

@app.route('/products')
def product():
    return "This is my product's hi page"


# Finally, the run method of the Flask class is used to run the flask application on the local development server.
if __name__ == '__main__':
        app.run(debug=True, port=8000)
