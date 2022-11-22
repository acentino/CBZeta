from curses.panel import top_panel
from msilib.schema import Directory
import os
#from tkinter import *
from cgitb import text
from re import MULTILINE
from turtle import width
from kivy.app import App
from tkinter import filedialog
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class Container(BoxLayout):
    pass

#SourceDirectory = filedialog.askdirectory()
#path = os.path.realpath(path)
#print(path)

class CBZeta(App):

    path = r'src'
    newpath = ''

    def build(self):
        
        #Create GUI

        self.window = GridLayout(
                                cols=2,
                                row_force_default=True,
                                row_default_height= 40
                                )

        self.top_grid = GridLayout(
                                cols=1,
                                row_force_default=True,
                                row_default_height= 40
                                )
        
        self.window.add_widget(self.top_grid)

        #Number of collumns
        self.top_grid.cols = 5

        self.top_grid.rows = 2

        #Margin
        self.top_grid.size_hint = (0.6, 0.7)

        #Centering GUI
        self.top_grid.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #Logo
        self.top_grid.add_widget(Image(source="data/logo.png"))

        #Source Label
        self.top_grid.srclabel = Label(
                                text= "Source : " + self.path,
                                font_size='20sp'
                            )
        self.top_grid.add_widget(self.top_grid.srclabel)

        #Create GUI
        self.window.bottom_grid = GridLayout(
                                cols=1,
                                row_force_default=True,
                                row_default_height= 40
                                )

        #Number of collumns
        self.window.bottom_grid.cols = 3
        self.window.bottom_grid.rows = 1

        

        #Change source folder
        self.bottom_grid.changesrcfolderbutton = Button(
                                text="Source Folder",
                                size_hint_x= None,
                                size_hint_y= None,
                                height = 50,
                                width = 150,
                                bold = True,
                                background_color = '#FFFFFF'
                                )
        self.bottom_grid.changesrcfolderbutton.bind(on_press=self.changesrcfolder)
        self.bottom_grid.add_widget(self.changesrcfolderbutton)

        #ZIP/RAR to CBZ/CBR Convertion button
        self.bottom_grid.ziprarconvbutton = Button(
                                text="ZIP/RAR/PDF to CBZ/CBR",
                                size_hint_x= None,
                                size_hint_y= None,
                                height = 50,
                                width = 200,
                                bold = True,
                                background_color = '#FFFFFF'
                                )
        self.bottom_grid.ziprarconvbutton.bind(on_press=self.ziprarconvertion)
        self.bottom_grid.add_widget(self.ziprarconvbutton)
        
        #CBZ/CBR to ZIP/RAR Convertion button
        self.bottom_grid.cbzcbrconvbutton = Button(
                                text="CBZ/CBR to ZIP/RAR",
                                size_hint_x= None,
                                size_hint_y= None,
                                height = 50,
                                width = 200,
                                bold = True,
                                background_color = '#FFFFFF'
                                )
        self.bottom_grid.cbzcbrconvbutton.bind(on_press=self.cbzcbrconvertion)
        self.bottom_grid.add_widget(self.cbzcbrconvbutton)

        self.add_widget(self.bottom_grid)


        return self.window

    #Change source folder
    def changesrcfolder(self, instance):
        SourceDirectory = filedialog.askdirectory()
        path = SourceDirectory
        os.path.realpath(path)
        self.newpath = path
        self.srclabel.text = path
        print(path)

    #Change ZIP/RAR extention to CBZ/CBR extention
    def ziprarconvertion(self, instance):

        if self.newpath:
            path = self.newpath
        else:
            path = r'src'

        with os.scandir(path) as files_and_folders:
            for element in files_and_folders:
                if element.is_file():
                    
                    root, ext = os.path.splitext(element.path)
                    if ext == '.zip':
                        new_path = root + ".cbz"
                        os.rename(element.path, new_path)
                    if ext == '.rar':
                        new_path = root + ".cbr"
                        os.rename(element.path, new_path)
                    if ext == '.pdf':
                        new_path = root + ".cbz"
                        os.rename(element.path, new_path)
                    if ext == '.7z':
                        new_path = root + ".cbr"
                        os.rename(element.path, new_path)
        print(self.path)


    def cbzcbrconvertion(self, instance):

        if self.newpath:
            path = self.newpath
        else:
            path = r'src'
        
        with os.scandir(path) as files_and_folders:
            for element in files_and_folders:
                if element.is_file():
                    
                    root, ext = os.path.splitext(element.path)
                    if ext == '.cbz':
                        new_path = root + ".zip"
                        os.rename(element.path, new_path)
                    if ext == '.cbr':
                        new_path = root + ".rar"
                        os.rename(element.path, new_path)
        print(self.path)
    
if __name__ == "__main__":
    CBZeta().run()