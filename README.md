# Guitar Database
Data-centric Development

This web application is a database of guitars that can be searched and viewed by any user. I have built this project using Flask, Python, HTML5, CSS3 and MongoDB.
The user is able to create, update and delete their own guitars.


## Demo
A live demo can be found [here](https://guitar-collection.herokuapp.com/).


## UX
My goal in the design was to make it as easy as possible to use the features of the site while striving for a minimalist design.

The intended users of the project are as follows:
- Users who are interested in guitars of all body types, makes and models.
- Users who are wanting to find out the specification of a particular guitar model.
- Users who want to share their knowledge of guitar models by adding guitars to the database.
- Users who wish to use the web application on multiple platforms.

The project helps to satisfy each user group’s request; it does this through a number of ways, explained as follows:
- **Users who are interested in guitars of all body types, makes and models.**
The web application provides a wide variety of guitar makes and models with various body types, which will continue to grow.
- **Users who are wanting to find out the specification of a particular guitar model.**
Each guitar on the database has a description and image, so the users can find out specifics of a guitar that they are interested. Other users can edit each guitar description, adding more details and also an image.
- **Users who want to share their knowledge of guitar models by adding guitars to the database.**
Users who have a wide knowledge of different guitar models can add guitars with full descriptions and images, to the database. Users can even add their own guitars that they own, to the database.
- **Users who wish to use the web application on multiple platforms.**
The web application is fully responsive so that all user groups may use the website.

Wireframes of the web application pages can be found [here](https://imgur.com/a/Vudbvck).

The following alterations were made after the mock-up phase:
Changed the accordion to displaying the guitars in cards.
Added a CSS3 gradient background animation.
Added the 80’s style text effect to the projects title.
Gradient colour styling to the navbar
Styling to buttons.


## Features
The application is fully responsive. Any user can search and view all of the guitars on the database. The guitars can also be edited and new ones can be added to the application which will get stored onto the MongoDB database. Each guitar can include the guitar name, make and model, the body type category, an image of the guitar and the date the user added the guitar.

### Features Left to Implement
As the database grows the Home page could be paginated to create a better user experience. To load thousands of recipes at one time would take too long, therefore if they were paginated with say 12 recipes to a page the loading time would be quicker and be much better for the end user.
I could also have a list of all of the guitars on another page to the Home page, and just the top viewed on the Home page.

### Database Schema
**guitar_collection**
- categories
- guitars

**categories** {<br>
 _id:<br>
category_name:<br>
},

**guitars** {<br>
_id:<br>
guitar_name:<br>
category_name:<br>
guitar_description:<br>
date_created:<br>
image_url:<br>
}<br>
Screenshots of the database can be viewed [here](https://imgur.com/a/h1Ssf6e)

## Technologies
1. HTML
2. CSS3
3. Bootstrap (3.3.7)
4. Python
5. PyMongo
6. Flask
7. JavaScript / JQuery


## Testing
I tested the application manually as follows:

1. **Home page**
    * Ensure loads correctly
    * Ensure that each guitar card loaded fully and are all following the same form.

2. **Add Guitar page**
    * Click on Add Guitar
    * Add a test Guitar and ensure that this Guitar gets added on submit.
    * I verified that the guitar can be viewed from the Home page, searched for and the full Guitar card is loaded.
    * I also verified that the test Guitar was saved in MongoDB.

3. **Search**
    * Enter any word from any part of a Guitar card eg. make, model, category.
    * I verify that the Guitar and any other Guitar which includes that word is displayed.
    * I also entered a random string of characters, which didn’t return any results.

4. **Edit Guitar page**
    * Change some data and resubmitting it.
    * This then redirects the user to the home page.
    * I then checked that the updated information was seen in that Guitar card and in MongoDB, which it was.

5. **Delete Guitar Card**
    * Click on Delete
    * This then refreshes to the Home page.
    * I then verified that the deleted guitar does not appear on the list.
    * I also searched for this guitar to check it had been deleted, and it had.


  **Works on Multiple Platforms**
- 	iPhones 5 to X
-     iPads, mini to pro
-     MacBook Pro
-     iMac, 27 inch.
-     I verified that the application works over different web browsers. I checked on:
-     Safari
-     Edge
-     iOS
-     Chrome

I had trouble with some of the CSS in the style.css sheet rendering properly in AWS Cloud 9. After some research, this seems to be a know issue in AWS.
Due to this issue, I had to put some of the CSS in the base.html page.


## Deployment
The application was coded on Cloud9 and AWS Cloud 9. I then committed the code to GITHUB at https://github.com/richdevelopments/guitar_database
The application was deployed from GITHUB to Heroku at https://guitar-collection.herokuapp.com/.
My database is stored on MongoDB. This is setup within Heroku.


## Credits

### Content
All Guitar descriptions in this application were taken from guitar shop website - GuitarGuitar and guitar manufacturers, Fender and Gibson.

### Media
All guitar picture urls were taken from guitar shop website - GuitarGuitar and guitar manufacturers - Fender and Gibson.

### Acknowledgements
For the title design I used a blog by a graphic designer called Jake Rocheleau, which looked at creative CSS3.
I got the idea of the animated background from a blog post by Vladimir Stepura, that looked at various animated backgrounds.
I significantly modified these ideas to fit the styling and sizing of the application.
