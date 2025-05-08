import pandas as pd
import random

# Load the CSV file
df = pd.read_csv('/Users/vale1/Downloads/dialogues_text.csv')  # <-- Change to your real CSV filename

# Assuming the dialogue sentences are in a column named "dialogue" or similar
sentences = []

for dialogue in df['dialogue']:  # <-- Make sure 'dialogue' matches your CSV column name
    parts = str(dialogue).strip().split('__eou__')
    for part in parts:
        clean = part.strip()
        if len(clean) > 0:
            sentences.append(clean)

# Optional: shuffle the sentences for randomness
random.shuffle(sentences)

# Save first 1000 sentences into english_corpus.txt
with open('english_corpus.txt', 'w', encoding='utf-8') as f:
    for sentence in sentences[:1000]:
        f.write(sentence + '\n')

print(f"Saved {min(1000, len(sentences))} sentences into english_corpus.txt!")
