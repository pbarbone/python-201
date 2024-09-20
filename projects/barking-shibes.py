# Use a quotes API, e.g. https://zenquotes.io/api/random
# to fetch a random quote.

import requests
from pathlib import Path

# Fetch a random quote

response = requests.get('https://zenquotes.io/api/random')
data = response.json()
quote = data[0]['q']
author = data[0]['a']

# Then use string manipulation to convert it to Doge speech (https://en.wikipedia.org/wiki/Doge_(meme))

doge_modifiers = ['very', 'much', 'many', 'so', 'such']

quote_words = quote.split(' ')

#filter quote_words to remove any words less than 3 characters
quote_words = [word for word in quote_words if len(word) > 3]

#for each word in quote_words, add a random doge modifier
doged_quote = ' '.join([f'{doge_modifiers[i % len(doge_modifiers)]} {word}' for i, word in enumerate(quote_words)])

print(quote)
print(doged_quote)


# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# https://dog.ceo/api/breed/shiba/images/random

doge_image_url = 'https://dog.ceo/api/breed/shiba/images/random'

html = "<img src={doge_image_url} alt='Doge image'>"
html += f"<p>{doged_quote}</p>"

# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

with open('doge_quote.html', 'w') as f:
    f.write(html)
    f.close()

# Open the file in the browser
import webbrowser

webbrowser.open('doge_quote.html')




