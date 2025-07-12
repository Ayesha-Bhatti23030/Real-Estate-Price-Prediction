import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def predict_price():
    house_type = house_type_var.get()
    rooms = rooms_var.get()
    bathrooms = bathrooms_var.get()
    area = area_var.get()
    location = location_var.get()
    city = city_var.get()

    if house_type in ['House', 'Flat']:
        if not rooms or not bathrooms:
            result = "Please enter number of rooms and bathrooms."
            result_label.config(text=result, fg="red")
            return
        price = int(area) * 2000 + int(rooms) * 50000 + int(bathrooms) * 30000
    else:
        price = int(area) * 2500

    if house_type and area and location and city:
        result = f"Predicted Price: PKR {price}"
    else:
        result = "Please fill all fields."

    result_label.config(text=result, fg="green")


def on_property_type_change(event):
    if house_type_var.get() in ['House', 'Flat']:
        rooms_label.grid()
        rooms_entry.grid()
        bathrooms_label.grid()
        bathrooms_entry.grid()
    else:
        rooms_label.grid_remove()
        rooms_entry.grid_remove()
        bathrooms_label.grid_remove()
        bathrooms_entry.grid_remove()
        rooms_var.set("")
        bathrooms_var.set("")

# === Main Window ===
window = tk.Tk()
window.title("Real Estate Moodboard UI")
window.geometry("1000x600")

# === Canvas for Background + Moodboard ===
canvas = tk.Canvas(window, width=1000, height=600)
canvas.pack(fill="both", expand=True)

# === Load and place small images in a grid without gaps ===
tile_width = 550
tile_height = 400
cols = 3  # number of images per row

mood_files = ["h1.jpg", "h7.jpg", "h3.jpg", "h4.jpg", "h5.jpg", "h6.jpg"]
loaded_images = []

for i, file in enumerate(mood_files):
    try:
        img = Image.open(file).resize((tile_width, tile_height))
        tk_img = ImageTk.PhotoImage(img)
        
        row = i // cols
        col = i % cols
        x = col * tile_width
        y = row * tile_height

        canvas.create_image(x, y, image=tk_img, anchor="nw")
        loaded_images.append(tk_img)  # keep reference
    except Exception as e:
        print(f"Failed to load {file}: {e}")


#Create main form 
form_frame = tk.Frame(canvas, bg="#ffffff", bd=0,highlightbackground="#d0d0e1", highlightthickness=2)

form_window = canvas.create_window(600, 200, anchor="nw", window=form_frame)


# Fonts (modern & aesthetic)
label_font = ("Century Gothic", 11)
entry_font = ("Century Gothic", 10)
button_font = ("Century Gothic", 11, "bold")
title_font = ("Century Gothic", 17, "bold")
entry_opts = {'font': entry_font, 'width': 33, 'relief': 'flat',
              'highlightbackground': '#cfcfe8', 'highlightthickness': 1, 'bg': '#ffffff'}
# Variables
house_type_var = tk.StringVar()
rooms_var = tk.StringVar()
bathrooms_var = tk.StringVar()
area_var = tk.StringVar()
location_var = tk.StringVar()
city_var = tk.StringVar()


# Title
tk.Label(form_frame, text="Real Estate Price Predictor", font=title_font,
         bg="#f9f9fb", fg="#2c2c3e").grid(row=0, columnspan=2, pady=(20, 15))


# Property Type
tk.Label(form_frame, text="Property Type:", font=label_font, bg="#f9f9fb", fg="#444").grid(row=1, column=0, pady=5, padx=20, sticky="e")
house_type_menu = ttk.Combobox(form_frame, textvariable=house_type_var,
                               values=["House", "Flat", "Plot", "Shop", "Warehouse"],
                               font=entry_font, state="readonly", width=30)
house_type_menu.grid(row=1, column=1, pady=5, padx=10, sticky="w")
house_type_menu.bind("<<ComboboxSelected>>", on_property_type_change)

# Rooms & Bathrooms (conditionally shown)
rooms_label = tk.Label(form_frame, text="Number of Rooms:", font=label_font,bg="#f9f9fb", fg="#444")
rooms_label.grid(row=2, column=0, pady=5, padx=20, sticky="e")
rooms_entry = tk.Entry(form_frame, textvariable=rooms_var, **entry_opts)
rooms_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w")

bathrooms_label = tk.Label(form_frame, text="Number of Bathrooms:", font=label_font, bg="#f9f9fb", fg="#444")
bathrooms_label.grid(row=3, column=0, pady=5, padx=20, sticky="e")
bathrooms_entry = tk.Entry(form_frame, textvariable=bathrooms_var, **entry_opts)
bathrooms_entry.grid(row=3, column=1, pady=5, padx=10, sticky="w")

# Area
tk.Label(form_frame, text="Area (sq. ft.):", font=label_font,  bg="#f9f9fb", fg="#444").grid(row=4, column=0, pady=5, padx=20, sticky="e")
tk.Entry(form_frame, textvariable=area_var, **entry_opts).grid(row=4, column=1, pady=5, padx=10, sticky="w")

# Location
tk.Label(form_frame, text="Location:", font=label_font,  bg="#f9f9fb", fg="#444").grid(row=5, column=0, pady=5, padx=20, sticky="e")
tk.Entry(form_frame, textvariable=location_var, **entry_opts).grid(row=5, column=1, pady=5, padx=10, sticky="w")

# City
tk.Label(form_frame, text="City:", font=label_font,  bg="#f9f9fb", fg="#444").grid(row=6, column=0, pady=5, padx=20, sticky="e")
tk.Entry(form_frame, textvariable=city_var, **entry_opts).grid(row=6, column=1, pady=5, padx=10, sticky="w")

predict_btn = tk.Button(
    form_frame, text="🔮 Predict Price", font=button_font,
    bg="#a78bfa", fg="white", activebackground="#c4b5fd",
    relief="flat", padx=15, pady=8, cursor="hand2",
    command=predict_price
)
predict_btn.grid(row=7, columnspan=2, pady=20)

# Result Label
result_label = tk.Label(form_frame, text="", font=("Century Gothic", 12, "bold"), bg="#f9f9fb", fg="#333")
result_label.grid(row=8, columnspan=2, pady=(0, 15))

window.mainloop()
