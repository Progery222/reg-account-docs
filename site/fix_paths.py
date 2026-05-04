import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
with open(p, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("../../chats/", "../chats/").replace("../../photos/", "../photos/")
with open(p, "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed", c.count("../chats/"), "media paths")
