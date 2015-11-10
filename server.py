from flask import Flask, request

from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)


@app.route("/data", methods=['GET', 'POST'])
def process_form():
    if request.method == "POST":
        data = {key:value for key, value in request.form.items()} # convert ImmutableMultiDict
        # Stubbed function #1
        if save_form_to_db(data):
            pass
        else:
            return "Invalid email address"

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

    if validate_email(data['email_address']):
        print "Valid email"
        mongo.db.data.insert_one(data)
        return True
    else:
        print "Invalid Email"
        return False


#CrowdFlower response 825646388
def validate_email(email):
   #simple email validator
   #checks if there is @ character in email
   #domain part of email need to have at least one dot

   email_split = email.split('@')
   #email_split = email.split(sep='@')  # Works in python 3, not python 2 - oops!
   if len(email_split) == 1:
       return False
   valid = False
   if email_split[-1].find('.') >= 0:
       valid = True

   return valid


if __name__ == '__main__':
    app.run(debug=True)
