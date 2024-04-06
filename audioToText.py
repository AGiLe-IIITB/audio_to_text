import speech_recognition as sr

def audio_to_text(audio_file):
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        # Record the audio input
        audio_data = recognizer.record(source)
    
    try:
        print("Recognizing audio...")
        # Recognize the audio using Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
        print("Recognition complete.")
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"

# Replace 'audio_file.wav' with the path to your audio file
audio_file = input("Enter the name of the audio file with .wav extension: ")
text = audio_to_text(audio_file)
print("\nText from audio:", text)