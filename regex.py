from filemanager import titles
import re

spotifyRegex = re.compile(r'''(
        [a-zA-Z0-9._%+ ]-[ a-zA-Z0-9._%+]
    )''', re.VERBOSE)

matches = []

for groups in spotifyRegex.findall(str(titles)):
    matches.append(groups)

print(spotifyRegex.findall(str(titles)))