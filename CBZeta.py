import os
from cgitb import text
from re import MULTILINE
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CBZeta(App):
    def build(self):
        
        #Create GUI
        self.window = GridLayout()

        #Number of collumns
        self.window.cols = 1

        #Margin
        self.window.size_hint = (0.6, 0.7)

        #Centering GUI
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #Logo
        self.window.add_widget(Image(source="data/logo.png"))

        #ZIP/RAR to CBZ/CBR Convertion button
        self.ziprarconvbutton = Button(
                                text="ZIP/RAR to CBZ/CBR",
                                size_hint = (1, 0.5),
                                bold = True,
                                background_color = '#FFFFFF'
                                )
        self.ziprarconvbutton.bind(on_press=self.ziprarconvertion)
        self.window.add_widget(self.ziprarconvbutton)

        #CBZ/CBR to ZIP/RAR Convertion button
        self.cbzcbrconvbutton = Button(
                                text="CBZ/CBR to ZIP/RAR",
                                size_hint = (1, 0.5),
                                bold = True,
                                background_color = '#FFFFFF'
                                )
        self.cbzcbrconvbutton.bind(on_press=self.cbzcbrconvertion)
        self.window.add_widget(self.cbzcbrconvbutton)
        
        return self.window

    #Change ZIP/RAR extention to CBZ/CBR extention
    def ziprarconvertion(self, instance):
        path_folder = r'src'
        
        with os.scandir(path_folder) as files_and_folders:
            for element in files_and_folders:
                if element.is_file():
                    
                    root, ext = os.path.splitext(element.path)
                    if ext == '.zip':
                        new_path = root + ".cbz"
                        os.rename(element.path, new_path)
                    if ext == '.rar':
                        new_path = root + ".cbr"
                        os.rename(element.path, new_path)
    
    def cbzcbrconvertion(self, instance):
        path_folder = r'.\src'
        
        with os.scandir(path_folder) as files_and_folders:
            for element in files_and_folders:
                if element.is_file():
                    
                    root, ext = os.path.splitext(element.path)
                    if ext == '.cbz':
                        new_path = root + ".zip"
                        os.rename(element.path, new_path)
                    if ext == '.cbr':
                        new_path = root + ".rar"
                        os.rename(element.path, new_path)




if __name__ == "__main__":
    CBZeta().run()
