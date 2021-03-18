from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.whatdoestrumpthink.com/api/v1/quotes/random/")  # get request to that API
    response.raise_for_status()  # raise exception in the case of unsuccessful request

    data = response.json()  # parse the response into JSON
    quote = data['message']  # extract quote from the data
    canvas.itemconfig(quote_text, text=quote)  # update the text to be displayed


window = Tk()
window.title("Trump's thoughts...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=" Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

trump_img = PhotoImage(file="trump.png")
trump_button = Button(image=trump_img, highlightthickness=0, command=get_quote)
trump_button.grid(row=1, column=0)

window.mainloop()
