
import logging
from telegram.ext import *
import re


API_KEY = '1917620048:AAHXGQg5XQojEuJigkUebRGKNyVkG5TX_z4'


def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        process_message(message, ['hola', 'que tal', 'Hola como estas?'], 'Hola en que puedo ayudarte!'),
        process_message(message, ['adiós', 'hasta luego'], 'hasta pronto!' ),
        process_message(message, ['como', 'estas'], 'Estoy\' muy bien gracias!'),
        process_message(message, ['cual', 'es', 'tu', 'nombre,'], 'Mi nombre es Cherson, mucho gusto!'),
        process_message(message, ['Ayudame', 'por favor'], '¡Haré todo lo posible para ayudarlo!')
        # Add more responses here
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'No entendí lo que escribiste.'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response

# Test your system
# get_response('What is your name bruv?')
# get_response('Can you help me with something please?')