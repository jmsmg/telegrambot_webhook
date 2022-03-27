
import json
import os
import lambdagram

TOKEN = os.environ['TOKEN']
TELEGRAM_API_HOST = 'api.telegram.org'

def lambda_handler(event, context):
    # TODO implement

    print("event : ", event)
    print("context : ", context)

#### 코드 부분 시작

    bot = lambdagram.Bot(TOKEN)
    bot.send_message(event, "ㅎㅇ")


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }