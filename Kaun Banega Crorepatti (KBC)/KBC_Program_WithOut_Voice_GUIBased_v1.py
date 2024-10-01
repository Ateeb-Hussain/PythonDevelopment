import pyttsx3
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from queue import Queue

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
            "A. 118   B.   120   C. 100   D. 150",
            "A. Force   B. Property   C. P = mv   D. Mass",
            "A. 114   B. 115   C. 116   D. 124",
            "A. Jerusalem   B. Hamas   C. Gaza   D. Israel",
            "A. 10   B. 5   C. 77   D. 11",
            "A. 40   B. 50   C. 57   D. 77",
            "A. 180   B. 195   C. 100   D. 265",
            "A. Pakistan   B. China   C. Russia   D. India",
            "A. Nope   B. Absolutely Not   C. No of course   D. No",
            "A. Nope   B. Absolutely Candyland   C. No of course   D. No"
        ]
        self.balance = 0
        self.current_question = 0
        self.layout = BoxLayout(orientation='vertical')
        
        self.question_label = Label(text="")
        self.layout.add_widget(self.question_label)
        
        self.input_label = Label(text="")
        self.layout.add_widget(self.input_label)
        
        self.input_text = TextInput(multiline=False)
        self.layout.add_widget(self.input_text)
        
        self.submit_button = Button(text="Submit Answer")
        self.submit_button.bind(on_press=self.check_answer)
        self.layout.add_widget(self.submit_button)

        self.text_queue = Queue()
        Clock.schedule_interval(self.process_text_queue, 1)  # Check the queue every 1 second

        self.text_queue.put(self.questions[self.current_question])
        self.text_queue.put(self.options[self.current_question])

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
            self.text_queue.put(self.questions[self.current_question])
            self.text_queue.put(self.options[self.current_question])
        else:
            result += f" Your total winnings: {self.balance} Rupees."
            self.text_queue.put("Quiz Complete!")
            self.text_queue.put(result)

    def speak(self, text):
        print(text)
        engine.say(text)
        engine.runAndWait()

    def process_text_queue(self, dt):
        if not self.text_queue.empty():
            text = self.text_queue.get()
            if text == self.questions[self.current_question]:
                self.question_label.text = text
            elif text == self.options[self.current_question]:
                self.input_label.text = text
            else:
                self.speak(text)
            if text == "Quiz Complete!":
                self.stop()
    
if __name__ == '__main__':
    KBCApp().run()
