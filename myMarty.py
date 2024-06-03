
from martypy import Marty as MartAPI

class Marty():
    def __init__(self,connection_type,ip_address):
        self.my_marty1 = MartAPI("wifi","192.168.0.100")