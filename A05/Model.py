class Model:

    def __init__(self):
        self.url = 'https://maps.googleapis.com/maps/api/directions/json'
        self.params = {"origin": "",
                  "destination": "",
                  "sensor": "false",
                  "language": "ger"}


    def setParams(self, origin, destination):
        self.params['origin'] = origin
        self.params['destination'] = destination