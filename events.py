class Events:
    def __init__(self):
        self.__events = {}

    def register(self, event_name, o={}):
        if event_name:
            self.__events[event_name] = o

    def listen(self, event_name, callback):
        if event_name in self.__events:
            callback(self.__events[event_name])


    def listenOnce(self, event_name, callback):
        if event_name in self.__events:
            temp = self.__events[event_name]
            self.remove(event_name)
            callback(temp)

    def listenAll(self, callback):
        callback(self.__events)

    def remove(self, event_name):
        if event_name in self.__events:
            self.__events.pop(event_name, None)


