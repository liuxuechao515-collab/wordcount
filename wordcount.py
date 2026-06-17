import argparse
import collections
import sys


def count_words(text):
    return len(text.split())


def count_chars(text):
    return len(text)


def top_words(text, n=5):
    words = text.lower().split()
    counter = collections.Counter(words)
    return counter.most_common(n)


def main():
    parser = argparse.ArgumentParser(description="Count words and characters in a text file.")
    parser.add_argument("file", help="Path to the text file")
    parser.add_argument("--top", type=int, default=5, metavar="N",
                        help="Show top N words (default: 5)")
    args = parser.parse_args()

    try:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    print(f"Words:      {count_words(text)}")
    print(f"Characters: {count_chars(text)}")
    print()
    print(f"Top {args.top} words:")
    for word, count in top_words(text, args.top):
        print(f"  {word:<12}{count}")


if __name__ == "__main__":
    main()
