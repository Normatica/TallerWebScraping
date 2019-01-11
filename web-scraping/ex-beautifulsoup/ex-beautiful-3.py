from bs4 import BeautifulSoup

soup = BeautifulSoup(open("ex-bs-3.html"), "html.parser")

lista_pizza = soup.find_all('ul', {'id': 'pizza'})

lista_pizza = lista_pizza[0].find_all('li')

for elemento in lista_pizza:
    # Verificamos si el elemento contiene un nodo
    # de tipo <a>
    if elemento.a:
        print(elemento.a.getText())
        print(elemento.a['href'])