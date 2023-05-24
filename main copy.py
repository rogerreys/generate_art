from src.generate_text_gpt3 import generate_text as gt
from src.generate_img import getQuery
from time import sleep
import datetime as dt

def main_app():
    paper = [
        {
            "category":"telecomunicaciones",
            "topic":"tcp",
            "img":"tcp protocolo telecomunicaciones"
        }   
    ]
    
    # Mensaje 
    msg_intro = "Escribe una introduccion profesional corta, de {category} sobre el temas de {topic}, para un sitio web con formato html omitir el <head> y solo escribir en el <body>"
    # msg_main = "Eres un redactor, crea un articulo entre 1000 a 2500 palabra, sobre temas de {category}, crea un articulo para un sitio web en formato html con titulo, subtituos, etc, sobre el tema de {topic}, escribe sobre"
    msg_content = "Apartir de la introduccion crea el contenido, para un sitio web con formato html omitir el <head> y solo escribir en el <body>"
    file_name = "{category}_{topic}.html"

    for dic in paper:
        # file_html = open(f"assts\\{dt.datetime.now().strftime('%Y%m%d')}\\"+file_name.format(**dic), "w")
        file_html = open(f"assts\\"+file_name.format(**dic), "w")

        msg = msg_intro.format(**dic)
        req = msg #+ " definiciones tecnicas, clasificaciones y usos"
    
        res1 = gt(req)
        res2 = gt(res1+"\n"+msg_content)
        # res1 += getQuery(dic["topic"],1)
        # sleep(5)
        # req = msg +" ultimas noticias, temas mas relevantes, uso en los ultimos 2 años y una conclusion"
        # res2 = gt(req)
        # res2 += getQuery(dic["topic"],3)
    
        res = res1 +"\n"+res2
        
        
        file_html.write(res)
        file_html.close()


if __name__ == '__main__':
    main_app()