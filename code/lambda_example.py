import json

def lambda_handler(event, context):
    message = 'Hi {} {}! Stay cool!!'.format(event['first_name'], event['other_name'])

    print(message)

    return {
        'message': message
    }
