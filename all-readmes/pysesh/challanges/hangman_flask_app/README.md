# Flask Hangman challenge

In one of the previous challenges, we created a game of
hangman which could be played directly with the python command
line. 

What would we do if we wanted to create a web site where
we could play hangman instead? The solution is Flask. 
Flask is a simple and lightweight way to create dynamic web pages.

Before you get started on this task, you probably need to 
know a little bit about how web pages work. 

- a web page is stored as a html file. Flask uses a template
and just changes some parameters within it
- cookies are where we store some information about a visitor
to a webpage. In Flask, cookies are handled via `session`. We can treat
it like a dictionary and add or remove stuff from it.
- aside from cookies/sessions Flask apps are meant to be 
"stateless". i.e. it cant/shouldnt remember something from
one page visit to the next. You store changes either in
a database, or in cookies.

I created a rough skeleton which:
 - sends parameters to a html template
 - updates the session
 - erases the session when `/reset` url is visited.
 
Your task now is to plug in rest of the hangman game and get it working.

## how to start your flask application 

Open anaconda prompt. cd into folder named hangman_flask_app. Run these two commands:

```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
Once running visit this link:

http://localhost:5000

