import customtkinter
from OSRSBytes import Items

items = Items()

items.update()

def button_callback():
    sell_average = customtkinter.CTkLabel(app, text="Sell average: " + str(items.getSellAverage(item_name.get())), fg_color="transparent")
    sell_average.grid(row=0, column=1, padx=20)

    sell_average = customtkinter.CTkLabel(app, text="Sell quantity: " + str(items.getSellQuantity(item_name.get())), fg_color="transparent")
    sell_average.grid(row=1, column=1, padx=20)

    sell_average = customtkinter.CTkLabel(app, text="Buy average: " + str(items.getBuyAverage(item_name.get())), fg_color="transparent")
    sell_average.grid(row=0, column=2, padx=20)

    sell_average = customtkinter.CTkLabel(app, text="Buy quantity: " + str(items.getBuyQuantity(item_name.get())), fg_color="transparent")
    sell_average.grid(row=1, column=2, padx=20)

    is_member = customtkinter.CTkLabel(app, text="Members: " + str(items.isMembers(item_name.get())), fg_color="transparent")
    is_member.grid(row=0, column=3, padx=20)

app = customtkinter.CTk()
app.title("OSRS GE tracker")
app.geometry("650x150")

button = customtkinter.CTkButton(app, text="Get data", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

item_name = customtkinter.CTkEntry(app, placeholder_text="Item name")
item_name.grid(row=1, column=0, padx=20)

app.mainloop()
