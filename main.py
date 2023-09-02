from datetime import datetime, timedelta
from time import sleep
from auth import *
import calendar

def last_bussines_day():
    today = datetime.today()
    last_day = calendar.monthrange(today.year, today.month)[1]
    last_bussines_day = datetime(today.year, today.month, last_day)

    while last_bussines_day.weekday() > 4:
        last_bussines_day -= timedelta(days=1)

    return last_bussines_day.day

na_sucessada = api.media_upload(filename="mas a bagaça tá no bolso to de boa na sucessada.mp4")

client.create_tweet(text="blz ja ta feito agora só esperar")

while datetime.today().day != last_bussines_day():
    sleep(86400)
    
client.create_tweet(media_ids=[na_sucessada.media_id])