import json
import requests as req

def key(page_img):
    with open('.\\assts\\keys\\config.json') as config_file:
        config_data = json.load(config_file)

    key_value = config_data["API_PEXEL"] if page_img =="pexel" else config_data["API_UNSPLASH"]
    return key_value

def getQuery(page_img, query, page, perpage):
    
    val = 0 if page_img=="pexel" else 1
    img_page = listPageImg(page_img)
    
    # Body
    url=img_page[val]["url"]
    headers={
        "Authorization": img_page[val]["headers"]
    }
    params={
        "query": query,
        "page": page,
        "per_page": perpage
    }
    try:
        resp = req.get(url, headers=headers, params=params)
        if resp.status_code==200:
            data = resp.json()
            # Procesar los datos según sea necesario
            res = img_page[val]["img"]
            
            return res.format(**data[img_page[val]["data"]][0])
        else:
            # La petición no fue exitosa
            print("Error:", resp.status_code)
    except NameError:
        print(NameError)
    
def listPageImg(page_img):
    img_page = [
        {
            "url":"https://api.pexels.com/v1/search",
            "headers":f"{key(page_img)}",
            "img":"<br><img src='{src[medium]}' alt='Foto de {photographer} en Pexels'>",
            "data" :"photos"
        },
        {
            "url":"https://api.unsplash.com/search/photos",
            "headers":f"Client-ID {key(page_img)}",
            "img":"<br><img src='{urls[small]}' alt='Foto de {user[name]} en Unsplash'>",
            "data" :"results"
        }
    ]

    return img_page

def getQueryTest(page_img, query, page):
    url="https://api.unsplash.com/search/collections"
    headers={
        "Authorization": f"Client-ID {key(page_img)}"
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
        # res = "<br><img src='{urls[small]}' alt='Foto de {user[name]} en Unsplash'>"
        
        # return res.format(**data["results"][0])
        return data
    else:
        # La petición no fue exitosa
        print("Error:", resp.status_code)


if __name__=='__main__':
    res = getQueryTest("unsplash", "programacion", 1)
    print(res)