import requests

pic_url = 'http://assets.pokemon.com/assets/cms2/img/pokedex/full/{}.png'

for i in range(1, 20):
    pid = ''
    if i < 10:
        pid = '00{}'.format(i)
    elif i >= 10 and i < 100:
        pid = '0{}'.format(i)
    else:
        pid = str(i)
    with open('img/{}.png'.format(pid), 'wb') as my_image:
        response = requests.get(pic_url.format(pid), stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break
            my_image.write(block)
