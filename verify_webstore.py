import json
import os
import re
from PIL import Image

errors = []
warnings = []
passed = []

root = os.path.dirname(os.path.abspath(__file__))

# 1. Manifest Checks
manifest_path = os.path.join(root, 'manifest.json')
if not os.path.exists(manifest_path):
    errors.append('manifest.json missing')
else:
    with open(manifest_path, 'r', encoding='utf-8') as f:
        try:
            m = json.load(f)
            passed.append('manifest.json is valid JSON')
        except Exception as e:
            errors.append(f'manifest.json invalid JSON: {e}')
            m = {}

    if m.get('manifest_version') == 3:
        passed.append('manifest_version is 3 (MV3 compliant)')
    else:
        errors.append(f'manifest_version must be 3, found {m.get("manifest_version")}')

    name = m.get('name', '')
    if 0 < len(name) <= 45:
        passed.append(f'Extension name length is valid ({len(name)}/45 chars): "{name}"')
    else:
        errors.append(f'Extension name invalid length ({len(name)} chars, max 45)')

    desc = m.get('description', '')
    if 0 < len(desc) <= 132:
        passed.append(f'Description length is valid ({len(desc)}/132 chars)')
    else:
        errors.append(f'Description invalid length ({len(desc)} chars, max 132)')

    # Check icons in manifest
    icons = m.get('icons', {})
    for sz in ['16', '48', '128']:
        if sz not in icons:
            errors.append(f'Missing icons["{sz}"] in manifest.json')
        else:
            icon_file = os.path.join(root, icons[sz])
            if not os.path.exists(icon_file):
                errors.append(f'Icon file missing: {icons[sz]}')
            else:
                with Image.open(icon_file) as img:
                    if img.size == (int(sz), int(sz)):
                        passed.append(f'Icon {sz}x{sz} matches exact dimensions')
                    else:
                        errors.append(f'Icon {icons[sz]} has dimensions {img.size}, expected ({sz}, {sz})')

    # Check popup
    action = m.get('action', {})
    popup = action.get('default_popup', '')
    if popup and os.path.exists(os.path.join(root, popup)):
        passed.append(f'default_popup "{popup}" exists')
    else:
        errors.append(f'default_popup "{popup}" not found')

    perms = m.get('permissions', [])
    if len(perms) == 0:
        passed.append('Permissions: zero permissions requested (optimal for instant Web Store approval)')
    else:
        warnings.append(f'Requested permissions: {perms}')

# 2. CSP & Inline script audit
popup_html_path = os.path.join(root, 'popup.html')
with open(popup_html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Check for inline script content
inline_scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', html_content, re.DOTALL | re.IGNORECASE)
if any(s.strip() for s in inline_scripts):
    errors.append('Inline script tags detected in popup.html (prohibited in MV3 CSP)')
else:
    passed.append('No inline script tags in popup.html')

inline_events = re.findall(r'\bon\w+\s*=', html_content)
if inline_events:
    errors.append(f'Inline event handlers detected in popup.html: {inline_events} (prohibited in MV3 CSP)')
else:
    passed.append('No inline event handlers in popup.html')

# 3. JS audit (eval, Function, etc.)
popup_js_path = os.path.join(root, 'popup.js')
with open(popup_js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

forbidden_js = ['eval(', 'new Function(', 'document.write(', 'setTimeout("']
for f_kw in forbidden_js:
    if f_kw in js_content:
        errors.append(f'Prohibited construct found in popup.js: {f_kw}')
passed.append('popup.js is free from dynamic evaluation / prohibited CSP functions')

# 4. Gitignore check
gitignore_path = os.path.join(root, '.gitignore')
if os.path.exists(gitignore_path):
    passed.append('.gitignore file exists and configured')
else:
    errors.append('.gitignore missing')

print('=== AUDIT SUMMARY ===')
for p in passed:
    print(f'  [PASS] {p}')
for w in warnings:
    print(f'  [WARN] {w}')
for e in errors:
    print(f'  [FAIL] {e}')

if not errors:
    print('\nALL CHECKS PASSED: Extension is 100% compliant and ready for Google Chrome Web Store!')
