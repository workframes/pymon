# import
import json
import requests
from requests_html import HTMLSession
from .util import *

global session 

session = HTMLSession()

'''
/Returned Item Array Setup/

[0] = Best Price
[1] = Recent Average Price(RAP)
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
    def PlayerAssets(self, Id):
        link = Base_Link + "/api/playerassets/" + str(Id)
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        }

        r = requests.get(link, headers=headers)
        if(r.status_code == 200):
            result = r.json()
            playerAssets = result["playerAssets"]
            returnArray = []

            for asset in playerAssets:
                returnArray.append(asset)

            return returnArray
            
    def ItemBestPrice(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[0].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})

    def ItemRAP(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[1].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})        

    def ItemValue(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[2].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})

    def ItemDemand(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[3].text
        
            return data
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})

    def ItemTotalCopies(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[4].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})        

    def ItemAvailableCopies(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[5].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})        
    
    def ItemPremiumCopies(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[6].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})       

    def ItemDeletedCopies(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[7].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})               

    def ItemOwnerCount(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[8].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})      


    def ItemPremiumOwnerCount(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[9].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})      


    def ItemHoardedCopies(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[10].text
        
            return int(data.replace(",", ""))
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})      


    def ItemPercentHoarded(self, Id):
        link = Base_Link + "/item/" + str(Id)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[11].text
        
            return data
        else:
            return json.dumps({"error": f"Unable to fetch data due to Item Id being invalid or request error."})                                      