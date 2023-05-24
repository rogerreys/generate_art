import openai
import json

openai.api_key = "";

def key():
    with open('.\\assts\\keys\\config.json') as config_file:
        config_data = json.load(config_file)

    openai.api_key = config_data["API_CHAT"]    
    

def generate_text(prompt):
    key()
    print("prompt:",prompt)
    report = []
    model_engine = "text-davinci-003" # Puede cambiar el modelo aquí
    prompt = (prompt[:2048]) # Asegura que la solicitud sea menor a 2048 caracteres
    for response in openai.Completion.create(
        model=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.2,
        stream = True
    ):
        report.append(response.choices[0].text)
        result = "".join(report).strip()
        # result = result.replace("\n", " ")
    return result

if __name__=="__main__":
    key()
