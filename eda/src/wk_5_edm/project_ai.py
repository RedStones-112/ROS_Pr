import json
from datetime import datetime
from flask import Flask, request, make_response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import subprocess
import mysql.connector
import pandas as pd
import io
import ast
import re
channel_id = 'C06EWB0LN80'
token = "xoxb-6476945611462-6483504980995-MS9fQ7NvoQLDQ3BIaUd8sA6j"
app = Flask(__name__)
client = WebClient(token)
age=20
sex='남성'
conn = mysql.connector.connect(
host = "database-1.cd2is2gsweff.ap-northeast-2.rds.amazonaws.com",
port = 3306,
user = "admin",
password = "kim82458529",
database = "amr_base"
)
cursor = conn.cursor(buffered=True)
cursor.execute("SELECT * FROM yousinsa")
columns = [i[0] for i in cursor.description]
df = pd.DataFrame(cursor.fetchall(), columns=columns)
cursor.close()
conn.close()
def get_score(user_age, user_sex, middle_category):
    global df
    # 좋아요, 리뷰 만족도
    like_list = []
    for idx, data in df.iterrows():
        try:
            like_list.append(data["likes"] / data["review"])
        except ZeroDivisionError:
            like_list.append(0)
    likes_list = [like / max(like_list) for like in like_list]
    df['만족도'] = likes_list
    # 판매량
    df["total"] = df["sold"] * df["price_member"]
    df["total"] = df["total"] / max(df["total"])
    # 선호나이
    pd.set_option("mode.chained_assignment", None)
    df['age'] = df['age'].apply(lambda x: int(re.findall(r'\d+', str(x))[0]) if re.findall(r'\d+', str(x)) else 0)
    df["age"] = abs(df["age"] - user_age)
    df["age"] = df["age"] / max(df["age"])
    # 브랜드별 만족도를 최대 만족도로 나누어 정규화
    max_brand_satisfaction = df.groupby('brand')['만족도'].max()
    
    df['brand 만족도'] = df.apply(lambda row: row['만족도'] / max_brand_satisfaction.get(row['brand'], 1), axis=1)
    # sex -> 리스트화 후 input과 다르면 0
    # 총점 계산
    df["총점"] = df["만족도"] * 4 + df["total"] * 3 + df["brand 만족도"] * 2 + df["age"] * 1
    # 사용자 input 값에 따른 선별
    df.loc[~df['sex'].apply(lambda x: user_sex in x), '총점'] = 0
    df.loc[df["sort1"] != middle_category, '총점'] = 0
    new_df = df.copy()  # 원본 DataFrame을 변경하지 않도록 복사본 사용
    new_df = new_df.sort_values(by="총점",ascending=False)
    return list(new_df["link"][:5])
def get_day_of_week():
    weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    weekday = weekday_list[datetime.today().weekday()]
    date = datetime.today().strftime("%Y년 %m월 %d일")
    result = '{}({})'.format(date, weekday)
    return result
def get_time():
    return datetime.today().strftime("%H시 %M분 %S초")
def get_answer(text):
    global age,sex,df
    trim_text = text.replace(" ", "")
    answer_dict = {
    '안녕': '안녕하세요. YouSinSa입니다. 나이와 성별을 입력해 주세요 (ex. 20,남성 )',
    '몇요일,몇요일이야': ':달력: 오늘은 {}입니다'.format(get_day_of_week()),
    '시간,몇시,몇시야': ':시계_9시: 현재 시간은 {}입니다.'.format(get_time()),
    '옷': '네 옷을 추천해드릴게요 , 어떤 종류의 옷을 찾으시나요?\n [아우터] , [상의] , [하의] , [신발] , [가방] , [모자]',
    '아우터': '아우터 카테고리 선택해주세요\n [겨울 싱글 코트] , [아노락 재킷] , [스포츠아우터] , [카디건] , [트레이닝 재킷] , [숏패딩,숏헤비] , [무스탕,퍼] , [베스트] , [스타디움 재킷] , [슈트,블레이저 재킷] , [플리스,뽀글이] , [나일론,코치 재킷] , [트러커 재킷] , [겨울 더블 코트] , [블루종,MA-1] , [롱패딩,롱헤비] , [후드 집업] , [레더,라이더스 재킷]',
    '상의' : '상의 카테고리 선택해주세요\n [니트,스웨터] , [후드 티셔츠] , [맨투맨,스웨트셔츠] , [스포츠 상의] , [긴소매 티셔츠] , [셔츠,블라우스] , [피케,카라 티셔츠] , [반소매 티셔츠] , [민소매 티셔츠] , [기타 상의]',
    '하의,바지' : '하의 카테고리 선택해주세요\n [슈트 팬츠,슬랙스] , [점프 슈트,오버올] , [스포츠 바지] , [코튼 팬츠] , [데님 팬츠] , [기타 바지] , [트레이닝,조거 팬츠] , [숏 팬츠]',
    '신발' : '신발 카테고리 선택해주세요\n [구두] , [로퍼] , [블로퍼] , [샌들] , [스포츠신발] , [슬리퍼] , [기타 신발] , [모카신,보트 슈즈] , [부츠]',
    '가방' : '가방 카테고리 선택해주세요\n [백팩],[스포츠 가방],[메신저,크로스 백],[크로스백],[숄더백],[토트백],[에코백],[웨이스트 백],[파우치 백],[브리프케이스],[캐리어],[기타 가방],[지갑,머니클립],[클러치 백]',
    '모자' : '모자 카테고리 선택해주세요\n [스포츠 모자],[캡,야구 모자],[헌팅캡,베레모],[페도라],[버킷,사파리햇],[비니],[트루퍼],[기타 모자]',
    '겨울 싱글 코트': None,
    '아노락 재킷': None,
    '스포츠아우터': None,
    '카디건': None,
    '트레이닝 재킷': None,
    '숏패딩,숏헤비': None,
    '무스탕,퍼': None,
    '베스트': '{}\n{}\n{}\n{}\n{}'.format(get_score(age,sex,'베스트')[0],get_score(age,sex,'베스트')[1],get_score(age,sex,'베스트')[2],get_score(age,sex,'베스트')[3],get_score(age,sex,'베스트')[4]),
    '스타디움 재킷': None,
    '슈트,블레이저 재킷': None,
    '플리스,뽀글이': None,
    '나일론,코치 재킷': None,
    '트러커 재킷': None,
    '겨울 더블 코트': None,
    '블루종,MA-1': None,
    '롱패딩,롱헤비': None,
    '후드 집업': None,
    '레더,라이더스 재킷': None,
    '니트,스웨터': None,
    '후드 티셔츠': None,
    '맨투맨,스웨트셔츠': None,
    '스포츠 상의': None,
    '긴소매 티셔츠': None,
    '셔츠,블라우스': None,
    '피케,카라 티셔츠': None,
    '반소매 티셔츠': None,
    '민소매 티셔츠': None,
    '기타 상의': None,
    '슈트 팬츠,슬랙스': None,
    '점프 슈트,오버올': None,
    '스포츠 바지': None,
    '코튼 팬츠': None,
    '데님 팬츠': None,
    '기타 바지': None,
    '트레이닝,조거 팬츠': None,
    '숏 팬츠': None,
    '구두': None,
    '로퍼': None,
    '블로퍼': None,
    '샌들': None,
    '스포츠신발': None,
    '슬리퍼': None,
    '기타 신발': None,
    '모카신,보트 슈즈': None,
    '부츠': None,
    '백팩': None,
    '스포츠 가방': None,
    '메신저,크로스 백': None,
    '크로스백': None,
    '숄더백': None,
    '토트백': None,
    '에코백': None,
    '웨이스트 백': None,
    '파우치 백': None,
    '브리프케이스': None,
    '캐리어': None,
    '기타 가방': None,
    '지갑,머니클립': None,
    '클러치 백': None,
    '스포츠 모자': None,
    '캡,야구 모자': None,
    '헌팅캡,베레모': None,
    '페도라': None,
    '버킷,사파리햇': None,
    '비니': '비밀',
    '트루퍼': None,
    '기타 모자': None,
    # '데이터':'{}'.format(fu()),
    'ㅇㅈ?':'ㅆㅇㅈ',
    '병신,바보,꺼져,ㅅㅂ,ㅄ':'ㅗㅗ',
    'ㅅㄱ':'ㅋ',
    '정보':'나이는 : {}, 성별은 : {}'.format(age,sex)
    }
    try:
        if trim_text[0].isdigit():
            parts = trim_text.split(',')
            age = int(parts[0])
            sex = parts[1].strip()
            return "저장되었습니다."
        elif trim_text == '' or None:
            return "알 수 없는 질의입니다. 답변을 드릴 수 없습니다."
        elif trim_text in answer_dict.keys():
            return answer_dict[trim_text]
        else:
            for key in answer_dict.keys():
                if key in trim_text:
                    return answer_dict[key]
                
            for key in answer_dict.keys():
                if key.find(trim_text) != -1:
                    return "연관 단어 [" + key + "]에 대한 답변입니다.\n" + answer_dict[key]
            
            for key in answer_dict.keys():
                if answer_dict[key].find(text[1:]) != -1:
                    return "질문과 가장 유사한 질문 [" + key + "]에 대한 답변이에요.\n"+ answer_dict[key]
        
        return text + "은(는) 없는 질문입니다."
    
    except:
        return text + "은(는) 없는 질문입니다."
def event_handler(event_type, slack_event):
    channel = slack_event["event"]["channel"]
    string_slack_event = str(slack_event)
    if string_slack_event.find("{'type': 'user', 'user_id': ") != -1:
        try:
            if event_type == 'app_mention':
                user_query = slack_event['event']['blocks'][0]['elements'][0]['elements'][1]['text']
                answer = get_answer(user_query)
                
                client.chat_postMessage(channel=channel,text=answer)
            return make_response("ok", 200, )
        except IndexError:
            pass
    message = "[%s] cannot find event handler" % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})

@app.route('/', methods=['POST'])
def hello_there():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)
    return make_response("There are no slack request events", 404, {"X-Slack-No-Retry": 1})
@app.route('/slash/', methods=['POST'])

def hello_slash():
    try:
        query_word = request.form['text']
        answer = get_answer(query_word)
        return make_response(answer, 200, {"content_type": "application/json"})
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return make_response("Internal Server Error", 500, {"content_type": "application/json"})
if __name__ == '__main__':
    app.run(debug=True, port=8000)