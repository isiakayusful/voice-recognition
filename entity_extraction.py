import spacy
from logging_util import get_logger

logger = get_logger()
nlp = spacy.load("en_core_web_sm")

def extract_entities_with_spacy(text):
    doc = nlp(text)
    entities = {}
    logger.debug(f"Processing text for entity extraction: {text}")

    for ent in doc.ents:
        entities[ent.label_] = ent.text
    return entities
