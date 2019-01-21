from bottle import default_app, route, template, post, debug, request;


#had to do it this way to solve odd issue with potentially redefining
#db here when it was defined in db.py
import db as db;

db = db.DB();

#to validate that the connection works
"""
#print(db.query("SELECT * FROM users"));

"""

@route('/')
def landingpage():
    return template("signUp.html");

@post('/result')
def result():
    #serverside validadtion for the user entering an actual number and not
    #some arbitrary string
    try:
        studentID = int(float(request.forms.get('studentID')));
    except ValueError:
        return "You have mis-entered the studentID. Please enter all numbers";

    cursor = db.query("SELECT * FROM users WHERE studentID=" + str(studentID));
    if cursor:
        presentTime = request.forms.get ('select');
        name = request.forms.get('name');
        #escapes the values given from the user
        db.query("INSERT INTO users (studentID, name, presentTime) VALUES (%s, %s, %s)", (studentID, name, presentTime));
        return template("result.html", db=db);
    else:
        modify();

@route('/view')
def view():
    return template("result.html", db=db);

@route('/modify')
def modify():
    return template("modify.html");


#REMOVE ONCE DONE DEVELOPING
debug(True);
application = default_app();
