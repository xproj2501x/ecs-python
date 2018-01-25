from src.services.log_service import LogService
from src.utilities.data_structures.queue import Queue


class MessageService:

    def __init__(self):
        """

        """
        self._log_service = LogService('MessageService')
        self._locked = False
        self._subscriptions = {}
        self._queue = Queue()
        self._bounced = Queue()

    def subscribe(self, subscriber, subject):
        """
        Adds a subscription for the subject to the message service
        :param subscriber: the handler for the subscription
        :type subscriber: string
        :param subject: the subject for the subscription
        :type subject: string
        """
        if not self._has_subject(subject):
            self._subscriptions[subject] = []
        if self._has_subscription(subscriber):
            raise Exception('Subscriber {0} already exists for subject {1}'.format(subscriber, subject))
        self._subscriptions[subject].append(subscriber)

    def unsubscribe(self, subscriber, subject):
        """
        Removes a subscription for the subject from the message service
        :param subscriber: the handler for the subscription
        :type subscriber: string
        :param subject: the subject for the subscription
        :type subject: string
        """
        if not self._has_subscription(subscriber, subject):
            raise Exception('Subscriber is not subscribed to subject {0}'.format(subscriber))
        subscriptions = self._subscriptions[subject]
        subscriptions.remove(subscriber)

    def publish(self):
        """

        """
        self._locked = True
        while self._queue.length:
            message = self._queue.dequeue()
            subscriptions = self._subscriptions[message.subject]
            for subscriber in subscriptions:
                subscriber(message)
        while self._bounced.length:
            message = self._bounced.dequeue()
            self._queue.enqueue(message)
        self._locked = False

    def send(self, message):
        """
        Adds a message to the queue if it is not locked
        :param message: the message to be sent
        :type message: object
        """
        if not self._has_subject(message.subject):
            raise Exception('Subject {0} does not exist'.format(subject))
        if self._locked:
            self._bounced.enqueue(message)
        self._queue.enqueue(message)

    def clear(self):
        """
        Clears the message queue
        """
        self._queue.clear()

    def _has_subject(self, subject):
        """
        Verifies that the subject exists in the message service
        :param subject: the subject for the subscription
        :type subject: string
        :return:
        :rtype: bool
        """
        return subject in self._subscriptions

    def _has_subscription(self, subscriber, subject):
        """
        Verifies that a subscriber has a subscription for the subject
        :param subscriber: the handler for the subscription
        :type subscriber: string
        :param subject: the subject for the subscription
        :type subject: string
        :return:
        :rtype: bool
        """
        if not self._has_subject(subject):
            raise Exception('Subject {0} does not exist'.format(subject))
        return subscriber in self._subscriptions[subject]

    @staticmethod
    def create():
        """
        Static factory method
        :return:
        :rtype: MessageService
        """
        return MessageService()
