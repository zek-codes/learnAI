import streamlit as st
import spacy
import pytextrank                                                                                                                                                                                                                                                                                                                                                                                                                                            
from gtts import gTTS
from io import BytesIO
import openai

# OpenAI API Key (replace with your own)
openai.api_key = ''

# Load the spaCy model and add PyTextRank to the pipeline
@st.experimental_memo
def load_nlp_model():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textrank")
    return nlp

nlp = load_nlp_model()

# Function to summarize text using spaCy and PyTextRank
def summarize(text, ratio=0.2):
    doc = nlp(text)
    # Calculate the number of sentences to include in the summary
    num_sentences = max(1, int(len(list(doc.sents)) * ratio))
    # Extract the top sentences
    summary = ' '.join([sent.text for sent in doc._.textrank.summary(limit_sentences=num_sentences)])
    return summary

# Function to extract key point sentences from the summary
def extract_key_points(summary, num_sentences=3):
  # Use spaCy to identify sentence boundaries
  doc = nlp(summary)
  sentences = [sent.text for sent in doc.sents]
  # Select the top sentences
  top_sentences = sentences[:num_sentences]
  return "\n".join(top_sentences)

# Function to refine key points using OpenAI
def refine_key_points(key_points, max_tokens=150):
  """
  Refine the key points using OpenAI to ensure they are relevant and sensible sentences.
  """
  prompt = f"""Here are some candidate key points from the summary:
{key_points}

Do these key points accurately reflect the most important aspects of the summarized text? Can you rewrite them to ensure they are concise, informative, and directly related to the summary content?"""

  response = openai.Completion.create(
      engine="babbage-002",
      prompt=prompt,
      max_tokens=max_tokens,
      n=1,
      stop=None,
      temperature=0.7,
  )
  refined_points = response.choices[0].text.strip()
  return refined_points

# Function to convert text to speech using gTTS
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

# Title of the app
st.title("Text Summarization and Text to Speech App")

# Text input for summarization
text = st.text_area("Enter Text Here", height=300)

# Check if text is provided
if text:
    # Summarize the text
    summary = summarize(text)

    # Create tabs for Text Summarization, Text to Speech, and Key Points
    tab1, tab2, tab3 = st.tabs(["Text Summarization", "Text to Speech", "Key Points"])

    # Tab 1: Text Summarization
    with tab1:
        st.write("Summary:")
        st.write(summary)

    # Tab 2: Text to Speech
    with tab2:
        if st.button('Generate Speech from Summary'):
            audio_file = text_to_speech(summary)
            st.audio(audio_file, format='audio/mp3', start_time=0)

    # Tab 3: Key Points
    with tab3:
        if st.button('Generate Key Points'):
            key_points = extract_key_points(summary)
            refined_points = refine_key_points(key_points)
            st.write("Key Points:")
            st.write(refined_points)
else:
    st.write("Please enter some text to summarize and generate speech.")
