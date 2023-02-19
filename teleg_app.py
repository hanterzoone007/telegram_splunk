from telethon import TelegramClient, events
import requests as r
import json


# api_id = 'api_id'
# api_hash = 'api_hash'

# chats = [chats_id]

header = { 'Authorization' : 'Splunk token',
        'Content-Type': 'application/x-www-form-urlencoded',}

client = TelegramClient(str('/opt/splunk/etc/apps/tested_app/bin/anon.session'),api_id, api_hash)

@client.on(events.NewMessage)
async def main(event):
    if event.chat_id in chats:
        data = '{"sourcetype": "_json", "event": "{\\"chatId\\":\\"'+str(event.chat_id)+'\\",\\"chatMessage\\":\\"'+event.message.text.encode('utf-8').decode('unicode-escape')+'\\",\\"userId\\":\\"'+str(event.message.from_id.user_id)+'\\",\\"date\\":\\"'+str(event.date)+'\\"}"}'
        conee=r.post('http://192.168.56.101:8088/services/collector/event',headers=header,data=data,verify=False)
        print(conee.text)
        print(event.chat_id, event.message.from_id.user_id,event.message.text,event.date)

@client.on(events.ChatAction)
async def main(event):
    if event.chat_id in chats:
        data = '{"sourcetype": "_json", "event": "{\\"action\\":\\"'+str(event.respond)+'\\",\\"titleChange\\":\\"'+str(event.action_message).encode('utf-8').decode('unicode-escape')+'\\",\\"userId\\":\\"'+str(event.user_id)+'\\"}"}'
        conee=r.post('http://192.168.56.101:8088/services/collector/event',headers=header,data=data,verify=False)
        print(conee.text)

client.start('0')

client.run_until_disconnected()

