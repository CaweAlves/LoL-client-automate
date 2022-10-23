import requests

class LeagueOfLegends:
    def __init__(self):
        pass

    async def get_champion_list():
        all_champions = []

        response = await requests.get('http://ddragon.leagueoflegends.com/cdn/12.20.1/data/en_US/champion.json')
        championsJson = response.json()
        for champion in championsJson['data']:
            all_champions.append(champion)
        return all_champions

    def get_champion_image(champion):
        url = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/" + champion + ".png"
        return url