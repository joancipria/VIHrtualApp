# VIHrtualApp
VIHrtualApp is an opensource (spanish) HIV Chatbot built with Rasa. Check out the web frontend repo [here](https://github.com/joancipria/VihrtualApp-app/).

## 📦 Install
Tested with `Python 3.7.10` and `pip 20.1.1`.
Rasa version: `Rasa: 2.5.1` and `Rasa X: 0.39.2`

Clone repo
```
git clone https://github.com/joancipria/VihrtualApp.git
cd VihrtualApp
```
Create virtual environment
```
python3.7 -m venv ./venv
source ./venv/bin/activate
```

Install requirements
```
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
pip3 install rasa[spacy]
pip install pyspellchecker
python3 -m spacy download es_core_news_md
```


This will install the bot and all of its requirements.

## 🤖 Run

Use `rasa train` to train a model 

Run `rasa shell` if you want to speak to the assistant

Run `rasa x --rasa-x-port 8080` to start Rasa X server

Run `rasa run -m models --enable-api --cors "*" --debug` to start the API rest server

Run `rasa run actions --cors "*"` to start actions server

## 🤔 Overview

`data/nlu/vih/*.yml` - Contains NLU training data for HIV

`data/*.yml` - Contains NLU training data for chitchat, out of scope and other basic stuff.

`data/stories/*.yml` - Contains stories

`data/rules.yml` - Contains rules

`actions` - Contains custom action code

`domain.yml` - The domain file, including basic bot responses

`config.yml` - Training configurations for the NLU pipeline and policy 

## 👨‍💻 Contributing

Feel free to send a pull request to this repository with your code contributions

## 📜 License
Licensed under the GNU General Public License v3.