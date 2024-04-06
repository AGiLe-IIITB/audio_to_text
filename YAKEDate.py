import re
import dateutil.parser

# Sample text containing dates
text = "breaking news on April 3rd 2024 at approximately 10:30 p.m. local time a bombing incident rocked the Downtown district of Bangalore emergency services quickly responded to the scene where Chaos and confusion rained as blooms of smoke beloved into the night sky the extent of casualties and the motives behind the attack remain under investigation leaving residence on edge and authorities on high alert"

# Regular expression pattern to find dates in words (e.g., April 10th)
date_pattern = r'(?:\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2}(?:st|nd|rd|th)?)'

# Find dates in the text
parsed_dates = [dateutil.parser.parse(match).date() for match in re.findall(date_pattern, text)]

print("Detected dates:", parsed_dates)
