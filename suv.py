import tkinter as tk

def draw_suv(canvas, x, y, scale, base_color, window_color, wheel_color, rim_color, secondary_color):
    # Main body
    body_start = x - 30*scale
    body_end = x + 300*scale
    body_top = y - 10
    body_bottom = y + 80*scale
    canvas.create_rectangle(body_start, body_top, body_end, body_bottom, fill=base_color, outline="black", width=3)

    # Roof and window frame
    canvas.create_polygon(x+30*scale, y-10, x+100*scale, y-60*scale,
                          x+190*scale, y-60*scale, x+260*scale, y-10,
                          fill=secondary_color, outline="black", width=3)

    # Windows
    canvas.create_polygon(x+45*scale, y-10, x+100*scale, y-53*scale,
                          x+140*scale, y-53*scale, x+140*scale, y-10,
                          fill=window_color, outline="black", width=2)
    canvas.create_polygon(x+145*scale, y-10, x+145*scale, y-53*scale,
                          x+190*scale, y-53*scale, x+250*scale, y-10,
                          fill=window_color, outline="black", width=2)

    # Wheels and rims
    for dx in [40, 190]:
        canvas.create_oval(x+dx*scale, y+60*scale, x+(dx+50)*scale, y+110*scale, fill=wheel_color, outline="black", width=3)
        canvas.create_oval(x+(dx+10)*scale, y+70*scale, x+(dx+40)*scale, y+100*scale, fill=rim_color, outline="black", width=2)

    # Headlight (front-left square, reduced size)
    headlight_size = 10 * scale
    canvas.create_rectangle(body_start, y + 35*scale, body_start + headlight_size, y + 35*scale + headlight_size,
                            fill="yellow", outline="black", width=1)

    # Taillight (rear-right square, reduced size)
    canvas.create_rectangle(body_end - headlight_size, y + 35*scale, body_end, y + 35*scale + headlight_size,
                            fill="red", outline="black", width=1)
