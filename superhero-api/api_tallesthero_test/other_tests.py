from api_tallesthero_test.superhero import get_tallest_hero_by_gender_and_work
"""
    Дополнительные тесты для функции которая возвращает самого высокого героя по полу и наличию работы.
    """
def validate_height_format(height):
    assert isinstance(height, list), "Height должен быть списком"
    assert len(height) == 2, "Height должен содержать два значения"
    feet_inches, cm = height
    assert isinstance(feet_inches, str) and feet_inches.strip() != "", "Рост в футах-дюймах должен быть строкой"
    assert isinstance(cm, str) and cm.strip().endswith("cm"), "Рост в см должен быть строкой, заканчивающейся на 'cm'"

def test_male_with_work():
    hero = get_tallest_hero_by_gender_and_work("Male", True)
    assert hero is not None, "Ожидался герой-мужчина с работой"
    assert hero["appearance"]["gender"].lower() == "male"
    assert hero["work"]["occupation"].strip() != ""
    validate_height_format(hero["appearance"]["height"])
    print(f"[Тест 1] Самый высокий мужчина с работой: {hero['name']}, рост: {hero['appearance']['height'][1]}")

def test_male_without_work():
    hero = get_tallest_hero_by_gender_and_work("Male", False)
    if hero:
        assert hero["appearance"]["gender"].lower() == "male"
        assert hero["work"]["occupation"].strip() == ""
        validate_height_format(hero["appearance"]["height"])
        print(f"[Тест 2] Самый высокий мужчина без работы: {hero['name']}, рост: {hero['appearance']['height'][1]}")
    else:
        print("[Тест 2] Нет мужчин без работы.")

def test_female_with_work():
    hero = get_tallest_hero_by_gender_and_work("Female", True)
    assert hero is not None, "Ожидалась женщина с работой"
    assert hero["appearance"]["gender"].lower() == "female"
    assert hero["work"]["occupation"].strip() != ""
    validate_height_format(hero["appearance"]["height"])
    print(f"[Тест 3] Самая высокая женщина с работой: {hero['name']}, рост: {hero['appearance']['height'][1]}")

def test_female_without_work():
    hero = get_tallest_hero_by_gender_and_work("Female", False)
    if hero:
        assert hero["appearance"]["gender"].lower() == "female"
        assert hero["work"]["occupation"].strip() == ""
        validate_height_format(hero["appearance"]["height"])
        print(f"[Тест 4] Самая высокая женщина без работы: {hero['name']}, рост: {hero['appearance']['height'][1]}")
    else:
        print("[Тест 4] Нет женщин без работы.")

