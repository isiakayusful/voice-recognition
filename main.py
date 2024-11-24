import speech_recognition as sr
from intent_detection import detect_intent
from entity_extraction import extract_entities_with_spacy
from command_execution import execute_command
from logging_util import get_logger

logger = get_logger()

def main():
    recognizer = sr.Recognizer()
    logger.info("Voice assistant started.")
    
    with sr.Microphone() as source:
        print("Listening... Please say something.")
        logger.debug("Listening for user input.")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        logger.info(f"Recognized text: {text}")

        intent = detect_intent(text)
        print(f"Detected intent: {intent}")
        logger.debug(f"Intent detected: {intent}")

        entities = extract_entities_with_spacy(text)
        print(f"Extracted entities: {entities}")
        logger.debug(f"Entities extracted: {entities}")

        execute_command(intent, entities)

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        logger.error("Speech recognition failed: Could not understand audio.")
    except Exception as e:
        print("An error occurred.")
        logger.exception(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
