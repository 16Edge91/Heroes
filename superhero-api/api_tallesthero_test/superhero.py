import requests

def get_tallest_hero_by_gender_and_work(gender: str, has_work: bool):
    """
    Возвращает самого высокого героя по полу и наличию работы.
    :param gender: "Male" или "Female"
    :param has_work: True — если должна быть работа, False — если работы нет
    :return: имя и рост героя
    """
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    heroes = response.json()

    filtered_heroes = []

    for hero in heroes:
        appearance = hero.get("appearance", {})
        work = hero.get("work", {})
        hero_gender = appearance.get("gender", "").strip().lower()
        occupation = work.get("occupation", "").strip()

        if hero_gender != gender.lower():
            continue

        if has_work and occupation:
            filtered_heroes.append(hero)
        elif not has_work and not occupation:
            filtered_heroes.append(hero)

    tallest_hero = None
    max_height = -1

    for hero in filtered_heroes:
        height_cm_str = hero.get("appearance", {}).get("height", ["", ""])[1]  # например: "188 cm"
        try:
            height_cm = int(height_cm_str.replace(" cm", ""))
            if height_cm > max_height:
                max_height = height_cm
                tallest_hero = hero
        except:
            continue  # пропускаем если высота некорректна

    return tallest_hero
