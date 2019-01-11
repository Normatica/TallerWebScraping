from bs4 import BeautifulSoup

soup = BeautifulSoup(open("ex-bs-2.html"), "html.parser")

lista_pizza = soup.find_all('ul', {'id': 'pizza'})

lista_pizza = lista_pizza[0].find_all('li')

for elemento in lista_pizza:
    print(elemento.getText())