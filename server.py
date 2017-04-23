from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import jinja2


app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route('/')
def index():
    """Show homepage"""

    return render_template('index.html')


@app.route('/application-form')
def apply():
    """Show application form"""

    jobs = ['Software Engineer', 'QA Engineer', 'Product Manager']
    return render_template('application-form.html', jobs=jobs)


@app.route('/application-success', methods=["POST"])
def application_complete():

    firstname = request.form.get('firstName')
    lastname = request.form.get('lastName')
    salary = request.form.get('salary')
    job = request.form.get('job')

    return render_template('application-response.html',
                            firstname=firstname,
                            lastname=lastname,
                            salary=salary,
                            job=job)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
