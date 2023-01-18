
import tkinter as tk
import openai
openai.api_key = "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"
def openai_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{input_text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def send_message():
    user_input = user_input_field.get()
    bot_response = openai_response(user_input)
    bot_response_field.config(text=bot_response)

root = tk.Tk()
root.title("OpenAI Chatbot")

user_input_field = tk.Entry(root)
user_input_field.pack()


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

bot_response_field = tk.Label(root, text="")
bot_response_field.pack()

root.mainloop()