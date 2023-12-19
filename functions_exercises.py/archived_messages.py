# Archived Messages 8.11

def send_messages(txt_messages, sent_message):
    while txt_messages:
        txt_message = txt_messages.pop()
        print(f"{txt_message}")
        sent_message.append(txt_message)

txt_messages = ['hi', 'hello', 'salam', 'bonjour']
sent_message= []

# Printing list before function ran and after to show they are the same still

print(txt_messages)
send_messages(txt_messages[:], sent_message)
print(txt_messages)