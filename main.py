from src.generate_text_gpt3 import generate_text as gt
from src.generate_img import getQuery
from time import sleep
import datetime as dt
import os 
import json

def main_app():
    # files
    path_files = f"assts/article/{dt.datetime.now().strftime('%Y%m%d')}"
    path_json = "assts/json/datos.json"
    
    # Mensaje 
    msg_generic = " de {category} sobre el temas de {topic}, para un sitio web con formato html omitir el <head> y solo escribir en el <body>"
    msg_intro = "Escribe una introduccion profesional corta,"
    msg_content = "Eres un profesional en {category} escribe un articulo interesante para sitio web" + msg_generic
    msg_technic = "Describe definiciones tecnica para un articulo" + msg_generic
    msg_features = "Describe funcionalidades y caractisticas interesantes para un articulo" + msg_generic
    file_name = "{category}_{topic}.html"

    # Create file
    manage_file(path_files)
    # Load data of json
    paper = load_json(path_json)

    for dic in paper:
        res1, res2, res3, res4= "","","",""

        file_html = open(path_files+"/"+file_name.format(**dic), "w", encoding="utf-8")

        # message generic
        msg = msg_generic.format(**dic)
        # Content Intro
        res1 = gt(msg_intro + msg)
        file_html.write(res1)
        file_html.write("\n"+ getQuery("unsplash", dic["img"],1,1) + "\n")
        sleep(2)
        file_html.write("\n"+ getQuery("unsplash", dic["img"],1,3) + "\n")
        # Content main
        msg_content = msg_content.format(**dic)
        res2 = gt(msg_content + msg)
        file_html.write("\n"+ res2)
        file_html.write("\n"+ getQuery("unsplash", dic["img"],1,5) + "\n")
        sleep(2)
        file_html.write("\n"+ getQuery("unsplash", dic["img"],1,7) + "\n")
        # Content technic
        res3 = gt(msg_technic + msg)
        file_html.write("\n"+ res3)
        file_html.write("\n"+ getQuery("unsplash", dic["img"],2,1) + "\n")
        sleep(2)
        file_html.write("\n"+ getQuery("unsplash", dic["img"],2,3) + "\n")
        # Content features
        res4 = gt(msg_features + msg)
        file_html.write("\n"+ res4)
        file_html.write("\n"+ getQuery("unsplash", dic["img"],2,5) + "\n")
        sleep(2)
        file_html.write("\n"+ getQuery("unsplash", dic["img"],2,7) + "\n")

        file_html.close()
        print("\n","/"*90,"\n",f"Termina el articulo {file_name.format(**dic)}","\n","/"*90,"\n")

# Create file
def manage_file(path_art):
    if not os.path.exists(path_art):
        # Create file
        os.makedirs(path_art)
    else:
        # Delete all files in this file
        for file in os.listdir(path_art):
            os.remove(path_art+"/"+file)


def load_json(path_json):
    with open(path_json) as file_json:
        # Cargar el contenido JSON en una variable
        content_json = json.load(file_json)
    # print(contenido_json.category, contenido_json.topic)
    
    # Verificar si el contenido es una lista
    if isinstance(content_json, list):
        # Utilizar el contenido como una lista en Python
        return content_json
    else:
        print("El contenido del archivo no es una lista.")


if __name__ == '__main__':
    main_app()