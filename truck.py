import tkinter as tk

def draw_truck(canvas, x, y, scale, base_color, secondary_color, window_color, wheel_color, rim_color):
    scale *= 1.2 

    # Truck head
    canvas.create_rectangle(x, y, x + 120*scale, y + 100*scale,
                            fill=base_color, outline="black", width=2)

    # Truck body
    canvas.create_rectangle(x + 120*scale, y + 20*scale, x + 350*scale, y + 100*scale,
                            fill=secondary_color, outline="black", width=2)

    # Window
    canvas.create_rectangle(x + 20*scale, y + 20*scale, x + 100*scale, y + 60*scale,
                            fill=window_color, outline="black", width=1)

    # Wheels and rims
    for dx in [30, 250]:
        canvas.create_oval(x + dx*scale, y + 80*scale, x + (dx + 50)*scale, y + 130*scale,
                           fill=wheel_color, outline="black", width=3)
        canvas.create_oval(x + dx*scale + 15*scale, y + 95*scale, x + (dx + 50)*scale - 15*scale, y + 115*scale,
                           fill=rim_color, outline="black", width=1)
