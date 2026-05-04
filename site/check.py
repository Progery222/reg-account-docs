import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

checks = {
    # VPN
    "Neo VPN Bot TG": "neovpnbot" in c,
    "VPN Liberty Bot": "vpn_liberty_bot" in c,
    "Browsec": "Browsec" in c,
    "Potatso": "Potatso" in c,
    "ipin.io": "ipin.io" in c,
    # Emails
    "DuckDuckGo guide": "duckduckgo" in c.lower(),
    "iCloud YT video": "dgYNIBcZYjw" in c,
    "Gmail V2 Telegraph": "V2-Beskonechnye" in c,
    "Gmail V1 Telegraph": "Beskonechnye-besplatnye-pochty--Gajd-03-09" in c,
    # Instagram
    "2 accs per IP tip": "2 акка на 1 IP" in c,
    "Reg every 1-2 days": "1-2 дня регайте" in c,
    # Facebook
    "FB iPhone problem": "Не регаются на iPhone" in c,
    "FB session detail": "Запомнить аккаунт" in c,
    "FB fanpage schedule": "График создания ФП" in c,
    "FB restrictions table": "Огран на охваты" in c,
    "FB fanpage deletion": "удалить страницу" in c,
    # Dolphin Anty
    "Dolphin step-by-step": "Пошаговая настройка Dolphin" in c,
    "Dolphin proxy format": "socks5://user:pass" in c,
    "Dolphin fingerprint": "fingerprint" in c,
    # TikTok
    "TT IP fraud 70": "фрод для ТТ" in c.lower() or "70 и ниже" in c,
    "TT combine with Insta": "ТТ и ИНСТУ" in c,
    "TT bulkfollows check": "10-50 подписчиков" in c,
    # Verification
    "Verify algorithm": "Подробный алгоритм" in c,
    "Verify steps": "step-num" in c,
    # Links
    "Redirect/cloaca detail": "редирект/клоаку" in c.lower() or "клоак" in c.lower(),
    # External links count
    "All Teletype links": c.count("teletype.in/@watles") >= 6,
    "All Telegraph links": c.count("telegra.ph") >= 6,
    "All YouTube links": c.count("youtube.com") >= 5,
}

ok = miss = 0
for k, v in checks.items():
    if v:
        ok += 1
    else:
        print(f"  MISSING: {k}")
        miss += 1
print(f"\nTotal: {ok} OK, {miss} MISSING out of {len(checks)}")
print(f"File: {len(c)} bytes, {c.count(chr(10))} lines")
print(f"Sections: {c.count('class=' + chr(34) + 'section' + chr(34))}")
print(f"Videos: {c.count('<video')}")
print(f"Photos: {c.count('photo-inline')}")
print(f"YouTube: {c.count('youtube.com')}")
print(f"Teletype: {c.count('teletype.in')}")
print(f"Telegraph: {c.count('telegra.ph')}")
