# OutriX-Task2
AWS Lambda function to reverse input text via API Gateway
# Let's generate the Lambda function code and a README.md for GitHub

lambda_code = 

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
"""

readme_content = """\
# AWS Lambda Text Reverser 🔁

This is a simple AWS Lambda function that takes a text input and returns the reversed version of it as a JSON response.

## ✅ Features

- Accepts text input via query string (e.g., ?text=hello)
- Returns JSON with original and reversed values
- Lightweight and ideal for AWS API Gateway triggers

## 🚀 Example

*API Endpoint:*

https://8ykoon98c3.execute-api.ap-south-1.amazonaws.com/default/OutriXTask2Function


*Response:*
json
{
  "original": "hello",
  "reversed": "olleh"
}


## 🧑‍💻 How to Deploy

1. Go to AWS Lambda Console
2. Create a new Lambda function (Python 3.12 or 3.11)
3. Replace the default code with lambda_function.py content
4. Attach an API Gateway trigger (HTTP API)
5. Deploy and test using the API URL

## 📁 Files

- lambda_function.py – Main Lambda handler
- README.md – This file

## 🏷 Tags

AWS Lambda API Gateway Python Serverless Beginner Project
"""

# Save both files to disk
from pathlib import Path

lambda_file_path = Path("/mnt/data/lambda_function.py")
readme_file_path = Path("/mnt/data/README.md")

lambda_file_path.write_text(lambda_code)
readme_file_path.write_text(readme_content)

lambda_file_path.name, readme_file_path.name
