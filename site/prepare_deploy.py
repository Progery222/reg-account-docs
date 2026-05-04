#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare project for GitHub/Vercel deployment"""
import os, shutil, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SRC_SITE = os.path.join(BASE, "site")
SRC_MEDIA = os.path.join(BASE, "chats")
DEST = os.path.join(BASE, "deploy")

# Clean destination
if os.path.exists(DEST):
    shutil.rmtree(DEST)
os.makedirs(DEST, exist_ok=True)

# 1. Copy site files
for f in ["index.html", "style.css", "script.js"]:
    src = os.path.join(SRC_SITE, f)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(DEST, f))
        print(f"Copied {f}")

# 2. Copy media files maintaining structure
media_src = os.path.join(SRC_MEDIA, "chat_562953382643143", "topic_1019")
media_dest = os.path.join(DEST, "chats", "chat_562953382643143", "topic_1019")

if os.path.exists(media_src):
    shutil.copytree(media_src, media_dest)
    print(f"Copied media directory")

# 3. Fix paths in index.html (from ../chats/ to chats/)
html_path = os.path.join(DEST, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace ../chats/ with chats/
content = content.replace("../chats/", "chats/")
print(f"Fixed {content.count('chats/')} media paths")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

# 4. Create .gitignore
with open(os.path.join(DEST, ".gitignore"), "w") as f:
    f.write("*.py\n__pycache__/\n.DS_Store\nThumbs.db\n")
print("Created .gitignore")

# 5. Create vercel.json for static site config
with open(os.path.join(DEST, "vercel.json"), "w") as f:
    f.write("""{
  "buildCommand": "",
  "outputDirectory": ".",
  "framework": null,
  "rewrites": [],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=86400" }
      ]
    },
    {
      "source": "/chats/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=604800, immutable" }
      ]
    }
  ]
}
""")
print("Created vercel.json")

# Count files
total_files = 0
total_size = 0
for dp, dn, fns in os.walk(DEST):
    for f in fns:
        total_files += 1
        total_size += os.path.getsize(os.path.join(dp, f))

print(f"\nProject ready: {total_files} files, {total_size/1024/1024:.1f} MB")
print(f"Location: {DEST}")
