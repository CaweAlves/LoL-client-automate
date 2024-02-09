import requests

class LeagueOfLegends:
    def __init__(self, base_url):
        self.base_url = "http://ddragon.leagueoflegends.com/cdn/"
    
    async def get_champion_list(self):
        all_champions = []

        response = await requests.get( self.base_url + '12.20.1/data/en_US/champion.json')
        champions_json = response.json()
        for champion in champions_json['data']:
            all_champions.append(champion)
        return all_champions

    def get_champion_image(self, champion):
        url = self.base_url + "6.24.1/img/champion/" + champion + ".png"
        return url