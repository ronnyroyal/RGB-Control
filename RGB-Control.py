#!/usr/bin/env python3

import os
import time
import serial
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

ser = serial.Serial('/dev/ttyUSB0', 500000)

file1 = open('RGB.value', 'r')
result = file1.read()

value1 = int(result[1:-6])
value2 = int(result[4:-3])
value3 = int(result[7:])

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    

        self.set_border_width(10)
        self.set_default_size(550, 250)

        grid = Gtk.Grid()
        self.add(grid)

        adjustment1 = Gtk.Adjustment(value1, 0, 255, 1.0, 1.0, 1.0)
        adjustment2 = Gtk.Adjustment(value2, 0, 255, 1.0, 1.0, 1.0)
        adjustment3 = Gtk.Adjustment(value3, 0, 255, 1.0, 1.0, 1.0)


        red = Gtk.Label(label="Red")
        grid.attach(red,0, 0, 3, 1)
        #Color slider for red
        self.colorscale1 = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjustment1)
        self.colorscale1.set_hexpand(True)
        grid.attach(self.colorscale1,0, 1, 3, 1)

        green = Gtk.Label(label="Green")
        grid.attach(green,0, 2, 3, 1)
        #Color slider for green
        self.colorscale2 = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjustment2)
        self.colorscale2.set_hexpand(True)
        grid.attach(self.colorscale2,0, 3, 3, 1)

        blue = Gtk.Label(label="Blue")
        grid.attach(blue,0, 4, 3, 1)
        #color slider for blue
        self.colorscale3 = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjustment3)
        self.colorscale3.set_hexpand(True)
        grid.attach(self.colorscale3,0, 5, 3, 1)

        #automodes
        blue = Gtk.Label(label="")
        grid.attach(blue,0, 6, 3, 1)

        auto = Gtk.Button.new_with_label("Auto")
        grid.attach(auto,0,7,1,1)
        
        strobo = Gtk.Button.new_with_label("Strobo")
        grid.attach(strobo,1,7,1,1)
        
        white = Gtk.Button.new_with_label("White")
        grid.attach(white,2,7,1,1)

        #setting the rest of the window settings
        self.set_title("RGB-Colour")
        self.connect("destroy", Gtk.main_quit)
        #connect the sliders to their functions
        self.colorscale1.connect("value-changed", self.on_scale1_adjusted)
        self.colorscale2.connect("value-changed", self.on_scale2_adjusted)
        self.colorscale3.connect("value-changed", self.on_scale3_adjusted)
        auto.connect("clicked", self.auto_pressed)
        strobo.connect("clicked", self.strobo_pressed)
        white.connect("clicked", self.white_pressed)
    
    #subfunctions for printing out the slider value
    def on_scale1_adjusted(self, scale):
        global value1
        value1 = int(self.colorscale1.get_value())
        #print("R" , end ="" )
        #print ( f'{value1:03}')
        #print ( "@" + f'{value1:03}' + f'{value2:03}' + f'{value3:03}')
        result = "@" + f'{value1:03}' + f'{value2:03}' + f'{value3:03}'
        ser.write(result.encode())
        file1 = open('RGB.value', 'w')
        file1.write(result)
        file1.close()
        time.sleep(0.05)

    def on_scale2_adjusted(self, scale):
        global value2
        value2 = int(self.colorscale2.get_value())
        #print("G" , end ="" )
        #print ( f'{value2:03}')
        #print ( "@" + f'{value1:03}' + f'{value2:03}' + f'{value3:03}')
        result = "@" + f'{value1:03}' + f'{value2:03}' + f'{value3:03}'
        ser.write(result.encode())
        file1 = open('RGB.value', 'w')
        file1.write(result)
        file1.close()
        time.sleep(0.05)


    def on_scale3_adjusted(self, scale):
        global value3
        value3 = int(self.colorscale3.get_value())
        #print("B" , end ="" )
        #print ( f'{value3:03}')
        #print ( "@" + f'{value1:03}' + f'{value2:03}' + f'{value3:03}')
        result = "@" + f'{value1:03}' + f'{value2:03}' + f'{value3:03}'
        ser.write(result.encode())
        file1 = open('RGB.value', 'w')
        file1.write(result)
        file1.close()
        time.sleep(0.05)

    def auto_pressed(self,button):
        print("Auto")
        colorscale1.set_value_pos(255)
    
    def strobo_pressed(self,button):
        print("Strobo")

    def white_pressed(self,button):
        print("White")

#print ( "@"f'{value1:03}' + f'{value2:03}' + f'{value3:03}')

win = MyWindow()
win.show_all()
Gtk.main()
