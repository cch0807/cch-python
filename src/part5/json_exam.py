# JSON(Java Script Object Notation)

import json
import os

path = os.path.join(os.getcwd(), "src", "part5", "sample.json")
print(path)

with open(path, mode="r") as f:
    data = json.loads(f.read())
    data["type"] = "drink"
    with open(path, mode="w") as w:
        w.write(json.dumps(data))
