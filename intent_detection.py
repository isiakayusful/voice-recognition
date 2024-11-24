from logging_util import get_logger

logger = get_logger()

def detect_intent(text):
    text = text.lower()
    logger.debug(f"Processing text for intent detection: {text}")

    if "weather" in text:
        return "check_weather"
    elif "reminder" in text:
        return "set_reminder"
    elif "search" in text or "look up" in text:
        return "search_web"
    elif "music" in text or "play" in text:
        return "play_music"
    else:
        return "unknown_intent"
