from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Planet Encycolopedia")
root.geomatry("500x500")
root.config(bg="lightblue")

Mercury = ImageTk.PhotoImage(Image.open ("Mercury.jpg"))
Venus = ImageTk.PhotoImage(Image.open ("Venus.jpg"))
Earth = ImageTk.PhotoImage(Image.open ("Earth.jpg"))
Mars = ImageTk.PhotoImage(Image.open ("Mars.jpg"))
Jupiter = ImageTk.PhotoImage(Image.open ("Jupiter.jpg"))
Saturn = ImageTk.PhotoImage(Image.open ("Saturn.jpg"))
Uranus = ImageTk.PhotoImage(Image.open ("Uranus.jpg"))
Neptune = ImageTk.PhotoImage(Image.open ("Neptune.jpg"))

label_planet = Label(root, text="Planet : ", bg="Lightblue")
label_planet_name = Label(root,font=("courier",18,"bold"),bg="lightblue")
LABEL_planet_image = Label(root,bg="gold2", highlightthickness=5, borderwidth=2,relief=SOLID)
label_planet_gravity_radius = Label(root,font=("castellar"), bg="lightblue")
label_planet_info = Label(root,font=("courier",10,"bold"), bg="lightblue", wrap=500)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable=selectdval)

def PlanetInfo():
    planet = selectedvl.get()
    if planet == "Mercury":
        label_planet_name['text']= "Mercury"
        label_planet_image['image'] = Mercury
        label_planet_gravity_radius['text'] = "Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        label_planet_info['text'] = " Mercury is the smallest planet in the Solar System and the closest to the Sun"
    elif planet == "Venus":
        label_planet_name['text']= "Venus"
        label_planet_image['image'] = Venus
        label_planet_gravity_radius['text'] = "Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
        label_planet_info['text'] = " Venus is the second planet in the Solar System and very hot planet with acid rain."
    elif planet == "Earth":
        label_planet_name['text']= "Earth"
        label_planet_image['image'] = Earth
        label_planet_gravity_radius['text'] = "Gravity : 9.807 m/s² \n Radius : 6,371 km"
        label_planet_info['text'] = " Mercury is the smallest planet in the Solar System and the closest to the Sun"
    elif planet == "Mars":
        label_planet_name['text']= "Mars"
        label_planet_image['image'] = Mars
        label_planet_gravity_radius['text'] = "Gravity : 3.721 m/s² \n Radius : 3,389.5 km"
        label_planet_info['text'] = "Mars is the fourth planet from the Sun and the third largest and massive terrestrial object in the Solar System."
    elif planet == "Jupiter":
        label_planet_name['text']= "Jupiter"
        label_planet_image['image'] = Jupiter
        label_planet_gravity_radius['text'] = "Gravity : 24.79 m/s² \n Radius : 69,911 km"
        label_planet_info['text'] = " Jupiter is the biggest planet in the solar system."
    elif planet == "Saturn":
        label_planet_name['text']= "Saturn"
        label_planet_image['image'] = Saturn
        label_planet_gravity_radius['text'] = "Gravity : 10.44 m/s² \n Radius : 58,232 km"
        label_planet_info['text'] = " It is 6th planet from the solar syatem."
    elif planet == "Uranus":
        label_planet_name['text']= "Uranus"
        label_planet_image['image'] = Uranus
        label_planet_gravity_radius['text'] = "Gravity : 8.87 m/s² \n Radius : 25,362 km"
        label_planet_info['text'] = " It is the seventh planet from the solar system and Uranus is the grandfather of zeus."
    elif planet == "Neptune":
         label_planet_name['text']= "Neptune"
         label_planet_image['image'] = Neptune
         label_planet_gravity_radius['text'] = "Gravity : 11.15 m/s² \n Radius : 24,622 km"
         label_planet_info['text'] = " Neptune is the eighth planet from the solar system."
dropdown.place(relx=0.5, rely=0.1 , anchor=CENTER)
btn = Button(root, text="Show Planet Info" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

label_planet.place(relx=0.2, rely=0.1 , anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor =CENTER)
label_planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
        