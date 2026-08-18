import sys

sys.path.append("src")

from summarizer import summarize, split_sentences


def test_sentence_split():

    text = "AI is useful. Machine learning is powerful."

    sentences = split_sentences(text)

    assert len(sentences) == 2

    print("Test 1 - Sentence Splitting: PASS")


def test_empty_text():

    result = summarize("")

    assert result == ""

    print("Test 2 - Empty Text: PASS")


def test_short_text():

    text = "Artificial intelligence is useful."

    result = summarize(text, 3)

    assert result == text

    print("Test 3 - Short Text: PASS")


def test_summary_length():

    text = (
        "Artificial intelligence is useful. "
        "Machine learning uses data. "
        "Natural language processing handles text. "
        "Robotics uses intelligent systems. "
        "AI is used in healthcare."
    )

    result = summarize(text, 2)

    sentences = split_sentences(result)

    assert len(sentences) == 2

    print("Test 4 - Summary Length: PASS")


def test_summary_not_empty():

    text = (
        "Artificial intelligence is useful. "
        "Machine learning is important. "
        "AI is used in many industries."
    )

    result = summarize(text, 2)

    assert len(result) > 0

    print("Test 5 - Summary Generation: PASS")


test_sentence_split()
test_empty_text()
test_short_text()
test_summary_length()
test_summary_not_empty()

print("\nAll Testbench Tests Passed.")