from hanspell import spell_checker


def pretreatment_text(text):
    # 양 공백 제거
    text = text.strip()

    # 맞춤법 검사
    text = spell_checker.check(text).checked
    return text


