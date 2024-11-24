from weather_api import get_weather
from reminder import set_reminder
from web_search import search_web
from music_player import play_music
from logging_util import get_logger

logger = get_logger()

def execute_command(intent, entities):
    try:
        if intent == "check_weather":
            location = entities.get("GPE", None)  # SpaCy uses "GPE" for locations
            if not location:
                print("Please specify a location for the weather.")
                logger.warning("Location not provided for weather check.")
            else:
                weather_report = get_weather(location)
                print(weather_report)
        elif intent == "set_reminder":
            time = entities.get("TIME", "some time")
            reminder = set_reminder(time)
            print(reminder)
        elif intent == "search_web":
            query = entities.get("query", "something")
            result = search_web(query)
            print(result)
        elif intent == "play_music":
            play_music()
        else:
            print("Sorry, I didn't understand that.")
            logger.warning("Unknown intent encountered.")
    except Exception as e:
        logger.exception(f"Error executing command: {e}")
