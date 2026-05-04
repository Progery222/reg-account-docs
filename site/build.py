#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генератор базы знаний v2 — профессиональные пошаговые гайды"""
import json, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA = "../chats/chat_562953382643143/topic_1019"

with open(os.path.join(BASE, "result.json"), encoding="utf-8") as f:
    data = json.load(f)

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "scraped_data.json"), encoding="utf-8") as f:
    scraped = json.load(f)

def V(path, poster="", dur=0, caption=""):
    """Video embed helper"""
    h = f'<div class="media-block"><video controls preload="none"'
    if poster: h += f' poster="../{poster}"'
    h += f' style="max-width:100%;max-height:500px;border-radius:12px"><source src="../{path}">Video</video>'
    if dur: h += f'<span class="dur">⏱ {dur} сек</span>'
    if caption: h += f'<p class="media-caption">{caption}</p>'
    return h + '</div>'

def P(path, caption=""):
    """Photo embed helper"""
    h = f'<div class="media-block"><img class="photo-inline" src="../{path}" alt="{caption}" loading="lazy">'
    if caption: h += f'<p class="media-caption">{caption}</p>'
    return h + '</div>'

def alert(type, text):
    icons = {"warning":"⚠️","danger":"🚫","success":"✅","info":"ℹ️","tip":"💡"}
    return f'<div class="alert alert-{type}"><strong>{icons.get(type,"")}</strong> {text}</div>'

def step(n, title, text):
    return f'<div class="step"><div class="step-num">{n}</div><div class="step-content"><h4>{title}</h4><p>{text}</p></div></div>'

# ============ BUILD SECTIONS ============
sections = []

# ---- 1. НАСТРОЙКА УСТРОЙСТВА ----
sections.append(("phone", "⚙️ Настройка устройства", f'''
<div class="card">
<h3>⚙️ Подготовка телефона к работе <span class="badge">Критически важно</span></h3>
{alert("danger","Любая невнимательность или пропущенный пункт = тени на аккаунтах, маленькие просмотры или нули. Делайте ВСЁ по инструкции!")}
{alert("warning","Перед началом работы: вытащите SIM-карту и обновите iOS/Android до последней версии.")}

<h4>📋 Чек-лист настройки (для всех платформ)</h4>
{step(1, "Полный сброс устройства", "Сброс до заводских настроек — обязательный первый шаг перед каждой сессией регистрации.")}
{step(2, "Настройка региона", "Регион: <strong>USA</strong> (или тир1 Европа для инсты). Часовой пояс должен соответствовать выбранному ГЕО. Язык — английский.")}
{step(3, "Отключаем всё лишнее", "<strong>Обязательно отключить:</strong> Геолокация (все виды), Bluetooth, NFC (только Android), Find My Device / Поиск устройства, Скрытая геолокация Google.")}
{step(4, "Удаляем РУ приложения", "Удалить: Яндекс, RuStore, любые приложения с российскими метаданными. Они палят ваше реальное ГЕО.")}
{step(5, "Режим полёта", "Включаем авиарежим (для тех, кто из СНГ), затем подключаемся к Wi-Fi.")}
{step(6, "Скачиваем необходимое", "Через VPN скачиваем: Instagram / TikTok / Facebook + Telegram + VPN-приложение.")}

<h4>📱 Видео-инструкция: Настройка Android</h4>
{V(f"{MEDIA}/video_files/IMG_1239.MOV", f"{MEDIA}/video_files/IMG_1239.MOV_thumb.jpg", 60, "Пошаговая настройка Android-устройства на ГЕО USA")}
<div class="text-summary">
<strong>Что показано в видео:</strong> Полный сброс Android, смена региона на US, отключение геолокации (в том числе скрытой от Google), отключение NFC, Bluetooth, удаление русскоязычных приложений, настройка часового пояса Eastern Time.
</div>

<h4>🍎 Видео-инструкция: Настройка iPhone</h4>
{V(f"{MEDIA}/video_files/IMG_1243.MP4", f"{MEDIA}/video_files/IMG_1243.MP4_thumb.jpg", 109, "Пошаговая настройка iPhone на ГЕО USA")}
<div class="text-summary">
<strong>Что показано в видео:</strong> Settings → General → Language & Region → Region: United States. Часовой пояс: New York (Eastern). Отключение Location Services, Bluetooth, NFC. Сброс сети: Settings → General → Transfer or Reset iPhone → Reset → Reset Network Settings.
</div>
{alert("warning","При сбросе сети удаляются все сохранённые пароли Wi-Fi. Выпишите их заранее!")}

<h4>🎯 Как правильно настроить гео (видео)</h4>
{V(f"{MEDIA}/video_files/IMG_4974.MOV", f"{MEDIA}/video_files/IMG_4974.MOV_thumb.jpg", 71, "Настройка телефона на нужное гео (USA) — обязательно БЕЗ SIM-КАРТЫ")}

<h4>🔤 Красивый шрифт для историй (Android)</h4>
<p>На Android стоковый шрифт некрасивый. Заходите на <a class="ext-link" href="https://textgenerator.ru/font/" target="_blank">textgenerator.ru/font/</a>, находите приятный шрифт, копируете и вставляете в историю.</p>
{P(f"{MEDIA}/photos/photo_5@22-12-2025_21-20-25.jpg", "Пример использования стороннего шрифта в историях")}
{P(f"{MEDIA}/photos/photo_6@22-12-2025_21-20-25.jpg", "Результат с красивым шрифтом")}

<h4>📌 Нюанс для Xiaomi</h4>
{alert("info","На Xiaomi нельзя отключить некоторые системные приложения. Рекомендуется выбирать Realme или другие телефоны, где все приложения можно отключить.")}
</div>
'''))

# ---- 2. VPN И IP ----
sections.append(("vpn", "🌐 VPN, IP и проверка на фрод", f'''
<div class="card">
<h3>🌐 Выбор VPN и проверка IP <span class="badge">Основа безопасности</span></h3>

<h4>📡 Какой VPN использовать?</h4>
<div class="info-box">
<h4>Для стран СНГ (РФ, Казахстан, Украина)</h4>
<p>Обязательно VPN/VPS/PROXY. Мобильный интернет НЕ подходит.</p>
</div>
<div class="info-box">
<h4>Для стран Европы (Австрия, Италия и др.)</h4>
<p>Можно использовать мобильный интернет. Просто включите самолёт → подождите → выключите для смены IP.</p>
</div>

<h4>✅ Рекомендованные VPN (для РФ)</h4>
<ul>
<li><strong>Neo VPN</strong> — <a class="ext-link" href="https://t.me/neovpnbot?start=1457307561" target="_blank">Telegram-бот</a> (хорош для реги, НО нельзя проливать через него — просмотры будут нули)</li>
<li><strong>ExpressVPN</strong> — <a class="ext-link" href="https://ggsel.io/catalog/product/expressvpn-premium-1-mesiac-licnyi-akkaunt-polnyi-dostup-102112190" target="_blank">купить через GGsel за 300₽</a> (хорош для пролива)</li>
<li><strong>Windscribe</strong> — альтернатива Express</li>
<li><strong>Browsec</strong> — бесплатный вариант</li>
<li><strong>AdGuard VPN</strong> — бесплатный (Нью-Йорк)</li>
<li><strong>Potatso</strong> — iOS, для прокси</li>
<li><strong>Amnezia VPN</strong> — <a class="ext-link" href="https://docs.amnezia.org/ru/documentation/" target="_blank">документация</a></li>
</ul>

{alert("danger","Neo VPN — ТОЛЬКО для регистрации и входа в аккаунт! Для пролива видео НЕ подходит — просмотры будут нулевые.")}
{alert("success","ExpressVPN — лучший для пролива. Можно купить через GGsel с оплатой по СБП.")}

<h4>🔍 Когда инста проверяет IP на фрод</h4>
{alert("warning","Инста проверяет IP только при ВХОДЕ и при РЕГИСТРАЦИИ. Когда проливаете — ей всё равно. Поэтому: входите с чистым IP (Neo VPN), потом переключайте на Express для пролива.")}

<h4>🛡️ Сервисы проверки IP на фрод</h4>
<ul>
<li><a class="ext-link" href="https://scamalytics.com/" target="_blank">scamalytics.com</a> — основной (ориентируйтесь на него)</li>
<li><a class="ext-link" href="https://ipin.io/ru" target="_blank">ipin.io</a> — дополнительный</li>
<li><a class="ext-link" href="https://www.apivoid.com/tools/ip-reputation-check/" target="_blank">APIVoid</a> — ещё один контроль</li>
<li><a class="ext-link" href="https://www.abuseipdb.com/check/" target="_blank">AbuseIPDB</a></li>
<li><a class="ext-link" href="https://trustmyip.com/ip-fraud-checker" target="_blank">TrustMyIP</a></li>
</ul>

<table class="data-table">
<tr><th>Фрод-скор</th><th>Статус</th><th>Риски</th></tr>
<tr><td style="color:var(--success)">0–35</td><td>Идеально ✅</td><td>Минимальные</td></tr>
<tr><td style="color:var(--warning)">35–50</td><td>Допустимо ⚠️</td><td>Могут быть верифы</td></tr>
<tr><td style="color:var(--danger)">50+</td><td>Рисково 🚫</td><td>Верифы, теневой бан, ограничения реги</td></tr>
</table>

{alert("info","Для Facebook допустимо до 65. Для TikTok — до 70.")}

<h4>🔒 Защита от утечки реального IP</h4>
<p>Включайте функцию блокировки интернета без VPN, чтобы инста случайно не увидела ваше реальное ГЕО:</p>
{P(f"{MEDIA}/photos/photo_2@22-12-2025_21-15-40.jpg", "Включите эту функцию ПОСЛЕ подключения к VPN — интернет не будет работать без VPN")}

<h4>💡 Лайфхак для браузера (оплата сервисов)</h4>
<p>Создайте чистый Chrome. С VPN (AdGuard, New York) погуглите новости Нью-Йорка, концерты, мероприятия. 1-2 дня отлежите браузер. После этого можно оплачивать VPN и сервисы с препейд-карт. Всегда заходить только через VPN, всегда NY.</p>
</div>
'''))

# ---- 3. ПОЧТЫ ----
sections.append(("email", "📧 Почты для регистрации", f'''
<div class="card">
<h3>📧 Создание почт для регистрации аккаунтов</h3>
{alert("danger","НИКОГДА не используйте временные почты — жёсткий триггер от Instagram!")}

<h4>🏆 Рекомендуемые сервисы (в порядке приоритета)</h4>
<ol>
<li><strong>iCloud</strong> — самый простой способ. Покупаете подписку iCloud+ 50 ГБ за $1, получаете возможность создавать кастомные почты.</li>
<li><strong>Gmail (+alias)</strong> — бесконечные бесплатные почты через трюк с токенами</li>
<li><strong>DuckDuckGo</strong> — <a class="ext-link" href="https://duckduckgo.com/" target="_blank">duckduckgo.com</a></li>
</ol>

<h4>🍎 Как создать почту iCloud (видео)</h4>
{V(f"{MEDIA}/video_files/IMG_1805.MP4", f"{MEDIA}/video_files/IMG_1805.MP4_thumb.jpg", 30, "Создание почты iCloud — покупка подписки iCloud+ 50 ГБ за $1")}
<p>Полный видеогайд: <a class="ext-link" href="https://www.youtube.com/watch?v=dgYNIBcZYjw" target="_blank">YouTube — iCloud почты за копейки</a></p>

<h4>♾️ Gmail: Бесконечные бесплатные почты через +alias</h4>
<div class="info-box">
<h4>Как это работает</h4>
<p>Gmail игнорирует всё после <code>+</code> до <code>@gmail.com</code>. Для сайтов это разные email, для Gmail — один ящик.</p>
</div>
<div class="code-block">
Основная: derevo134@gmail.com<br>
Для реги:  derevo134+L2apf@gmail.com<br>
Для реги:  derevo134+xyz99@gmail.com<br>
→ Все письма приходят на derevo134@gmail.com (задержка 2-3 сек)
</div>

<p><strong>Генерация через ИИ:</strong> «Логин основной почты ____@gmail.com, сгенерируй мне 1000 адресов с +токен alias» → нейросеть за секунды соберёт txt-файл.</p>

<p><strong>Сортировка писем:</strong> В поиске Gmail → Показать параметры → Кому: <code>derevo134+*gmail.com</code> → Создать фильтр → Пропустить входящие + Применить ярлык.</p>

{alert("warning","Instagram ограничивает регу после 15-20 аккаунтов с одного Gmail-корня. Блок длится 48 часов. Имейте 6-7 основных почт для чередования.")}

<h4>📱 Как регать Gmail на Android (видео)</h4>
<p><a class="ext-link" href="https://www.youtube.com/watch?v=1cpxKtkWWWA&t=1s" target="_blank">YouTube — Как регать Google аккаунты</a></p>
<p>Используйте домашний Wi-Fi и мобильный инет. Если просит номер — меняете IP (самолёт или перезагрузка роутера). В среднем 5 акков на 1 сброс.</p>

{alert("tip","Нафармите себе гуглов заранее, чтобы потом не тратить время!")}
</div>
'''))

# Write first part
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write('''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Полная база знаний по работе с аккаунтами Instagram, TikTok, Facebook. Пошаговые гайды.">
<title>МАНУАЛЫ — База знаний</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sidebar">
<div class="sidebar-header"><h1>📚 МАНУАЛЫ</h1><p>База знаний команды v2.0</p></div>
<nav class="sidebar-nav">
<a class="nav-item active" data-section="home"><span class="icon">🏠</span><span class="label">Главная</span></a>
<div class="nav-divider"></div>
''')
    nav_items = [
        ("phone","⚙️","Настройка устройства"),
        ("vpn","🌐","VPN, IP и фрод"),
        ("email","📧","Почты для реги"),
        ("reg","📱","Рега акков Instagram"),
        ("video","🎬","Залив видео Instagram"),
        ("content","🎥","Создание контента"),
        ("tiktok","🎵","TikTok: полный гайд"),
        ("facebook","📘","Facebook + Dolphin"),
        ("links_redirect","🔗","Прокладки и ссылки"),
        ("bio","✍️","Описания и BIO"),
        ("payment","💳","Оплата из РФ"),
        ("tools","🛠","Инструменты и софт"),
        ("updates","📢","Обновления и нюансы"),
    ]
    for sid, icon, label in nav_items:
        f.write(f'<a class="nav-item" data-section="{sid}"><span class="icon">{icon}</span><span class="label">{label}</span></a>\n')
    
    f.write('</nav></aside>\n<main class="main">\n')
    f.write('<div class="topbar"><button class="hamburger" id="hamburger">☰</button><h2 id="topbar-title">Главная</h2><div class="search-box"><input id="search-input" placeholder="Поиск по базе..."></div></div>\n')
    f.write('<div class="content">\n')
    
    # HOME
    f.write('''<div class="section active" id="home">
<div class="hero"><h2>📚 МАНУАЛЫ</h2><p>Полная база знаний. Пошаговые гайды с интеграцией всех внешних источников (Telegraph, Teletype), видео и скриншотов.</p>
<div class="stats-row">
<div class="stat"><div class="num">10</div><div class="label">Гайдов</div></div>
<div class="stat"><div class="num">13</div><div class="label">Разделов</div></div>
<div class="stat"><div class="num">26</div><div class="label">Видео</div></div>
</div></div>
<div class="quick-nav">
''')
    for sid, icon, label in nav_items:
        f.write(f'<div class="quick-card" data-go="{sid}"><div class="qicon">{icon}</div><h4>{label}</h4></div>\n')
    f.write('</div>\n')
    
    # Противоречия на главной
    f.write('''<div class="card" style="margin-top:32px">
<h3>⚠️ Важные обновления и изменения</h3>
<div class="contradiction"><h4>⚡ Отлёжка аккаунтов Instagram</h4>
<p><strong>Старая инфа (дек 2025):</strong> «СУТКИ ОТЛЕГА потом заливаем видосы»</p>
<p><strong>Актуально (мар 2026):</strong> «Отлега на акки инсты НЕ нужна, зарегали и сразу можете пролить 2-4-6 видео, просмотры 5-10-20к на первом проливе»</p></div>
<div class="contradiction"><h4>⚡ Количество видео за пролив</h4>
<p><strong>Старая инфа:</strong> «Проливаем 2 видео в день»</p>
<p><strong>Актуально (фев 2026):</strong> «Льем по 4 видео. ВСЕ ВИДЕО УНИКАЛЬНЫЕ. 10 акков = 40 видео»</p></div>
<div class="contradiction"><h4>⚡ Сброс телефона</h4>
<p><strong>Старая инфа:</strong> «5 аккаунтов на сессию потом полный сброс»</p>
<p><strong>Актуально (фев 2026):</strong> Сброс не обязателен. «кеш не чистил, трубку не сбрасывал» — 12 из 15 акков стрельнуло</p></div>
</div></div>
''')
    
    # Write sections that are ready
    for sid, title, html in sections:
        f.write(f'<div class="section" id="{sid}">\n<h2 style="margin-bottom:24px;font-size:1.5rem">{title}</h2>\n{html}\n</div>\n')

print("Part 1 written. Sections:", len(sections))
