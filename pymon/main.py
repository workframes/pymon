#import 
import requests
from .util import *


class pymon:
    def ItemValue(self, Id):
        r = requests.get(Base_Link + str(Id))
        print(r)