# Text-to-Speech Audio Generator

This Python script converts text from a file into audio using the `pyttsx3` library. It allows you to choose from different voices (English, Hindi) and save the generated audio files to your Downloads folder.

## Features

- **Multiple Voice Options:** Choose from English (female) and Hindi (male/female) voices.
- **Adjustable Speech Rate:** Customize the speed of the generated speech.
- **File Input:** Read text from a specified text file.
- **Automatic File Naming:** Generates unique filenames for audio files to avoid overwriting.
- **Save to Downloads Folder:** Saves the audio files to your Downloads folder by default.

## Requirements

- Python 3.x
- `pyttsx3` library: Install using `pip install pyttsx3`

## Usage

1. **Run the script:** Execute the `Text_To_Speech_Voice_Generator.py` file.
2. **Select a voice:** Enter the corresponding number for the desired voice:
   - 2: English (Female)
   - 3: Hindi (Male)
   - 4: Hindi (Female)
3. **Enter the text file path:** Provide the full path to the text file you want to convert.
4. **Generate audio:** The script will read the text from the file, generate the audio, and save it to your Downloads folder.
5. **Repeat for more files:** You can continue entering text file paths to generate more audio files.
6. **Exit:** Enter 'exit' to quit the script.

## Example

```
Enter: 
2 for English voice (Female) 
3 for Hindi voice (Male) 
4 for Hindi voice (Female) 
The Selected voice is: 2

Enter the path of the text file or 'exit' to quit: D:\TextToSpeech_AudioGenerator_Completed\sample_text.txt

Audio saved as C:\Users\YourUsername\Downloads\audio01.wav at Downloads Folder
```

## Notes

- The script uses the default Downloads folder for saving audio files. You can modify the `downloads_folder` variable to change the output location.
- The speech rate can be adjusted by modifying the `rate` property in the script.
- The script uses the `find_next_file_number` function to ensure unique filenames for audio files.
- The script assumes the text file uses UTF-8 encoding. If your file uses a different encoding, adjust the `encoding` parameter in the `open` function.
