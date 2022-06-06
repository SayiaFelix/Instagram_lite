# Instagram_Lite
![InstagramLite](/static/image/bg.png)

## Author: [SayiaFelix](https://github.com/sayiaFelix/)
![InstagramLite](/static/image/bg.png)

## Description
This is an Instagram Clone application where it allows users to upload, like and comment on other peoples images/posts. Images must have captions and users are required to add their Profile after login before uploading posts.All posts will be displayed on the Profile of a user.
**Users must log in with credible emails**
![InstagramLite](/static/image/profil.png)

## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* View all images submitted by any user.
* Click on images to display more details.
* Search for users.
* Receive email when signing up.
* Follow others.
* Like Images.


## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete images
* Delete images
* Manage the application.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display all images with comments and likes | **Home page** | Clickable links to open any images in a modal |
| Display single images on modal | **On  click** | All details should be viewed|
| To add an image  | **Through Admin and also homepage** | Click on upload icon on the navbar and also on the comment section and upload respectively|
| To edit image  | **Use Admin dashboard** | Redirected to the  image form details and editing happens|
| To search  | **Enter text in search bar** | Users can search by username|
| Comment on images | **Add comments below respective image** | Users can add comments on any image|
| Like images | **Add likes to an image** | Users can add likes to images they like|



## SetUp / Installation Requirements
### Prerequisites
* python3.9
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/SayiaFelix/Instagram_lite.git
        $ cd Instagram_lite

## Running the Application
* Creating the virtual environment

        $ python3.9 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.9 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.9 manage.py test 

## Technologies Used
* Python3.9
* Django  framework and postgresql database

## Known Bugs
* User must add profile before uploading an image or viewing profiles


## License

Copyright (c) 2022 Sayia Felix

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
