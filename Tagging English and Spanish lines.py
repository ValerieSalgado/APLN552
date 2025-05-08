# Tagging English and Spanish lines

# Load your original file (without tags)
with open('bilingual_cognates_corpus.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Open a new file to save tagged lines
with open('bilingual_cognates_corpus_tagged.txt', 'w', encoding='utf-8') as f_out:
    for idx, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue  # skip empty lines
        
        if idx % 2 == 0:
            # Even lines are English
            f_out.write(f"[EN] {line}\n")
        else:
            # Odd lines are Spanish
            f_out.write(f"[ES] {line}\n")