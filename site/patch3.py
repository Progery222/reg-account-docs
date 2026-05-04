#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch 3: Final audit fixes - broken HTML, missing info from messages"""
import re

p = r"c:\Users\Alex\Downloads\Telegram Desktop\ChatExport_2026-05-01\site\index.html"
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

count = 0

# ============================================================
# FIX 1: Broken HTML on lines 158-159 (TrustMyIP + duplicate ipin.io)
# ============================================================
old_broken = '<a class="ext-link" href="https://trustmyip.com</a></li>\n<li><a class="ext-link" href="https://ipin.io/ru" target="_blank">ipin.io</a> — удобная проверка на русском/ip-fraud-checker" target="_blank">TrustMyIP</a></li>'
new_fixed = '<li><a class="ext-link" href="https://trustmyip.com/ip-fraud-checker" target="_blank">TrustMyIP</a></li>'
if old_broken in c:
    c = c.replace(old_broken, new_fixed)
    count += 1
    print(f"[{count}] Fixed broken TrustMyIP + ipin.io HTML")
else:
    # Try alternative matching
    old2 = 'href="https://trustmyip.com</a></li>'
    if old2 in c:
        # Find and replace the whole broken block
        idx = c.find(old2)
        # Find the start of the <li> before this
        li_start = c.rfind('<li>', 0, idx)
        # Find the end of the next </li>
        li_end = c.find('</li>', idx + len(old2))
        if li_start >= 0 and li_end >= 0:
            broken_block = c[li_start:li_end + 5]
            c = c.replace(broken_block, '<li><a class="ext-link" href="https://trustmyip.com/ip-fraud-checker" target="_blank">TrustMyIP</a></li>')
            count += 1
            print(f"[{count}] Fixed broken TrustMyIP HTML (alt method)")
    else:
        print("[SKIP] TrustMyIP HTML already fixed or not found")

# ============================================================
# FIX 2: Fix broken VPN Liberty Bot closing tag (line 354)
# ============================================================
old_liberty = 'VPN Liberty Bot</a</li>'
new_liberty = 'VPN Liberty Bot</a></li>'
if old_liberty in c:
    c = c.replace(old_liberty, new_liberty)
    count += 1
    print(f"[{count}] Fixed broken VPN Liberty Bot closing tag")
else:
    print("[SKIP] VPN Liberty Bot tag OK or not found")

# ============================================================
# FIX 3: Add Telegraph links to Instagram registration section
# ============================================================
reg_section_anchor = '<h3>📱 Полный гайд по регистрации аккаунтов Instagram</h3>'
if reg_section_anchor in c and 'Manual-po-rege-akkov-INST' not in c.split('id="reg"')[1].split('id="verify"')[0] if 'id="reg"' in c else True:
    # Add the telegraph link reference near the start of reg section
    old_reg_info = '<div class="alert alert-info"><strong>ℹ️</strong> Источники: Telegraph-мануал + обновления из чата (дек 2025 — мар 2026)</div>'
    new_reg_info = '<div class="alert alert-info"><strong>ℹ️</strong> Источники: <a class="ext-link" href="https://telegra.ph/Manual-po-rege-akkov-INST-03-12" target="_blank">Telegraph-мануал по реге Instagram</a> + обновления из чата (дек 2025 — мар 2026)</div>'
    if old_reg_info in c:
        c = c.replace(old_reg_info, new_reg_info, 1)
        count += 1
        print(f"[{count}] Added Telegraph link to Instagram reg section")

# ============================================================
# FIX 4: Add Telegraph link to Instagram video pour section
# ============================================================
video_section = '<h3>🎬 Пошаговый гайд по заливу видео в Instagram</h3>'
if video_section in c:
    old_video = video_section
    new_video = video_section + '\n<div class="alert alert-info"><strong>ℹ️</strong> Полный мануал: <a class="ext-link" href="https://telegra.ph/Manual-po-zalivu-INST-03-21" target="_blank">Telegraph — Залив Instagram</a></div>'
    # Only add if not already there
    if 'Manual-po-zalivu-INST-03-21' not in c.split('id="video"')[1].split('id="content"')[0]:
        c = c.replace(old_video, new_video, 1)
        count += 1
        print(f"[{count}] Added Telegraph link to video pour section")

# ============================================================
# FIX 5: Add sorting info for accounts (from msg 7096)
# ============================================================
sort_info_target = '<div class="alert alert-tip"><strong>💡</strong> Для тех с 2+ трубками'
sort_info_addition = """<div class="alert alert-info"><strong>ℹ️</strong> <strong>Сортировка аккаунтов:</strong> если из 5 акков набрали 3, а 2 нет — 2 выкидываем и регаем 2 новых акка без сброса, без чистки кэша. Если все 5 не набрали — фулл сброс и по новой.</div>
"""
if sort_info_target in c and 'Сортировка аккаунтов' not in c:
    c = c.replace(sort_info_target, sort_info_addition + sort_info_target)
    count += 1
    print(f"[{count}] Added account sorting info")

# ============================================================
# FIX 6: Add important VPN note for prolivs about IP fraud check details  
# (from msg 6152 - detailed ExpressVPN fraud explanation)
# ============================================================
vpn_fraud_target = 'Инста проверяет IP только при ВХОДЕ и при РЕГИСТРАЦИИ.'
vpn_fraud_new = 'Инста проверяет IP только при ВХОДЕ и при РЕГИСТРАЦИИ. Фрод до 40-45 максимум при входе/реге.'
if vpn_fraud_target in c and '40-45' not in c:
    c = c.replace(vpn_fraud_target, vpn_fraud_new, 1)
    count += 1
    print(f"[{count}] Added fraud score limit detail (40-45)")

# ============================================================
# FIX 7: Add the Teletype link to TikTok section 
# (Manual po TT telegraph link)
# ============================================================
tt_section = '<h3>🎵 TikTok — регистрация и пролив</h3>'
if tt_section in c and 'Manual-po-TT-03-09' not in c.split('id="tiktok"')[1].split('id="facebook"')[0]:
    tt_new = tt_section + '\n<div class="alert alert-info"><strong>ℹ️</strong> Полный мануал: <a class="ext-link" href="https://telegra.ph/Manual-po-TT-03-09" target="_blank">Telegraph — Мануал по TikTok</a></div>'
    c = c.replace(tt_section, tt_new, 1)
    count += 1
    print(f"[{count}] Added Telegraph TT manual link to TikTok section")

# ============================================================
# FIX 8: Add Teletype link to Facebook section 
# ============================================================
fb_section = '<h3>📘 Facebook — регистрация, ФП и пролив</h3>'
fb_teletype_link = 'teletype.in/@watles/c-gxK4iVvKN'
if fb_section in c and fb_teletype_link not in c.split('id="facebook"')[1].split('id="links_redirect"')[0]:
    fb_new = fb_section + '\n<div class="alert alert-info"><strong>ℹ️</strong> Мануалы на Teletype: <a class="ext-link" href="https://teletype.in/@watles/c-gxK4iVvKN" target="_blank">Создание аккаунтов FB</a> | <a class="ext-link" href="https://teletype.in/@watles/EA9kT75v8KR" target="_blank">Пролив FB</a></div>'
    c = c.replace(fb_section, fb_new, 1)
    count += 1
    print(f"[{count}] Added Teletype links to Facebook section header")

# ============================================================
# FIX 9: Add Teletype link to content creation section
# ============================================================
content_section_header = '<div class="alert alert-info"><strong>ℹ️</strong> Источник: Teletype-мануал «Как создавать видео» + обновления из чата</div>'
if content_section_header in c and 'teletype.in/@watles/aPPZlzmLN8r' not in content_section_header:
    content_new = '<div class="alert alert-info"><strong>ℹ️</strong> Источник: <a class="ext-link" href="https://teletype.in/@watles/aPPZlzmLN8r" target="_blank">Teletype — Как создавать видео</a> + обновления из чата</div>'
    c = c.replace(content_section_header, content_new, 1)
    count += 1
    print(f"[{count}] Added Teletype link to content creation section")

# ============================================================
# FIX 10: Add TikTok Teletype link to content section
# ============================================================
tt_teletype = 'teletype.in/@watles/dYkO3cUWyDZ'
if tt_teletype not in c.split('id="tiktok"')[1].split('id="facebook"')[0]:
    tt_reg_section = '<h4>📱 Регистрация аккаунтов TikTok</h4>'
    if tt_reg_section in c:
        tt_reg_new = '<div class="alert alert-info"><strong>ℹ️</strong> Мануал на Teletype: <a class="ext-link" href="https://teletype.in/@watles/dYkO3cUWyDZ" target="_blank">Создание аккаунтов TikTok</a></div>\n' + tt_reg_section
        c = c.replace(tt_reg_section, tt_reg_new, 1)
        count += 1
        print(f"[{count}] Added TikTok Teletype link to TT reg section")

# ============================================================
# FIX 11: Add links section Teletype link
# ============================================================
links_section = '<h3>🔗 Прокладки, редиректы и универсальные ссылки</h3>'
links_teletype = 'teletype.in/@watles/YQ1hNMz-6QP'
if links_section in c and links_teletype not in c.split('id="links_redirect"')[1].split('id="bio"')[0]:
    links_new = links_section + '\n<div class="alert alert-info"><strong>ℹ️</strong> Полный мануал: <a class="ext-link" href="https://teletype.in/@watles/YQ1hNMz-6QP" target="_blank">Teletype — Прокладки и мультиссылки</a></div>'
    c = c.replace(links_section, links_new, 1)
    count += 1
    print(f"[{count}] Added Teletype link to links/redirect section")

# ============================================================
# FIX 12: Add BIO Teletype link to BIO section
# ============================================================
bio_section = '<h3>✍️ Промт для генерации описаний и BIO через ИИ</h3>'
bio_teletype = 'teletype.in/@watles/9xBldwE6tbx'
if bio_section in c and bio_teletype not in c.split('id="bio"')[1].split('id="payment"')[0]:
    bio_new = bio_section + '\n<div class="alert alert-info"><strong>ℹ️</strong> Источник: <a class="ext-link" href="https://teletype.in/@watles/9xBldwE6tbx" target="_blank">Teletype — Промт для описаний/BIO</a></div>'
    c = c.replace(bio_section, bio_new, 1)
    count += 1
    print(f"[{count}] Added Teletype link to BIO section")

# ============================================================
# FIX 13: Add YouTube link for Gmail reg to email section
# ============================================================
gmail_youtube = 'https://www.youtube.com/watch?v=1cpxKtkWWWA'
if gmail_youtube in c:
    print("[SKIP] Gmail YouTube link already exists")
else:
    gmail_target = '<h4>📱 Как регать Gmail на Android (видео)</h4>'
    if gmail_target in c:
        print("[SKIP] Gmail reg YouTube section already exists")

# ============================================================
# FIX 14: Add missing "do not give access" info for TikTok reg
# (from msg 1682 - не даём доступ к контактам, камере и микро)
# ============================================================
tt_permissions = 'не даём доступ к контактам'
if tt_permissions not in c:
    tt_exit_step = '<h4>Выход и очистка</h4>'
    if tt_exit_step in c:
        old_exit = '<h4>Выход и очистка</h4><p>Выходим → сбрасываем кэш/данные TikTok (или удаляем + скачиваем заново на iPhone). Регаем следующий.</p>'
        new_exit = '<h4>Выход и очистка</h4><p>Выходим → сбрасываем кэш/данные TikTok (или удаляем + скачиваем заново на iPhone). Регаем следующий.</p>\n<div class="alert alert-danger"><strong>🚫</strong> При регистрации НЕ даём доступ к контактам, камере и микрофону — только к галерее!</div>'
        if old_exit in c:
            c = c.replace(old_exit, new_exit, 1)
            count += 1
            print(f"[{count}] Added TT permissions warning")

# ============================================================
# FIX 15: Add Nastrojka-ustrojstva Telegraph link to device section
# ============================================================
device_telegraph = 'telegra.ph/Nastrojka-ustrojstva-04-29'
if device_telegraph not in c.split('id="phone"')[1].split('id="vpn"')[0]:
    device_target = '<h3>⚙️ Подготовка телефона к работе'
    if device_target in c:
        device_new = '<div class="alert alert-info"><strong>ℹ️</strong> Полный мануал: <a class="ext-link" href="https://telegra.ph/Nastrojka-ustrojstva-04-29" target="_blank">Telegraph — Настройка устройства</a></div>\n' + device_target
        # Only inject before the h3, not replacing it
        # Actually let's put it after the h3
        device_target2 = device_target
        idx = c.find(device_target2)
        if idx >= 0:
            end_h3 = c.find('</h3>', idx)
            if end_h3 >= 0:
                insert_pos = end_h3 + 5
                insert_html = '\n<div class="alert alert-info"><strong>ℹ️</strong> Полный мануал: <a class="ext-link" href="https://telegra.ph/Nastrojka-ustrojstva-04-29" target="_blank">Telegraph — Настройка устройства</a></div>'
                c = c[:insert_pos] + insert_html + c[insert_pos:]
                count += 1
                print(f"[{count}] Added Telegraph device setup link to phone section")

# ============================================================
# FIX 16: Fix unclosed alert tag on line 303
# ============================================================
broken_alert = '<div class="alert alert-warning"><strong>⚠️\n<div class="alert alert-danger">'
if broken_alert in c:
    c = c.replace(broken_alert, '<div class="alert alert-danger">')
    count += 1
    print(f"[{count}] Fixed unclosed alert tag on line 303")
else:
    # Try with \r\n
    broken_alert2 = '<div class="alert alert-warning"><strong>⚠️\r\n<div class="alert alert-danger">'
    if broken_alert2 in c:
        c = c.replace(broken_alert2, '<div class="alert alert-danger">')
        count += 1
        print(f"[{count}] Fixed unclosed alert tag (CRLF)")

# ============================================================
# WRITE RESULT
# ============================================================
with open(p, "w", encoding="utf-8") as f:
    f.write(c)

print(f"\n{'='*50}")
print(f"✅ Applied {count} fixes out of 16 checks")
print(f"{'='*50}")
