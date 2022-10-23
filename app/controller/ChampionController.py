from app.controller.utils.Recognition import Recognition as rec
import urllib.request
import asyncio
import pyautogui as pg
import PIL


class ChampionController:

    async def find_champion(champion):
        urllib.request.urlretrieve(
            'http://ddragon.leagueoflegends.com/cdn/12.20.1/img/champion/' + champion + '.png', champion + '.png')
        while True:
            try:
                for i in range(1, 4):
                    await asyncio.sleep(1)
                    image = PIL.Image.open(champion + '.png')
                    image = image.resize(
                        (int(image.size[0] / 2), int(image.size[1] / 2)))
                    image.save(champion + '.png')
                    print('image resized -----')
                    print(champion)
                    location = rec.find_image(champion + '.png')
                    print(location)
                    if location:
                        print(location)
                        pg.click(location)
                        return print('found')
                    print(str(i))
                    if i == 3:
                        print('image not found +++++')
                        image.close()
                        urllib.request.urlretrieve(
                            'http://ddragon.leagueoflegends.com/cdn/12.20.1/img/champion/' + champion + '.png', champion + '.png')
            except:
                pass
