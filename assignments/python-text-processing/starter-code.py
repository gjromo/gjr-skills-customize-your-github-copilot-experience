def count_words(text):
    """Return the number of words in a string."""
    return len(text.split())


def clean_text(text):
    """Remove extra whitespace and normalize the text."""
    return " ".join(text.split())


# TODO: Read a file from disk
# TODO: Count lines, words, and characters
# TODO: Search for a keyword in the text
# TODO: Display a cleaned version of the content
