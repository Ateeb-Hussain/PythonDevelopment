from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class RockPaperScissorsApp(App):
    def build(self):
        self.p_score = 0

        layout = BoxLayout(orientation='vertical')

        options_layout = BoxLayout(orientation='horizontal', spacing=10)
        options_layout.add_widget(Button(text='Snake', on_press=self.choose_option))
        options_layout.add_widget(Button(text='Water', on_press=self.choose_option))
        options_layout.add_widget(Button(text='Gun', on_press=self.choose_option))

        self.result_label = Label(text='', font_size=20)

        layout.add_widget(options_layout)
        layout.add_widget(self.result_label)

        return layout

    def choose_option(self, instance):
        usert = instance.text  # No need to convert to lowercase

        user = {"Snake": 1, "Water": 2, "Gun": 3}[usert]
        comp = random.randint(1, 3)

        if comp == 1:
            compt = "Snake"
        elif comp == 2:
            compt = "Water"
        elif comp == 3:
            compt = "Gun"

        self.result_label.text = f"\nYou: {usert}\nComputer: {compt}"

        score = self.check(user, comp)
        self.p_score += score

        if score == 0:
            self.result_label.text += f"\nIt's a Draw!\nScore: {self.p_score}\n"
        elif score == 1:
            self.result_label.text += f"\nYou Win!\nScore: {self.p_score}\n"
        elif score == -1:
            self.result_label.text += f"\nYou Lose!\nScore: {self.p_score}\n"


    def check(self, user, comp):
        if user == comp:
            return 0
        elif user == 1 and comp == 2 or user == 2 and comp == 3 or user == 3 and comp == 1:
            return 1
        else:
            return -1

if __name__ == '__main__':
    RockPaperScissorsApp().run()
