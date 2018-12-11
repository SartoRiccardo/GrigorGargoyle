"""
A queue of events for the main thread to handle.
"""


class Queue:
    def __init__(self):
        self.__queue = []

    def add(self, procedure):
        self.__queue.append(procedure)

    def remove(self, procedure):
        if procedure in self.__queue:
            self.__queue.remove(procedure)

    def getQueue(self):
        return self.__queue


updates = Queue()
