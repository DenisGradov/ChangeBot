token='5919074774:AAEYk4bkd3P1RJPKlXiQGI3GU4eNQrSVRwg'#Токен бота
adminId=390627714#Айди Админа
logs=-1001547811788#Канал с логами. Важно - бот должен быть в этом канале, а так же должен быть админом

mast_sub=True#Обязательная подписка на канал. Trye - включена, False - выключена. Важно - бот должен быть в этом канале, а так же быть в нем админом
mast_sub_Id=['🔗Канал',-1001739153721,'t.me/MultihumanNews','Для использования бота необходимо подписаться на наш новостной канал','✅Я подписался']#Надпись на переходе в канал, айди канала, с сылка на канал, текст при не-подписки на канал, надпись на кнопке для проверки подписки 

notif_about_new_user=True#Уведы о новых юзерах. True - если включить, False - если выключить
new_user_ms='🥳В твоего бота зашел новый юзер - @{username} (`{tg_id}`)'
btn_new_user='📩Написать'

error_ms='⭕️Я не знаю такой команды. Воспользуйся /start'

start_ms='Приветствуем Вас в нашем боте 🙋\nВ нем Вы можете оставить свою заявку на обмен валюты 💰'
btn_start=['💾Профиль💾','📝Обменять📝','🎁Акции🎁','🗒Правила🗒']
btn_owner=['👑Владелец👑','t.me/Multihuman']
btn_settings='⚙️Настройки⚙️'

profile_ms=' 💾 Ваш профиль 💾\n\n 🆔 ID и пригласительный код: `{tg_id}`\n 🤝 Всего сделок : `{trades}`\n 💰 Сделок на общую сумму: `{tradesSum}`\n 📢 Рефералов: `{referalsCol}`\n 💸 Реферальный баланс: `{referalsBal}`'
btn_profile=['🤝Ввести реферальный код🤝','◀️Назад◀️']

referal_ms='Введите код человека, который пригласил вас в бота:'
btn_referal='◀️Назад'
referal_error_ms='❌Вы не можете указать код, т.к. уже сделали это'
referal_error2_ms='❌Вы не можете указать свой код'
referal_beg_ms='Возвращаюсь назад'
referal_good_ms='✅Вы успешно ввели код пользователя @{username} (`{tg_id}`)'
referal_good2_ms='🔥У вас новый реферал - @{username} (`{tg_id}`)\nВсего у вас `{referalsCol}` рефералов.'

admin_ms='Меню настроек'
btn_admin=['📉Смена скупаемой валюты','📈Смена продаваемой валюты','👥Реф.система','🎁Акции','🏚Меню']
btn_rules='🗒Правила'
btn2_admin=['🎬Реклама','🤖Юзер']

to_input_ms='✍️Введи список валют которые юзеры смогут обменять (эти валюты они будут отправлять в тебе), через запятую(без пробелов). Например: `RUB,UAH,BYN,KZT,PLN,BTC,ETH,USDT,USD,EUR`'
from_input_ms='✍️Введи список валют которые юзеры смогут получить (эти валюты ты сможешь отправить юзеру), через запятую(без пробелов). Например: `UAH,RUB,BYN,KZT,PLN,BTC,ETH,USDT,USD,EUR`'
btn_to_input='◀️Назад'
to_input_beh='Возвращаемся в настройки'
ti_input_primer='Пример'
to_input_ac='✅Скупаемая валюта была изменена (список валюты выше)'
from_input_ac='✅Продаваемая валюта была изменена (список валюты выше)'
to_input_nac='❌Произошла ошибка, попробуй еще раз'


ref_system_on_ms='🟢Реф.система *включена*\nРеферальный бонус составляет `{refBonys}%`'
ref_system_of_ms='🔴Реф.система *выключена*'
btn_ref_system=['🔴Выключить реф.систему','🟢Включить реф.систему','⚒Изменить реф.бонус','◀️Вернуться']
ref_bonys_ms='Введите Новый реферальный % (без значка %, например: `5`)'
beg_ref_bonys='Возвращаюсь в реф.систему'
btn_ref_bonys='🔙Вернуться'
new_ref_bonys_ms='🎉Реферальный бонус сменен на `{refBonys}%`!'

acsii_noth_ms='✖️У вас еще нет акций'
btn_acsii=['➕Добавить акции','⬅️Вeрнуться']
add_acsii='Введи акциии (в одном сообщении):'
btn_acsii_beh='🔙Вeрнуться'
btn_acsii_beh_ms='Возвращаюсь в меню'
add_acsii_sec='Акции успешно обновлены!'


rule_noth_ms='✖️У вас еще нет правил'
btn_rule=['➕Добавить правила','⬅️Вeрнyться']
add_rule='Введи правила (в одном сообщении):'
btn_rule_beh='🔙Вeрнyться'
btn_rule_beh_ms='Возвращаюсь в меню'
add_rule_sec='Правила успешно обновлены!'

btrn_error_not_val='❌Обмен невозможен, т.к. в обменнике не указаны валюты обмена'
how_crypto_change_ms='💰 Какую валюту нужно обменять?'
how_crypto_change_take_ms='💰 Какую валюту хотите получить?'
choose_sum_ms='Отлично, укажите сумму 💬'
comment_ms='Отлично, оставтье комментарий и контакт для связи 💬'
change_beh='Возвращаюсь в меню'
btn_change_beh='◀️Назад◀️'
btn_change_beh2='◀️Haзaд◀️'
form_ms='💾 Ваша заявка:\n\n 📈Какую валюту нужно обменять > `{fromm}`\n 📉Какую валюту хотите получить > `{too}`\n 💸Сумма > `{sum}`\n 📝Комментарий > `{comm}`'
btn_form=['✉️Отправить✉️','🗑Отменить🗑']
form_suc_ms='✅Ваща заявка была успешно отправлено!'
for_admin_form_ms='Новая заявка от @{username} (`{tg_id}`)!\nОн хочет обменять `{fromm}` на `{too}`. Сумма: `{sum}`. Комментарий: `{comm}`'
btn_for_admin_form=['✉️Написать','💰Выплатить','❌Забанить']

trade_conf='✅Ваша сделка успешно закрыта!'
fromReferalBonys='🎉Вам начислен бонус за вашего реферала @{username} (`{referal}`) в размере `{summa}`. На вашем реф.балансе уже `{refBal}`!'

ref_system_of_ms='Реф.система офнута'
user_havent_ref='У юзера нет рефералов'

input_id='Введи id юзера'
input_id_beh='◀️Возврaт'
user_inf='Юзер: @{username}\nId: `{tg_id}`\nРефералов: `{referalsCol}`\nРеф.Баланс: `{referalsBal}`\nЯвляется рефералом: `{myReferal}`\nСделок: `{trades}`\nОбщая сумма сделок: `{tradesSum}`\nБан: `{ban}`'
btn_user_inf=['⚒Изменить баланс','🔪Забанить','Мeню']

money_input='💵Введи сумму, которая должна быть на балансе у человека'
money_input_suc='✅Баланс успешно изменен!'