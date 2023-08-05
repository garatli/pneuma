
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time  
import json
import urllib

# Function for loading animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function for querying Hugging Face models
def query_with_retry(payload, API_URL, headers, max_retries=3, delay=30):
    for i in range(max_retries):
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        except Exception as e:
            print(f'API Error: {str(e)}. Retrying in {delay} seconds.')
            if i < max_retries - 1:  # no delay for the last try
                time.sleep(delay)
            else:
                raise


# Function to fetch book details using Google Books API
def fetch_book_info(title):
    title = urllib.parse.quote(title)  # URL encode the book title
    response = urllib.request.urlopen(f'https://www.googleapis.com/books/v1/volumes?q={title}&key=AIzaSyCsYBqQ45tYCBhEbBbmpBFnB9cH1Bret_w')
    data = json.load(response)
    info = data['items'][0]['volumeInfo']  # Get info of the first matched book
    return info['title'], info['imageLinks']['thumbnail'], info['previewLink']

# Function for classifying and generating recommendations
def classify_and_recommend(text):
    progress_bar = st.progress(0)
    
    # Emotion Classification
    progress_bar.text("Classifying emotion...")
    API_URL = "https://api-inference.huggingface.co/models/poom-sci/bert-base-uncased-multi-emotion"
    headers = {"Authorization": "Bearer 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"}
    output_1 = query_with_retry({"inputs": text,}, API_URL, headers)
    emotion = output_1[0][0].get('label')
    progress_bar.progress(50)

    # Ailment Classification
    progress_bar.text("Predicting ailment...")
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
    if emotion == 'fear':
      candidate_labels = ['fear of death', 'fear of flying']
    elif emotion == 'sadness':
      candidate_labels = ['depression', 'grief']
    output_2 = query_with_retry({
        "inputs": text,
        "parameters": {"candidate_labels": candidate_labels},
    }, API_URL, headers)
    ailment = output_2.get('labels')[0]
    progress_bar.progress(100)
    time.sleep(1)
    progress_bar.empty()

    # Books recommended by The Novel Cure
    if ailment == 'fear of death':
        book_list = ['White Noise', 'Hundred Years of Solitude']
    elif ailment == 'fear of flying':
        book_list = ["Night Flight", "The Count of Monte Cristo", "The Magus", "In the Woods", "Carter Beats the Devil"]
    elif ailment == 'depression':
        book_list = ['The Unbearable Lightness of Being', 'The Bell Jar', 'Mr. Chartwell', 'The Marriage Plot']
    elif ailment == 'grief':
        book_list = ["After You'd Gone", 'Incendiary', 'Extremely Loud & Incredibly Close', 'What I Loved']


    # Fetch book info from Google Books API (You can replace this part with static list as you needed)
    progress_bar.text("Fetching book information...")
    book_info_list = []
    for book in book_list:
        title, image, url = fetch_book_info(book)
        book_info_list.append((title, image, url))
    progress_bar.progress(100)
    time.sleep(1)
    progress_bar.empty()

    return emotion, ailment, book_info_list

# Load Animation
lottie_anim = load_lottieurl("https://lottie.host/fa433011-9a30-4fcc-a03e-a7c9c76a917b/feBor8W1MA.json")

# Page Configuration
st.set_page_config(page_title="Unstuck", page_icon="📕", layout="wide")
header_text = "Unstuck by Abdullah Garatli"
st.markdown(f"<h1 style='text-align: center;'>{header_text}</h1>", unsafe_allow_html=True)
st.markdown("#### Befriend a Book.. And You Will Never Walk Alone")

# Entry Box & Animation
with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        with st.form('my_form'):
            text = st.text_area('Enter tweets here:', 'The world keeps spinning, indifferent to my loss. The sun still rises, the birds still sing, but the joy in these simple miracles of life seems to have faded.')
            submitted = st.form_submit_button('Get Books')
            if submitted:  
                emotion, ailment, book_info_list = classify_and_recommend(text)

    with col2:
        st_lottie(lottie_anim, height=250, key="coding")

# Display Model Results
if submitted:
    st.markdown("### Predominant Emotion:")
    st.markdown(emotion)
    st.markdown("### Predicted Ailment:")
    st.markdown(ailment)
    # Display Recommended Books
    st.markdown("<h2 style='text-align: center; color: white;'>Recommended Books</h2>", unsafe_allow_html=True)
    cols = st.columns(len(book_info_list))  # Create as many columns as there are books
    for i, info in enumerate(book_info_list):
        cols[i].markdown(f'<a href="{info[2]}" target="_blank"><img src="{info[1]}" style="width:100px;height:150px;display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
        cols[i].markdown(f"<center>{info[0]}</center>", unsafe_allow_html=True)
