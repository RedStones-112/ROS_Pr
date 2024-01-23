import json
from datetime import datetime
from flask import Flask, request, make_response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import subprocess
import mysql.connector###
import pandas as pd
import io
conn = mysql.connector.connect(
host = "database-1.cd2is2gsweff.ap-northeast-2.rds.amazonaws.com",
port = 3306,
user = "admin",
password = "kim82458529",
database = "amr_base"
)###
channel_id = 'C06EWB0LN80'
token = "xoxb-6476945611462-6483504980995-xlzOEVG8Q8BuNkoRTextlfO9"
app = Flask(__name__)
client = WebClient(token)

def get_day_of_week():
    weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    weekday = weekday_list[datetime.today().weekday()]
    date = datetime.today().strftime("%Y년 %m월 %d일")
    result = '{}({})'.format(date, weekday)
    return result

def get_time():
    return datetime.today().strftime("%H시 %M분 %S초")
# def get_graph():
#     try:
#         response = client.files_upload(
#             channels=channel_id,
#             file='/home/addinedu/amr_ws/eda/data/test_graph.png',
#             title='Matplotlib Graph'
#         )
#         print(response)
#     except SlackApiError as e:
#         print(f"Error uploading file to Slack: {e.response['error']}")

# def send_dataframe_to_slack():
#     try:
#         with app.app_context():
#             # 데이터베이스에서 데이터프레임을 가져오는 부분
#             cursor = conn.cursor(buffered=True)
#             cursor.execute("SELECT * FROM yousinsa LIMIT 5")
#             result = cursor.fetchall()
#             df = pd.DataFrame(result)
#             # 데이터프레임을 표로 변환하여 Slack 메시지로 전송
#             table_message = "\n".join([" | ".join(map(str, row)) for row in df.itertuples(index=False)])
#             client.chat_postMessage(channel=channel_id, text=f"```\n{table_message}\n```")
#             df = None
#             return make_response("DataFrame sent to Slack successfully", 200, {"content_type": "application/json"})
#     except Exception as e:
#         app.logger.error(f"An error occurred: {str(e)}")
#         with app.app_context():
#             return make_response("Internal Server Error", 500, {"content_type": "application/json"})

def get_answer(text):
    trim_text = text.replace(" ", "")
    answer_dict = {
        '안녕': '안녕하세요. YouSinSa입니다.',
        '요일': ':달력: 오늘은 {}입니다'.format(get_day_of_week()),
        '시간': ':시계_9시: 현재 시간은 {}입니다.'.format(get_time()),
        '옷': '네 옷을 추천해드릴게요 , 어떤 종류의 옷을 찾으시나요?\n [아우터] , [상의] , [하의] , [신발] , [가방] , [모자]',
        '아우터': '카테고리 선택해주세요\n [겨울 싱글 코트] , [아노락 재킷] , [스포츠아우터] , [카디건] , [트레이닝 재킷] , [숏패딩,숏헤비] , [무스탕,퍼] , [베스트] , [스타디움 재킷] , [슈트,블레이저 재킷] , [플리스,뽀글이] , [나일론,코치 재킷] , [트러커 재킷] , [겨울 더블 코트] , [블루종,MA-1] , [롱패딩,롱헤비] , [후드 집업] , [레더,라이더스 재킷]',
        '상의' : '상의 카테고리 선택해주세요\n [니트,스웨터] , [후드 티셔츠] , [맨투맨,스웨트셔츠] , [스포츠 상의] , [긴소매 티셔츠] , [셔츠,블라우스] , [피케,카라 티셔츠] , [반소매 티셔츠] , [민소매 티셔츠] , [기타 상의]',
        '하의' : '하의 카테고리 선택해주세요\n [슈트 팬츠,슬랙스] , [점프 슈트,오버올] , [스포츠 바지] , [코튼 팬츠] , [데님 팬츠] , [기타 바지] , [트레이닝,조거 팬츠] , [숏 팬츠]',
        '신발' : '신발 카테고리 선택해주세요\n [구두] , [로퍼] , [블로퍼] , [샌들] , [스포츠신발] , [슬리퍼] , [기타 신발] , [모카신,보트 슈즈] , [부츠]',
        '가방' : '가방 카테고리 선택해주세요\n [백팩],[스포츠 가방],[메신저,크로스 백],[크로스백],[숄더백],[토트백],[에코백],[웨이스트 백],[파우치 백],[브리프케이스],[캐리어],[기타 가방],[지갑,머니클립],[클러치 백]',
        '모자' : '모자 카테고리 선택해주세요\n [스포츠 모자],[캡,야구 모자],[헌팅캡,베레모],[페도라],[버킷,사파리햇],[비니],[트루퍼],[기타 모자]',
        '순위' : None,
        '그래프':None
    }
    # if trim_text == '순위':
    #     if answer_dict['순위'] is None:
    #         response = send_dataframe_to_slack()
    #         answer_dict['순위'] = response
    #         return response
    # elif trim_text == '그래프':
    #     if answer_dict['그래프'] is None:
    #         response = get_graph()
    #         answer_dict['그래프'] = response
    #         return response
    if trim_text == '' or None:
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

def event_handler(event_type, slack_event):
    channel = slack_event["event"]["channel"]
    string_slack_event = str(slack_event)
    if string_slack_event.find("{'type': 'user', 'user_id': ") != -1:
        try:
            if event_type == 'app_mention':
                user_query = slack_event['event']['blocks'][0]['elements'][0]['elements'][1]['text']
                answer = get_answer(user_query)
                result = client.chat_postMessage(channel=channel,text=answer)
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