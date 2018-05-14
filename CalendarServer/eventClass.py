class EventClass(object):
    start = ""
    name = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, start, name):
        self.start = start
        self.name = name

def make_eventClass(start, name):
    event = EventClass(start, name)
    return event