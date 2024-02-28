"""
File: draw.py 
Author: COMP 120 class
Description: A simple drawing program using Tkinter
"""

# Imports
import tkinter as tk
    
class Draw:
    def __init__(self):
        """ Initialize Draw object """

        # Set up window
        self.window = tk.Tk() 
        self.window.title("Drawing Program") 

        # Set some constants
        self.canvas_width = 600
        self.canvas_height = 400
        self.highlightthickness = 10
        self.frame_height = 50
        self.min_line_width = 1
        self.max_line_width = 10

        # Set default line color and thickness
        self.color = "black"
        self.line_width = 1
        
        # Place canvas in window
        self.canvas = tk.Canvas(self.window, width = self.canvas_width, 
            height = self.canvas_height, bg = "white", highlightbackground='black',
            highlightcolor='black', highlightthickness=self.highlightthickness)
        self.canvas.grid(row = 1, column = 1)
        
        # Bind canvas mouse events to handler.
        self.canvas.bind("<ButtonPress-1>", 
                self.mouse_press_handler)
        self.canvas.bind("<B1-Motion>", 
                self.mouse_motion_handler)

        # Create frame for color buttons
        self.color_frame = tk.Frame(self.window, width = self.canvas_width, height = self.frame_height)
        self.color_frame.grid(row = 2, column = 1)
        self.color_frame.grid_propagate(False)


        # Put color buttons in color frame.
        self.red_button = tk.Button(self.color_frame, text = 'red',
                    command = self.red, highlightbackground='red')
        self.red_button.grid(row = 1, column = 1)

        self.blue_button = tk.Button(self.color_frame, text = 'blue',
                    command = self.blue, 
                    highlightbackground = 'blue')
        self.blue_button.grid(row = 1, column = 2)

        self.green_button = tk.Button(self.color_frame, text = 'green',
                    command = self.green, 
                    highlightbackground = 'green')
        self.green_button.grid(row = 1, column = 3)

        self.yellow_button = tk.Button(self.color_frame, text = 'yellow',
                    command = self.yellow, 
                    highlightbackground = 'yellow')
        self.yellow_button.grid(row = 1, column = 4)

        self.black_button = tk.Button(self.color_frame, text = 'black',
                    command = self.black, 
                    highlightbackground = 'black')
        self.black_button.grid(row = 1, column = 5)

        # Center the color buttons in their frame
        self.color_frame.grid_rowconfigure(1, weight = 1)
        self.color_frame.grid_columnconfigure(1, weight = 0)
        self.color_frame.grid_columnconfigure(2, weight = 0)
        self.color_frame.grid_columnconfigure(3, weight = 0)
        self.color_frame.grid_columnconfigure(4, weight = 0)
        self.color_frame.grid_columnconfigure(5, weight = 0)
        self.color_frame.grid_columnconfigure(0, weight = 5)
        self.color_frame.grid_columnconfigure(6, weight = 5)

        # Create frame for line width slider
        self.line_width_slider_frame = tk.Frame(self.window, width = self.canvas_width, height = self.frame_height)
        self.line_width_slider_frame.grid(row = 3, column = 1)
        self.line_width_slider_frame.grid_propagate(False)

        # Put the slider in the frame
        self.line_width_slider = tk.Scale(self.line_width_slider_frame,
                    from_ = self.min_line_width, to = self.max_line_width, 
                    label = 'line width',
                    showvalue = False,
                    orient = tk.HORIZONTAL)
        self.line_width_slider.grid(row = 1, column = 1)
        self.line_width_slider.configure(
                command = self.line_width_handler)

        # Center the slider in its frame.
        self.line_width_slider_frame.grid_rowconfigure(1, weight = 1)
        self.line_width_slider_frame.grid_columnconfigure(1, weight = 1)

        # Create frame for clear and quit buttons
        self.button_frame = tk.Frame(self.window, width = self.canvas_width, height = self.frame_height)
        self.button_frame.grid(row = 4, column = 1)
        self.button_frame.grid_propagate(False)
        
        # Put the clear and quit buttons in their freame.
        self.clear_button = tk.Button(self.button_frame, 
                    text = "Clear",
                    command = self.clear_canvas)
        self.clear_button.grid(row = 1, column = 1)
        self.quit_button = tk.Button(self.button_frame, 
                text = "Quit",
                command = self.quit)
        self.quit_button.grid(row = 1, column = 2)

        # Center the clear and quit buttons in their frame.
        self.button_frame.grid_rowconfigure(1, weight = 1)
        self.button_frame.grid_columnconfigure(1, weight = 1)
        self.button_frame.grid_columnconfigure(2, weight = 1)
        self.button_frame.grid_columnconfigure(0, weight = 5)
        self.button_frame.grid_columnconfigure(3, weight = 5)

        # Start event loop
        self.window.mainloop() 
    
    def clear_canvas(self):
        """ Clear the drawings in the canvas """
        self.canvas.delete("line")

    def red(self):
        """ Make line color red """
        self.color = 'red'
    
    def blue(self):
        """ Make line color blue """
        self.color = 'blue'

    def green(self):
        """ Make line color green """
        self.color = 'green'

    def yellow(self):
        """ Make line color yellow """
        self.color = 'yellow'

    def black(self):
        """ Make line color black """
        self.color = 'black'

    def mouse_press_handler(self, event):
        """ Handle mouse press in canvas """
        # Remember x, y coords for the first mouse motion event.
        self.prev_x = event.x
        self.prev_y = event.y

    def mouse_motion_handler(self, event):
        """ Handle mouse movement in canvas """
        # Get location of mouse, and draw a line
        # from previous location to current location.
        #print(f"P{event.x},{event.y}")
        cur_x = event.x
        cur_y = event.y
        self.canvas.create_line(self.prev_x, self.prev_y, 
                cur_x, cur_y, fill = self.color, 
                width = self.line_width, tags = "line")
        self.prev_x = cur_x
        self.prev_y = cur_y

    def quit(self):
        """ Quit program """
        self.window.destroy()

    def line_width_handler(self, value):
        """ Change line width.  """ 
        self.line_width = int(value)

if __name__ == "__main__":
    # Create GUI
    Draw() 
