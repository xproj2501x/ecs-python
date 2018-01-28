LOG_LEVEL = {}
LOG_LEVEL.NONE = 1 << 0
LOG_LEVEL.LOG = 1 << 1
LOG_LEVEL.DEBUG = 1 << 2
LOG_LEVEL.WARNING = 1 << 3
LOG_LEVEL.ERROR = 1 << 4
LOG_LEVEL.ALL = 1 << 5


class LogService:

    def __init__(self, context, log_level):
        """

        :param context:
        :type context: string
        :param log_level:
        :type log_level: int
        """
        self._context = context
        self._log_level = log_level
        self._data = []

    def log(self, message):
        """

        :param message:
        :type message: string

        """
        self._write(LOG_LEVEL.LOG, message)

    def debug(self, message):
        """

        :param message:
        :type message: string

        """
        self._write(LOG_LEVEL.DEBUG, message)

    def warning(self, message):
        """

        :param message:
        :type message: string

        """
        self._write(LOG_LEVEL.WARNING, message)

    def error(self, message):
        """

        :param message:
        :type message: string

        """
        self._write(LOG_LEVEL.ERROR, message)

    def _write(self, log_level, message):
        """

        :param log_level:
        :type log_level: int
        :param message:
        :type message: string

        """
        if log_level <= self._log_level:
            self._data.append(message)
