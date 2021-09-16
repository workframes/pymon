# import
import json
from requests_html import HTMLSession
from .util import *


'''
Returned Item Arry Setup

[0] = Best Price
[1] = Reent Average Price(RAP)
[2] = Value
[3] = Demand
[4] = Total Copies
[5] = Available Copies
[6] = Premium Copies
[7] = Deleted Copies
[8] = Owners
[9] = Premium Owners
[10] = Hoarded Copies
[11] = Percent Hoarded
'''

class pymon:
    def ItemValue(self, Id):
        link = Base_Link + "/item/" + str(Id)
        session = HTMLSession()

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[2].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})

  
