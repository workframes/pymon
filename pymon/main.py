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
    def LimitedCount(self):
        link = Base_Link + "/itemapi/itemdetails"
        r = requests.get(link)

        if(r.status_code == 200):
            result = r.json()

            return result['item_count']


    def LimitedCatalog(self, format=None):
        total = []
        link = Base_Link + "/itemapi/itemdetails"
        r = requests.get(link)

        if(r.status_code == 200):
            result = r.json()
            if(format == "ID" or format == None):
                for obj in result['items']:
                    total.append(obj)
                return total
            elif(format == "NAME"):
                for obj in result['items']:
                    total.append(result['items'][str(obj)][0])
                return total    
        else:
            return json.dumps({"error": f"Unable to fetch Catalog [Code: {r.status_code}]"})

    def IdToName(self, ID):
        link = Base_Link + "/itemapi/itemdetails"
        r = requests.get(link)

        if(r.status_code == 200):
            result = r.json()
            item = result["items"][str(ID)][0]
            if(item):
                return item
            else:
                return json.dumps({"error": "Unable to fetch Item"})
        else:
            return json.dumps({"error": f"Unable to fetch Item [Code: {r.status_code}]"})

    def ItemBestPrice(self, ID):
        link = Base_Link + "/item/" + str(ID)

        r = session.get(link)
        if(r.status_code == 200):
            elements = r.html.find(".value-stat-data")
            data = elements[0].text
            if(data):
                return int(data.replace(",", ""))
            else:
                return json.dumps({"error": "Unable to fetch Item"})
        else:
            return json.dumps({"error": f"Unable to fetch Item [Code: {r.status_code}]"})

    def ItemRAP(self, ID):
        link = Base_Link + "/itemapi/itemdetails"
        r = requests.get(link)

        if(r.status_code == 200):
            result = r.json()
            item = result["items"][str(ID)][2]
            if(item):
                if(str(item) != "-1"):
                    return item
                else:
                    return result["items"][str(ID)][1]
            else:
                return json.dumps({"error": "Unable to fetch Item"})
        else:
            return json.dumps({"error": f"Unable to fetch Item [Code: {r.status_code}]"})

    def ItemValue(self, ID):
        link = Base_Link + "/itemapi/itemdetails"
        r = requests.get(link)

        if(r.status_code == 200):
            result = r.json()
            item = result["items"][str(ID)][3]
            if(item):
                if(str(item) != "-1"):
                    return item
                else:
                    return result["items"][str(ID)][2]    
            else:
                return json.dumps({"error": "Unable to fetch Item"})
        else:
            return json.dumps({"error": f"Unable to fetch Item [Code: {r.status_code}]"})

    def ItemDemand(self, ID):
        link = Base_Link + "/itemapi/itemdetails"
        r = requests.get(link)

        if(r.status_code == 200):
            result = r.json()
            item = result["items"][str(ID)][5]
            if(item):
                return Demand_Check[item]
            else:
                return json.dumps({"error": "Unable to fetch Item"})
        else:
            return json.dumps({"error": f"Unable to fetch Item [Code: {r.status_code}]"})

    def ItemTrend(self, ID):
        link = Base_Link + "/itemapi/itemdetails"
        r = requests.get(link)

        if(r.status_code == 200):
            result = r.json()
            item = result["items"][str(ID)][6]
            return Trends[item]
        else:
            return json.dumps({"error": f"Unable to fetch Item [Code: {r.status_code}]"})

    def ItemProjectedCheck(self, ID):
        link = Base_Link + "/itemapi/itemdetails"
        r = requests.get(link)

        if(r.status_code == 200):
            result = r.json()
            item = result["items"][str(ID)][7]
            if(item):
                return Bool_Check[item]
            else:
                return json.dumps({"error": "Unable to fetch Item"})
        else:
            return json.dumps({"error": f"Unable to fetch Item [Code: {r.status_code}]"})              

    def ItemAcronym(self, ID):
        link = Base_Link + "/itemapi/itemdetails"
        r = requests.get(link)

        if(r.status_code == 200):
            result = r.json()
            item = result["items"][str(ID)][1]
            if(item):
                return item
            else:
                return json.dumps({"error": "Unable to fetch Item"})
        else:
            return json.dumps({"error": f"Unable to fetch Item [Code: {r.status_code}]"})

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
