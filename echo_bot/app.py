from time import sleep

def respond(message):
    return "I can hear you! You said '{}'.".format(message)

def send_message(message):
    response = respond(message)
    print("BOT: {}".format(response))

message = input('BOT: Hi there. What can I echo for ya?\n')
send_message(message)