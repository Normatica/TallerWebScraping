from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()

page = urlopen('http://www.emol.com', context=context).read()
soup = BeautifulSoup(page)
mostViewed = soup.findAll("div",
                         {"class": "caja_contenedor_masvistos_modulo_texto"})
print("###")
urlViewed = []
for div in mostViewed:
    if div.a:
        urlViewed.append(div.a["href"])

count = 1
for url in urlViewed:
    print("### Noticia {}: ".format(count))
    try:
        page = urlopen("http://www.emol.com{}".format(url), context=context).read()
        soup = BeautifulSoup(page)
    except:
        print("Error al intentar recuperar noticia.")
    print("Título: ")
    try:
        title = soup.find("h1",
                         {"id": "cuDetalle_cuTitular_tituloNoticia"})
        print(title.getText())
    except:
        print("Error al intentar recuperar título de noticia.")
    print("Contenido: ")
    try:
        content = soup.find("div",
                         {"id": "cuDetalle_cuTexto_textoNoticia"})
        print(content.getText())
    except:
        print("Error al intentar recuperar contenido de noticia.")
    print("")
    count += 1
