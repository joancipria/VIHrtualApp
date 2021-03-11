# Vihrtual-App - HIV Chatbot


## 👷‍ Installation

Clone repo
```
cd vihrtual-app
git clone
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
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple`
pip3 install rasa[spacy]
python3 -m spacy download es_core_news_md
python3 -m spacy link es_core_news_md es
```


This will install the bot and all of its requirements.

## 🤖 To run Vihrtual-App:

Use `rasa train` to train a model 

Run `rasa shell` ff you want to speak to the assistant

Run `rasa x` to start Rasa X server


## 👩‍💻 Overview of the files

`data/stories.yml` - contains stories 

`data/nlu.yml` - contains NLU training data

`data/rules.yml` - contains rules

`actions` - contains custom action code

`domain.yml` - the domain file, including bot responses

`config.yml` - training configurations for the NLU pipeline and policy ensemble

## :gift: License
Licensed under the GNU General Public License v3.