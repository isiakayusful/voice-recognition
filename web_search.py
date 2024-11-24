import webbrowser
from logging_util import get_logger

logger = get_logger()

def search_web(query):
    logger.info(f"Performing web search for: {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching for '{query}' online."
