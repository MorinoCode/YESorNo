# Chrome Web Store Listing Information

Use this guide and copy-paste text directly into the [Chrome Developer Dashboard](https://chrome.google.com/webstore/devconsole).

---

## 1. Store Metadata

* **Name:** `Yes or No - Decision Maker` (27 / 45 chars)
* **Summary (Short Description):**
  > Instant and minimal Yes or No decision maker. Get a fast answer or enter your dilemma to decide.
  *(96 / 132 chars)*
* **Category:** `Productivity` (or `Workflow & Planning`)
* **Language:** `English`
* **Visibility:** `Public` (or `Unlisted`)

---

## 2. Detailed Description

```text
Stuck on a decision? Let Yes or No decide for you in a fraction of a second.

Yes or No is an ultra-minimalist, fast, and distraction-free decision maker for Google Chrome. Whether you need a quick coin-toss answer or want to write down your dilemma before deciding, this extension gives you an authoritative answer instantly.

KEY FEATURES:
• Instant Quick Decide: Just click "Decide" (or hit Enter / Space) to get an immediate, definitive YES or NO.
• Dilemma / Question Mode: Type your question or decision into the input field to see it paired with your verdict.
• Zero Distractions & No Animations: Snappy, instant UI with zero waiting time or bloated transitions.
• Sleek Modern Dark Design: High-contrast typography with clear emerald-green (YES) and rose-red (NO) indicators.
• Complete Privacy: Runs 100% locally on your machine. Does not collect, track, or transmit any user data.
• Zero Permissions: Requires no special browser permissions, camera, storage, or website access.

HOW TO USE:
1. Click the Yes or No icon in your toolbar.
2. Choose "Direct" for an instant decision or "With Question" to type what's on your mind.
3. Click "Decide" (or press Enter).
4. Click "Decide Again" as many times as you like.
```

---

## 3. Privacy Practices (Chrome Web Store Developer Console)

When filling out the **Privacy** tab in the developer console:

* **Single Purpose Description:**
  > "A minimalist utility to help users make quick binary (Yes or No) decisions."
* **Host Permissions:** None
* **Permission Justification:** No permissions are requested or required.
* **Data Usage:**
  * Select: **"I certify that this extension does not collect or transmit user data."**
  * Data collected: **None** (No PII, no browsing activity, no analytics).

---

## 4. Visual Assets Checklist

* **Store Icon:** 128x128 PNG (use `icons/icon128.png`).
* **Screenshots:** At least one screenshot (1280x800 or 640x400 PNG).
* **Zip Package:** Generated using `python package.py` (produces `yes-or-no-v1.0.0.zip`).
