import json, random
from collections import deque
from datetime import date

def one_away(w1, w2):
    return sum(l1 != l2 for l1, l2 in zip(w1, w2)) == 1

def bfs(start, wordSet):
    q = deque([start])
    distances = {start: 0}

    while q:
        cur = q.popleft()

        for word in wordSet:
            if word not in distances and one_away(cur, word):
                distances[word] = distances[cur] + 1
                q.append(word)

    return distances

with open("./src/data/difficultWords.json", "r") as f1:
    data = json.load(f1)

    startWord = random.choice(data)
    
    start_date = date(2026, 11, 18)

    cur_date = date.today()

    delta = cur_date - start_date
    
    with open("./src/data/reachableWords.json", "r") as file:
        wordSet = set(json.load(file))
    
    distances = bfs("WORD", wordSet)

    wordData = {"day": delta.days + 1, "word": startWord, "bestPathLength": distances[startWord]}

    with open("./src/data/dailyWord.json", "w") as file:
        json.dump(wordData, file)


