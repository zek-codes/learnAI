from gtts import gTTS

# Text to be converted to speech
text = "My name is Zivai Emmanuel Karenga, I am singer, athlete, designer and philanthropist."

# Language code (en for English, fr for French, etc.)
language = 'en'

# Optional: Slow down speech (slow=False for normal speed)
slow = False

# Create the gTTS object
tts = gTTS(text=text, lang=language, slow=slow)

# Save the audio to a file (mp3 format)
filename = "sampl2.mp3"
tts.save(filename)

print(f"Audio saved to: {filename}")

# Optionally, play the audio using an external library
# You'll need to install the playsound library: pip install playsound
# from playsound import playsound
# playsound(filename)
