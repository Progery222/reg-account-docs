#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch 2: Add missing info from Teletype/Telegraph articles + chat messages"""
import re

p = r"c:\Users\Alex\Downloads\Telegram Desktop\ChatExport_2026-05-01\site\index.html"
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

MEDIA = "../chats/chat_562953382643143/topic_1019"
changes = 0

def safe_replace(old, new):
    global c, changes
    if old in c:
        c = c.replace(old, new)
        changes += 1
        return True
    else:
        print(f"  SKIP: marker not found: {old[:60]}...")
        return False

# ============================================================
# 1. VPN section: add missing VPN bots, Browsec, Potatso, ipin.io
# ============================================================
old = 'Neo VPN), для пролива — ExpressVPN / Windscribe'
new = '''Neo VPN), для пролива — ExpressVPN / Windscribe</li>
<li><strong>Browsec</strong> — простой VPN, работает в РФ</li>
<li><strong>Potatso</strong> (iOS) — для прокси-подключений</li>
<li><strong>VPN-боты в Telegram:</strong> <a class="ext-link" href="https://t.me/neovpnbot?start=1457307561" target="_blank">Neo VPN Bot</a>, <a class="ext-link" href="https://t.me/vpn_liberty_bot?start=referral_1457307561" target="_blank">VPN Liberty Bot</a'''
safe_replace(old, new)

# 2. Add ipin.io to fraud check sites
old = 'trustmyip.com'
new = '''trustmyip.com</a></li>
<li><a class="ext-link" href="https://ipin.io/ru" target="_blank">ipin.io</a> — удобная проверка на русском'''
safe_replace(old, new)

# 3. Add DuckDuckGo email guide
old = '<div class="alert alert-tip"><strong>💡</strong> Нафармите себе гуглов'
new = '''<h4>🦆 DuckDuckGo почты</h4>
<p>Ещё один вариант — уникальные почты от DuckDuckGo. Гайд: <a class="ext-link" href="https://vc.ru/id1325277/1156565-unikalnye-pochty-ot-duckduckgo" target="_blank">vc.ru — Уникальные почты от DuckDuckGo</a></p>

<h4>📹 Видео: как регать iCloud почты</h4>
<p><a class="ext-link" href="https://www.youtube.com/watch?v=dgYNIBcZYjw" target="_blank">YouTube — Как создавать iCloud почты</a></p>

<h4>📄 Гайды по Gmail (альтернативные способы)</h4>
<ul>
<li><a class="ext-link" href="https://telegra.ph/V2-Beskonechnye-besplatnye-pochty--Gajd-03-14" target="_blank">Telegraph — Бесконечные бесплатные почты V2</a></li>
<li><a class="ext-link" href="https://telegra.ph/Beskonechnye-besplatnye-pochty--Gajd-03-09" target="_blank">Telegraph — Бесконечные бесплатные почты V1</a></li>
</ul>

<div class="alert alert-danger"><strong>🚫</strong> Временные почты НИКОГДА не используем — жёсткий триггер от Instagram, моментальный бан.</div>

<div class="alert alert-tip"><strong>💡</strong> Нафармите себе гуглов'''
safe_replace(old, new)

# ============================================================
# 4. Instagram reg: add VPN bots + detailed verification info
# ============================================================
old = 'почту и ник нужно менять на новые!</p></div>'
new = '''почту и ник нужно менять на новые!</p>
<p><strong>Важно:</strong> повторяем процесс (закрываем инсту → принудительно останавливаем → меняем IP → проверяем фрод → новая почта → новый ник) пока не поможет. В итоге даст регнуть или выдаст вериф.</p></div>'''
safe_replace(old, new)

# 5. Add "2 accounts per IP" diagnostic tip
old = 'Если акки отлетают — можете сменить IP прямо в процессе!</div>'
new = '''Если акки отлетают — можете сменить IP прямо в процессе!</div>
<div class="alert alert-tip"><strong>💡</strong> <strong>Как определить грязный IP:</strong> регайте по 2 акка на 1 IP. Если оба ушли в моментальную верификацию — меняйте IP при следующей реге.</div>'''
safe_replace(old, new)

# 6. Add "reg every 1-2 days" recommendation
old = 'Без стабильности не будет трафика.</div>'
new = '''Без стабильности не будет трафика.</div>
<div class="alert alert-warning"><strong>⚠️</strong> Раз в 1-2 дня регайте по 5 аккаунтов, потому что акки меняются быстро (так как льём спамом). Всегда держите запас свежих аккаунтов!</div>'''
safe_replace(old, new)

# ============================================================
# 7. Instagram pour: add "забыли про акки на сутки" detail from article
# ============================================================
old = 'Проливаем 4 видео на каждый акк</td><td>—</td></tr>'
new = '''Проливаем 4 видео на каждый акк (флеши)</td><td>Забываем про акки на сутки</td></tr>'''
safe_replace(old, new)

# 8. Instagram pour: add "link via stories only" detail
old = 'В БИО ссылку ставить НЕЛЬЗЯ! Только через сторис.'
new = '''В БИО ссылку ставить НЕЛЬЗЯ! Только через сторис.</p>
<p><strong>Почему не в БИО?</strong> Площадки научились вычислять прокладки. Ссылка в шапке → ограничение или вериф. Ссылку ставим ТОЛЬКО через истории и закрепляем в хайлайтах.'''
safe_replace(old, new)

# ============================================================
# 9. Facebook: MAJOR expansion with Teletype content
# ============================================================
# Add iPhone registration problem
old = 'Код приходит в WhatsApp. После реги: привязать почту'
new = '''Код приходит в WhatsApp. После реги: привязать почту'''
# Already there, skip

# Add detailed FB registration issues
old = 'Покупные номера: <a class="ext-link" href="https://smsfast.pro/?ref=943107" target="_blank">smsfast.pro</a></p>'
new = '''Покупные номера: <a class="ext-link" href="https://smsfast.pro/?ref=943107" target="_blank">smsfast.pro</a></p>

<h4>⚠️ Проблемы при регистрации Facebook</h4>
<div class="alert alert-warning"><strong>⚠️</strong> <strong>Не пропускает после ввода почты:</strong> выходите из ФБ → принудительно останавливаете → удаляете данные (iPhone: удалить ФБ и скачать заново). Меняем IP (самолёт на 15-20 сек для мобильного инета). Меняем почту. Регаем заново. Повторяем пока не поможет.</div>
<div class="alert alert-warning"><strong>⚠️</strong> <strong>Способ 2 — номер + почта (подробно):</strong> вводим номер с обязательным "+" перед ним (пример: +79876543210). На моменте подтверждения код НЕ вводим → «подтвердить другим способом» → выбираем «с помощью почты». Если ошибка при вводе номера — вводите не свой номер, а случайный (меняйте пару цифр).</div>
<div class="alert alert-danger"><strong>🚫</strong> <strong>Не регаются на iPhone:</strong> проблема не до конца решена. Помогает: регнуть через номер (способ 2), удалить ФБ и скачать заново, сменить IP + почту.</div>'''
safe_replace(old, new)

# Add "session of accounts" detail
old = '<strong>2 дня отлёга.</strong></p>'
new = '''<strong>2 дня отлёга.</strong></p>
<div class="alert alert-info"><strong>ℹ️</strong> <strong>Создаём сессию аккаунтов:</strong> после реги заходите в каждый аккаунт и выходите с <strong>«Запомнить аккаунт»</strong>. Так пока не зайдёте в последний — появится сессия всех аккаунтов.</div>'''
safe_replace(old, new)

# ============================================================
# 10. Facebook fanpages: expand with Teletype content
# ============================================================
old = '2 пролива нули → удаляем ФП, создаём новый.</p></div></div>'
new = '''2 пролива нули → удаляем ФП, создаём новый.</p></div></div>

<div class="card">
<h3>📋 Подробный гайд по Фанпейджам (ФП)</h3>
<div class="alert alert-info"><strong>ℹ️</strong> Источник: <a class="ext-link" href="https://teletype.in/@watles/EA9kT75v8KR" target="_blank">Teletype — Пролив аккаунтов FACEBOOK</a></div>

<h4>📅 График создания ФП</h4>
<table class="data-table">
<tr><th>День</th><th>Действие</th></tr>
<tr><td>1-2</td><td>Отлёга после регистрации аккаунтов</td></tr>
<tr><td>3</td><td>Создаём по 1 ФП на каждый аккаунт</td></tr>
<tr><td>4</td><td>Создаём ещё по 1 ФП (итого 2)</td></tr>
<tr><td>5</td><td>Создаём ещё по 1 ФП (итого 3)</td></tr>
<tr><td>6</td><td>Создаём последний ФП (итого 4 на аккаунт)</td></tr>
</table>

<h4>⚙️ Настройки ФП при создании</h4>
<ul>
<li>Ссылка: ставим сразу <code>private69</code></li>
<li>BIO: заполняем сразу, <strong>всегда уникальное</strong> (генерируем через ИИ)</li>
<li>Аватарку и шапку ставим сразу</li>
<li>После создания ФП можно сразу пролить 4 видео</li>
</ul>

<h4>📹 Пролив ФП</h4>
<p>Проливаем <strong>только ФП</strong>, личный аккаунт Facebook НЕ льём! Каждый день по 4 видео на каждый ФП.</p>
<p><strong>Хештеги/Описание:</strong> работают как в Instagram. Рекомендация: начать лить без описаний, позже тестировать хештеги.</p>

<h4>🗑 Что делать с нулями</h4>
<ol>
<li>Первый пролив: нули → ждём</li>
<li>Второй пролив: снова нули → удаляем ФП, создаём новый</li>
</ol>
<p><strong>Как удалить ФП:</strong> заходите на ФП → настройки и конфиденциальность → управление статусом страницы → удалить страницу.</p>

<h4>⚠️ Ограничения Facebook</h4>
<table class="data-table">
<tr><th>Тип ограничения</th><th>Что делать</th></tr>
<tr><td>Огран на охваты без даты</td><td>Удаляем ФП, создаём новый</td></tr>
<tr><td>Огран с датой (запрет на создание ФП/групп)</td><td>Ждём до указанной даты. Удаление ФП не поможет — огран на аккаунт</td></tr>
<tr><td>Верификация ФП</td><td>Нажимаем «не сейчас» и продолжаем проливать</td></tr>
</table>
<div class="alert alert-danger"><strong>🚫</strong> Ограничения в ФБ подсвечиваются КРАСНЫМ восклицательным знаком. Следите за статусом аккаунта!</div>
</div>'''
safe_replace(old, new)

# ============================================================
# 11. Dolphin Anty: MAJOR expansion
# ============================================================
old = '<h4>🐬 Dolphin Anty (антидетект-браузер)</h4>'
new = '''<h4>🐬 Dolphin Anty (антидетект-браузер) — полный гайд</h4>
<div class="alert alert-info"><strong>ℹ️</strong> Dolphin Anty — это антидетект-браузер, который позволяет запускать множество профилей (каждый со своим fingerprint и прокси) для работы с Facebook на ПК.</div>'''
safe_replace(old, new)

old = '<p>Видеогайд: <a class="ext-link" href="https://www.youtube.com/watch?v=bkCEC9-RRlk" target="_blank">YouTube — Dolphin Anty</a></p>'
new = '''<p>📹 Видеогайд: <a class="ext-link" href="https://www.youtube.com/watch?v=bkCEC9-RRlk" target="_blank">YouTube — Полный гайд по Dolphin Anty</a></p>'''
safe_replace(old, new)

old = '1 профиль = 1 прокси = 1 аккаунт. При создании каждого профиля нажимать «Новый отпечаток».</p>'
new = '''1 профиль = 1 прокси = 1 аккаунт. При создании каждого профиля нажимать «Новый отпечаток».</p>

<h4>📋 Пошаговая настройка Dolphin Anty</h4>
<div class="step"><div class="step-num">1</div><div class="step-content"><h4>Скачать и установить</h4><p>Скачиваем с <a class="ext-link" href="https://dolphin-anty.com" target="_blank">dolphin-anty.com</a>. Регистрируемся и оплачиваем подписку ($10/мес за 20 профилей).</p></div></div>
<div class="step"><div class="step-num">2</div><div class="step-content"><h4>Купить прокси</h4><p>На <a class="ext-link" href="https://9proxy.com" target="_blank">9proxy.com</a> покупаем резидентские прокси (SOCKS5). ~$3 за 50 IP, хватает на 2 дня.</p></div></div>
<div class="step"><div class="step-num">3</div><div class="step-content"><h4>Создать профиль</h4><p>Создаём профиль → вставляем прокси → нажимаем <strong>«Новый отпечаток»</strong> → сохраняем. Повторяем для каждого аккаунта.</p></div></div>
<div class="step"><div class="step-num">4</div><div class="step-content"><h4>Запустить профиль</h4><p>Нажимаем «Запустить» → откроется браузер с уникальным fingerprint и прокси → заходим в Facebook → регистрируем или входим в аккаунт.</p></div></div>
<div class="step"><div class="step-num">5</div><div class="step-content"><h4>Работа с аккаунтами</h4><p>В каждом профиле работаем как в обычном браузере. Сессия сохраняется — при следующем запуске не нужно логиниться заново.</p></div></div>

<h4>🔧 Формат прокси для Dolphin Anty</h4>
<div class="code-block">Тип: SOCKS5
Host: ip-адрес прокси
Port: порт
Login: логин (если есть)
Password: пароль (если есть)

Пример: socks5://user:pass@123.45.67.89:1080</div>

<div class="alert alert-warning"><strong>⚠️</strong> Каждый профиль = уникальный прокси. Нельзя использовать один прокси на несколько профилей — аккаунты свяжутся!</div>
<div class="alert alert-tip"><strong>💡</strong> При покупке прокси выбирайте резидентские (residential) — они имеют самый низкий фрод-скор. Дата-центровые прокси банятся чаще.</div>'''
safe_replace(old, new)

# ============================================================
# 12. TikTok: expand with Teletype content
# ============================================================
old = 'Убираем ВСЕ галочки сохранения пароля!</p></div></div>'
new = '''Убираем ВСЕ галочки сохранения пароля!</p>
<p><strong>ВАЖНО:</strong> убираем/отклоняем ВСЕ предложения ТТ сохранить пароль/аккаунт/вход. Это обязательно, иначе акки могут связаться между собой!</p></div></div>'''
safe_replace(old, new)

# Add TT pouring details
old = 'Оранжевая плашка «контент не подходит для ленты Для Тебя» = видео не будет набирать. Удаляйте и меняйте.</div>'
new = '''Оранжевая плашка «контент не подходит для ленты Для Тебя» = видео не будет набирать. Удаляйте и меняйте.</div>
<div class="alert alert-info"><strong>ℹ️</strong> Есть видео без плашки, но стоят в нулях. Они могут начать набирать позже, но просмотры будут мизерные — лучше удалить и залить другое.</div>
<div class="alert alert-warning"><strong>⚠️</strong> <strong>Накрутка подписчиков TikTok:</strong> обязательно проверяйте работоспособность «номерка» (исполнителя) — ставьте 10-50 подписчиков и ждите накрутки. Только после этого ставьте полный заказ. При проблемах — обращайтесь в поддержку BulkFollows, вернут средства на счёт.</div>'''
safe_replace(old, new)

# Add TT VPN detail
old = 'VPN обязателен даже если ТТ работает без ограничений.</div>'
new = '''VPN обязателен даже если ТТ работает без ограничений.</div>
<div class="alert alert-info"><strong>ℹ️</strong> ВПН/ПРОКСИ/ВПС используем ВСЕ, даже если ТТ у вас работает без ограничений. IP фрод для ТТ: берите 70 и ниже.</div>'''
safe_replace(old, new)

# TT can combine with Insta on same reset
old = 'Полный сброс устройства → настройка на USA → включить самолёт → Wi-Fi → VPN (USA) → скачать TikTok'
new = '''Полный сброс устройства → настройка на USA → включить самолёт → Wi-Fi → VPN (USA) → скачать TikTok</p>
<p><strong>Совет:</strong> можно настраивать трубку сразу под ТТ и ИНСТУ, чтобы на один сброс зарегать акки на обе площадки'''
safe_replace(old, new)

# ============================================================
# 13. Links/redirects: expand with Teletype detail
# ============================================================
old = 'Для ботов/модерации → пустая страница. Для реальных пользователей → ваша прокладка.</p></div></div>'
new = '''Для ботов/модерации → пустая страница. Для реальных пользователей → ваша прокладка.</p></div></div>

<h4>⚠️ Почему нужна универсальная ссылка?</h4>
<p>Площадки научились вычислять прокладки типа gaml. Если поставить обычную ссылку gaml в профиль — получите ограничение или вериф. Универсальная ссылка делает <strong>редирект/клоаку</strong>: для ботов и модерации показывает пустую страницу, а для настоящих пользователей — вашу прокладку.</p>
<div class="alert alert-danger"><strong>🚫</strong> Обычный gaml снесут быстро! Ссылки на онлик НЕЛЬЗЯ ставить в профиль напрямую — это сексуальный контент, площадка ограничит вашу страницу.</div>'''
safe_replace(old, new)

# ============================================================
# 14. Verification section: expand
# ============================================================
old = 'Если вериф пришёл после 3+ дней пролива и акк уже набирает — проходите вериф, акк стоит того.</div>'
new = '''Если вериф пришёл после 3+ дней пролива и акк уже набирает — проходите вериф, акк стоит того.</div>

<h4>📋 Подробный алгоритм действий при верификации</h4>
<div class="step"><div class="step-num">1</div><div class="step-content"><h4>Вериф на новом акке (до 3 дней)</h4><p>Акк в помойку. ВСЮ пачку аккаунтов с этого устройства тоже в помойку. Сбрасываем трубку и начинаем заново.</p></div></div>
<div class="step"><div class="step-num">2</div><div class="step-content"><h4>Вериф по камере</h4><p>Включаем камеру, кривляемся и делаем гримасы. Система проверяет наличие живого человека. Данные НЕ сохраняются. Ждём 1-12 часов.</p></div></div>
<div class="step"><div class="step-num">3</div><div class="step-content"><h4>Вериф по номеру</h4><p>Вводим СВОЙ номер → код приходит в WhatsApp → крутим лицом в камеру.</p></div></div>
<div class="step"><div class="step-num">4</div><div class="step-content"><h4>Вериф по ID (документы)</h4><p>НЕ проходим. Акк удаляем.</p></div></div>

<div class="alert alert-danger"><strong>🚫</strong> Если IP грязный — верифы будут ПОСТОЯННО. 80% верифов = грязный IP. Проверяйте фрод-скор ПЕРЕД регистрацией!</div>'''
safe_replace(old, new)

# ============================================================
# 15. Add missing external links to manuals section
# ============================================================
old = 'Настройка устройства (Telegraph)</a></li>'
new = '''Настройка устройства (Telegraph)</a></li>
<li><a class="ext-link" href="https://telegra.ph/V2-Beskonechnye-besplatnye-pochty--Gajd-03-14" target="_blank">Бесконечные почты Gmail V2 (Telegraph)</a></li>
<li><a class="ext-link" href="https://telegra.ph/Beskonechnye-besplatnye-pochty--Gajd-03-09" target="_blank">Бесконечные почты Gmail V1 (Telegraph)</a></li>
<li><a class="ext-link" href="https://vc.ru/id1325277/1156565-unikalnye-pochty-ot-duckduckgo" target="_blank">Уникальные почты от DuckDuckGo (vc.ru)</a></li>
<li><a class="ext-link" href="https://www.youtube.com/watch?v=dgYNIBcZYjw" target="_blank">Как регать iCloud почты (YouTube)</a></li>'''
safe_replace(old, new)

# ============================================================
# 16. Content section: add detail about NN for TikTok only
# ============================================================
old = 'Классический НоуНюд</td><td>Редко залетает</td>'
new = '''Классический НоуНюд</td><td>Редко залетает</td>'''

# Add detail to video creation
old = 'Музыка: поверх голоса накладываем популярную музыку из USA'
new = '''Музыка: поверх голоса накладываем популярную музыку из USA</li>
<li><strong>Голос модели:</strong> желательно оставлять, но можно и без него. Если есть возможность — поверх голоса в редакторе накладывайте свою музыку'''
safe_replace(old, new)

with open(p, "w", encoding="utf-8") as f:
    f.write(c)

print(f"Patch 2 applied! {changes} replacements made.")
print(f"File size: {len(c)} bytes")
