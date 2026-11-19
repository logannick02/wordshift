from wordfreq import word_frequency, zipf_frequency
import json
validWords = []

with open("./scrabble-unsanitized.txt", "r") as file:
    content = file.read()
    # print(content)
    
    for word in content.split():
        # print(zipf_frequency(word, 'en'))
              
        if zipf_frequency(word, 'en') > 3:
            validWords.append(word)
    
with open("./src/data/sanitized.json", "w") as file:
    json.dump(validWords, file)
