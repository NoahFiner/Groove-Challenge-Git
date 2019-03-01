import json
import time
import hashlib

def get_md5(filename):
    md5 = hashlib.md5()
    file = open(filename, "r")
    while True:
        data = file.read(32)
        if not data:
            break
        md5.update(data.encode("utf-8"))
    return md5.hexdigest()


if(__name__ == "__main__"):
    config = dict()
    print("""
HOW TO USE:
This program assumes you've already written a new program to groove_program.py under run().
This simply sets up config.json.
You are responsible for pushing this release to https://github.com/NoahFiner/Groove-Challenge-Git.git.
    """)

    config["version"] = input("Input a version: ")
    config["notes"] = input("Add any release notes: ")
    config["date"] = int(time.time())
    config["hash"] = get_md5("groove_program.py")
    
    file = open("config.json", "w")
    json.dump(config, file)
    file.close()