# VIHrtual-App (Servidor)
VIHrtual-App es un chatbot de código libre para la divulgación médica del VIH. Este repositorio contiene el código fuente del servidor. Puedes acceder al repositorio del cliente web desde [aquí](https://github.com/joancipria/VIHrtualApp-app/).

<img style="width: 60%" title="VIHrtul-App screenshot" alt="VIHrtul-App screenshot" src="https://raw.githubusercontent.com/joancipria/VIHrtualApp-app/master/screenshot.png">

## 📦 Instalación
Requiere `Python 3.7 o 3.8`. Testeado con `Python 3.7.11` y `pip 22.2.2`. Versión de Rasa: `Rasa: 3.0.9` `Rasa SDK: 3.0.6` y `Rasa X: 0.39.3`. Podría dar problemas en versiones posteriores.

Clona el repositorio
```
git clone https://github.com/joancipria/VIHrtualApp.git
cd VIHrtualApp
```
Crea un entorno virtual de Python 3.7
```
python3.7 -m venv ./venv
source ./venv/bin/activate
```

Descarga e instala los requisitos. Rasa recomienda utilizar `pip 21.3` o posterior. Las versiones anteriores tardan mucho tiempo en resolver las dependencias.
```
pip3 install -U --user pip && pip3 install rasa
```

Si utilizas como terminal `zsh` utiliza `pip install -U "rasa[spacy]"`.

## 🤖 Ejecución

Ejecuta `rasa train` para entrenar un modelo.

Ejecuta `rasa shell` si deseas hablar con el asistente a través de la terminal

Ejecuta `rasa x --rasa-x-port 8080` para arrancar el servidor (con Rasa X)

Ejecuta `rasa run -m models --enable-api --cors "*" --debug` para arrancar el servidor (sin Rasa X)

Ejecuta `rasa run actions --cors "*"` para arrancar el servidor de acciones

## 🤔 Resumen

`data/` - Contiene los datos de entrenamiento de NLU agrupados por temática. Cada carpeta puede contener los siguientes archivos:

`*_intents.yml` - Contiene `intents`.

`*_stories.yml` - Contiene historias

`*_rules.yml` - Contiene reglas

`actions/actions.py` - Contiene el código de las acciones personalizadas

`domain.yml` - El archivo de dominio. Entre otros, contiene el registro de `intents`, `slots` y `entities`

`config.yml` - Configuración del entrenamiento para `NLU pipeline` y `Policy` 

## 👨‍💻 Contribuciones
Siéntete libre de enviar una `pull request` a este repositorio con tus contribuciones.

## 📚 Publicaciones
   
- [A Conversational Agent for Medical Disclosure of Sexually Transmitted Infections](https://link.springer.com/chapter/10.1007/978-3-031-15471-3_37)

## 📝 Citar
Para citar este recurso en una publicación, utilice lo siguiente:

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

## 📜 Licencia
Licenciado bajo GNU General Public License v3. VIHrtual-App es un proyecto de investigación de la Universitat Politècnica de València, la Fundación FISABIO y la Unidad de Enfermedades Infecciosas del Hospital General de Elche para la prevención del VIH.
<div align="center">
<img style="width: 15%" title="a title" alt="Alt text" src="https://raw.githubusercontent.com/joancipria/VIHrtualApp-app/master/static/img/logos/upv.jpg">
<img style="width: 15%" title="a title" alt="Alt text" src="https://raw.githubusercontent.com/joancipria/VIHrtualApp-app/master/static/img/logos/elche.jpg">
</div>