

def count_words(text: str) -> int:
    """
    Count the number of words in the given text
    text (str): the input text for word counting
    returns: the number of words in the input text
    """
    words = text.split()
    return len(words)

def calculate_reading_time(text: str, average_words_per_minute: int = 250) -> int:
    """
    Calculate the estimated reading time in minutes based on word count

    text (str): The input text for which reading time is calculated
    average_words_per_minute (int, optional): Average words read per minute. Default is 250
    returns: The estimated reading time in minutes.
    """
    word_count = count_words(text)
    reading_time_minutes = max(1, word_count // average_words_per_minute)
    return reading_time_minutes