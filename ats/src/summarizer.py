import re
from sklearn.feature_extraction.text import TfidfVectorizer


def split_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [sentence.strip()
            for sentence in sentences
            if sentence.strip()]


def summarize(text, num_sentences=3):

    sentences = split_sentences(text)

    if not sentences:
        return ""

    if len(sentences) <= num_sentences:
        return " ".join(sentences)

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    matrix = vectorizer.fit_transform(sentences)

    scores = matrix.sum(axis=1).A1

    ranked_indices = sorted(
        range(len(sentences)),
        key=lambda i: scores[i],
        reverse=True
    )

    selected_indices = sorted(
        ranked_indices[:num_sentences]
    )

    summary = [
        sentences[i]
        for i in selected_indices
    ]

    return " ".join(summary)