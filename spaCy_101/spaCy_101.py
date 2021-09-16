import spacy

if __name__ == "__main__":
    # nlp = spacy.load("en_core_web_sm")
    nlp = spacy.load("es_core_news_sm")
    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
    for token in doc:
        print(token.text)
