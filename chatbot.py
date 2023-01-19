import openai
import tkinter as tk
import pyttsx3

engine = pyttsx3.init()
openai.api_key = "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"
previous_messages = []

def get_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()

def speak_response():
    last_response = previous_messages[-1]
    engine.say(last_response)
    engine.runAndWait()



def handle_input():
    user_input = input_field.get()
    previous_messages.append(f"You: {user_input}")
    response = get_response(user_input)
    previous_messages.append(f"Chatbot: {response}")
    chat_history.configure(state='normal')
    chat_history.insert(tk.END, f"You: {user_input}\n")
    chat_history.insert(tk.END, f"Chatbot: {response}\n")
    chat_history.configure(state='disabled')
    input_field.delete(0, tk.END)

root = tk.Tk()
root.title("Chatbot")
root.geometry("600x400")

input_field = tk.Entry(root)
input_field.config(width=100)
input_field.pack(side=tk.BOTTOM)
input_field.pack()

input_button = tk.Button(root, text="Send", command=handle_input)
input_button.pack(side=tk.BOTTOM)
input_button.pack()

speak_button = tk.Button(root, text="Speak", command=speak_response)
speak_button.pack(side=tk.RIGHT)

chat_history = tk.Text(root)
chat_history.pack()
chat_history.configure(state='disabled')
root.mainloop()