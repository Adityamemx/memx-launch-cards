# MemX — Product Hunt launch cards

Apple-caliber light-theme gallery cards for the MemX Product Hunt launch.
Live preview: **https://adityamemx.github.io/memx-launch-cards/**

- `index.html` — scaled gallery of all 8 cards (self-contained fonts; references the PNG assets)
- `cards/*.png` — full-resolution exports at Product Hunt size (**1270×760**)
- `build.py` — regenerates `index.html` + `cards/*.html` from the shared design system
  (`head_verbatim.html` = embedded Inter fonts + CSS + `#5B9CD8` accent)

## Cards
1. Hook — "Where did I save that?"
2. Self-chat — "Stop texting yourself things you'll never find again" (before→after)
3. Dosage — "You need the dosage, not a scavenger hunt"
4. Client call — "What did the client agree to?"
5. Deadlines — "Deadlines don't send warnings"
6. Ask, don't search — "Go from searching to simply asking" (1.8 hrs / McKinsey)
7. Privacy — "Your memories are yours" (access log)
8. CTA — "Stop remembering. Start asking"

## Regenerate
```bash
python3 build.py
# then render each cards/*.html at 1270×760 (headless Chrome):
for f in cards/*.html; do n=$(basename "$f" .html); \
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1270,760 --screenshot="cards/$n.png" "file://$PWD/$f"; done
```
