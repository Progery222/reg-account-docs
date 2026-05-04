import os
total = 0
count = 0
big = []
root = r"c:\Users\Alex\Downloads\Telegram Desktop\ChatExport_2026-05-01\chats\chat_562953382643143\topic_1019"
for dp, dn, fns in os.walk(root):
    for f in fns:
        fp = os.path.join(dp, f)
        sz = os.path.getsize(fp)
        total += sz
        count += 1
        if sz > 50_000_000:
            big.append((sz, f))
print(f"Files: {count}, Total: {total/1024/1024:.1f} MB")
for s, n in sorted(big, reverse=True):
    print(f"  BIG (>50MB): {s/1024/1024:.1f}MB - {n}")
