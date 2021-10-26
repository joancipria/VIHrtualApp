# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    SessionStarted,
    ActionExecuted,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)


class ActionDarBienvenida(Action):
    """Recibe al usuario con el mensaje de bienvenida"""

    def name(self) -> Text:
        return "action_dar_bienvenida"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # dispatcher.utter_message(response="utter_bienvenida")
        buttons = [{"title": "¿Qué es el VIH?", "payload": "¿Qué es el VIH?"}, {"title": "¿Cuántas personas tienen VIH hoy?",
                                                                                                     "payload": "¿Cuántas personas tienen VIH hoy?"}, {"title": "¿Existe una vacuna contra el VIH?", "payload": "¿Existe una vacuna contra el VIH?"}]
        dispatcher.utter_message("¡Hola! Soy Juan, encantado de conocerte!");
        dispatcher.utter_button_message(
            "Puedo ayudarte con cualquier pregunta relacionada con el VIH. Escríbeme directamente cualquier duda que tengas, y si no se te ocurre qué preguntar, prueba a pulsar sobre alguno de los siguientes botones 👇", buttons)

        return []

class ActionComoUsarPreservativo(Action):
    """Informa al usuario sobre como usar un preservativo"""

    def name(self) -> Text:
        return "action_como_usar_preservativo"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # Get tipo_condon entity
        tipo_condon = next(tracker.get_latest_entity_values("tipo_condon"), None)

        # If tipo_condon is empty, show male condom
        if tipo_condon is None:
            dispatcher.utter_message(response="utter_instrucciones_preservativo_masculino")
        
        # If not, show requested condom
        if tipo_condon == "female_condom":
            dispatcher.utter_message(response="utter_instrucciones_preservativo_femenino")
        
        if tipo_condon == "male_condom":
            dispatcher.utter_message(response="utter_instrucciones_preservativo_masculino")
        
        return []