from flask import Flask, request

from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)


@app.route("/data", methods=['GET', 'POST'])
def process_form():
    if request.method == "POST":
        data = {key:value for key, value in request.form.items()} # convert ImmutableMultiDict
        # Stubbed function #1
        save_form_to_db(data)

    # Just grab the last record from the db and display that
    last_person = mongo.db.data.find(sort=[('$natural',-1)], limit=1).next()
    return "The last person to fill out this form was {}".format(last_person['name'])


# Stub #1
def save_form_to_db(data):
    # the input variable `data` will look like
    # {
    #  "name": "Some Name", 
    #  "age", 32,
    #  "email_address": "some@email.com"
    # }
    # call a function `validate_email(email_string)`, which returns a boolean, and
    # if true, save the data to mongo collection `data`
    # assume that `mongo` has already been defined as `mongo = PyMongo(app)`
    pass


# Stub #2
def validate_email(email_string):
    # return a boolean indicating whether the email is a valid email string
    pass


if __name__ == '__main__':
    app.run(debug=True)
