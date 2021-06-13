# radiology-image-webapp
An example web app using flask and sqlite.

Run these commands in terminal for installing project dependencies:

`pip install -r requirements.txt`

Run these commands in terminal to run it locally:

```text
$ git clone https://github.com/mah-moh/radiology-image-webapp.git
$ cd radiology-image-webapp
$ python app.py
```

App should be running on `http://localhost:5000`

Run these commands in seperate terminal window for sqlite3 setup:

```text
$ python
$ from app import db
$ db.create_all()
```