
from PIL import Image
from pystray import *
from easygui import fileopenbox, msgbox
import os

from rembg import remove, new_session

class Main():
    def __init__(self):
        self.icon = Icon(
            name="zangetcy",
            icon=self.get_icon_image(), 
            menu=self.get_menu(),
        )
        
        self.session = new_session("isnet-anime")

    def get_icon_image(self):
        return Image.open("icon.ico")

    def get_menu(self):
        return Menu(
            MenuItem('Удалить фон', lambda: self.remove_background()),
            MenuItem('Выход', self.quit)
        )
        
    def remove_background(self):
        file_path = fileopenbox(
            msg="select img",
            title="zangetcy",
            filetypes=["*.jpg", "*.jpeg", "*.png"]
        )
        
        if not file_path:
            return

        try:
            image = remove(Image.open(file_path), session=self.session)
            
            directory, filename = os.path.split(file_path)
            name, ext = os.path.splitext(filename)
            
            save_path = os.path.join(directory, f"{name}_zangetcy.png")
            image.save(save_path)
            msgbox(f"ready\n{save_path}", title="success")
        except Exception as e:
            msgbox(f"error\n{str(e)}", title="error")

    def quit(self, icon, item):
        icon.stop()
        
    def run(self):
        self.icon.run()
        
if __name__ == "__main__":
    app = Main()
    app.run()