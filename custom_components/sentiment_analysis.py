from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import pipeline

# Load sentiment model
load_model = AutoModelForSequenceClassification.from_pretrained("joancipria/roberta-base-biomedical-es-FineTunedEmoEvent")
load_tokenizer = AutoTokenizer.from_pretrained("joancipria/roberta-base-biomedical-es-FineTunedEmoEvent")

# Create pipeline
sentiment_pipeline  = pipeline("sentiment-analysis", model=load_model, tokenizer=load_tokenizer)

# Rasa
import logging
from typing import Dict, Text, Any, List

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer

from rasa.shared.nlu.constants import (
    ENTITY_ATTRIBUTE_TYPE,
    ENTITY_ATTRIBUTE_START,
    ENTITY_ATTRIBUTE_END,
    ENTITY_ATTRIBUTE_VALUE,
    ENTITIES,
)

logger = logging.getLogger(__name__)

@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.ENTITY_EXTRACTOR], is_trainable=False
)
class SentimentAnalysis(GraphComponent):
    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> GraphComponent:
        # TODO: Implement this
        ...
    
    @staticmethod
    def required_packages() -> List[Text]:
        """Any extra python dependencies required for this component to run."""
        return ["transformers", "torch"]


    def process(self, messages: List[Message]) -> List[Message]:
        #logger.debug("|---- START DEBUGGING ----|")
        
        # For each message
        for message in messages:
            # Extract text
            text = message.get("text")

            # Get sentiment
            sentiment_dump = sentiment_pipeline(text)
            sentiment_label = sentiment_dump[0]["label"]

            if sentiment_label == 'LABEL_6':
                sentiment = "other"
            elif sentiment_label == 'LABEL_5':
                sentiment = "surprise"
            elif sentiment_label == 'LABEL_4':
                sentiment = "disgust"
            elif sentiment_label == 'LABEL_3':
                sentiment = "joy"
            elif sentiment_label == 'LABEL_2':
                sentiment = "sadness"
            elif sentiment_label == 'LABEL_1':
                sentiment = "fear"
            elif sentiment_label == 'LABEL_0':
                sentiment = "anger"
            else:
                sentiment = "unknown"

            # Set entity
            entity= {
                ENTITY_ATTRIBUTE_TYPE: "sentimiento",
                # ENTITY_ATTRIBUTE_START: token.start,
                # ENTITY_ATTRIBUTE_END: token.end,
                ENTITY_ATTRIBUTE_VALUE: sentiment,
                "confidence": sentiment_dump[0]["score"], 
            }

            message.set(ENTITIES, message.get(ENTITIES, []) + [entity], add_to_output=True)          

        return messages