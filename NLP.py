import yake

# Input text
input_text = input("Enter the text: ")

# Initialize YAKE keyword extractor
kw_extractor = yake.KeywordExtractor()

# Extract keywords from the input text
wordScoreList = kw_extractor.extract_keywords(input_text)

keywords = [word for word, score in wordScoreList]

# Remove smaller substrings if they are part of larger substrings
filtered_keywords = []
for word in keywords:
    is_substring = False
    for other_word in keywords:
        if word != other_word and word in other_word:
            is_substring = True
            break
    if not is_substring:
        filtered_keywords.append(word)

print("Keywords identified: ", filtered_keywords)