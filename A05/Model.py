class Model:

    def __init__(self):
        self.url = 'https://maps.googleapis.com/maps/api/directions/json'
        self.params = {"origin": "",
                  "destination": "",
                  "sensor": "false",
                  "language": "ger"}


    def setParams(self, origin, destination):
        """
        setter for parameters in url
        :param origin: start
        :param destination: end
        :return: None
        """
        self.params['origin'] = origin
        self.params['destination'] = destination