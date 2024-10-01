import streamlit as st
import requests
import toml
import json
import datetime
import os
from PIL import Image

DEFAULT_API_KEY = st.secrets["elevenlab"]["api_key"]
BASE_URL = "https://api.elevenlabs.io/v1"

AZURACAST_API_URL = "https://tuneyourstore.net/api/station/{station_id}/files/upload"  # Replace with actual URL
STATION_ID = "radio_1"  # Replace with your station ID

# Ensure audio directory exists
if not os.path.exists("audios"):
    os.makedirs("audios")

config_data = toml.load(".streamlit/config.toml")
theme_config = config_data.get("theme", {})
logo = Image.open("favicon.png")
try:
    st.set_page_config(
        page_title="Text to Speech App - Tune Your Store",
        layout="centered",
        initial_sidebar_state="auto",
        page_icon=logo,
    )  
except Exception as e:
    pass

# Add a logo at the top of the app
st.image("logo.png", use_column_width=True)

def get_available_voices(api_key):
    """Fetch the list of available voices using Eleven Labs API."""
    headers = {
        "Accept": "application/json",
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(f"{BASE_URL}/voices", headers=headers, timeout=10)

        if response.status_code == 200:
            return response.json().get('voices', [])
        else:
            st.error(f"Error fetching voices: {response.status_code} - {response.text}")
            return []

    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch voices. Error: {str(e)}")
        return []

def text_to_speech(api_key, text, model_id, voice_id, stability, similarity, style, speaker_boost, output_file, AZURACAST_API_KEY):
    """Convert text to speech using Eleven Labs API with customizable parameters."""
    tts_url = f'{BASE_URL}/text-to-speech/{voice_id}'
    headers = {
        'Content-Type': 'application/json',
        'xi-api-key': api_key,
    }
    payload = {
        'text': text,
        'model_id': model_id,
        'voice_settings': {
            'stability': stability,
            'similarity_boost': similarity,
            'style': style,
            'use_speaker_boost': speaker_boost,
        }
    }
    
    if not output_file:
        time_file = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
        output_file = f"AzuraCast_Generated_Audio_radio_1_session_{time_file}.wav"

    try:
        response = requests.post(tts_url, headers=headers, data=json.dumps(payload), timeout=30)

        if response.status_code == 200:
            # Save the output audio file
            audio_path = os.path.join("audios", output_file)
            with open(audio_path, 'wb') as f:
                f.write(response.content)
            st.success(f"Audio saved to {output_file}")
            st.audio(audio_path, format="audio/wav")

            # Upload the audio file to AzuraCast
            upload_to_azuracast(audio_path, AZURACAST_API_KEY)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Failed to generate speech. Error: {str(e)}")

def upload_to_azuracast(file_path, AZURACAST_API_KEY):
    """Uploads a generated audio file to AzuraCast."""
    if not os.path.exists(file_path):
        st.error("File does not exist.")
        return
    
    url = AZURACAST_API_URL.replace("{station_id}", STATION_ID)
    headers = {
        "Authorization": f"Bearer {AZURACAST_API_KEY}"
    }

    try:
        with open(file_path, "rb") as file:
            files = {
                "file": file
            }
            response = requests.post(url, headers=headers, files=files, timeout=30)

        if response.status_code == 200:
            st.success("Audio uploaded successfully to AzuraCast.")
        else:
            st.error(f"Failed to upload audio to AzuraCast. Error: {response.status_code} - {response.text}")
    
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to upload to AzuraCast. Error: {str(e)}")

st.markdown(
    """
    <style>
    * {
        list-style-type: none;
        margin: 0;
        padding: 0;
    }
    
    li {
        display: flex;
        align-items: center;
    }
    
    #home-icon {
        font-size: 24px;
    }
    
    a {
        font-family: 'Poppins', sans-serif;
        font-size: 18px;
        font-weight: bold;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    a:hover {
        transform: scale(1.1);
        color: black;
        transition: all ease 0.3s;
        text-decoration: none;
    }
    
    .material-symbols-outlined {
      font-variation-settings:
      'FILL' 1,
      'wght' 400,
      'GRAD' 0,
      'opsz' 24
    }
    </style>
    """, unsafe_allow_html=True
)

def main():
    st.title("Create Your Text-to-Speech Ad")

    # Sidebar with Google Material Icons for home
    st.sidebar.markdown("""
    <head>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    </head>
    <li>
        <a href='https://tuneyourstore.net/dashboard'>
            <span class="material-symbols-outlined">home</span>
        </a>
    </li>
    """, unsafe_allow_html=True)
    
    # API Key Section
    st.sidebar.header("API Key Settings")
    api_key = DEFAULT_API_KEY
    
    AZURACAST_API_KEY = st.sidebar.text_input("Enter your AzuraCast API key", type="password", placeholder="*Required Field")
    if st.sidebar.button("Save Key"):
        st.success("API key saved successfully.")

    output_file = st.sidebar.text_input("Enter output file name", type="default", placeholder="*Required Field")
    if st.sidebar.button("Save File"):
        st.success(f"Output file name set to: {output_file}")

    # TTS Mode Selection
    st.sidebar.header("Model")
    model = st.sidebar.selectbox("Select TTS Model", ["Eleven Multilingual V2", "Eleven Turbo V2_5", "Eleven Turbo V2", "Eleven Monolingual V1", "Eleven Multilingual V1"])
    models = {
        "Eleven Multilingual V2": "eleven_multilingual_v2",
        "Eleven Turbo V2_5": "eleven_turbo_v2_5",
        "Eleven Turbo V2": "eleven_turbo_v2",
        "Eleven Monolingual V1": "eleven_monolingual_v1",
        "Eleven Multilingual V1": "eleven_multilingual_v1"
    }
    model_id = models[model]

    # Fetch available voices
    voices = get_available_voices(api_key)

    if not voices:
        st.warning("No voices available. Check your API key and try again.")
        return

    voice_options = {voice['name']: voice['voice_id'] for voice in voices}
    voice_name = st.selectbox("Select a Voice", list(voice_options.keys()))
    voice_id = voice_options[voice_name]

    # Input text for TTS
    text = st.text_area("Enter the text to convert to speech", height=150)

    # Customization parameters for TTS
    st.sidebar.header("Customization Parameters")
    stability = st.sidebar.slider("Stability", 0.0, 1.0, 0.5, help="More variable to More stable")
    similarity = st.sidebar.slider("Similarity Boost", 0.0, 1.0, 0.75, help="Low to High")
    style = st.sidebar.slider("Style Exaggeration", 0.0, 1.0, 0.0, help="None to Exaggerated")
    speaker_boost = st.sidebar.checkbox("Speaker Boost")

    if st.button("Generate Speech"):
        if not output_file and not AZURACAST_API_KEY:
            st.warning("Please fill required fields to continue.")
        else:
            with st.spinner("Generating Speech..."):
                if text.strip():
                    text_to_speech(api_key, text, model_id, voice_id, stability, similarity, style, speaker_boost, output_file=output_file, AZURACAST_API_KEY=AZURACAST_API_KEY)
                else:
                    st.error("Please enter some text to convert.")

if __name__ == "__main__":
    main()