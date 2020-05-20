import logging
import colorama
from logging import handlers


def filter(record):
    record.msg = ' '.join(str(record.msg).split())
    if record.levelname == 'DEBUG':
        record.customcolor = colorama.Fore.YELLOW
    else:
        record.customcolor = colorama.Fore.GREEN
    return True


def logger_maker(name):
    logger = logging.getLogger("my_log:" + name)
    logger.info("{0}".format(logger.handlers))
    if not len(logger.handlers):
        terminal_logging_format = logging.Formatter(
            "{customcolor}" + "[{asctime}|" + colorama.Fore.BLUE + "{levelname}" +
            "{customcolor}" + ":{name}:{funcName}:{lineno}]" +
            colorama.Style.RESET_ALL + " - {message:.100}", style='{'
            )
        terminal_logging_handler = logging.StreamHandler()
        terminal_logging_handler.setLevel(logging.DEBUG)
        terminal_logging_handler.setFormatter(terminal_logging_format)
        terminal_logging_handler.addFilter(filter)

        file_logging_format = logging.Formatter(
            "[{asctime}|" + "{levelname}" +
            ":{name}:{funcName}:{lineno}]" +
            " - {message}", style='{'
            )
        file_logging_handler = handlers.RotatingFileHandler(
            'my_logger.log', maxBytes=2**30, backupCount=5
            )
        file_logging_handler.setLevel(logging.DEBUG)
        file_logging_handler.setFormatter(file_logging_format)

        logger.setLevel(logging.DEBUG)
        logger.propagate = False

        logger.addHandler(terminal_logging_handler)
        logger.addHandler(file_logging_handler)

        logger.info("----- Starting a new logger! -----")
        logger.debug("logger.handlers: {0}".format(logger.handlers))

    return logger
