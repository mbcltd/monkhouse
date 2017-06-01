import json
from pprint import pprint

with open('data/wocka.json') as data_file:
    data = json.load(data_file)

def process_joke(joke):
    a = ' '.join(joke.splitlines())
    b = a.lower()
    c = b.strip()
    d = ''.join([i if ord(i) < 128 else ' ' for i in c])

    e = ' '.join(d.split())
    return e


jokes = [process_joke(a["body"]) for a in data]

for joke in jokes:
    print joke

print len(jokes)

string = '\n'.join(jokes)

text_file = open("data/wocka/input.txt", "w")

text_file.write(string)

text_file.close()
