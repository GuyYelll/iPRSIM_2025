#import spacy

#nlp = spacy.load("en_core_web_sm")
#nlp.max_length = 2_000_000  # increase to 2 million characters or more

#with open(r"C:\iPRSIM Project\data\eng_news_2023_10K\eng_news_2023_10K-sources.txt", "r", encoding="utf-8") as f:
    #text = f.read()

#doc = nlp(text)

#print(doc)
#print(len(text))
#print(len(doc))


 #for token in text [0:100]:
   # print(token)

#for token in doc[:100]:
    #print (token)

#for sent in doc.sents:
    #print (sent)

import json

# Full file paths
sources_path = r"C:\iPRSIM Project\data\eng_news_2023_10K\eng_news_2023_10K-sources.txt"
sentences_path = r"C:\iPRSIM Project\data\eng_news_2023_10K\eng_news_2023_10K-sentences.txt"
output_path = r"C:\iPRSIM Project\news_corpus_with_sources.json"

# Load sources into a dictionary {id: (url, date)}
sources = {}
with open(sources_path, encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) == 3:
            sid, url, date = parts
            sources[int(sid)] = (url, date)

# Merge with sentences
corpus = []
with open(sentences_path, encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            sid, sentence = parts
            sid = int(sid)
            url, date = sources.get(sid, ("", ""))  # fallback if missing
            corpus.append({
                "id": sid,
                "text": sentence,
                "source": url,
                "date": date
            })

# Save as JSON
with open(output_path, "w", encoding="utf-8") as out:
    json.dump(corpus, out, indent=2, ensure_ascii=False)
