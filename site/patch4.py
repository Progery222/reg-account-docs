#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch 4: Add missing IMG_7715.MP4 example video"""
import re

p = r"c:\Users\Alex\Downloads\Telegram Desktop\ChatExport_2026-05-01\site\index.html"
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

count = 0

# Add IMG_7715.MP4 after the IMG_7712.MOV flash example
target = 'IMG_7712.MOV_thumb.jpg'
if target in c and 'IMG_7715.MP4' not in c:
    # Find the end of the IMG_7712 media block
    idx = c.find(target)
    end_div = c.find('</div>', idx)
    if end_div > 0:
        insert_pos = end_div + 6
        new_video = '\n<div class="media-block"><video controls preload="none" poster="../chats/chat_562953382643143/topic_1019/video_files/IMG_7715.MP4_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="../chats/chat_562953382643143/topic_1019/video_files/IMG_7715.MP4">Video</video><span class="dur">15 sec</span></div>'
        c = c[:insert_pos] + new_video + c[insert_pos:]
        count += 1
        print(f"[{count}] Added IMG_7715.MP4 flash example")

with open(p, "w", encoding="utf-8") as f:
    f.write(c)

print(f"Applied {count} fix(es)")
