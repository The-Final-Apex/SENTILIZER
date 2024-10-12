import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter import scrolledtext
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import customtkinter
import nltk

# Download vader lexicon (for sentiment analysis)
nltk.download('vader_lexicon')


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# download vader lexicon (for sentiment analysis)
nltk.download('vader_lexicon')


import nltk
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Create the GUI
root = customtkinter.CTk()
root.title("Sentiment Analyzer")
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")
# Create input box for user input
input_label = ttk.Label(root, text="Enter text:", background='grey10', foreground='white')
input_label.pack()
input_box = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD, background='grey10', foreground='white')
input_box.pack()
output_box = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD, state="disabled", background='grey10', foreground='white')

# download vader lexicon (for sentiment analysis)
nltk.download('vader_lexicon')

def clean_text(text):
    """
    This function takes in a string of text and returns a cleaned version of the text
    with all punctuation removed and the first letter of each sentence capitalized.
    """
    # remove all punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # capitalize the first letter of each sentence
    sentences = nltk.sent_tokenize(text)
    sentences = [s[0].upper() + s[1:] for s in sentences]

    return ' '.join(sentences)

def sentiment_analyzer(paragraph, threshold=0.5):
    """
    This function takes in a paragraph of text as input and returns its sentiment score.
    If the sentiment score's confidence value (previously called "compound") is below the threshold,
    the sentiment is classified as "neutral".
    The function returns a dictionary containing the sentiment score, suggestions for how to improve
    the paragraph based on its sentiment score, and an improved version of the paragraph with better
    capitalization and punctuation based on the sentiment score.
    """
    # initialize SentimentIntensityAnalyzer object
    sid = SentimentIntensityAnalyzer()

    # obtain sentiment score for paragraph
    sentiment_score = sid.polarity_scores(paragraph)

    # check if sentiment is confident enough to be reliable
    if sentiment_score['compound'] < threshold:
        sentiment = 'neutral'
        suggestions = []
    else:
        sentiment = 'positive' if sentiment_score['compound'] > 0 else 'negative'
        # generate suggestions based on the paragraph's sentiment score
        if sentiment == 'positive':
            suggestions = ['Try to make more specific statements.', 'Consider adding more supporting details.']
        elif sentiment == 'negative':
            suggestions = ['Focus on one clear point instead of multiple.',
                            'Use less negative language and more neutral or positive language.']
        else:
            suggestions = ['Consider adding more details or evidence to clarify your point.']

    # rename the 'compound' key to 'confidence'
    sentiment_score['confidence'] = sentiment_score.pop('compound')
    sentiment_score['mood'] = sentiment
    sentiment_score['positive'] = sentiment_score.pop('pos')
    sentiment_score['negative'] = sentiment_score.pop('neg')
    sentiment_score['neutral'] = sentiment_score.pop('neu')

    # clean and improve the paragraph based on the sentiment score
    return {'sentiment_score': sentiment_score, 'suggestions': suggestions}

def decode():
    file = open('morsedecoder.txt', 'a')
    text=input_box.get("1.0", "end-1c").lower()
    for letter in text:
        if ' ' in text:
            file.write(" ")
        if 'a' in text:
            file.write("._")
        if 'b' in text:
            file.write("_...")
        if 'c' in text:
            file.write("_._.")
        if 'd' in text:
            file.write("_..")
        if 'e' in text:
            file.write(".")
        if 'f' in text:
            file.write(".._.")
        if 'g' in text:
            file.write("__.")
        if 'h' in text:
            file.write("....")
        if 'i' in text:
            file.write("..")
        if 'j' in text:
            file.write(".___")
        if 'k' in text:
            file.write("_._")
        if 'l' in text:
            file.write("._..")
        if 'm' in text:
            file.write("__")
        if 'n' in text:
            file.write("_.")
        if 'o' in text:
            file.write("___")
        if 'p' in text:
            file.write(".__.")
        if 'q' in text:
            file.write("__._")
        if 'r' in text:
            file.write("._.")
        if 's' in text:
            file.write("...")
        if 't' in text:
            file.write("_")
        if 'u' in text:
            file.write(".._")
        if 'v' in text:
            file.write("..._")
        if 'w' in text:
            file.write(".__")
        if 'x' in text:
            file.write("_.._")
        if 'y' in text:
            file.write("_.__")
        if 'z' in text:
            file.write("__..")
    file.write("\n\n")
    file.close()
    file = open('morsedecoder.txt', 'r')
    sent = file.read()
    output_box.config(state="normal")  # Enable editing of the output box
    output_box.insert("1.0", sent)
    output_box.config(state="disabled")
    file.close()
    file = open('morsedecoder.txt', 'w')
    file.truncate(0)
    file.close()

def submit_text():
    text = input_box.get("1.0", "end-1c")  # Get input text from text box
    result = sentiment_analyzer(text)  # Analyze sentiment of the text
    output_box.config(state="normal")  # Enable editing of the output box
    output_box.delete("1.0", "end")  # Clear previous output from the output box
    output_box.insert("1.0", result)  # Insert new output into the output box
    output_box.config(state="disabled")  # Disable editing of the output box

def save():
    text = output_box.get("1.0", "end-1c")
    file = open('rating.txt', 'a')
    strtime = datetime.now().strftime("%H:%M:%S")
    file.write(f'{strtime}:   {text} \n \n')
    file.close()
    tk.messagebox.showinfo("Saved", "Saved Successfully")

translate_button = customtkinter.CTkButton(root, text="Morse", command=decode)
translate_button.pack()

# Create button to submit text for analysis
submit_button = customtkinter.CTkButton(root, text="Check", command=submit_text)
submit_button.pack()

# Create output box for displaying analysis
output_label = customtkinter.CTkLabel(root, text="Analysis result:")
output_label.pack()

output_box.pack()
Saveb = customtkinter.CTkButton(root, text="Save", command=save)
Saveb.pack()

root.mainloop()
# {'sentiment_score': {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'confidence': 0.0, 'sentiment': 'neutral'}, 'suggestions': [], 'improved_paragraph': 'Hi'}
