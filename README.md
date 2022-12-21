<h1 align="center">
    <br>
    <img style="width: 50%" src="https://raw.githubusercontent.com/joancipria/VIHrtualApp-app/master/logo.png" alt="VIHrtual-App">
</h1>
A conversational agent which uses machine learning to offer an engaging sex educational tool to promote HIV/STI awareness and prevention. VIHrtual-App can identify more than 250 STI/HIV-related questions and respond accordingly, attractively providing reliable information. This repository contains the chatbot server source code. Access to the UI source code [from here](https://github.com/joancipria/VIHrtualApp-app/).

<div align="center">
  <br>
  <img style="width: 60%" title="VIHrtul-App screenshot" alt="VIHrtual-App screenshot" src="https://raw.githubusercontent.com/joancipria/VIHrtualApp-app/master/screenshot.png">
</div>

## 📦 Install
Requires `Python 3.7` and `pip 21.3` or higher. Lower versions of `pip` take too much to resolve dependencies. 
Tested with: `Python 3.7.11` and `pip 22.2.2`. Rasa version: `Rasa: 3.2.10` and `Rasa SDK: 3.2.2`. Newer versions of Rasa may not work.

Clone repository
```shell
git clone https://github.com/joancipria/vhihrtualapp.git && cd vihrtualapp
```

Create and activate a Python virtual environment
```shell
python3.7 -m venv ./venv && source ./venv/bin/activate
```

Upgrade `pip` and install `rasa`
```shell
pip3 install -U pip && pip3 install rasa
```

## 🤖 Run

Run `rasa train` to train a new model.

Run `rasa shell` to chat with the agent using the terminal .

Run `rasa run -m models --enable-api --cors "*" --debug` to start the conversational server .

Run `rasa run actions --cors "*"` to start the actions server.

## 📚 Articles
   
- [A Conversational Agent for Medical Disclosure of Sexually Transmitted Infections](https://link.springer.com/chapter/10.1007/978-3-031-15471-3_37)

## 📝 Cite
To cite this resource in a publication, please use the following:
```
@inproceedings{moreno2022conversational,
  title={A Conversational Agent for Medical Disclosure of Sexually Transmitted Infections},
  author={Moreno, Joan C and S{\'a}nchez-Anguix, Victor and Alberola, Juan M and Juli{\'a}n, Vicente and Botti, Vicent},
  booktitle={International Conference on Hybrid Artificial Intelligence Systems},
  pages={431--442},
  year={2022},
  organization={Springer}
}
```

## 📜 License
Licensed under GNU General Public License v3. VIHrtual-App is a research project of the Polytechnic University of Valencia, FISABIO Foundation and the Infectious Diseases Unit of the General Hospital of Elche for the prevention of HIV.

<div align="center">
<img style="width: 15%" title="a title" alt="Alt text" src="https://raw.githubusercontent.com/joancipria/VIHrtualApp-app/master/static/img/logos/upv.jpg">
<img style="width: 15%" title="a title" alt="Alt text" src="https://raw.githubusercontent.com/joancipria/VIHrtualApp-app/master/static/img/logos/elche.jpg">
</div>