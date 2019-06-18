import os
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "randomstring123"

app.config["MONGO_DBNAME"] = 'guitar_collection'
app.config["MONGO_URI"] = 'mongodb+srv://root:rOOtUser@myfirstcluster-2whkw.mongodb.net/guitar_collection?retryWrites=true&w=majority'

mongo = PyMongo(app)

# @app.route('/')
# @app.route('/get_guitars')
# def get_guitars():
#     guitars=mongo.db.guitars.find()
#     category_id = guitars[0]['category_id']
#     category_name = mongo.db.categories.find({"_id":ObjectId(category_id)})[0]
#     return render_template("guitars.html", guitars=guitars, category_name = category_name)


@app.route('/', methods = ["GET", "POST"])
def index():

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])


@app.route('/<username>')
def user(username):
    return "Hi " + username

@app.route('/<username/<message>')


@app.route('/')
@app.route('/get_guitars')
def get_guitars():
    return render_template("guitars.html",
                           guitars=mongo.db.guitars.find())


@app.route('/add_guitars')
def add_guitars():
    return render_template('addguitars.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_guitars', methods=['POST'])
def insert_guitars():
    guitars =  mongo.db.guitars
    guitars.insert_one(request.form.to_dict())
    return redirect(url_for('get_guitars'))


@app.route('/edit_guitars/<guitar_id>')
def edit_guitars(guitar_id):
    the_guitar =  mongo.db.guitars.find_one({"_id": ObjectId(guitar_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editguitars.html', guitar=the_guitar,
                           categories=all_categories)


@app.route('/update_guitar/<guitar_id>', methods=["POST"])
def update_guitar(guitar_id):
    guitars = mongo.db.guitars
    guitars.update( {'_id': ObjectId(guitar_id)},
    {
        'guitar_name':request.form.get('guitar_name'),
        'category_name':request.form.get('category_name'),
        'guitar_description': request.form.get('guitar_description'),
        'date_created': request.form.get('date_created')
    })
    return redirect(url_for('get_guitars'))


@app.route('/delete_guitar/<guitar_id>')
def delete_guitar(guitar_id):
# we access the tasks collection and we call remove and we pass in the task_id as the parameter.
# Key value pair inside the curly braces.We use the object ID to format or parse the task ID in a way that's acceptable to Mongo.
# Once that's in place, we want to return or redirect.So we redirect to get tasks.
# Why?
# Because once that function is complete, we want to see it disappear. We want visual evidence to see that that task is no longer on our list.
# So we redirect to the get_tasks function.
    mongo.db.guitars.remove({'_id': ObjectId(guitar_id)})
    return redirect(url_for('get_guitars'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    # accessing mongoDB data base in preperstion of the insert. category_doc is creating a new BSON formatted doc.
    category_doc = {'category_name': request.form.get('category_name')}
    # adding the category doc into the catergory table.
    mongo.db.categories.insert_one(category_doc)
    # then return a redirect back to categories.
    return redirect(url_for('get_categories'))

# the function that will direct us and render the view that allows us to add a new category in the first place.
@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)