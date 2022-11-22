from msilib.schema import Directory
import os
from cgitb import text
from re import MULTILINE
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#from tkinter import *
from tkinter import filedialog



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

        #Number of collumns
        self.window.cols = 5

        self.window.rows = 2

        #Margin
        self.window.size_hint = (0.6, 0.7)

        #Centering GUI
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #Logo
        self.window.add_widget(Image(source="data/logo.png"))

        #Source Label
        self.srclabel = Label(
                                text= "Source : " + self.path,
                                font_size='20sp'
                            )
        self.window.add_widget(self.srclabel)

        #Change source folder
        self.changesrcfolderbutton = Button(
                                text="Source Folder",
                                size_hint = (2.5, 0.5),
                                bold = True,
                                background_color = '#FFFFFF'
                                )
        self.changesrcfolderbutton.bind(on_press=self.changesrcfolder)
        self.window.add_widget(self.changesrcfolderbutton)

        #ZIP/RAR to CBZ/CBR Convertion button
        self.ziprarconvbutton = Button(
                                text="ZIP/RAR/PDF to CBZ/CBR",
                                size_hint = (2.5, 0.5),
                                bold = True,
                                background_color = '#FFFFFF'
                                )
        self.ziprarconvbutton.bind(on_press=self.ziprarconvertion)
        self.window.add_widget(self.ziprarconvbutton)
        
        #CBZ/CBR to ZIP/RAR Convertion button
        self.cbzcbrconvbutton = Button(
                                text="CBZ/CBR to ZIP/RAR",
                                size_hint = (2.5, 0.5),
                                bold = True,
                                background_color = '#FFFFFF'
                                )
        self.cbzcbrconvbutton.bind(on_press=self.cbzcbrconvertion)
        self.window.add_widget(self.cbzcbrconvbutton)
        
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