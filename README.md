# YouTube Comment Toxicity Analyzer

The goal is to fetch comments from YouTube videos and then analyze whether they are toxic, hateful, spammy, or neutral using Natural Language Processing (NLP) + Machine Learning.

🔹 Features

Fetch Comments – Use YouTube Data API to extract comments from a video.

Preprocessing – Clean text (remove emojis, links, stopwords).

Toxicity Detection – Use:

Pre-trained models (e.g., Google’s Perspective API, Hugging Face models).

Or train your own ML model with datasets like Jigsaw Toxic Comment Dataset.

Classification Categories:

Toxic

Severe Toxic

Obscene

Threat

Insult

Identity Hate

Neutral

Visualization – Show percentage of toxic vs. non-toxic comments.

Streamlit App (Optional) – Build an interactive web app for demo.

🔹 Tech Stack

Python (pandas, numpy, scikit-learn, tensorflow/pytorch)

YouTube Data API → for fetching comments

NLP libraries → NLTK, spaCy, Hugging Face transformers

Visualization → Matplotlib, Seaborn, Plotly

Frontend (optional) → Streamlit

🔹 Example Workflow

User enters a YouTube video URL.

Script fetches top 100 comments.

Each comment is cleaned + tokenized.

Model predicts toxicity probability.

Show results:

Comment-wise classification

## How to run
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```
