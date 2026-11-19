import json, string
from collections import deque
letters = list(string.ascii_uppercase)

def one_away(w1, w2):
    diff = 0

    for l1, l2 in zip(w1, w2):
        if l1 != l2:
            diff += 1
    
    if diff == 1:
        return True
    
    return False

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



with open("./src/data/sanitized.json", "r") as file:
    data = json.load(file)
    wordSet = set(data)

    distances = bfs("WORD", wordSet)
    
    # reachableWords - intermediate and final guesses
    rw = sorted(distances.keys())

    # only choose words with a distance of 4 or greater and 10 or less 
    # for the valid final words
    dw = []

    for word, moves in distances.items():
        if moves >= 4 and moves <= 10:
            dw.append(word)
    
    dw.sort()


    with open("./src/data/reachableWords.json", "w") as f2:
        json.dump(rw, f2)
    
    with open("./src/data/difficultWords.json", "w") as f3:
        json.dump(dw, f3)



    