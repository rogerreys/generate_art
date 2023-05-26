import json
import requests as req


def key():
    with open('.\\assts\\keys\\config.json') as config_file:
        config_data = json.load(config_file)

    key_value = config_data["API_PEXEL"]
    return key_value

def getQuery(query, page):
    url="https://api.pexels.com/v1/search"
    headers={
        "Authorization": key()
    }
    params={
        "query": query,
        "page": page,
        "per_page": page
    }
    resp = req.get(url, headers=headers, params=params)
    if resp.status_code==200:
        data = resp.json()
         # Procesar los datos según sea necesario
        res = "<br><img src='{src[medium]}' alt='Foto de {photographer} en Pexels'>"
        
        return res.format(**data["photos"][0])
    else:
        # La petición no fue exitosa
        print("Error:", resp.status_code)

if __name__=='__main__':
    res = getQuery("snake" ,10)
    print(res)
    res = getQuery("snake" ,1)
    print(res)