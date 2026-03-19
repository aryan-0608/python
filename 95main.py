import re

pattern = r"[A-Z]+yclone"
text = '''Cyclone is Dumazile was a strong tropical cyclone in the south_west Indian Ocean that affect Madagascar and Reunion in early March 2018.
The cyclone formed on 27 February 2018, and reached its peak intensity on 2 March, with maximum sustained winds of 165 km/h (105 mph) and a minimum central pressure of 955 hPa (28.20 inHg).
Dumazile made landfall in Madagascar on 3 March, causing widespread damage and flooding. The cyclone then moved back out to sea and made a second landfall in Reunion on 4 March, causing further damage and power outages.
Overall, Cyclone Dumazile caused significant damage and disruption in the affected areas, with at least 2 fatalities reported in Madagascar.'''

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])