# <center> Simple Quiz API </center>

<p align="center">
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version">
    <img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg" alt="python version">
</a>
  <a href="https://github.com/Inkapable/spotify-viewer/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/mashape/apistatus.svg" alt="license">
  </a>
</p>

English | [Français](./README.fr-FR.md)

---

## Introduction

This is a simple asynchronous quiz API built for a [Simple Quiz](https://github.com/Inkapa/quiz-app)

The API uses the [FastAPI](https://github.com/tiangolo/fastapi) infrastructure and a PostgreSQL database

## How does it work?

The api allows you to do the following:

- ✅ - Create a new Quiz
- ✅ - Fetch a quiz's information with a uuid key
- ✅ - Fetch a random quiz
- *✔️ - verify if an answer is correct through uuid keys (disabled by default)*


# Preview

[Live demo](https://quiz-api.liam.social)

![](https://i.imgur.com/bklpNO6.png)

## Project setup
To build the project as intended, both the API and Frontend are required.

For more information of how to setup the Frontend please refer yourself 
to the Frontend's [README page](https://github.com/Inkapa/quiz-app#project-setup)

---
To get started with the API, you must first install the python dependencies needed by the application,
to do so simply run:
```
pip install -r requirements.txt
```
---
You now need a PostgreSQL database, this can be obtained through different means.

You can either install PostgreSQL [locally](https://www.postgresql.org/download/) (possibly through docker) if you're running this on your own server

Or you can use a hosting platform, such as [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)

---
Once you have a database you simply need to create a `.env` file in your `src` directory following the `.env.sample` format.

In it put your PostgreSQL uri.

You can now run `main.py` and it'll take care of the rest
For additional configuration such as CORS, use `config.py`

## Credits

The project was built with [FastAPI](https://github.com/tiangolo/fastapi), [Ormar](https://github.com/collerek/ormar), 
[Pydantic](https://github.com/samuelcolvin/pydantic) and [Uvicorn](https://github.com/encode/uvicorn)

It is hosted using [Heroku](https://github.com/heroku)

## License

[MIT](https://github.com/Inkapa/quiz-api/blob/master/LICENSE)
