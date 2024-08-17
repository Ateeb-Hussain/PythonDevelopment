import pyttsx3
import os

# Function to find the next available file number
def find_next_file_number(folder, base_filename):
    i = 1
    while True:
        file_path = os.path.join(folder, f"{base_filename}{i:02d}.wav")
        if not os.path.exists(file_path):
            return file_path
        i += 1

i = int(input("Enter: \n2 for English voice (Female)\n3 for  Hindi voice (Male)\n4 for Hindi voice (Female)\nThe Selected voice is: "))

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[i].id)

# print(voices)

# Adjust the speech rate (WPM) to make it slower
if i == 2:
    engine.setProperty('rate', 150)  # Adjust the value as needed
else:
    engine.setProperty('rate', 200)  # Adjust the value as needed


# Infinite loop until 'exit' is entered
while True:
    text_file_path = input("Enter the path of the text file or 'exit' to quit: ")

    if text_file_path == 'exit':
        break

    if not os.path.exists(text_file_path):
        print("File not found.")
    else:
        # Read text from the file with explicit encoding
        with open(text_file_path, "r", encoding="utf-8") as file:
            text_to_speak = file.read()
            

        # Define the folder path for the saved audio files (Downloads folder by default)
        downloads_folder = os.path.expanduser("~") + "/Downloads"

        # Find the next available file number
        output_file = find_next_file_number(downloads_folder, "audio")

        # Convert text to speech and save the audio file in the default downloads folder
        engine.save_to_file(text_to_speak, output_file)
        engine.runAndWait()

        print(f"Audio saved as {output_file} at Downloads Folder") 