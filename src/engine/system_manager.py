from src.services.log_service import LogService
from src.engine.event_manager import EventManager


class SystemManager:

    def __init__(self):
        pass

    @staticmethod
    def create():
        """
        Static factory method
        :return:
        :rtype: SystemManager
        """
        return SystemManager()
