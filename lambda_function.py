import json

def lambda_handler(event, context):
    # Get the 'text' from the API call (query string)
    text = event.get('queryStringParameters', {}).get('text', '')

    # Reverse the input text
    reversed_text = text[::-1]

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'original': text,
            'reversed': reversed_text
        })
    }
