from app.controller.ChampionController import ChampionController
import asyncio

class Main:

    def __init__(self):
        pass

    async def main():
        select_champion = asyncio.create_task(ChampionController.find_champion('Ahri'))
        teste_async_loop = asyncio.create_task(ChampionController.find_champion('Vayne'))

        await teste_async_loop
        await select_champion

asyncio.run(Main.main())
