import os
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo, pymongo
from flask_paginate import Pagination, get_page_parameter
from bson.objectid import ObjectId
import re


app = Flask(__name__)
app.secret_key = "randomstring123"

app.config["MONGO_DBNAME"] = 'guitar_collection'
app.config["MONGO_URI"] = 'mongodb+srv://root:rOOtUser@myfirstcluster-2whkw.mongodb.net/guitar_collection?retryWrites=true&w=majority'

mongo = PyMongo(app)

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
        'date_created': request.form.get('date_created'),
        'image_url': request.form.get('image_url')
    })
    return redirect(url_for('get_guitars'))


@app.route('/delete_guitar/<guitar_id>')
def delete_guitar(guitar_id):
# access the tasks collection and call remove and we pass in the task_id as the parameter.
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


# Search Database for Guitars
@app.route('/find_guitars', methods=['GET', 'POST'])
def find_guitars():
    if request.method=='POST':

        # get the search term
        search_term = request.form.get("search_term")

        #  create the index
        mongo.db.guitars.create_index( [("$**", 'text')] )

         # search with the search term that came through the form
        cursor = mongo.db.guitars.find({ "$text": { "$search": search_term } })
        guitars = [guitar for guitar in cursor]

        # send guitars to page
        return render_template('search.html', guitars=guitars, query=search_term)

    return render_template('search.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)