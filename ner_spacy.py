import spacy
from collections import Counter
from spacy.explain import explain

# Load English model
nlp = spacy.load("en_core_web_sm")

print("🔍 Named Entity Recognition (NER) using spaCy")
print("Type 'exit' to quit.\n")

while True:
    text = input("Enter a sentence: ")

    if text.lower() == "exit":
        print("Exiting program. 👋")
        break

    doc = nlp(text)

    if not doc.ents:
        print("No named entities found.\n")
        continue

    print("\nNamed Entities Found:")
    for ent in doc.ents:
        print(f"{ent.text:<25} {ent.label_:<10} ({explain(ent.label_)})")

    # Count entity types
    entity_counts = Counter(ent.label_ for ent in doc.ents)
    print("\nSummary:")
    for label, count in entity_counts.items():
        print(f"{label:<10} ({explain(label)}): {count} occurrence(s)")
    print()