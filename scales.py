#!/usr/bin/env python3

import json
from random import randint

keys = ["A", "B", "C", "D", "E", "F", "G"]
modes = ["Major", "Minor", "Dorian", "Pentatonic", "Blues", "Mixolydian"]

key = randint(0, len(keys)-1)
mode = randint(0, len(modes)-1)

scale = str(modes[mode])+ " in " + str(keys[key])

reply = {"writeBody":True, "contentType": "text/html", "statusCode": 200}

reply["output"] = "<h1> Play a "+scale

print(json.dumps(reply))


