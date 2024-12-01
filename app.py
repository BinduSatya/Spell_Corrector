import streamlit as st
import re
import pandas as pd
import numpy as np
import textdistance
import os
from collections import Counter

current_directory = os.getcwd()
file_path = os.path.join(current_directory, "text_data")
path = file_path

text = ""
for temp in os.listdir(path):
    with open(f"{path}/{temp}", 'r', encoding='utf-8') as file:
        content = file.read()
        text = " ".join([text,content])
        text = text.strip()
        # print(len(text))


words = []
data = text.lower()


words = re.findall('\w+', data)

# Get unique words and frequency count
unq_words = set(words)

word_freq_dict = Counter(words)
total_word_freqs = sum(word_freq_dict.values())
# Calculate word probabilities

prob = {}
for word, freq in word_freq_dict.items():
    prob[word] = freq / total_word_freqs

def autocorrect(word):
    word = word.lower()
    if word in prob:
        print(f"The word: {word} is already present")
        return None 
    else:
        similarities = []
        for w in word_freq_dict.keys():
            lev_distance = textdistance.levenshtein(w, word)
            lev_similarity = 1 - (lev_distance / max(len(w), len(word)))
            # similarities.append(1 - (textdistance.Jaccard()).distance(w, word))
            similarities.append(lev_similarity)

        df = pd.DataFrame.from_dict(prob, orient='index').reset_index()
        df.rename(columns={'index': 'Word', 0: 'Probability'}, inplace=True)

        df['Similarity'] = similarities

        output = df.sort_values(['Similarity', 'Probability'], ascending=False).head(5)
        return output

def main():
    st.title("Spell Corrector Model")
    inputted_text = st.text_input("Enter a word:")
    
    if inputted_text:
        df1 = autocorrect(inputted_text)

        if df1 is not None: 
            # df1.drop(labels=['Probability'], axis=1, inplace=True)  # Drop 'Probability' column
            # st.write(df1)
            for index, row in df1.iterrows():
                st.write(f"{row['Word']} ->  {row['Similarity']*100}% similar")
                
            
        else:
            st.write(f"The word '{inputted_text}' is already correct!")
    
if __name__ == "__main__":
    main()
