#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Part 3 — TikTok, Facebook, links, payment, tools, updates + close HTML"""
import os
MEDIA = "../chats/chat_562953382643143/topic_1019"
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

def V(p,po="",d=0,c=""): 
    h=f'<div class="media-block"><video controls preload="none"'
    if po: h+=f' poster="../{po}"'
    h+=f' style="max-width:100%;max-height:500px;border-radius:12px"><source src="../{p}">V</video>'
    if d: h+=f'<span class="dur">⏱ {d}с</span>'
    if c: h+=f'<p class="media-caption">{c}</p>'
    return h+'</div>'
def P(p,c=""):
    h=f'<div class="media-block"><img class="photo-inline" src="../{p}" alt="{c}" loading="lazy">'
    if c: h+=f'<p class="media-caption">{c}</p>'
    return h+'</div>'
def A(t,x):
    i={"warning":"⚠️","danger":"🚫","success":"✅","info":"ℹ️","tip":"💡"}
    return f'<div class="alert alert-{t}"><strong>{i.get(t,"")}</strong> {x}</div>'
def S(n,t,x): return f'<div class="step"><div class="step-num">{n}</div><div class="step-content"><h4>{t}</h4><p>{x}</p></div></div>'

pp=[]

# ---- TIKTOK ----
pp.append(("tiktok","🎵 TikTok: полный гайд",f'''
<div class="card">
<h3>🎵 TikTok — регистрация и пролив</h3>
{A("danger","ГЕО: ТОЛЬКО USA! Никакой Европы. VPN обязателен даже если ТТ работает без ограничений.")}

<h4>📱 Регистрация аккаунтов TikTok</h4>
{S(1,"Сброс и настройка","Полный сброс устройства → настройка на USA → включить самолёт → Wi-Fi → VPN (USA) → скачать TikTok")}
{S(2,"Регистрация","Заходим в ТТ с VPN USA → регистрируем через почту (iCloud/Gmail). Убираем ВСЕ галочки сохранения пароля!")}
{S(3,"Профиль","Ставим имя модели. Аватарка: СКРОМНАЯ (без бюста/лифчика/трусов/ног). БИО — пусто. В историю НЕ публикуем.")}
{S(4,"Выход и очистка","Выходим → сбрасываем кэш/данные TikTok (или удаляем + скачиваем заново на iPhone). Регаем следующий.")}

<table class="data-table">
<tr><th>Параметр</th><th>Значение</th></tr>
<tr><td>Акков на 1 сброс</td><td>5-15 штук (каждый раз чистим кэш)</td></tr>
<tr><td>IP на 5 акков</td><td>Каждые 5 акков меняем IP</td></tr>
<tr><td>Отлёжка</td><td>48-96 часов минимум</td></tr>
<tr><td>Прогрев</td><td>НЕ нужен</td></tr>
</table>

<h4>📹 Видео: как сбрасывать кэш TikTok</h4>
{V(f"{MEDIA}/video_files/IMG_1810.MOV",f"{MEDIA}/video_files/IMG_1810.MOV_thumb.jpg",10,"Быстрый сброс кэша TikTok между регистрациями")}

<h4>🎬 Пролив TikTok</h4>
{A("danger","Контент: СУПЕР ноунюд! Никаких намеков на трусы/лифчики. Про 18+ молчим. Можно обрезанные флеши (БЕЗ видимых сосков/пуси).")}
<p><strong>День 1:</strong> Заливаем 2-3 видео без описания. Оставляем на сутки.</p>
<p><strong>День 2:</strong> Проверяем аналитику. Акки с 500+ → накручиваем 1000 подписчиков через <a class="ext-link" href="https://bulkfollows.com/" target="_blank">bulkfollows.com</a> (мин. пополнение $10). Ставим ссылку. Остальные — проливаем ещё раз.</p>
<p><strong>День 3:</strong> Сортируем. 3-4 дня без просмотров → в отлёгу (проверяем на ограны).</p>

{A("warning","Проверяйте аналитику! Оранжевая плашка «контент не подходит для ленты Для Тебя» = видео не будет набирать. Удаляйте и меняйте.")}
{A("tip","Канал с примерами: <a class='ext-link' href='https://t.me/tiktokmnogokrut' target='_blank'>t.me/tiktokmnogokrut</a>")}
</div>
'''))

# ---- FACEBOOK ----
pp.append(("facebook","📘 Facebook + Dolphin Anty",f'''
<div class="card">
<h3>📘 Facebook — регистрация, ФП и пролив</h3>

<h4>📱 Регистрация аккаунтов Facebook</h4>
{A("info","3 способа регистрации. Выбирайте подходящий.")}

<p><strong>Способ 1 — по почте:</strong> VPN → Facebook → регистрация по почте. Если не пропускает: удалить данные ФБ, сменить IP и почту.</p>
<p><strong>Способ 2 — по номеру + переключение на почту:</strong> Вводим +номер → НЕ вводим код → «подтвердить другим способом» → почта. После реги: ОБЯЗАТЕЛЬНО удалить номер из профиля.</p>
<p><strong>Способ 3 — по номеру напрямую:</strong> Код приходит в WhatsApp. После реги: привязать почту → удалить номер. Покупные номера: <a class="ext-link" href="https://smsfast.pro/?ref=943107" target="_blank">smsfast.pro</a></p>

<p>На 1 сброс: <strong>3 аккаунта</strong>. После реги: заходим в каждый акк, выходим с «Запомнить аккаунт». <strong>2 дня отлёга.</strong></p>

<h4>📄 Фанпейджи (ФП) — главный инструмент</h4>
{A("danger","Проливаем ТОЛЬКО ФП! Личный аккаунт Facebook НЕ льём!")}
{S(1,"Создаём ФП","После 2 дней отлёги: по 1 ФП в день на каждый аккаунт, пока не будет по 4 ФП")}
{S(2,"Настройки ФП","Ссылка: «private69». BIO: уникальное через ИИ. Аватарка + шапка сразу.")}
{S(3,"Пролив","Сразу после создания ФП: 4 видео. Далее каждый день по 4 видео на каждый ФП.")}
{S(4,"Отсев","2 пролива нули → удаляем ФП, создаём новый.")}

<h4>🐬 Dolphin Anty (антидетект-браузер)</h4>
<p>Видеогайд: <a class="ext-link" href="https://www.youtube.com/watch?v=bkCEC9-RRlk" target="_blank">YouTube — Dolphin Anty</a></p>
<p>Скачать: <a class="ext-link" href="https://dolphin-anty.com" target="_blank">dolphin-anty.com</a>. Прокси: <a class="ext-link" href="https://9proxy.com" target="_blank">9proxy.com</a> (резидентские, SOCKS5).</p>

<p><strong>Настройка:</strong> 1 профиль = 1 прокси = 1 аккаунт. При создании каждого профиля нажимать «Новый отпечаток».</p>

{P(f"{MEDIA}/photos/photo_11@29-03-2026_19-38-19.jpg","Настройка Dolphin Anty — правильные параметры профиля")}
{P(f"{MEDIA}/photos/photo_12@29-03-2026_19-38-19.jpg","Пример настройки прокси в Dolphin Anty")}

<h4>💰 Бюджет</h4>
<div class="code-block">$10/мес — подписка Dolphin Anty (20 профилей)<br>$3/50 IP — хватает на 2 дня<br>~$40/мес — прокси<br>Итого: ~$50/мес на антик + прокси</div>
</div>
'''))

# ---- ПРОКЛАДКИ И ССЫЛКИ ----
pp.append(("links_redirect","🔗 Прокладки и мультиссылки",f'''
<div class="card">
<h3>🔗 Прокладки, редиректы и универсальные ссылки</h3>

<h4>Что такое прокладка?</h4>
<p>Специальная страница с вашими ссылками, куда уводится трафик. Нужна потому что ссылки на adult-контент нельзя ставить в профиль напрямую.</p>

{S(1,"Создаём прокладку","<a class='ext-link' href='https://getallmylinks.com' target='_blank'>getallmylinks.com</a> — оформляем профиль. ОБЯЗАТЕЛЬНО домен <code>.app</code>!")}
{S(2,"Создаём универсальную ссылку","Для ботов/модерации → пустая страница. Для реальных пользователей → ваша прокладка.")}

<h4>🔗 Универсальные ссылки по площадкам</h4>
<table class="data-table">
<tr><th>Площадка</th><th>Формат ссылки</th><th>Пример</th></tr>
<tr><td>Instagram</td><td><code>https://private12.fun/?a=МОДЕЛЬ</code></td><td>private12.fun/?a=sofiasof</td></tr>
<tr><td>Facebook</td><td><code>https://private69.fun/?a=МОДЕЛЬ</code></td><td>private69.fun/?a=sofiasof</td></tr>
<tr><td>TikTok</td><td>Отдельная ссылка</td><td>Запросите в ЛС</td></tr>
</table>

{A("warning","Обычный gaml снесут быстро. Используйте ТОЛЬКО универсальные ссылки с доменов, которые даёт тимлид.")}
{A("info","Из gaml.app/modelname берёте только 'modelname' и подставляете после ?a=")}
</div>
'''))

# ---- BIO ----
pp.append(("bio","✍️ Описания и BIO",f'''
<div class="card">
<h3>✍️ Промт для генерации описаний и BIO через ИИ</h3>
<p>Используйте этот промт для создания описаний видео и BIO профилей. Замените <code>[X]</code> на количество, <code>[INSERT VIDEO DESCRIPTION HERE]</code> на примеры ваших видео.</p>
<div class="code-block" style="font-size:0.78rem;white-space:pre-wrap">You are an expert in viral short-form content, social media algorithms, and engagement psychology.

Your task is to generate long, informative, and highly engaging English descriptions for vertical videos (Instagram Reels, Facebook, TikTok).

The descriptions must follow this style:
- Written like an informative or analytical explanation
- Sound factual, neutral, and slightly "educational"
- Include elements of psychology, media analysis, or technology
- Be easy to read but feel "smart" and credible
- Written in 4–8 sentences
- Include 3–6 relevant hashtags at the end

Tone: Calm, informative, slightly analytical. No slang, no aggressive marketing.
Avoid: Direct calls to action, overhyped clickbait, fake claims.

Now generate [X] different descriptions based on this video idea:
[INSERT VIDEO DESCRIPTION HERE]

Make each description unique.</div>

<h4>Примеры BIO для Facebook ФП</h4>
<ul>
<li><em>Daily moments, exclusive previews and things I don't post anywhere else. Curious?</em></li>
<li><em>Official page. Sharing daily moments, special previews and a little more behind the scenes</em></li>
<li><em>Just a little preview of my world. The rest is for those who know where to look.</em></li>
</ul>
{A("tip","BIO всегда должно быть уникальным. Генерируйте через ИИ для каждого аккаунта отдельно.")}
</div>
'''))

# ---- ОПЛАТА ----
pp.append(("payment","💳 Оплата сервисов из РФ",f'''
<div class="card">
<h3>💳 Как оплачивать зарубежные сервисы из России</h3>
{S(1,"Включаем VPN","Любой европейский VPN (хоть бесплатный AdGuard)")}
{S(2,"Покупаем препейд-карту","На <a class='ext-link' href='https://ggsel.io' target='_blank'>GGsel.io</a> покупаем препейд-карту USA на нужный баланс. Оплата через СБП.")}
{S(3,"Вводим карту","При вводе карты — <strong>РУЧНОЙ ввод</strong> (не сканирование)")}
{A("tip","С крипты дешевле — нет комиссии.")}
{A("info","ExpressVPN через GGsel: ~300₽ за 20-25 дней. Оплата СБП.")}
</div>
'''))

# ---- ИНСТРУМЕНТЫ ----
pp.append(("tools","🛠 Инструменты и софт",f'''
<div class="card">
<h3>🛠 Необходимые инструменты</h3>
<h4>Софт для склейки видео (Python + FFmpeg)</h4>
{S(1,"Устанавливаем Python","<a class='ext-link' href='https://www.python.org/downloads/' target='_blank'>python.org/downloads</a>")}
{S(2,"Устанавливаем FFmpeg","Открываем командную строку: <code>winget install ffmpeg</code>")}
{S(3,"Перезагружаем","Перезагружаем компьютер и запускаем программу")}

<h4>Другие инструменты</h4>
<ul>
<li><strong>BulkFollows</strong> — <a class="ext-link" href="https://bulkfollows.com/" target="_blank">bulkfollows.com</a> — накрутка подписчиков (мин $10)</li>
<li><strong>VPS-сервис</strong> — <a class="ext-link" href="https://62yun.ru" target="_blank">62yun.ru</a></li>
<li><strong>Clone App</strong> — клонирование приложений (APK не включён в экспорт)</li>
<li><strong>CapCut</strong> — видеоредактор для уникализации</li>
<li><strong>Amnezia VPN</strong> — <a class="ext-link" href="https://docs.amnezia.org/ru/documentation/" target="_blank">документация</a>, <a class="ext-link" href="https://www.youtube.com/watch?v=CotlyGI4dZE" target="_blank">видеогайд</a></li>
</ul>
</div>
'''))

# ---- ОБНОВЛЕНИЯ ----
pp.append(("updates","📢 Обновления и хронология",f'''
<div class="card">
<h3>📢 Хронология обновлений</h3>
<div class="timeline-item"><div class="tdate">29 апреля 2026</div><p>Вышли обновлённые мануалы на Teletype: создание аккаунтов FB, пролив FB, создание ТТ, описания/BIO, прокладки, создание видео. <strong>Закреплённое сообщение.</strong></p></div>
<div class="timeline-item"><div class="tdate">23 марта 2026</div><p>Отлёжка Instagram НЕ нужна. Регаете → сразу проливаете 2-4-6 видео. Просмотры 5-10-20к на первом проливе.</p></div>
<div class="timeline-item"><div class="tdate">17 марта 2026</div><p>Расширена классификация видео: классический ноунюд, ноунюд+флеш, флеши. Для каждого типа — своя площадка.</p></div>
<div class="timeline-item"><div class="tdate">16 февраля 2026</div><p>Гайд по Gmail +alias: бесконечные бесплатные почты. После 15-20 реги — блок на 48ч.</p></div>
<div class="timeline-item"><div class="tdate">10 февраля 2026</div><p>Новая связка: 15 акков → 12 стрельнуло. Без сброса кэша, без смены IP, без сброса трубки. Льём по 4 видео.</p></div>
<div class="timeline-item"><div class="tdate">1 февраля 2026</div><p>Neo VPN для реги ОК, но для пролива — нули. ExpressVPN для пролива. IP проверяется только при входе и реге.</p></div>
<div class="timeline-item"><div class="tdate">7 декабря 2025</div><p>Первый мануал: рега, залив, верифы. 5 акков на сброс, сутки отлёга.</p></div>
</div>

<div class="card">
<h3>🔗 Все внешние мануалы</h3>
<ul>
<li><a class="ext-link" href="https://teletype.in/@watles/c-gxK4iVvKN" target="_blank">Создание аккаунтов FACEBOOK</a></li>
<li><a class="ext-link" href="https://teletype.in/@watles/EA9kT75v8KR" target="_blank">Пролив аккаунтов FACEBOOK</a></li>
<li><a class="ext-link" href="https://teletype.in/@watles/dYkO3cUWyDZ" target="_blank">Создание аккаунтов TIKTOK</a></li>
<li><a class="ext-link" href="https://teletype.in/@watles/9xBldwE6tbx" target="_blank">Промт для описаний/BIO</a></li>
<li><a class="ext-link" href="https://teletype.in/@watles/YQ1hNMz-6QP" target="_blank">Прокладки и мультиссылки</a></li>
<li><a class="ext-link" href="https://teletype.in/@watles/aPPZlzmLN8r" target="_blank">Как создавать видео</a></li>
<li><a class="ext-link" href="https://telegra.ph/Manual-po-rege-akkov-INST-03-12" target="_blank">Рега акков Instagram (Telegraph)</a></li>
<li><a class="ext-link" href="https://telegra.ph/Manual-po-zalivu-INST-03-21" target="_blank">Залив Instagram (Telegraph)</a></li>
<li><a class="ext-link" href="https://telegra.ph/Manual-po-TT-03-09" target="_blank">Мануал по ТТ (Telegraph)</a></li>
<li><a class="ext-link" href="https://telegra.ph/Nastrojka-ustrojstva-04-29" target="_blank">Настройка устройства (Telegraph)</a></li>
</ul>
</div>
'''))

with open(out, "a", encoding="utf-8") as f:
    for sid, title, html in pp:
        f.write(f'<div class="section" id="{sid}">\n<h2 style="margin-bottom:24px;font-size:1.5rem">{title}</h2>\n{html}\n</div>\n')
    f.write('</div></main>\n<script src="script.js"></script>\n</body></html>\n')

print("Part 3 done:", len(pp), "sections. HTML complete!")
