import imaplib
import email
import telebot   # установите в свое окружение библиотеку pip install PyTelegramBotAPI

bot = telebot.TeleBot('YOUTOKENBOT')  # укажите ваш токен

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('yougmail@gmail.com', 'gmailpassword')  # ваш новый аккаунт @gmail
mail.list()  # Смотрим на папки в ящике
mail.select('INBOX')  # Подключаемся к папке входящие
result, data = mail.uid('search', None, 'UNSEEN') # выбираем непрочитанные

i = len(data[0].split())
for x in range(i):
    latest_email_uid = data[0].split()[x]
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = email_data[0][1]
    mail.store(latest_email_uid, '+FLAGS', '\Deleted')  # удаляем чтоб не было повторной отправки
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string) # получаем сырое письмо в виде строки

for part in email_message.walk():
    if part.get_content_type() == "text/html" or part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        s = (email_message['Subject'])
        # Выделяем номер получателя 11 значный в виде 7XXXXXXXXXX с помощью среза,
        # если 12 значный например для Украины то s[5:17]
        numb = s[5:16]
        # декодируем тело письма и в Python3 отменяем unicode, если 2я ветка то отменять не нужно
        mss = str(body.decode('unicode-escape'))
        # выделяем номер отправителя
        abon = mss[54:67]
        # выделяем тело СМС, а именно собственно само сообщение
        smss = mss[77:]
        # форматируем для отправки
        soobsh = (numb + 'n' + 'n' + smss + 'n' + 'От:' + abon)
        bot.send_message(chat_id, soobsh) # укажите ваш chat_id и отправляйте в телегу ваше СМС
    else:
        continue