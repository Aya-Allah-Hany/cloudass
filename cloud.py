import re
from collections import Counter
from nltk.corpus import stopwords

file_path = "paragraphs.txt"
with open(file_path, 'r') as file:
    text = file.read()
stop_words = set(stopwords.words('english'))
processed_text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
words = processed_text.split()
filtered_words = [word for word in words if word not in stop_words]
word_counts = Counter(filtered_words)
for word, count in word_counts.items():
    print(f'{word}: {count}')