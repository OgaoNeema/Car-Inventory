import tkinter as tk

def draw_car(canvas, x, y, scale, base_color, window_color, wheel_color, rim_color,secondary_color):
    # Body
    canvas.create_rectangle(x, y, x + 220*scale, y + 50*scale, fill=base_color, outline="black", width=2)

    # Window frame and roof
    canvas.create_polygon(x+30*scale, y, x+80*scale, y-30*scale,
                          x+140*scale, y-30*scale, x+190*scale, y,
                          fill = secondary_color, outline="black", width=2)

    # Windows
    canvas.create_polygon(x+40*scale, y, x+81*scale, y-25*scale, #left window
                          x+110*scale, y-25*scale, x+110*scale, y,
                          fill=window_color, outline="black", width=1)
    canvas.create_polygon(x+114*scale, y, x+114*scale, y-25*scale, #right window
                          x+140*scale, y-25*scale, x+180*scale, y,
                          fill=window_color, outline="black", width=1)

    # Headlights and taillights
    canvas.create_rectangle(x+10*scale, y+10*scale, x+20*scale, y+20*scale, fill="#FFFF99", outline="black")
    canvas.create_rectangle(x+200*scale, y+10*scale, x+210*scale, y+20*scale, fill="red", outline="black")

    # Wheels and rims
    for dx in [30, 160]:
        canvas.create_oval(x+dx*scale, y+30*scale, x+(dx+30)*scale, y+60*scale, fill=wheel_color, outline="black", width=2)
        canvas.create_oval(x+(dx+8)*scale, y+38*scale, x+(dx+22)*scale, y+52*scale, fill=rim_color, outline="black", width=1)
