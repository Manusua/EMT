import requests
from requests.exceptions import HTTPError
ACCES_TOKEN = "9c9e5391-2499-44e7-8bcd-d852c15a9029"

def make_petition(url, headers, type, params = "",  data = ""):
    if type == "GET":
        try:
            response = requests.get(
                url=url,
                params=params,
                headers=headers,
                )
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  
        except Exception as err:
            print(f'Other error occurred: {err}')  
        else:
            return response.json()
        
    elif type == "POST":
        try:
            response = requests.post(
                url=url,
                data=data,
                headers=headers,
                )
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  
        except Exception as err:
            print(f'Other error occurred: {err}')  
        else:
            return response.json()
    else:
        print("Error, tipo de petición diferente a GET y POST: " + str(type))
        return -1



def get_geo_dist(file_w):
    longitude = ""
    latitude = ""
    radius = ""
    url = "https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/arroundxy/" + longitude + '/' + latitude + '/' + radius + '/'


# Escribe en file_w todas las paradas con su información (y posición)
def get_geo_stops(file_w):
    return




file_w = "../files/bus_stops.json"

useragent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'


headers = { 'User-Agent' : useragent,'accessToken':'9c9e5391-2499-44e7-8bcd-d852c15a9029' }
#url = "https://openapi.emtmadrid.es/v1/transport/busemtmad/lines/1/route"
url = "https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/arroundxy/-3.78288324038992/40.4701435453176/200/"

print(make_petition(url, headers, "GET"))