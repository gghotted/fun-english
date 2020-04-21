from google_api import translate
from utils import pretreatment_text
import html


def create_workbook(input_text):
    texts = input_text.split('.')
    texts = map(pretreatment_text, texts)
    responses = map(translate, texts)
    workbook = map(response_parse, responses)
    return workbook


def response_parse(response):
    input_text = response['input']
    if input_text == '':
        return
    translated_text = response['translatedText']
    return [html.unescape(input_text),
            html.unescape(translated_text)]


if __name__ == '__main__':
    input_text = '''
        그룹 레드벨벳 아이린과 슬기가 유닛 활동에 나선다.
        
        21일 SM엔터테인먼트는 "레드벨벳 아이린, 슬기가 유닛을 준비하고 있다"며 "앨범 발표 시기는 확정되는 대로 공개할 것"이라고 밝혔다.
        
        
        이로써 아이린과 슬기는 데뷔 후 6년 만에 레드벨벳 중 처음으로 유닛을 결성하게 됐다. 특히 두 사람은 데뷔 전 SM루키즈 소속 SR14G 슬기 앤 아이린으로 호흡을 맞춘 바 있어 이번 활동에 대한 팬들의 기대가 높아지고 있다.
        
        또 레드벨벳 내 각각 메인댄서와 리드댄서로 활약하고 있는 아이린과 슬기가 유닛 활동으로 어떤 퍼포먼스를 선보일지 관심이 모아지고 있다.
        
        한편 레드벨벳은 지난해 12월 "사이코(Psycho)" 발매 후 개별 활동을 이어오고 있다.
    '''
    for i, work in enumerate(create_workbook(input_text)):
        if work is None:
            continue
        print(f"번역 {i+1}")
        print(work[0])
        print(work[1])
        print('\n\n')

