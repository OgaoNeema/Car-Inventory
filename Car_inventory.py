import tkinter as tk
import random
from roses import Roses

def random_color():
    # Generates a random color.
    return "#" + ''.join(random.choices('0123456789ABCDEF', k=6))

# A dictionary holding basic vehicle details
vehicles = {
    "SALOON": {"make": "BMW", "model": 2001, "mileage": 70000, "price": 15000, "extra": "4"},
    "SUV": {"make": "Volvo", "model": 2000, "mileage": 30000, "price": 18500, "extra": "5"},
    "TRUCK": {"make": "Toyota", "model": 2002, "mileage": 40000, "price": 12000, "extra": "4WD"},
}

class VehicleApp:
    # Initializing the main window
    def __init__(self, root):
        self.root = root
        self.root.title("Car Inventory")  # title
        self.canvas_width = 1000
        self.canvas_height = 600
        # Where the vehicles are drawn
        self.main_canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.main_canvas.pack()
        
        # Buttons to draw the corresponding vehicle(v)
        for idx, vehicle in enumerate(["SALOON", "SUV", "TRUCK"]):
            tk.Button(root, bg="#007ACC", fg="white", width=6, padx=20, pady=8, text=vehicle, command=lambda v=vehicle: self.display_vehicle(v)).place(x=10 + idx*100, y=10)

        # Frame for roses
        self.rose_frame = tk.Frame(root, bg="white", bd=0, highlightthickness=0, relief="flat")
        self.rose_frame.place(relx=0.5, rely=0.8, anchor="center", width=700, height=100)
        self.roses = Roses(self.rose_frame) 
        
        # Initial vehicle
        self.display_vehicle("SALOON")
    
    def show_vehicle_info(self, vehicle_type):
        vehicle = vehicles[vehicle_type]
        title = "USED CAR INVENTORY"
        labels = {
            "SALOON": "Number of doors:",
            "SUV": "Passenger Capacity",
            "TRUCK": "Drive type"
        }

        self.main_canvas.create_text(720, 50, text=title, font=("Helvetica", 14, "bold", "underline"))

        details = [
            f"Make: {vehicle['make']}",
            f"Model: {vehicle['model']}",
            f"Mileage: {vehicle['mileage']}",
            f"Price: ${vehicle['price']}",
            f"{labels[vehicle_type]} {vehicle['extra']}"  # Other details ie no of doors and drive type
        ]
        # Showing the vehicle detail
        for i, line in enumerate(details):
            self.main_canvas.create_text(720, 80 + i*20, text=line, font=("Helvetica", 12), anchor='center')

    def display_vehicle(self, vehicle_type):
        self.main_canvas.delete("all")  # First clears the canvas
        # Draw a black outer border around the canvas
        self.main_canvas.create_rectangle(3, 3, self.canvas_width-3, self.canvas_height-3, outline="black", width=4)

        scale = random.uniform(0.9, 1.1)  # Used to randomize the size of the vehicle
        base_color = random_color()  # random vehicle color
        secondary_color = random_color()  # For the truck
        window_color = "#e0f7fa"
        wheel_color = "#222222"
        rim_color = "#aaaaaa"

        x, y = 400, 260  # Base position for drawing the vehicle

        # Saloon 
        if vehicle_type == "SALOON":
            # Body
            self.main_canvas.create_rectangle(x, y, x + 220*scale, y + 50*scale, fill=base_color, outline="black", width=2)
            # Roof and window frame
            self.main_canvas.create_polygon(x+30*scale, y, x+80*scale, y-30*scale,
                                            x+140*scale, y-30*scale, x+190*scale, y,
                                            fill=base_color, outline="black", width=2)
            # Windows
            self.main_canvas.create_polygon(x+40*scale, y, x+81*scale, y-25*scale,
                                            x+110*scale, y-25*scale, x+110*scale, y,
                                            fill=window_color, outline="black", width=1)
            self.main_canvas.create_polygon(x+114*scale, y, x+114*scale, y-25*scale,
                                            x+140*scale, y-25*scale, x+180*scale, y,
                                            fill=window_color, outline="black", width=1)
            # Wheels and rims
            for dx in [30, 160]:
                self.main_canvas.create_oval(x+dx*scale, y+30*scale, x+(dx+30)*scale, y+60*scale,
                                             fill=wheel_color, outline="black", width=2)
                self.main_canvas.create_oval(x+(dx+8)*scale, y+38*scale, x+(dx+22)*scale, y+52*scale,
                                             fill=rim_color, outline="black", width=1)
            # Headlights and taillights
            self.main_canvas.create_oval(x+5*scale, y+15*scale, x+15*scale, y+25*scale, fill="#FFFF99", outline="black")
            self.main_canvas.create_oval(x+205*scale, y+15*scale, x+215*scale, y+25*scale, fill="red", outline="black")

        # SUV
        elif vehicle_type == "SUV":
            # Body
            self.main_canvas.create_rectangle(x-20, y-10, x + 290*scale, y + 80*scale,
                                              fill=base_color, outline="black", width=3)
            self.main_canvas.create_polygon(x+40*scale, y-10, x+100*scale, y-60*scale,
                                            x+180*scale, y-60*scale, x+240*scale, y-10,
                                            fill=base_color, outline="black", width=3)
            # Windows
            self.main_canvas.create_polygon(x+50*scale, y-10, x+100*scale, y-53*scale,
                                            x+135*scale, y-53*scale, x+135*scale, y-10,
                                            fill=window_color, outline="black", width=2)
            self.main_canvas.create_polygon(x+140*scale, y-10, x+140*scale, y-53*scale,
                                            x+180*scale, y-53*scale, x+230*scale, y-10,
                                            fill=window_color, outline="black", width=2)
            # Tyres and rims
            for dx in [40, 190]:
                self.main_canvas.create_oval(x+dx*scale, y+60*scale, x+(dx+50)*scale, y+110*scale,
                                             fill=wheel_color, outline="black", width=3)
                self.main_canvas.create_oval(x+(dx+10)*scale, y+70*scale, x+(dx+40)*scale, y+100*scale,
                                             fill=rim_color, outline="black", width=2)
            # Grille
            self.main_canvas.create_line(x-15, y+20, x+10, y+20, fill="black", width=4)

        # Truck
        elif vehicle_type == "TRUCK":
            # Truck head
            self.main_canvas.create_rectangle(x, y, x + 120*scale, y + 100*scale,
                                              fill=base_color, outline="black", width=2)
            # Larger cargo area
            self.main_canvas.create_rectangle(x+120*scale, y+20*scale, x + 350*scale, y + 100*scale,
                                              fill=secondary_color, outline="black", width=2)
            # Window
            self.main_canvas.create_rectangle(x+20*scale, y+20*scale, x+100*scale, y+60*scale,
                                              fill=window_color, outline="black", width=1)
            # Wheels
            for dx in [30, 250]:
                self.main_canvas.create_oval(x+dx*scale, y+80*scale, x+(dx+50)*scale, y+130*scale,
                                             fill=wheel_color, outline="black", width=3)
                self.main_canvas.create_oval(x+dx*scale+15*scale, y+80*scale+15*scale,
                                             x+(dx+50)*scale-15*scale, y+130*scale-15*scale,
                                             fill=rim_color, outline="black", width=1)
            # Exhaust pipe
            self.main_canvas.create_line(x+110*scale, y, x+110*scale, y-30*scale, fill="gray", width=5)

        self.show_vehicle_info(vehicle_type)  # Vehicle details 
        self.roses.update_roses()

# Run app
if __name__ == "__main__":
    root = tk.Tk()  # Creating the root window
    app = VehicleApp(root)  # Instantiating the GUI
    root.mainloop()
