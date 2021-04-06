# Vihrtual-App

<p align="center">
    <a href="#-install">Install</a> •
    <a href="#-run">Run</a> •
    <a href="#-overview">Overview</a> •
    <a href="#-contributing">Contributing</a> •
    <a href="#-license">License</a>
</p>

![screenshot](docs/mockup.jpg)

Vihrtual-App is an opensource (spanish) HIV Chatbot built with Rasa.

⚠️⚠️ **Currently in early development** ⚠️⚠️

## 📦 Install

Clone repo
```
git clone https://github.com/joancipria/VihrtualApp.git
cd vihrtual-app
```
Create virtual environment
```
source ./venv/bin/activate
python3 -m venv ./venv
```

Downgrade pip (temporal fix)
```
pip install --upgrade pip==20.2
```

Install requirements
```
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
pip3 install rasa[spacy]
pip install pyspellchecker
python3 -m spacy download es_core_news_md
python3 -m spacy link es_core_news_md es
```


This will install the bot and all of its requirements.

## 🤖 Run

Use `rasa train` to train a model 

Run `rasa shell` if you want to speak to the assistant

Run `rasa x` to start Rasa X server

Run `rasa run -m models --enable-api --cors "*" --debug` to start the API rest server

Run `rasa run actions --cors "*"` to start actions server

## 🤔 Overview

`data/nlu/vih/*.yml` - Contains NLU training data for HIV

`data/*.yml` - Contains NLU training data for chitchat, out of scope and other basic stuff.

`data/rules.yml` - Contains stories

`data/rules.yml` - Contains rules

`actions` - Contains custom action code

`domain.yml` - The domain file, including basic bot responses

`config.yml` - Training configurations for the NLU pipeline and policy 

## 👨‍💻 Contributing

Feel free to send a pull request to this repository with your code contributions

## 📜 License
Licensed under the GNU General Public License v3.