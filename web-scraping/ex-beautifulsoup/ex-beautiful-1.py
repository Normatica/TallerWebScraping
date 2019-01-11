from bs4 import BeautifulSoup

soup = BeautifulSoup(open("ex-bs-1.html"), "html.parser")

lista_supermercado = soup.find_all('li')
for elemento in lista_supermercado:
    print(elemento)

print("###")

# Para imprimir sólo el texto
for elemento in lista_supermercado:
    print(elemento.getText())