import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = "../chats/chat_562953382643143/topic_1019"

with open(os.path.join(BASE, "result.json"), encoding="utf-8") as f:
    data = json.load(f)

msgs = [m for m in data["messages"] if m["type"] == "message"]

def get_text(m):
    t = m.get("text", "")
    if isinstance(t, str):
        return t
    parts = []
    for p in t:
        if isinstance(p, str):
            parts.append(p)
        elif isinstance(p, dict):
            tt = p.get("text", "")
            tp = p.get("type", "")
            href = p.get("href", "")
            if tp == "link":
                parts.append(f'<a class="ext-link" href="{tt}" target="_blank">{tt}</a>')
            elif tp == "text_link":
                parts.append(f'<a class="ext-link" href="{href}" target="_blank">{tt}</a>')
            elif tp == "bold":
                parts.append(f'<strong>{tt}</strong>')
            elif tp == "strikethrough":
                parts.append(f'<del>{tt}</del>')
            elif tp in ("blockquote",):
                parts.append(f'<span class="bq">{tt}</span>')
            else:
                parts.append(tt)
    return "".join(parts)

# Group messages into topics
sections = {
    "reg": {"title": "📱 Регистрация аккаунтов Instagram", "icon": "📱", "msgs": []},
    "video": {"title": "🎬 Залив и пролив видео", "icon": "🎬", "msgs": []},
    "verify": {"title": "🔒 Верификации (верифы)", "icon": "🔒", "msgs": []},
    "vpn": {"title": "🌐 VPN и IP", "icon": "🌐", "msgs": []},
    "phone": {"title": "⚙️ Настройка телефона", "icon": "⚙️", "msgs": []},
    "email": {"title": "📧 Почты и Gmail-трюки", "icon": "📧", "msgs": []},
    "payment": {"title": "💳 Оплата из РФ", "icon": "💳", "msgs": []},
    "tiktok": {"title": "🎵 TikTok", "icon": "🎵", "msgs": []},
    "facebook": {"title": "📘 Facebook + Dolphin Anty", "icon": "📘", "msgs": []},
    "content": {"title": "🎥 Типы контента и креативы", "icon": "🎥", "msgs": []},
    "tools": {"title": "🛠 Инструменты и софт", "icon": "🛠", "msgs": []},
    "tips": {"title": "💡 Советы и обновления", "icon": "💡", "msgs": []},
    "links": {"title": "🔗 Мануалы (ссылки)", "icon": "🔗", "msgs": []},
}

def classify(m):
    txt = get_text(m).lower()
    fid = str(m.get("id",""))
    
    # Links/manuals
    if "telegra.ph" in txt or "teletype.in" in txt:
        return "links"
    
    # Facebook / Dolphin
    if "dolphin" in txt or "facebook" in txt or "антик" in txt or m.get("id") in [11123, 11217, 11218, 14591]:
        return "facebook"
    
    # TikTok
    if "тик ток" in txt or "тикток" in txt or "tiktok" in txt or "tik tok" in txt:
        return "tiktok"
    
    # Registration
    if "рега" in txt or "регаю" in txt or "регать" in txt or "регист" in txt or "регнул" in txt:
        if "facebook" not in txt and "тик ток" not in txt:
            return "reg"
    
    # Verification
    if "вериф" in txt:
        return "verify"
    
    # VPN / IP
    if "впн" in txt or "vpn" in txt or "айпи" in txt or "ip " in txt or "фрод" in txt or "scamalytics" in txt or "apivoid" in txt or "прокси" in txt or "expressvpn" in txt or "neo впн" in txt or "адгуард" in txt:
        if "dolphin" not in txt and "facebook" not in txt:
            return "vpn"
    
    # Video
    if "залив" in txt or "пролив" in txt or "видео" in txt or "видос" in txt or "хешт" in txt or "hash" in txt:
        if "создавать видео" not in txt and "креатив" not in txt and "крео" not in txt:
            return "video"
    
    # Phone setup
    if "настройк" in txt or "сбрас" in txt or "телефон" in txt or "андроид" in txt or "айфон" in txt or "xiaomi" in txt or "realme" in txt:
        return "phone"
    
    # Email
    if "почт" in txt or "gmail" in txt or "icloud" in txt or "email" in txt or "alias" in txt or "токен" in txt:
        return "email"
    
    # Payment
    if "оплат" in txt or "ggsell" in txt or "ggsel" in txt or "препейд" in txt or "карт" in txt:
        return "payment"
    
    # Content types
    if "крео" in txt or "ноу нюд" in txt or "флеш" in txt or "липс" in txt or "формат" in txt or "уникал" in txt:
        return "content"
    
    # Tools
    if "софт" in txt or "скле" in txt or "капкут" in txt or "python" in txt or "ffmpeg" in txt or "питон" in txt or "bulkfollows" in txt or "clone_app" in txt or "scleicaGPT" in txt:
        return "tools"
    
    # Photo/media with description
    if m.get("photo") or m.get("file"):
        return "tips"
    
    return "tips"

for m in msgs:
    cat = classify(m)
    sections[cat]["msgs"].append(m)

# Build HTML
html_parts = []
html_parts.append('''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>МАНУАЛЫ — База знаний</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sidebar">
<div class="sidebar-header">
<h1>📚 МАНУАЛЫ</h1>
<p>База знаний команды</p>
</div>
<nav class="sidebar-nav">
<a class="nav-item active" data-section="home"><span class="icon">🏠</span><span class="label">Главная</span></a>
<div class="nav-divider"></div>
''')

for key, sec in sections.items():
    cnt = len(sec["msgs"])
    html_parts.append(f'<a class="nav-item" data-section="{key}"><span class="icon">{sec["icon"]}</span><span class="label">{sec["title"].split(" ",1)[1]} ({cnt})</span></a>\n')

html_parts.append('''
</nav>
</aside>
<main class="main">
<div class="topbar">
<button class="hamburger" id="hamburger">☰</button>
<h2 id="topbar-title">Главная</h2>
<div class="search-box"><input id="search-input" placeholder="Поиск по базе..."></div>
</div>
<div class="content">
''')

# HOME section
html_parts.append('''
<div class="section active" id="home">
<div class="hero">
<h2>📚 МАНУАЛЫ</h2>
<p>Полная база знаний по работе с аккаунтами Instagram, TikTok, Facebook. Все инструкции структурированы по темам.</p>
<div class="stats-row">
<div class="stat"><div class="num">''' + str(len(msgs)) + '''</div><div class="label">Сообщений</div></div>
<div class="stat"><div class="num">''' + str(len(sections)) + '''</div><div class="label">Разделов</div></div>
<div class="stat"><div class="num">12</div><div class="label">Фото</div></div>
<div class="stat"><div class="num">26</div><div class="label">Видео</div></div>
</div>
</div>
<div class="quick-nav">
''')

for key, sec in sections.items():
    cnt = len(sec["msgs"])
    html_parts.append(f'<div class="quick-card" data-go="{key}"><div class="qicon">{sec["icon"]}</div><h4>{sec["title"].split(" ",1)[1]}</h4><p>{cnt} записей</p></div>\n')

html_parts.append('</div>\n')

# Contradictions section on home
html_parts.append('''
<div class="card" style="margin-top:32px">
<h3>⚠️ Противоречия и обновления</h3>
<div class="contradiction">
<h4>⚡ Отлёжка аккаунтов</h4>
<p><strong>Ранее (дек 2025):</strong> «СУТКИ ОТЛЕГА потом заливаем видосы»</p>
<p><strong>Обновление (мар 2026):</strong> «Отлега на акки инсты не нужна, зарегали и сразу можете пролить 2-4-6 видео, просмотры очень хорошие 5-10-20к на первом проливе»</p>
<p style="color:var(--accent2);margin-top:8px">✅ Актуально: отлёжка НЕ нужна (март 2026)</p>
</div>
<div class="contradiction">
<h4>⚡ Количество видео за пролив</h4>
<p><strong>Ранее:</strong> «Проливаем 2 видео в день»</p>
<p><strong>Обновление (фев 2026):</strong> «Льем по 4 видео... ВСЕ ВИДЕО УНИКАЛЬНЫЕ»</p>
<p style="color:var(--accent2);margin-top:8px">✅ Актуально: 4 уникальных видео за пролив</p>
</div>
<div class="contradiction">
<h4>⚡ Сброс телефона при реге</h4>
<p><strong>Ранее (дек 2025):</strong> «5 аккаунтов на сессию потом полный сброс»</p>
<p><strong>Обновление (фев 2026):</strong> «кеш приложения я не чистил... трубку не сбрасывал» — 12 из 15 акков стрельнуло</p>
<p style="color:var(--accent2);margin-top:8px">✅ Актуально: сброс не обязателен, работает без него</p>
</div>
</div>
</div>
''')

# Generate each section
for key, sec in sections.items():
    html_parts.append(f'<div class="section" id="{key}">\n')
    html_parts.append(f'<h2 style="margin-bottom:24px;font-size:1.5rem">{sec["title"]}</h2>\n')
    
    for m in sec["msgs"]:
        text = get_text(m)
        if not text.strip() and not m.get("photo") and not m.get("file"):
            continue
        
        author = m.get("from", "")
        date = m.get("date", "")[:10]
        fwd = m.get("forwarded_from", "")
        
        html_parts.append('<div class="card">\n')
        html_parts.append(f'<div class="meta"><span>👤 {author}</span><span>📅 {date}</span>')
        if fwd:
            html_parts.append(f'<span>↗️ от {fwd}</span>')
        html_parts.append('</div>\n')
        
        # Text content
        if text.strip():
            # Replace newlines with <br>
            formatted = text.replace("\n", "<br>")
            html_parts.append(f'<div class="card-text">{formatted}</div>\n')
        
        # Photo
        photo = m.get("photo", "")
        if photo and "not included" not in photo:
            photo_path = "../" + photo
            html_parts.append(f'<img class="photo-inline" src="{photo_path}" alt="Фото" loading="lazy">\n')
        
        # Video
        file_path = m.get("file", "")
        media_type = m.get("media_type", "")
        if file_path and "not included" not in file_path and media_type in ("video_file", "animation"):
            vid_path = "../" + file_path
            thumb = m.get("thumbnail", "")
            dur = m.get("duration_seconds", 0)
            html_parts.append(f'<div style="margin:12px 0"><video controls preload="none" ')
            if thumb and "not included" not in thumb:
                html_parts.append(f'poster="../{thumb}" ')
            html_parts.append(f'style="max-width:100%;max-height:500px;border-radius:10px"><source src="{vid_path}">Видео</video>')
            html_parts.append(f'<div style="font-size:0.75rem;color:var(--text-muted);margin-top:4px">⏱ {dur} сек</div></div>\n')
        
        # APK or script file
        if file_path and "not included" not in file_path and media_type not in ("video_file", "animation"):
            fname = m.get("file_name", "")
            if fname:
                html_parts.append(f'<div class="alert alert-info">📎 Файл: <strong>{fname}</strong></div>\n')
        elif file_path and "not included" in file_path:
            fname = m.get("file_name", "")
            if fname:
                html_parts.append(f'<div class="alert alert-warning">📎 Файл не включён в экспорт: <strong>{fname}</strong></div>\n')
        
        html_parts.append('</div>\n')
    
    html_parts.append('</div>\n')

html_parts.append('''
</div>
</main>
<script src="script.js"></script>
</body>
</html>
''')

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("".join(html_parts))

print(f"Generated: {output_path}")
print(f"Total messages processed: {len(msgs)}")
for k,v in sections.items():
    print(f"  {v['title']}: {len(v['msgs'])} msgs")
