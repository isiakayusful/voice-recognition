from logging_util import get_logger

logger = get_logger()

def set_reminder(time):
    logger.info(f"Setting reminder for {time}")
    return f"Reminder set for {time}."
