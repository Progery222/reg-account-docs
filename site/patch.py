#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch missing content into index.html"""
import os

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

MEDIA = "../chats/chat_562953382643143/topic_1019"

# 1. Add missing setup videos (parts 2-3) after IMG_1239 block
old1 = '<h4>🍎 Видео-инструкция: Настройка iPhone</h4>'
add_setup_videos = f'''<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_1240.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_1240.MOV">Video</video><span class="dur">⏱ 55 сек</span><p class="media-caption">Настройка Android — часть 2: Wi-Fi, VPN, скачивание приложений</p></div>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_1241.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_1241.MOV">Video</video><span class="dur">⏱ 191 сек</span><p class="media-caption">Настройка Android — часть 3: подробная пошаговая инструкция (3+ минуты)</p></div>

<h4>🍎 Видео-инструкция: Настройка iPhone</h4>'''
c = c.replace(old1, add_setup_videos)

# 2. Add YouTube link for phone setup
old2 = '<div class="alert alert-tip"><strong>💡</strong> Для iPhone 15+ без SIM-лотка'
add_yt = f'''<h4>📹 Видео: настройка телефона на ГЕО (YouTube)</h4>
<p><a class="ext-link" href="https://www.youtube.com/watch?v=lnd8F2vEBx0" target="_blank">YouTube — Настройка телефона на нужное ГЕО (USA)</a></p>
<div class="alert alert-danger"><strong>🚫</strong> ТЕЛЕФОН ДОЛЖЕН БЫТЬ ОБЯЗАТЕЛЬНО БЕЗ СИМ КАРТЫ!</div>

<div class="alert alert-tip"><strong>💡</strong> Для iPhone 15+ без SIM-лотка'''
c = c.replace(old2, add_yt)

# 3. Add VPN photos (2-4) and Neo VPN loca detail in VPN section
old3 = '<div class="alert alert-tip"><strong>💡</strong> Нафармите себе гуглов'
add_vpn_photos = f'''<h4>📸 Настройка VPN-блокировки интернета без VPN</h4>
<p>Включаем функцию блокировки интернета без VPN — чтобы инста случайно не спалила ваше реальное ГЕО:</p>
<div class="media-block"><img class="photo-inline" src="{MEDIA}/photos/photo_2@22-12-2025_21-15-40.jpg" alt="Включаем блокировку интернета без VPN" loading="lazy"><p class="media-caption">Включаем эту функцию после подключения к VPN. Интернет не будет работать без VPN</p></div>
<div class="media-block"><img class="photo-inline" src="{MEDIA}/photos/photo_3@22-12-2025_21-15-41.jpg" alt="Настройка VPN — шаг 2" loading="lazy"></div>
<div class="media-block"><img class="photo-inline" src="{MEDIA}/photos/photo_4@22-12-2025_21-15-41.jpg" alt="Настройка VPN — шаг 3" loading="lazy"></div>

<h4>✏️ Красивый шрифт для историй (Android)</h4>
<p>На Android идёт некрасивый стоковый шрифт. Решение: заходим на <a class="ext-link" href="https://textgenerator.ru/font/" target="_blank">textgenerator.ru/font</a>, находим приятный шрифт, копируем и вставляем в историю.</p>
<div class="media-block"><img class="photo-inline" src="{MEDIA}/photos/photo_5@22-12-2025_21-20-25.jpg" alt="Пример красивого шрифта" loading="lazy"></div>
<div class="media-block"><img class="photo-inline" src="{MEDIA}/photos/photo_6@22-12-2025_21-20-25.jpg" alt="Результат красивого шрифта в истории" loading="lazy"></div>

<div class="alert alert-tip"><strong>💡</strong> Нафармите себе гуглов'''
c = c.replace(old3, add_vpn_photos)

# 4. Add Neo VPN loca detail after ExpressVPN fraud info
old4 = 'После входа можете включать экспресс и больше не проверять'
if old4 in c:
    old4_full = c[c.index(old4):c.index('</div>', c.index(old4))]
    # just add after the existing content
    pass

# Find the VPN section and add Neo VPN loca warning
old_neo = 'НЕО ВПН для реги и для входа'
if old_neo not in c:
    # Add it in the VPN section
    old_vpn_marker = 'Neo VPN), для пролива — ExpressVPN / Windscribe'
    add_neo = '''Neo VPN), для пролива — ExpressVPN / Windscribe</li>
<li><strong>⚠️ Neo VPN + лока:</strong> чтобы лока в инсте определилась как USA, нужно в течение 3-4 дней войти и пролить через ExpressVPN, иначе лока будет РФ'''
    c = c.replace(old_vpn_marker, add_neo.rstrip())

# 5. Add verification section (new section after reg)
old_reg_end = '</div>\r\n\r\n</div>\r\n<div class="section" id="video">'
if old_reg_end not in c:
    old_reg_end = '</div>\n\n</div>\n<div class="section" id="video">'

verif_section = '''</div>

</div>
<div class="section" id="verify">
<h2 style="margin-bottom:24px;font-size:1.5rem">🛡 Верификации и как с ними бороться</h2>

<div class="card">
<h3>🛡 Полный гайд по верификациям Instagram</h3>
<div class="alert alert-danger"><strong>🚫</strong> Верификация ДО пролива (первые 3 дня) = акк в помойку! Вся пачка аккаунтов с этого устройства тоже в помойку!</div>

<h4>⚡ Цепная реакция</h4>
<p>Если один акк попал на верификацию по ID — все остальные акки на этом устройстве тоже получат вериф. <strong>Решение:</strong> немедленно сбрасываем трубку и начинаем заново.</p>

<h4>📋 Типы верификаций</h4>
<table class="data-table">
<tr><th>Тип</th><th>Что делать</th><th>Шансы</th></tr>
<tr><td>Камера (покрутить лицом)</td><td>Проходим — кривляемся на камеру, делаем гримасы</td><td>Высокие</td></tr>
<tr><td>ID (документы)</td><td>Акк в помойку, не тратьте время</td><td>Нулевые</td></tr>
<tr><td>Код на WhatsApp</td><td>Вводим свой номер → код в WA → проходим камеру</td><td>80% если IP чистый</td></tr>
</table>

<h4>⏱ Сроки проверки</h4>
<p>После прохождения верификации камерой: от 1 до 12 часов. В 80% случаев причина верифа — <strong>грязный IP</strong> (высокий фрод-скор).</p>

<div class="alert alert-tip"><strong>💡</strong> Лайфхак: при верификации камерой — кривляйтесь, делайте гримасы. Система проверяет что перед камерой живой человек, а не фото.</div>
<div class="alert alert-warning"><strong>⚠️</strong> Если вериф пришёл после 3+ дней пролива и акк уже набирает — проходите вериф, акк стоит того.</div>
</div>

</div>
<div class="section" id="video">'''
c = c.replace(old_reg_end, verif_section)

# 6. Add TikTok videos (creation examples) in TikTok section
old_tt_cache = '<h4>📹 Видео: как сбрасывать кэш TikTok</h4>'
add_tt_creo = f'''<h4>🎬 Видео: как делать и уникалить крео для ТТ</h4>
<p>Пример формата крео: подставляем отдельно реакцию + отдельно крео (танец, липсинг и т.д.). <strong>ВАЖНО:</strong> никакого сексуального контента! В ТТ льём исключительно ноу-нюд.</p>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_5014.MP4_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_5014.MP4">Video</video><span class="dur">⏱ 71 сек</span><p class="media-caption">Пример создания крео для TikTok — склейка реакции + контента</p></div>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_5013.MP4_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_5013.MP4">Video</video><span class="dur">⏱ 12 сек</span><p class="media-caption">Пример готового крео</p></div>

<h4>📹 Видео-гайды по ТТ мануалу</h4>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_8359.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_8359.MOV">Video</video><span class="dur">⏱ 91 сек</span><p class="media-caption">Видео-гайд по TikTok — часть 1</p></div>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_8355.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_8355.MOV">Video</video><span class="dur">⏱ 50 сек</span><p class="media-caption">Видео-гайд по TikTok — часть 2</p></div>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_8357.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_8357.MOV">Video</video><span class="dur">⏱ 49 сек</span><p class="media-caption">Видео-гайд по TikTok — часть 3</p></div>

<h4>📹 Видео: как сбрасывать кэш TikTok</h4>'''
c = c.replace(old_tt_cache, add_tt_creo)

# 7. Add more content examples in Content section
old_content_end = 'Флеш едва уловим — можно лить без вырезки. Не банится при наборе.</p></div>'
add_more_examples = f'''Флеш едва уловим — можно лить без вырезки. Не банится при наборе.</p></div>

<h4>📹 Ещё примеры контента</h4>
<p><strong>Классический НоуНюд — дополнительные примеры:</strong></p>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_5635 (2).MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_5635 (2).MOV">Video</video><span class="dur">⏱ 7 сек</span></div>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_5647 (3).MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_5647 (3).MOV">Video</video><span class="dur">⏱ 12 сек</span></div>

<p><strong>НоуНюд Флеш — дополнительные примеры:</strong></p>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_7726.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_7726.MOV">Video</video><span class="dur">⏱ 14 сек</span></div>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_7731.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_7731.MOV">Video</video><span class="dur">⏱ 9 сек</span></div>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_7722.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_7722.MOV">Video</video><span class="dur">⏱ 12 сек</span></div>

<p><strong>Флеши — дополнительные примеры:</strong></p>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_7712.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_7712.MOV">Video</video><span class="dur">⏱ 15 сек</span></div>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_9304.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_9304.MOV">Video</video><span class="dur">⏱ 12 сек</span></div>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_9319.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_9319.MOV">Video</video><span class="dur">⏱ 13 сек</span></div>
<div class="media-block"><video controls preload="none" poster="{MEDIA}/video_files/IMG_9318.MOV_thumb.jpg" style="max-width:100%;max-height:500px;border-radius:12px"><source src="{MEDIA}/video_files/IMG_9318.MOV">Video</video><span class="dur">⏱ 15 сек</span></div>'''
c = c.replace(old_content_end, add_more_examples)

# 8. Add BulkFollows screenshots in TikTok section
old_bulk = 'накручиваем 1000 подписчиков через <a class="ext-link" href="https://bulkfollows.com/"'
add_bulk_photos = f'''накручиваем 1000 подписчиков через <a class="ext-link" href="https://bulkfollows.com/"'''
# Photos for bulkfollows - add after the paragraph
old_bulk_after = 'Остальные — проливаем ещё раз.</p>'
add_bulk_screens = f'''Остальные — проливаем ещё раз.</p>
<div class="media-block"><img class="photo-inline" src="{MEDIA}/photos/photo_9@12-03-2026_22-41-45.jpg" alt="BulkFollows — интерфейс заказа" loading="lazy"><p class="media-caption">BulkFollows — выбираем услугу накрутки подписчиков</p></div>
<div class="media-block"><img class="photo-inline" src="{MEDIA}/photos/photo_10@12-03-2026_22-41-45.jpg" alt="BulkFollows — варианты" loading="lazy"><p class="media-caption">Цифры можно подбирать разные. На скрине дешёвые, которые долго крутят</p></div>'''
c = c.replace(old_bulk_after, add_bulk_screens)

# 9. Add ExpressVPN purchase screenshot in payment section
old_pay = 'ExpressVPN через GGsel: ~300₽ за 20-25 дней'
add_express_photo = f'''ExpressVPN через GGsel: ~300₽ за 20-25 дней. <a class="ext-link" href="https://ggsel.io/catalog/product/expressvpn-premium-1-mesiac-licnyi-akkaunt-polnyi-dostup-102112190" target="_blank">Ссылка на товар</a></div>
<div class="media-block"><img class="photo-inline" src="{MEDIA}/photos/photo_7@10-01-2026_18-12-14.jpg" alt="Подтверждение покупки ExpressVPN через GGsel" loading="lazy"><p class="media-caption">Подтверждение покупки и работоспособности ExpressVPN через GGsel</p></div>
<div class="alert alert-tip"><strong>💡</strong> Это триальные акки. Можно самому регать триалы каждый месяц и не платить. Для покупки нужен VPN — без него сайт не откроет (из-за РКН)'''
c = c.replace(old_pay, add_express_photo)

# 10. Add IP problem screenshot in reg section
old_ip_prob = 'IP проверяется на фрод в момент нажатия «Agree»'
add_ip_screen = f'''IP проверяется на фрод в момент нажатия «Agree» (подтверждение соглашения). Если акки отлетают — можете сменить IP прямо в процессе!</div>
<div class="media-block"><img class="photo-inline" src="{MEDIA}/photos/photo_8@11-03-2026_16-19-16.jpg" alt="Ошибка при регистрации — смените IP" loading="lazy"><p class="media-caption">У кого данная проблема — меняйте IP и всё будет ОК</p></div>
<div class="alert alert-warning"><strong>⚠️'''
old_ip_full = 'IP проверяется на фрод в момент нажатия «Agree» (подтверждение соглашения). Если акки отлетают — можете сменить IP прямо в процессе!</div>'
c = c.replace(old_ip_full, add_ip_screen.rstrip())

# 11. Add nav item for verify section
old_nav = '<a class="nav-item" data-section="video">'
add_nav = '<a class="nav-item" data-section="verify"><span class="icon">🛡</span><span class="label">Верификации</span></a>\n' + old_nav
c = c.replace(old_nav, add_nav)

# 12. Add quick card for verify
old_qc = '<div class="quick-card" data-go="video">'
add_qc = '<div class="quick-card" data-go="verify"><div class="qicon">🛡</div><h4>Верификации</h4></div>\n' + old_qc
c = c.replace(old_qc, add_qc)

# 13. Add Dolphin Anty detailed day-by-day in Facebook section
old_dolphin_budget = '<h4>💰 Бюджет</h4>'
add_dolphin_detail = '''<h4>📅 Пошаговый план работы с Facebook (Dolphin Anty)</h4>
<table class="data-table">
<tr><th>День</th><th>Действие</th></tr>
<tr><td>1</td><td>Создаём профиль в Dolphin → прокси → регистрация FB → аватарка → закрываем</td></tr>
<tr><td>2-3</td><td>Прогрев: заходим на 2-3 минуты, подписываемся на 1 модель + 1 группу знакомств USA, пару лайков</td></tr>
<tr><td>4</td><td>Первый залив: 4 видео без описания, без хештегов, только обрезанные флеш+реакция</td></tr>
<tr><td>5</td><td>Второй залив: снова 4 видео, тот же формат</td></tr>
<tr><td>6</td><td>Третий залив: 4 видео</td></tr>
<tr><td>7</td><td>Проверка: &lt;1000 просмотров → удаляем акк. 5000+ → ставим ссылку</td></tr>
</table>

<div class="alert alert-warning"><strong>⚠️</strong> При регистрации: если ошибка — профиль удаляется, почта больше не используется. Если вериф — аккаунт удаляется. Только если прошла без вопросов — работаем дальше.</div>

<h4>💰 Бюджет</h4>'''
c = c.replace(old_dolphin_budget, add_dolphin_detail)

# 14. Update stats
c = c.replace('<div class="num">26</div><div class="label">Видео</div>', '<div class="num">40+</div><div class="label">Видео</div>')
c = c.replace('<div class="num">13</div><div class="label">Разделов</div>', '<div class="num">14</div><div class="label">Разделов</div>')

# 15. Add Amnezia VPN youtube link reference
old_amnezia = 'https://www.youtube.com/watch?v=CotlyGI4dZE'
# Already present ✓

# 16. Add "прогрев браузера" tip to payment section  
old_pay_tip = 'С крипты дешевле — нет комиссии.'
add_browser_tip = '''С крипты дешевле — нет комиссии.</div>
<div class="alert alert-info"><strong>ℹ️</strong> <strong>Прогрев браузера для оплат:</strong> Сделайте чистый Chrome, с VPN (AdGuard, NY) полдня гуглите новости Нью-Йорка, концерты, куда сходить. Через 1-2 дня отлежите браузер → можете на постоянке оплачивать с препейд карт. В браузер ВСЕГДА только с VPN, всегда NY'''
c = c.replace(old_pay_tip, add_browser_tip)

with open(p, "w", encoding="utf-8") as f:
    f.write(c)

# Count replacements
print("Patch applied!")
print(f"File size: {len(c)} bytes")
