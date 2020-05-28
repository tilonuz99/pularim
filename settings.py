#coding:utf-8

db_url='sqlite:///db.sqlite'

ref_pay_perc_1lvl=0.09  #столько получит от 1 уровная рефералов за оплату
ref_pay_perc_2lvl=0.03  #столько получит от 2 уровная рефералов за оплату
ref_view_pay_1lvl=0.15  #столько получит от 1 уровная рефералов за подписку
ref_view_pay_2lvl=0.05  #столько получит от 2 уровная рефералов за подписку
new_ref_cost=0.30       #автоначисление за нового реферала.в копейках.
user_view_perc=0.40  #столько получит пользователь за вступление(проценты от стоимости установленной заказчиком)
min_out_pay=20  #минимальная сумма для вывода
min_post_cost=0.4  #минимальная стоимость 1 подписчика
user_post_perc=0.40 #процент от цены просмотра  
user_timewait_sec=6  #время просмотра поста
min_view_cost=0.05   #минимальная стоимость 1 просмотра


number="+998995322553"
qiwi_token ='7a0dcc88009c545ea4ed110574f19769'

ya_number='998995322553'
ya_token='8fd7f1a92bfd4a0ca9da47ada258988b'
telegram_token='1067916497:AAHVRdSlntWiVuar2I95fpIJiE-DnLRQ9pI'



uah_to_rub=2.76
usd_to_rub=60.85
eur_to_rub=75.73

admins = [444444]
bans = [589010424,13032321]

tutorial_url = 'https'





WEBHOOK_HOST = '3.17.207.133'
WEBHOOK_PORT = 443
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_SSL_CERT = './key.pem'
WEBHOOK_SSL_PRIV = './key.pem'



WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)

WEBHOOK_URL_PATH = "/{}/".format(telegram_token)
