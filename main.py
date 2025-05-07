import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.somosjacarandas.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
data = []

# Encuentra el contenedor principal de las tarjetas
highlights_list = soup.find("div", class_="highlights-list")
if highlights_list:
    # Encuentra todas las tarjetas individuales
    cards = highlights_list.find_all("div", class_="highlight-item")
    for card in cards:
        title = card.find("h2", class_="highlight_h2").text if card.find("h2", class_="highlight_h2") else "No title found"
        text = card.find("p", class_="p-small").text if card.find("p", class_="p-small") else "No text found"
        boton = card.find("div", class_="highlight-bottom-wrapper")
        boton_tag = boton.find("a") if boton else None
        buton = boton_tag["href"] if boton_tag and "href" in boton_tag.attrs else "No button link found"
        img_tag = card.find("img")
        img = img_tag["src"] if img_tag and "src" in img_tag.attrs else "No image found"

        # Agregar los datos al arreglo
        data.append({
            "title": title,
            "text": text,
            "button_link": buton,
            "image": img
        })

        # Imprimir los datos de cada tarjeta
        print(f"Title: {title}")
        print(f"Text: {text}")
        print(f"Button Link: {buton}")
        print(f"Image: {img}")
        print("-" * 40)

# Crear un DataFrame con los datos y exportarlo a CSV
if data:
   df = pd.DataFrame(data)
   df.to_excel("jacarandas.xlsx", index=False)
   print("Datos exportados a jacarandas.xlsx")
else:
    print("No se encontraron tarjetas.")