from summarizer import summarize


def main():

    print("===================================")
    print("       AI TEXT SUMMARIZER")
    print("===================================")

    print("\nEnter your text below.")
    print("Press ENTER twice when finished.\n")

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    text = " ".join(lines)

    if not text.strip():

        print("No text entered.")
        return

    summary = summarize(
        text,
        num_sentences=3
    )

    print("\n===================================")
    print("             SUMMARY")
    print("===================================")

    print(summary)

    print("\n===================================")
    print("       SUMMARIZATION COMPLETE")
    print("===================================")


if __name__ == "__main__":
    main()