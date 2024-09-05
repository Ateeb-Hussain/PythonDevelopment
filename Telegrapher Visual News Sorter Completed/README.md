# Telegrapher Visual News Sorter

This Python script automates the sorting of visual news files (images, videos) downloaded from the internet. It organizes the files into daily folders and increments a counter for each new batch of files.

## Functionality

1. **Creates Daily Folders:**
   - The script checks if a folder for the current date exists in the target directory (`F:/Telegrapher.pk official/Telegrapher.pk Visual News`).
   - If not, it creates a new folder named with the current date (e.g., "2023 28 October").
   - It also creates a `config.py` file within the daily folder to store a counter for tracking the number of news batches.

2. **Moves and Renames Files:**
   - The script iterates through files in the source directory (`C:/Users/Khraab PC/Downloads`) that contain the letter "n" (likely indicating news files).
   - It moves these files to a new folder within the daily folder, named "News {counter}" (e.g., "News 1").
   - The files are then renamed sequentially (e.g., "0.jpg", "1.mp4", etc.).

3. **Updates Counter:**
   - After moving and renaming the files, the script increments the counter in the `config.py` file for the next batch of news files.

## Requirements

- Python 3.x
- `shutil` module (for file moving and renaming)
- `os` module (for file system operations)
- `datetime` module (for date handling)

## Usage

1. **Configure Paths:**
   - Modify the `source_path` variable to point to the directory where you download your news files.
   - Modify the `destination_path` variable to point to the desired location for storing the sorted news files.

2. **Run the Script:**
   - Execute the `Telegrapher_Visual_News_Sorter.py` script.

## Notes

- The script assumes that news files contain the letter "n" in their filenames.
- The script renames files sequentially, starting from 0.
- The counter is stored in a `config.py` file within the daily folder.

## Future Improvements

- Add error handling for cases where files cannot be moved or renamed.
- Implement a more robust file filtering mechanism to identify news files.
- Allow for user-defined file naming conventions.
- Add support for different file types (e.g., PDFs, documents).

This README provides a comprehensive overview of the Telegrapher Visual News Sorter script. Feel free to modify and enhance it to suit your specific needs.
