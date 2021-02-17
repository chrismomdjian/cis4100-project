# cis4100-project

This is a project I created for my Hardware and Software Architecture course at California State University Los Angeles. It showcases how I can build a basic Django site and host it for free using Heroku.

The site will allow users to search up retro games by their name and other key search values and return the top playthroughs and information about the game(s). I also list some of my favorite retro games.

## URL for the site
https://retro-games-app.herokuapp.com/

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
