# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
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
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionSaludarUsuario(Action):
    """Greets the user with/without privacy policy"""

    def name(self) -> Text:
        return "action_saludar_usuario"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")
        name_entity = next(tracker.get_latest_entity_values("PER"), None)        
        
        if intent == "saludar" or (intent == "introducir_datos" and name_entity):
            if name_entity and name_entity.lower() != "":
                dispatcher.utter_message(template="utter_saludar_con_nombre", nombre=name_entity)
                return []
            else:
                dispatcher.utter_message(template="utter_saludar")
                return []
        return []


# class ActionSessionStart(Action):
#     def name(self) -> Text:
#         return "action_session_start"

#     @staticmethod
#     def fetch_slots(tracker: Tracker) -> List[EventType]:
#         """Collect slots that contain the user's name and phone number."""

#         slots = []
#         return slots

#     async def run(
#       self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:

#         # the session should begin with a `session_started` event
#         events = [SessionStarted()]
#         dispatcher.utter_message(template="utter_bienvenida")

#         # any slots that should be carried over should come after the
#         # `session_started` event
#         events.extend(self.fetch_slots(tracker))

#         # an `action_listen` should be added at the end as a user message follows
#         events.append(ActionExecuted("action_listen"))

#         return events