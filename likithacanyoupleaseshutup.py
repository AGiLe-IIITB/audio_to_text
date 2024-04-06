import re
import dateutil.parser
import yake
import audioToText

# Sample text containing cities, dates, times, and keywords
input_text = audioToText.text

# List of cities
cityList = [
    "mumbai", "delhi", "bangalore", "kolkata", "chennai", "hyderabad", "pune", "ahmedabad", "surat", "jaipur",
    "lucknow", "kanpur", "nagpur", "patna", "indore", "thane", "bhopal", "visakhapatnam", "vadodara", "firozabad",
    "ludhiana", "rajkot", "agra", "nashik", "faridabad", "meerut", "howrah", "jabalpur", "varanasi", "srinagar",
    "aurangabad", "dhanbad", "amritsar", "navi mumbai", "allahabad", "ranchi", "haora", "coimbatore", "jabalpur",
    "gwalior", "vijayawada", "jodhpur", "madurai", "raipur", "kota", "guwahati", "chandigarh", "solapur",
    "hubli", "dharwad", "bareilly", "ghaziabad", "noida", "gurgaon"
]

cityFound = [city.title() for city in cityList if city in input_text.lower()]


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

print("\nKeywords identified:", filtered_keywords)

print("\nDetected cities:", cityFound)

# Regular expression pattern to find dates in words (e.g., April 10th)
date_pattern = r'(?:\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2}(?:st|nd|rd|th)?)'

# Find dates in the text
parsed_dates = [dateutil.parser.parse(match).strftime("%B %d, %Y") for match in re.findall(date_pattern, input_text)]

print("Detected dates:", parsed_dates)

# Regular expression pattern to find time expressions in "xx:xx a.m./p.m." format
time_pattern = r'\b\d{1,2}:\d{2}\s(?:a\.m\.|p\.m\.)'

# Find time expressions in the text
parsed_times = [dateutil.parser.parse(match, fuzzy=True).strftime("%I:%M %p") for match in re.findall(time_pattern, input_text)]

print("Detected times:", parsed_times)