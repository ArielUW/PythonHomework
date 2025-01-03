import spacy
file = "/Users/arieldrozd/Downloads/PythonHomework-1/19-12-nlp/text.txt"
with open(file, "r") as file:
    text = file.read()
nlp = spacy.load("en_core_web_lg")
tokens = nlp(text)
print(tokens)