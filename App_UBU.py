import customtkinter

from customtkinter import CTkLabel

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("my app")
app.geometry("850x650")

customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


label = CTkLabel(app, text="Translator, Переводчик", corner_radius=10, fg_color='black', text_color='white',
                 width=500, height=50, font=(None, 17))
label.grid(padx=180, pady=40)  # разница в 50 пикселей




app.mainloop()

# Some changes???!!!

