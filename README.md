# Yes or No - Decision Maker (Chrome Extension)

A minimal, modern, and instant Yes or No decision maker for Google Chrome (Manifest V3).

## Features
- **Direct Mode:** Instant decision with one click or a hit of the `Space` / `Enter` key.
- **With Question Mode:** Type your dilemma or question into the input field to view it alongside the verdict.
- **No Animations:** Zero transitions or artificial wait times for maximum speed and minimalism.
- **Modern Dark UI:** High contrast dark interface with emerald (YES) and rose (NO) state badges.
- **100% Private:** Operates entirely locally with zero permissions requested.

## Development & Installation
1. Clone or download this repository.
2. Open Google Chrome and navigate to `chrome://extensions`.
3. Enable **Developer mode** toggle in the top-right corner.
4. Click **Load unpacked** and select this directory.

## Packaging for Chrome Web Store
To package the extension for publishing:
```bash
python package.py
```
This generates `yes-or-no-v1.0.0.zip` ready for upload to the [Chrome Developer Dashboard](https://chrome.google.com/webstore/devconsole).
