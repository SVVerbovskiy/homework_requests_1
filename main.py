import requests

superhero_list_id = [332, 655, 149]


def intelligence_compare(hero_list):
    super_man = []
    for hero in superhero_list_id:
        url = f'https://akabab.github.io/superhero-api/api/id/{hero}.json'
        info = requests.get(url).json()
        super_man.append({
            'name': info['name'],
            'intelligence': info['powerstats']['intelligence'],
        })

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Супергерой с самым высоким интеллектом: {name}, его интеллект: {intelligence_super_hero}")


if __name__ == '__main__':
    intelligence_compare(superhero_list_id)
