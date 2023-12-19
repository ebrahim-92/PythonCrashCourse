# Sending Messages 8.10

def send_messages(txt_messages, sent_message):
    while txt_messages:
        txt_message = txt_messages.pop()
        print(f"{txt_message}")
        sent_message.append(txt_message)

txt_messages = ['hi', 'hello', 'salam', 'bonjour']
sent_message= []
send_messages(txt_messages, sent_message)