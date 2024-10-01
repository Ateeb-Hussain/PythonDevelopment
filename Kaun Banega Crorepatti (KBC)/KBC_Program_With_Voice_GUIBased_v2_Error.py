import pyttsx3
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)

class KBCApp(App):
    def build(self):
        self.answers = ["a", "b", "a", "a", "d", "c", "b", "d", "a", "b"]
        self.questions = [
            "How Many Elements are there in the Periodic Table?",
            "What is inertia?",
            "The Holy Quran has surahs:",
            "The Capital of Palestine is:",
            "Russia has Timezones.",
            "How Many Muslim Countries are there?",
            "According to USA, the Number of Countries in the World is:",
            "Country with the world's Largest Population is:",
            "Are you playing KBC",
            "Are Feastables better than Hershey's Chocolate bars?",
        ]
        self.options = [
            "A. 118\t\tB. 120\t\tC. 100\t\tD. 150",
            "A. Force\t\tB. Property\t\tC. P = mv\t\tD. Mass",
            "A. 114\t\tB. 115\t\tC. 116\t\tD. 124",
            "A. Jerusalem\t\tB. Hamas\t\tC. Gaza\t\tD. Israel",
            "A. 10\t\tB. 5\t\tC. 77\t\tD. 11",
            "A. 40\t\tB. 50\t\tC. 57\t\tD. 77",
            "A. 180\t\tB. 195\t\tC. 100\t\tD. 265",
            "A. Pakistan\t\tB. China\t\tC. Russia\t\tD. India",
            "A. Nope\t\tB. Absolutely Not\t\tC. No of course\t\tD. No",
            "A. Nope\t\tB. Absolutely Candyland\t\tC. No of course\t\tD. No"
        ]
        self.balance = 0
        self.current_question = 0
        self.layout = BoxLayout(orientation='vertical')
        
        self.question_label = Label(text=self.questions[self.current_question])
        self.layout.add_widget(self.question_label)

        self.input_label = Label(text=self.options[self.current_question])
        self.layout.add_widget(self.input_label)
        
        self.input_text = TextInput(multiline=False)
        self.layout.add_widget(self.input_text)
        
        self.submit_button = Button(text="Submit Answer")
        self.submit_button.bind(on_press=self.check_answer)
        self.layout.add_widget(self.submit_button)

        Clock.schedule_once(self.speak_question, 1)  # Speak the question after a delay

        return self.layout

    def check_answer(self, instance):
        answer = self.input_text.text.lower()
        if answer == self.answers[self.current_question]:
            self.balance += 500
            result = "Correct! You won 500 Rupees."
        else:
            self.balance = 0
            result = "Wrong! You lost all your winnings."
        
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.question_label.text = self.questions[self.current_question]
            self.input_label.text = self.options[self.current_question]
            Clock.schedule_once(self.speak_question, 1)  # Speak the new question after a delay
        else:
            result += f" Your total winnings: {self.balance} Rupees."
            self.question_label.text = "Quiz Complete!"
            self.input_label.text = result
            Clock.schedule_once(lambda dt: self.speak(result), 1)  # Speak the final result after a delay

    def speak(self, text):
        print(text)
        engine.say(text)
        engine.runAndWait()

    def speak_question(self, dt):
        self.speak(self.questions[self.current_question])
        self.speak(self.options[self.current_question])

if __name__ == '__main__':
    KBCApp().run()
