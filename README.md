# Pneuma: NLP-based Book Recommender


Pneuma is a unique book recommendation system that employs Natural Language Processing (NLP) to suggest books based on users' emotional expressions. By tapping into Hugging Face's state-of-the-art machine learning models, Pneuma delivers insights into users' emotions and offers literature that can provide comfort, understanding, or even avenues of exploration.

## 🌟 Features

- **Emotion Classification**: Discerns the dominant emotion from a user's text input.
- **Ailment Prediction**: Given the detected emotion, the system projects potential concerns or mental states.
- **Book Recommendations**: Provides a curated list of books tailored to the identified emotion or concern.

## 🛠 Tech Stack

- **Streamlit**: Web application framework that brings the project to life.
- **Hugging Face**: Powers the emotion recognition using pre-trained NLP models.
- **Google Books API**: Fetches detailed information on books, inclusive of titles and cover art.
- **Other Libraries**: The project also utilizes `requests`, `streamlit_lottie`, and others.

## 🚀 Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/garatlia/pneuma.git
    cd pneuma
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Launch the Application**:
    ```bash
    streamlit run app.py
    ```

## 🌐 Deployment

Pneuma is deployed on Heroku. Experience it in action [here](https://pneuma-ade4f5d0b8ca.herokuapp.com/).

## 🤝 Contributing

While we genuinely appreciate your interest in the Pneuma project, we are currently not accepting public contributions as there are significant future developments and features in the pipeline. If you have feedback or ideas, please feel free to open an issue to discuss them, but kindly refrain from making direct pull requests to the repository.

If you're interested in collaboration or potential partnerships, please reach out directly. We would love to talk.

## 📜 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## 🙏 Acknowledgments

- A huge shoutout to Facebook, Google, and Hugging Face for making advanced models accessible to developers.
- Drawing inspiration from "[The Novel Cure](https://www.goodreads.com/book/show/20893421-the-novel-cure)", a beautiful book offering literature as remedies for an array of human conditions.
