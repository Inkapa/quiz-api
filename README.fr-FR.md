# <center> Simple Quiz API </center>

<p align="center">
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version">
    <img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg" alt="python version">
</a>
  <a href="https://github.com/Inkapable/spotify-viewer/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/mashape/apistatus.svg" alt="license">
  </a>
</p>

Français | [English](./README.md)

---

## Introduction

Ce projet est une API asynchrone simple pour un [Simple Quiz](https://github.com/Inkapa/quiz-app)

Cette API est fondé sur l'infrastructure [FastAPI](https://github.com/tiangolo/fastapi) et une base de données PostgreSQL

## Comment ça marche ?

Cette API permet d'accomplir les choses suivantes :

- ✅ - Créer un nouveau quiz
- ✅ - Récupérer les informations d'un quiz à l'aide d'un identifiant UUID
- ✅ - Récupérer les informations d'un quiz au hasard
- *✔️ - Verifier la validité d'une réponse (désactivé par défaut)*

# Démonstration

[Live demo](https://quiz-api.liam.social)

![](https://i.imgur.com/bklpNO6.png)

## Mise en place
Pour plus d'informations sur comment mettre en place le Frontend, veuillez vous referer
à son [README](https://github.com/Inkapa/quiz-app/blob/master/README.fr-FR.md#mise-en-place)

---
Pour commencer, vous devez installer les dépendances

```
pip install -r requirements.txt
```
---
You now need a PostgreSQL database, this can be obtained through different means.
Vous aurez aussi besoin d'avoir une base de données PostgreSQL.

You can either install PostgreSQL [locally](https://www.postgresql.org/download/) (possibly through docker) if you're running this on your own server
Vous pouvez soit installer PostrgreSQL [localement](https://www.postgresql.org/download/) (avec docker par exemple) si vous êtes sur un serveur

Ou vous pouvez héberger votre base de données sur une plateforme tiers telle que [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)

---
Une fois votre base de donnée obtenue, il vous faut créer un fichier `.env` dans votre repertoire `src` en suivant le modèle `.env.sample`

Dans ce fichier mettez votre URI PostgreSQL

Vous pouvez maintenant executer `main.py` et il s'occupera du reste
Pour paramétrer davantage, les CORS par exemple, utilisez `config.py`

## Crédits

Ce projet a été construit avec [FastAPI](https://github.com/tiangolo/fastapi), [Ormar](https://github.com/collerek/ormar), 
[Pydantic](https://github.com/samuelcolvin/pydantic) et [Uvicorn](https://github.com/encode/uvicorn)

Il est hébergé à l'aide avec [Heroku](https://github.com/heroku)

## License

[MIT](https://github.com/Inkapa/quiz-api/blob/master/LICENSE)
