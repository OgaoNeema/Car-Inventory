import tkinter as tk
import random
from vehicles import Car, SUV, Truck  # Import vehicle classes from external module
from roses import Roses               # Import rose drawing class
from car import draw_car              # Import car drawing function
from suv import draw_suv              # Import SUV drawing function
from truck import draw_truck          # Import truck drawing function

# Utility function to generate a random hex color
def random_color():
    return "#" + ''.join(random.choices('0123456789ABCDEF', k=6))

# Dictionary holding instances of each vehicle type with sample data
vehicle_instances = {
    "CAR": Car("BMW", 2001, 70000, 15000, 4),
    "SUV": SUV("Volvo", 2000, 30000, 18500, 5),
    "TRUCK": Truck("Toyota", 2002, 40000, 12000, "4WD"),
}

# Main application class for vehicle GUI
class VehicleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Inventory")

        # Set up the canvas for drawing vehicles
        self.canvas_width = 1000
        self.canvas_height = 600
        self.main_canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.main_canvas.pack()

        # Create buttons for each vehicle type
        for idx, vehicle in enumerate(["CAR", "SUV", "TRUCK"]):
            tk.Button(
                root,
                bg="#007ACC",
                fg="white",
                width=6,
                padx=20,
                pady=8,
                text=vehicle,
                command=lambda v=vehicle: self.display_vehicle(v)
            ).place(x=10 + idx * 100, y=10)

        # Created a frame for roses at the bottom
        self.rose_frame = tk.Frame(root, bg="white", bd=0)
        self.rose_frame.place(relx=0.5, rely=0.8, anchor="center", width=700, height=100)
        self.roses = Roses(self.rose_frame)  # Initialize roses display

        # Show default vehicle to be car on startup
        self.display_vehicle("CAR")

    # Function to display vehicle details
    def show_vehicle_info(self, vehicle_type):
        vehicle = vehicle_instances[vehicle_type]

        # Display a title
        self.main_canvas.create_text(720, 50, text="USED CAR INVENTORY", font=("Helvetica", 14, "bold", "underline"))

        # Prepare a list of detail lines
        details = [
            f"Make: {vehicle.get_make()}",
            f"Model: {vehicle.get_model()}",
            f"Mileage: {vehicle.get_mileage()}",
            f"Price: ${vehicle.get_price()}",
        ]

        # Add vehicle-specific detail
        if vehicle_type == "CAR":
            details.append(f"Number of doors: {vehicle.get_doors()}")
        elif vehicle_type == "SUV":
            details.append(f"Passenger Capacity: {vehicle.get_pass_cap()}")
        elif vehicle_type == "TRUCK":
            details.append(f"Drive type: {vehicle.get_drive_type()}")

        # Display each line of detail on the canvas
        for i, line in enumerate(details):
            self.main_canvas.create_text(720, 80 + i * 20, text=line, font=("Helvetica", 12), anchor='center')

    # Method to draw and update the selected vehicle on the canvas
    def display_vehicle(self, vehicle_type):
        # Clear the canvas
        self.main_canvas.delete("all")

        # Draw a border around the canvas
        self.main_canvas.create_rectangle(3, 3, self.canvas_width - 3, self.canvas_height - 3, outline="black", width=4)

        # Generate random values
        scale = random.uniform(1.2, 1.1)
        base_color = random_color()
        secondary_color = random_color()
        window_color = "#cccccc"
        wheel_color = "#222222"
        rim_color = "#aaaaaa"
        x, y = 350, 260  # Starting position for drawing the vehicle

        # Draw selected vehicle type
        if vehicle_type == "CAR":
            draw_car(self.main_canvas, x, y, scale, base_color, window_color, wheel_color, rim_color, secondary_color)
        elif vehicle_type == "SUV":
            draw_suv(self.main_canvas, x, y, scale, base_color, window_color, wheel_color, rim_color, secondary_color)
        elif vehicle_type == "TRUCK":
            draw_truck(self.main_canvas, x, y, scale, base_color, secondary_color, window_color, wheel_color, rim_color)

        # Show vehicle information and update flowers
        self.show_vehicle_info(vehicle_type)
        self.roses.update_roses()

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleApp(root)
    root.mainloop()
