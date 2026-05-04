#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Final comprehensive audit check"""
import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

checks = {
    # === STRUCTURAL HTML FIXES ===
    "TrustMyIP link valid": 'href="https://trustmyip.com/ip-fraud-checker"' in c,
    "No broken trustmyip tag": 'trustmyip.com</a></li>' not in c,
    "VPN Liberty Bot tag closed": '</a</li>' not in c,
    "No unclosed alert tag line303": '<strong>\u26a0\ufe0f\n<div' not in c and '<strong>\u26a0\ufe0f\r\n<div' not in c,
    
    # === TELEGRAPH/TELETYPE LINKS IN SECTIONS ===
    "Telegraph link in reg section": 'Manual-po-rege-akkov-INST' in c.split('id="reg"')[1].split('id="verify"')[0],
    "Telegraph link in video section": 'Manual-po-zalivu-INST' in c.split('id="video"')[1].split('id="content"')[0],
    "Telegraph link in TT section": 'Manual-po-TT-03-09' in c.split('id="tiktok"')[1].split('id="facebook"')[0],
    "Teletype FB links in FB section": 'teletype.in/@watles/c-gxK4iVvKN' in c.split('id="facebook"')[1].split('id="links_redirect"')[0],
    "Teletype content link": 'teletype.in/@watles/aPPZlzmLN8r' in c.split('id="content"')[1].split('id="tiktok"')[0],
    "Teletype TT create link in TT": 'teletype.in/@watles/dYkO3cUWyDZ' in c.split('id="tiktok"')[1].split('id="facebook"')[0],
    "Teletype links in links section": 'teletype.in/@watles/YQ1hNMz-6QP' in c.split('id="links_redirect"')[1].split('id="bio"')[0],
    "Teletype BIO link": 'teletype.in/@watles/9xBldwE6tbx' in c.split('id="bio"')[1].split('id="payment"')[0],
    "Telegraph device in phone section": 'Nastrojka-ustrojstva-04-29' in c.split('id="phone"')[1].split('id="vpn"')[0],
    
    # === CONTENT FROM MESSAGES ===
    "Sorting accounts info": '\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u043e\u0432' in c,
    "Fraud score 40-45": '40-45' in c,
    "TT no access contacts": '\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0430\u043c' in c.split('id="tiktok"')[1].split('id="facebook"')[0],
    
    # === ALREADY EXISTING CONTENT (from prev patches) ===
    "Neo VPN Bot": 'neovpnbot' in c,
    "VPN Liberty Bot": 'vpn_liberty_bot' in c,
    "DuckDuckGo email": 'duckduckgo' in c.lower(),
    "BulkFollows": 'bulkfollows.com' in c,
    "62yun VPS": '62yun.ru' in c,
    "Amnezia VPN": 'amnezia.org' in c,
    "GGsel": 'ggsel.io' in c,
    "9proxy": '9proxy.com' in c,
    "Dolphin Anty": 'dolphin-anty.com' in c,
    "ipin.io": 'ipin.io' in c,
    "Scamalytics": 'scamalytics.com' in c,
    "APIVoid": 'apivoid.com' in c,
    "AbuseIPDB": 'abuseipdb.com' in c,
    "textgenerator.ru": 'textgenerator.ru' in c,
    "sms-activate": 'sms-activate.io' in c,
    "smsfast.pro": 'smsfast.pro' in c,
    "YouTube Gmail reg": 'youtube.com/watch?v=1cpxKtkWWWA' in c,
    "YouTube iCloud": 'youtube.com/watch?v=dgYNIBcZYjw' in c,
    "YouTube Dolphin Anty": 'youtube.com/watch?v=bkCEC9-RRlk' in c,
    "YouTube Amnezia": 'youtube.com/watch?v=CotlyGI4dZE' in c,
    "YouTube GEO setup": 'youtube.com/watch?v=lnd8F2vEBx0' in c,
    "TG channel tiktokmnogokrut": 'tiktokmnogokrut' in c,
    "getallmylinks.com": 'getallmylinks.com' in c,
    "Clone App APK mention": 'Clone App' in c,
    "CapCut mention": 'CapCut' in c,
    "Python downloads link": 'python.org/downloads' in c,
    "FFmpeg install": 'ffmpeg' in c.lower(),
    
    # === ALL TELETYPE LINKS IN EXTERNAL MANUALS SECTION ===
    "Ext: FB create teletype": 'teletype.in/@watles/c-gxK4iVvKN' in c,
    "Ext: FB pour teletype": 'teletype.in/@watles/EA9kT75v8KR' in c,
    "Ext: TT create teletype": 'teletype.in/@watles/dYkO3cUWyDZ' in c,
    "Ext: BIO teletype": 'teletype.in/@watles/9xBldwE6tbx' in c,
    "Ext: Links teletype": 'teletype.in/@watles/YQ1hNMz-6QP' in c,
    "Ext: Video teletype": 'teletype.in/@watles/aPPZlzmLN8r' in c,
    "Ext: TT telegraph": 'telegra.ph/Manual-po-TT-03-09' in c,
    "Ext: IG reg telegraph": 'telegra.ph/Manual-po-rege-akkov-INST-03-12' in c,
    "Ext: IG pour telegraph": 'telegra.ph/Manual-po-zalivu-INST-03-21' in c,
    "Ext: Device telegraph": 'telegra.ph/Nastrojka-ustrojstva-04-29' in c,
    "Ext: Gmail V2 telegraph": 'telegra.ph/V2-Beskonechnye-besplatnye-pochty' in c,
    "Ext: Gmail V1 telegraph": 'telegra.ph/Beskonechnye-besplatnye-pochty' in c,
    "Ext: DuckDuckGo vc.ru": 'vc.ru/id1325277' in c,
    
    # === VIDEOS ===
    "Video: Android setup 1": 'IMG_1239.MOV' in c,
    "Video: Android setup 2": 'IMG_1240.MOV' in c,
    "Video: Android setup 3": 'IMG_1241.MOV' in c,
    "Video: iPhone setup": 'IMG_1243.MP4' in c,
    "Video: GEO setup": 'IMG_4974.MOV' in c,
    "Video: iCloud creation": 'IMG_1805.MP4' in c,
    "Video: TT cache reset": 'IMG_1810.MOV' in c,
    "Video: TT creo example": 'IMG_5014.MP4' in c,
    "Video: TT creo result": 'IMG_5013.MP4' in c,
    "Video: CapCut tutorial": '0323.mp4' in c,
    "Video: TT guide pt1": 'IMG_8359.MOV' in c,
    "Video: TT guide pt2": 'IMG_8355.MOV' in c,
    "Video: TT guide pt3": 'IMG_8357.MOV' in c,
    "Video: NoNud example": 'IMG_5590.MOV' in c,
    "Video: NoNud flash": 'IMG_7727.MOV' in c,
    "Video: Flash subtle": 'IMG_7711.MOV' in c,
    
    # === PHOTOS ===
    "Photo: Account status": 'photo_1@10-12-2025' in c,
    "Photo: VPN block": 'photo_2@22-12-2025' in c,
    "Photo: VPN step2": 'photo_3@22-12-2025' in c,
    "Photo: VPN step3": 'photo_4@22-12-2025' in c,
    "Photo: Font example": 'photo_5@22-12-2025' in c,
    "Photo: Font result": 'photo_6@22-12-2025' in c,
    "Photo: ExpressVPN proof": 'photo_7@10-01-2026' in c,
    "Photo: Reg error": 'photo_8@11-03-2026' in c,
    "Photo: BulkFollows 1": 'photo_9@12-03-2026' in c,
    "Photo: BulkFollows 2": 'photo_10@12-03-2026' in c,
    "Photo: Dolphin settings": 'photo_11@29-03-2026' in c,
    "Photo: Dolphin proxy": 'photo_12@29-03-2026' in c,
}

ok = 0
fail = 0
for name, result in checks.items():
    status = "OK" if result else "FAIL"
    if result:
        ok += 1
    else:
        fail += 1
        print(f"  FAIL: {name}")

print(f"\nResult: {ok}/{ok+fail} checks passed")
if fail == 0:
    print("ALL CHECKS PASSED!")
else:
    print(f"{fail} checks FAILED")
