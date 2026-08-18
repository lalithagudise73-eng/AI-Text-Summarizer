# 🤖 AI Text Summarizer

## Introduction

AI Text Summarizer is a Python-based Natural Language
Processing project that automatically generates a shorter
version of a long text.

The project uses an extractive summarization approach.
Important sentences are identified using TF-IDF scores
and selected to create the final summary.

## Objectives

- Automatically summarize long text.
- Reduce the time required to read documents.
- Apply Natural Language Processing techniques.
- Calculate sentence importance.
- Generate an extractive summary.

## Technologies Used

- Python
- Natural Language Processing
- Scikit-learn
- TF-IDF
- Regular Expressions
- VS Code
- Git
- GitHub

## Algorithm

The project uses TF-IDF (Term Frequency-Inverse Document
Frequency).

The process is:

1. Accept input text.
2. Divide the text into sentences.
3. Convert sentences into TF-IDF vectors.
4. Calculate importance scores.
5. Rank the sentences.
6. Select the highest-scoring sentences.
7. Preserve their original order.
8. Generate the final summary.

## Features

- Text input
- Automatic sentence segmentation
- TF-IDF-based sentence scoring
- Extractive summarization
- Configurable summary length
- Testbench
- Simulation results

## Project Structure

AI-Text-Summarizer/

├── README.md
├── requirements.txt
│
├── src/
│   ├── summarizer.py
│   └── main.py
│
├── data/
│   └── sample_text.txt
│
├── testbench/
│   └── test_summarizer.py
│
└── simulation/
    └── simulation_results.txt

## Installation

Install Python and then install the required library:

pip install -r requirements.txt

## Run the Project

Go to the src folder:

cd src

Run:

python main.py

Enter your text and press ENTER twice.

The program will generate the summary.

## Run Testbench

From the project root:

python testbench/test_summarizer.py

Expected result:

Test 1 - Sentence Splitting: PASS
Test 2 - Empty Text: PASS
Test 3 - Short Text: PASS
Test 4 - Summary Length: PASS
Test 5 - Summary Generation: PASS

All Testbench Tests Passed.

## Simulation

The simulation demonstrates:

Input Text
     ↓
Sentence Segmentation
     ↓
TF-IDF Processing
     ↓
Sentence Scoring
     ↓
Important Sentence Selection
     ↓
Summary

## Advantages

- Simple implementation
- Fast processing
- Easy to understand
- No external AI API required
- Suitable for academic projects

## Limitations

- It is extractive rather than generative.
- It does not truly understand context like a modern
  large language model.
- Results depend on word frequency.
- Very short or unusual texts may produce weaker summaries.

## Future Enhancements

- Add transformer-based summarization.
- Add a web interface.
- Support PDF and Word documents.
- Add multilingual summarization.
- Add abstractive summarization.
- Add summary quality evaluation.

## Conclusion

The AI Text Summarizer demonstrates how Natural Language
Processing and TF-IDF can be used to automatically identify
important sentences and create a concise summary.

This project is designed for educational purposes and can
be extended into a more advanced AI/NLP application.