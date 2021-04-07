from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata

from spellchecker import SpellChecker
spell = SpellChecker(language='es')

class CorrectSpelling(Component):

    name = "Spell_checker"
    provides = ["message"]
    requires = ["message"]
    language_list = ["es"]

    def __init__(self, component_config=None):
        super(CorrectSpelling, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass

    def process(self, message, **kwargs):
        """Retrieve the text message, do spelling correction word by word,
        then append all the words and form the sentence,
        pass it to next component of pipeline"""

        #textdata = message.text
        textdata = message.data["text"]
        textdata = textdata.split()
        new_message = ' '.join(spell.correction(w) for w in textdata)
        #message.text = new_message
        message.set('text', new_message, add_to_output=True)

    def persist(self,file_name, model_dir):
        """Pass because a pre-trained model is already persisted"""
        pass