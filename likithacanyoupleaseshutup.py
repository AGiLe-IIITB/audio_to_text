import yake
import audioToText

# Input text
input_text = audioToText.text
monthList = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

dateList = [
    "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"
]

cityList = [
"mumbai", "delhi", "bangalore", "kolkata", "chennai", "hyderabad", "pune", "ahmedabad", "surat", "jaipur", "lucknow", "kanpur", "nagpur", "patna", "indore", "thane", "bhopal", "visakhapatnam", "vadodara", "firozabad", "ludhiana", "rajkot", "agra", "nashik", "faridabad", "meerut", "howrah", "jabalpur", "varanasi", "srinagar", "aurangabad", "dhanbad", "amritsar", "navi mumbai", "allahabad", "ranchi", "haora", "coimbatore", "jabalpur", "gwalior", "vijayawada", "jodhpur", "madurai", "raipur", "kota", "guwahati", "chandigarh", "solapur", "hubli", "dharwad", "bareilly", "ghaziabad", "noida", "gurgaon"
]

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

print("\nKeywords identified: ", filtered_keywords)
print()

monthFound = {}
cityFound = {}
dateFound = {}

filtered_keywords_copy = filtered_keywords.copy()
for phrase in filtered_keywords_copy:
    for month in monthList:
        if month in phrase.lower():
            filtered_keywords.remove(phrase)
            break
    for date in dateList:
        if date in phrase.lower():
            filtered_keywords.remove(phrase)
            break
    for city in cityList:
        if city.lower() in phrase.lower():
            filtered_keywords.remove(phrase)
            break
    
print("Months found: ", monthFound)
print("Dates found: ", dateFound)
print("Cities found: ", cityFound)
print("Other keywords: ", filtered_keywords)