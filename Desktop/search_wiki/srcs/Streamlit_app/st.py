import streamlit as st
import wikipedia
import spacy
import random
from IPython.display import display, HTML

def search():
    st.title('Wiki Search')
    search_text = st.text_input('Enter search word:')
    try:
        if search_text:
            results = wikipedia.summary(search_text, sentences=4) 
            return results
    except wikipedia.exceptions.DisambiguationError:
        return None

def POS(results):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(results)
    sentence_with_class = ' '.join(f"{word.text} {word.pos_}" for word in doc)
    words = sentence_with_class.split()
    highlighted_text = ''
    for i in range(0, len(words), 2):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        highlighted_text += '<span style="background-color:{}">{}</span> '.format(color, ' '.join(words[i:i+2]))
    st.markdown(highlighted_text, unsafe_allow_html=True)

def main():
       results = search()
       if results:
           POS(results)

if __name__ == '__main__':
    main()
