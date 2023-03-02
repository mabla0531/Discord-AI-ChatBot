import openai

tokenfile = open("chattoken.txt")
openai.api_key = tokenfile.read()
tokenfile.close()

def process_message(text):
    message = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    ).choices[0].message

    return message["content"]
