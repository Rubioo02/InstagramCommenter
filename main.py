#   Required libraries:
from instagrapi import Client
from instagrapi.exceptions import (
    ChallengeRequired,
    FeedbackRequired
)
import time, random, requests, json

#   Variables required:
with open('config.json', 'r') as f:
    data = json.load(f)
    use_telegram_telegram = data['Use_telegram_telegram']
    username = data['username']
    password = data['password']
    telegram_token = data['telegram_token']
    id_chat = data['id_chat']
    publication = data['publication']
mensaje_url = ('https://api.telegram.org/bot'+telegram_token+"/SendMessage?chat_id="+id_chat+'&text=You need to complete a challenge to be able to use the bot.')

#   Code:
def sesion():
    cl = Client()
    cl.login(username, password)

    return cl

def comentario():
    comments = ['Comment1', 'Comment2', 'Comment3'] 
    random.shuffle(comments) 
    for comment in comments:
        yield comment


def comentar(comentarios, cl):
    media_id = cl.media_id(cl.media_pk_from_url(publication))
    comment = cl.media_comment(media_id, comentarios)
    a = comment.dict()
    print(a)

def main():
    cl = sesion()
    gen = comentario()
    while True:
        try:
            comentar(next(gen), cl)
            time.sleep(180)
        except (StopIteration, FeedbackRequired, ):
            message = cl.last_json["feedback_message"]
            print(message)
            break
        except ChallengeRequired:
            if use_telegram_telegram == True:
                requests.get(url=mensaje_url)
            else:
                break

if __name__ == '__main__':
    main()