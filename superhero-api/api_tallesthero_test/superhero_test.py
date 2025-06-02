from api_tallesthero_test.superhero import get_tallest_hero_by_gender_and_work
"""
    Тест для функции которая возвращает самого высокого героя по полу и наличию работы.
    """
if __name__ == "__main__":
    hero = get_tallest_hero_by_gender_and_work("Male", True)
    if hero:
        print(f"Самый высокий герой: {hero['name']}, рост: {hero['appearance']['height'][1]}")
    else:
        print("Героев по таким критериям не найдено.")
