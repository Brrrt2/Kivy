from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from username import username_helper
from password import password_helper
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window
from kivymd.uix.label import MDLabel

Window.size = (400,700)




class DemoApp(MDApp):


    def build(self):
        screen = Screen()
        label = MDLabel(text="LaShopee",pos_hint={'center_x':.88, 'center_y': .8})

        button=MDRectangleFlatButton(text='Show',
                               pos_hint={'center_x':0.6, 'center_y': 0.4},on_release=self.show_data)
        self.username = Builder.load_string(username_helper)

        self.password = Builder.load_string(password_helper)

        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(button)
        screen.add_widget(label)
        #screen.add_widget(img)
        return screen
    def show_data(self,obj):
        if self.username.text is "":
            check_string = "Please enter username/password"
        else:
            check_string = self.username.text + ' does not exists'

        close_button = MDFlatButton(text='Close',on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Log in' ,
                          text = check_string ,
                                size_hint=(0.7,1),
                                buttons=[close_button,more_button])
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()







DemoApp().run()