import os
import openai
# from colorama import Fore

# openai.api_key = os.environ ['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']

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

text = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "


def color_text(tex):
    tex = tex.split("\n")
    tex2 = []
    # q  	 if i[:1] == "A":

    # tex2.append(Fore.RED + i)
    # elif i[:1] == "H":
    # tex2.append(Fore.GREEN + i)
    # else:
    # tex2.append(Fore.WHITE + i)
    return "\n".join(tex2)


while True:
    os.system('clear')
    resp = input(color_text(text))
    text = text + resp + start_sequence
    response = openai.Completion.create(engine="text-davinci-001",
                                        prompt=text,
                                        temperature=1,
                                        max_tokens=150,
                                        top_p=1,
                                        frequency_penalty=1,
                                        presence_penalty=1,
                                        stop=[" Human:", " AI:"])
    os.system('clear')
    # text = text + rresponse.choices[0].text.replace("\n", "") + restart_sequence
    print(color_text(text))
#
