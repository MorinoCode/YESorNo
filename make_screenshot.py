import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 800
img = Image.new('RGB', (W, H), (11, 15, 25))
draw = ImageDraw.Draw(img)

# Background subtle gradient effect
for y in range(H):
    ratio = y / H
    r = int(11 + 6 * ratio)
    g = int(15 + 10 * ratio)
    b = int(25 + 18 * ratio)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Subtle grid dots
for x in range(0, W, 40):
    for y in range(0, H, 40):
        draw.point((x, y), fill=(30, 41, 59))

try:
    font_large = ImageFont.truetype('arialbd.ttf', 44)
    font_sub = ImageFont.truetype('arial.ttf', 20)
    font_card_title = ImageFont.truetype('arialbd.ttf', 16)
    font_btn = ImageFont.truetype('arialbd.ttf', 14)
    font_res = ImageFont.truetype('arialbd.ttf', 38)
    font_badge = ImageFont.truetype('arialbd.ttf', 12)
    font_text = ImageFont.truetype('arial.ttf', 13)
except Exception:
    font_large = ImageFont.load_default()
    font_sub = font_large
    font_card_title = font_large
    font_btn = font_large
    font_res = font_large
    font_badge = font_large
    font_text = font_large

# Main Promo Title
title_text = 'YES OR NO'
sub_text = 'Minimalist & Instant Decision Maker for Google Chrome'
feature_pills = ['Instant Verdict', 'Zero Animations', '100% Private (No Permissions)']

# Draw Title
draw.text((W // 2, 80), title_text, fill=(248, 250, 252), font=font_large, anchor='mm')
draw.text((W // 2, 125), sub_text, fill=(148, 163, 184), font=font_sub, anchor='mm')

# Feature tags
pill_start_x = W // 2 - 280
p_x = pill_start_x
for feat in feature_pills:
    bbox = font_badge.getbbox(feat)
    pw = (bbox[2] - bbox[0]) + 24
    ph = 28
    draw.rounded_rectangle([p_x, 155, p_x + pw, 155 + ph], radius=14, fill=(26, 34, 52), outline=(51, 65, 85))
    draw.text((p_x + pw // 2, 169), feat, fill=(203, 213, 225), font=font_badge, anchor='mm')
    p_x += pw + 16

# Draw 2 UI Preview Cards side by side
card_w = 340
card_h = 440
card_y = 230
c1_x = W // 2 - card_w - 30
c2_x = W // 2 + 30

def draw_mock_popup(x, y, is_question=False, is_yes=True, question_str=''):
    draw.rounded_rectangle([x - 2, y - 2, x + card_w + 2, y + card_h + 2], radius=14, fill=(38, 51, 74))
    draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=12, fill=(9, 13, 22))

    # Top header bar
    draw.rounded_rectangle([x + 16, y + 18, x + 54, y + 38], radius=6, fill=(14, 43, 61), outline=(56, 189, 248))
    draw.text((x + 35, y + 28), 'Y/N', fill=(56, 189, 248), font=font_badge, anchor='mm')
    draw.text((x + 64, y + 20), 'YES OR NO', fill=(248, 250, 252), font=font_card_title)

    # Tabs
    tab_y = y + 54
    draw.rounded_rectangle([x + 16, tab_y, x + card_w - 16, tab_y + 34], radius=8, fill=(17, 24, 39), outline=(38, 51, 74))
    if not is_question:
        draw.rounded_rectangle([x + 19, tab_y + 3, x + 166, tab_y + 31], radius=6, fill=(37, 99, 235))
        draw.text((x + 92, tab_y + 17), 'Direct', fill=(255, 255, 255), font=font_badge, anchor='mm')
        draw.text((x + 243, tab_y + 17), 'With Question', fill=(148, 163, 184), font=font_badge, anchor='mm')
    else:
        draw.rounded_rectangle([x + 170, tab_y + 3, x + card_w - 19, tab_y + 31], radius=6, fill=(37, 99, 235))
        draw.text((x + 92, tab_y + 17), 'Direct', fill=(148, 163, 184), font=font_badge, anchor='mm')
        draw.text((x + 243, tab_y + 17), 'With Question', fill=(255, 255, 255), font=font_badge, anchor='mm')

    content_y = tab_y + 48

    if is_question:
        draw.rounded_rectangle([x + 16, content_y, x + card_w - 16, content_y + 54], radius=8, fill=(17, 24, 39), outline=(38, 51, 74))
        draw.text((x + 26, content_y + 12), 'QUESTION', fill=(100, 116, 139), font=font_badge)
        draw.text((x + 26, content_y + 32), question_str, fill=(248, 250, 252), font=font_text)
        content_y += 66

    res_h = 136 if not is_question else 114
    if is_yes:
        border_col = (16, 185, 129)
        text_col = (16, 185, 129)
        val_str = 'YES'
    else:
        border_col = (244, 63, 94)
        text_col = (244, 63, 94)
        val_str = 'NO'

    draw.rounded_rectangle([x + 16, content_y, x + card_w - 16, content_y + res_h], radius=10, fill=(17, 24, 39), outline=border_col, width=2)

    ic_cx = x + card_w // 2
    ic_cy = content_y + (res_h // 2) - 18
    if is_yes:
        draw.line([ic_cx - 16, ic_cy, ic_cx - 4, ic_cy + 12], fill=border_col, width=4)
        draw.line([ic_cx - 4, ic_cy + 12, ic_cx + 16, ic_cy - 10], fill=border_col, width=4)
    else:
        draw.line([ic_cx - 12, ic_cy - 12, ic_cx + 12, ic_cy + 12], fill=border_col, width=4)
        draw.line([ic_cx + 12, ic_cy - 12, ic_cx - 12, ic_cy + 12], fill=border_col, width=4)

    draw.text((ic_cx, ic_cy + 34), val_str, fill=text_col, font=font_res, anchor='mm')

    btn_y = content_y + res_h + 16
    draw.rounded_rectangle([x + 16, btn_y, x + 190, btn_y + 38], radius=8, fill=(37, 99, 235))
    draw.text((x + 103, btn_y + 19), 'Decide Again', fill=(255, 255, 255), font=font_btn, anchor='mm')

    sec_label = 'Reset' if not is_question else 'New Question'
    draw.rounded_rectangle([x + 200, btn_y, x + card_w - 16, btn_y + 38], radius=8, fill=(30, 41, 59), outline=(51, 65, 85))
    draw.text((x + 255, btn_y + 19), sec_label, fill=(148, 163, 184), font=font_btn, anchor='mm')

    draw.line([x + 16, y + card_h - 36, x + card_w - 16, y + card_h - 36], fill=(38, 51, 74))
    draw.text((x + card_w // 2, y + card_h - 18), 'Press Enter to decide', fill=(100, 116, 139), font=font_badge, anchor='mm')

draw_mock_popup(c1_x, card_y, is_question=False, is_yes=True)
draw_mock_popup(c2_x, card_y, is_question=True, is_yes=False, question_str='Should I deploy this to production?')

out_path = os.path.join(os.path.dirname(__file__), 'store_screenshot_1280x800.png')
img.save(out_path, 'PNG')
print(f'Screenshot saved successfully: {out_path} ({os.path.getsize(out_path)} bytes)')
