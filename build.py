#!/usr/bin/env python3
# MemX PH launch cards: hosted DESIGN + v1 (Downloads) STORIES.
# Reuses head_verbatim.html (embedded Inter fonts + full CSS + #5B9CD8 accent)
# so rendering is pixel-identical to the original hosted deck. Adds a few components.
# Regenerate:  python3 build.py   then render each cards/*.html at 1270x760.
import os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
HEAD = open(os.path.join(HERE, "head_verbatim.html")).read()
LOGO = "logo.png"; PHONE = "phone_hero.png"; TILT = "phone_tilted.png"

def wave(heights):
    return "".join(f'<span style="height:{h}%"></span>' for h in heights)

EXTRA_CSS = """
<style>
/* ===== render-mode: native full-size export ===== */
body.render { padding:0; margin:0; background:#fff; }
body.render .exportframe { width:1270px; height:760px; overflow:hidden; }
body.render .exportframe > .stage { transform:none !important; width:1270px; height:760px; }

/* ===== doc-flow (card 3): tighten so top wordmark never clips ===== */
.docflowstage { justify-content:center; }
.docflowstage .dfcopy { margin-bottom:26px; }
.docflowstage .headline.dfhead { font-size:42px; margin-bottom:13px; }
.docflowstage .sub.dfsub { font-size:19px; }

/* ===== before -> after two-panel (self-chat, ask-dont-search) ===== */
.baflow { flex-direction:column; justify-content:center; }
.bacopy { position:relative; z-index:2; text-align:center; display:flex; flex-direction:column;
  align-items:center; margin-bottom:26px; }
.headline.bahead { font-size:41px; margin-bottom:13px; }
.sub.basub { max-width:660px; font-size:19px; }
.bapanels .mscreen { padding:22px 26px 24px; }
.statpill { display:inline-flex; align-items:baseline; gap:12px; margin-top:14px;
  background:#fff; border-radius:16px; padding:11px 19px;
  box-shadow:0 18px 40px -20px rgba(20,25,45,0.30), 0 0 0 1px rgba(20,25,45,0.06); }
.statpill .snum { font-size:30px; font-weight:700; color:#1D6FE6; letter-spacing:-0.02em; line-height:1; }
.statpill .stxt { font-size:15px; color:#6E6E73; line-height:1.35; text-align:left; max-width:330px; }
.statpill .stxt b { color:#3a3f49; font-weight:600; }
.bapanels { position:relative; z-index:2; display:flex; align-items:center; justify-content:center;
  gap:24px; width:100%; padding:0 60px; }
.bapanel { flex:0 0 452px; }
.baarrow { flex:0 0 auto; font-size:40px; color:#b9c4d2; font-weight:300; line-height:1; }
.panelcap { text-align:center; font-size:13.5px; color:#8f95a0; margin-top:14px; }
.panelcap.good { color:#12a594; font-weight:600; }
.selfnote { align-self:flex-end; max-width:88%; background:#e9edf2; color:#3a3f49; border-radius:15px;
  border-bottom-right-radius:6px; padding:11px 14px; font-size:15px; line-height:1.32; margin-bottom:9px; }
.selfnote.imp { box-shadow:inset 0 0 0 1.5px rgba(231,120,90,0.55); }
.selfnote .fade { color:#9aa2ad; }
.selffrom { align-self:flex-start; font-size:13px; color:#7f8794; margin-bottom:14px; }
.msrchbox { display:flex; align-items:center; gap:10px; background:#181c24; border-radius:13px;
  padding:13px 15px; margin-bottom:16px; box-shadow:inset 0 0 0 1px rgba(255,255,255,0.06); }
.msrchbox .mag { width:17px; height:17px; flex:0 0 auto; opacity:0.6; }
.msrchbox .q { font-size:16px; color:#e8ecf4; }
.msrchbox .cur { width:2px; height:18px; background:#5B9CD8; display:inline-block; margin-left:1px; }
.mfile { display:flex; align-items:center; gap:11px; padding:11px 6px; border-bottom:1px solid rgba(255,255,255,0.06); }
.mfile:last-child { border-bottom:none; }
.mfic { width:26px; height:26px; border-radius:7px; background:#232a36; flex:0 0 auto; }
.mfnm { font-size:14.5px; color:#8b93a1; }
/* live recording (client-call) */
.rec-hd { display:flex; align-items:center; gap:11px; margin-bottom:6px; }
.rec-dot { width:12px; height:12px; border-radius:50%; background:#e0483e; box-shadow:0 0 0 5px rgba(224,72,62,0.18); flex:0 0 auto; }
.rec-lbl { font-size:15px; font-weight:600; color:#eef1f6; }
.rec-time { margin-left:auto; font-size:26px; font-weight:600; color:#eef1f6; font-variant-numeric:tabular-nums; letter-spacing:-0.01em; }
.rec-sub { font-size:13px; color:#8f95a0; margin-bottom:18px; }
.recwave { display:flex; align-items:center; gap:3px; height:52px; margin:4px 0 20px; }
.recwave span { flex:1; min-width:2.5px; background:#e0483e; border-radius:2px; opacity:0.9; }
.rec-tx { border-top:1px solid rgba(255,255,255,0.07); padding-top:16px; }
.rec-tx .tline { font-size:15.5px; line-height:1.45; color:#c7cdd6; margin-bottom:8px; }
.rec-tx .tline .sp { color:#5B9CD8; font-weight:600; }
.rec-tx .tline.live { color:#eef1f6; }
.rec-tx .tline.live::after { content:"▍"; color:#5B9CD8; margin-left:2px; }
.rec-chips { display:flex; gap:8px; margin-top:16px; flex-wrap:wrap; }
.rec-chip { font-size:12.5px; font-weight:600; color:#5B9CD8; background:rgba(91,156,216,0.15);
  padding:6px 12px; border-radius:999px; }
/* access log (privacy) */
.aclog { display:flex; flex-direction:column; }
.acrow { display:flex; align-items:center; gap:13px; padding:15px 4px; border-bottom:1px solid rgba(255,255,255,0.07); }
.acrow:last-child { border-bottom:none; }
.aclock { width:34px; height:34px; border-radius:10px; background:rgba(18,165,148,0.14);
  display:flex; align-items:center; justify-content:center; flex:0 0 auto; }
.aclock svg { width:17px; height:17px; }
.acmid { flex:1; }
.actitle { font-size:16px; font-weight:500; color:#eef1f6; }
.acsub { font-size:13px; color:#8f95a0; margin-top:3px; }
.acok { flex:0 0 auto; color:#12c8ad; font-size:19px; font-weight:700; }
.acfoot { display:flex; align-items:center; gap:9px; margin-top:18px; font-size:13.5px; color:#8f95a0; }
.acfoot .k { color:#5B9CD8; }
/* CTA (download) */
.ctamedia { flex:0 0 auto; width:560px; display:flex; align-items:center; justify-content:center;
  position:relative; z-index:2; }
.ctaphone { height:620px; width:auto; display:block; }
.badges { display:flex; gap:10px; margin-top:30px; flex-wrap:wrap; }
.badge { display:inline-flex; align-items:center; gap:8px; font-size:15px; font-weight:600; color:#1D1D1F;
  background:#fff; padding:10px 16px; border-radius:12px;
  box-shadow:0 8px 20px -12px rgba(20,25,45,0.28), 0 0 0 1px rgba(20,25,45,0.06); }
.badge svg { width:18px; height:18px; }
.badge.wa { color:#128C4B; }
</style>
"""

LOCK_SVG = '<svg viewBox="0 0 24 24" fill="none"><rect x="4" y="10" width="16" height="11" rx="2.5" fill="#12a594"/><path d="M8 10V7a4 4 0 0 1 8 0v3" stroke="#12a594" stroke-width="2" fill="none"/></svg>'
MAG_SVG = '<svg class="mag" viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="#8b93a1" stroke-width="2"/><line x1="16.5" y1="16.5" x2="21" y2="21" stroke="#8b93a1" stroke-width="2" stroke-linecap="round"/></svg>'
DROID = '<svg viewBox="0 0 24 24" fill="#3DDC84"><path d="M6 18a1 1 0 0 0 1 1h1v3a1.2 1.2 0 0 0 2.4 0v-3h3.2v3a1.2 1.2 0 0 0 2.4 0v-3h1a1 1 0 0 0 1-1V9H6v9zM3.3 9a1.2 1.2 0 0 0-1.2 1.2v5.6a1.2 1.2 0 0 0 2.4 0v-5.6A1.2 1.2 0 0 0 3.3 9zm17.4 0a1.2 1.2 0 0 0-1.2 1.2v5.6a1.2 1.2 0 0 0 2.4 0v-5.6A1.2 1.2 0 0 0 20.7 9zM15.5 3.6l1.1-2a.3.3 0 0 0-.5-.3l-1.2 2.1a6.9 6.9 0 0 0-5.8 0L7.9 1.3a.3.3 0 0 0-.5.3l1.1 2A6.3 6.3 0 0 0 6 8h12a6.3 6.3 0 0 0-2.5-4.4zM9.5 6.2a.7.7 0 1 1 0-1.4.7.7 0 0 1 0 1.4zm5 0a.7.7 0 1 1 0-1.4.7.7 0 0 1 0 1.4z"/></svg>'
APPLE = '<svg viewBox="0 0 24 24" fill="#1D1D1F"><path d="M16.4 12.6c0-2.3 1.9-3.4 2-3.5-1.1-1.6-2.8-1.8-3.4-1.9-1.4-.1-2.8.9-3.5.9-.7 0-1.9-.8-3-.8-1.6 0-3 .9-3.8 2.3-1.6 2.8-.4 6.9 1.2 9.2.8 1.1 1.7 2.3 2.9 2.3 1.2 0 1.6-.7 3-.7 1.4 0 1.8.7 3 .7 1.2 0 2-1.1 2.7-2.2.9-1.3 1.2-2.5 1.3-2.6-.1 0-2.5-1-2.5-3.9zM14.1 5.3c.6-.8 1.1-1.9.9-3-1 0-2.1.7-2.8 1.5-.6.7-1.1 1.8-1 2.8 1.1.1 2.2-.6 2.9-1.3z"/></svg>'
WA = '<svg viewBox="0 0 24 24" fill="#128C4B"><path d="M12 2a10 10 0 0 0-8.5 15.2L2 22l4.9-1.4A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .1-1.7-.1-.4-.1-.9-.3-1.5-.6-2.7-1.2-4.4-3.9-4.6-4.1-.1-.2-1-1.3-1-2.6 0-1.2.6-1.8.9-2.1.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5.2.5.7 1.7.7 1.8.1.1.1.3 0 .4l-.3.5c-.1.2-.3.3-.1.6.1.3.6 1.1 1.4 1.7 1 .8 1.7 1.1 2 1.2.2.1.4.1.5-.1.1-.2.6-.7.8-.9.1-.2.3-.2.5-.1.2.1 1.4.7 1.6.8.2.1.4.2.4.3.1.1.1.6-.1 1.1z"/></svg>'

def wordmark():
    return f'<div class="wordmark"><img class="logo" src="{LOGO}" alt="MemX logo"><span class="wm-text">MemX</span></div>'

def copy_block(chip, headline, sub):
    return f'''<div class="copy">
      {wordmark()}
      <span class="chip"><span class="dot"></span>{chip}</span>
      <div class="headline">{headline}</div>
      <div class="sub">{sub}</div>
    </div>'''

CARDS = []

# 1. HOOK
CARDS.append(("01_hook", f'''<div class="stage rev">
    <div class="phone"><div class="device"><div class="screen"><img src="{PHONE}" alt=""></div></div></div>
    {copy_block("Meet MemX",
      "Where did I<br><span class='hl'>save that?</span>",
      "A warranty. A deadline. The thing the client said. It's buried in a PDF, note, screenshot or chat. <b>Stop scrolling — just ask</b>, and MemX hands it back the second you need it.")}
  </div>'''))

# 2. SELF-CHAT before -> after
left_self = f'''<div class="snap bapanel"><div class="mscreen">
        <div class="selffrom">You (yourself)</div>
        <div class="mchat">
          <div class="selfnote imp">landlord no. 555-0182 &nbsp;IMP!!</div>
          <div class="selfnote">lease_final_v3_FINAL.pdf</div>
          <div class="selfnote">wifi pwd = <span class="fade">gx77#Km2</span></div>
          <div class="selfnote">[photo of a receipt]</div>
          <div class="selfnote imp">remember to renew passport!!</div>
        </div>
        <div class="panelcap">Buried under 400 messages by Tuesday.</div>
      </div></div>'''
right_self = f'''<div class="snap bapanel"><div class="mscreen">
        <div class="mtop"><img class="mlogo" src="{LOGO}"><span>MemX</span></div>
        <div class="mchat">
          <div class="bout">What's the landlord's number?<span class="btime">now</span></div>
          <div class="bmemx">MemX</div>
          <div class="bans"><span class="bacc">555-0182</span> — saved with your lease note on 14 Jan.</div>
          <div class="bfrom"><span class="bfrom-ic">&#9635;</span>from <b>lease note · 14 Jan</b></div>
        </div>
        <div class="panelcap good">Saved once. Found forever.</div>
      </div></div>'''
CARDS.append(("02_self_chat", f'''<div class="stage baflow">
    <div class="bacopy">
      {wordmark()}
      <span class="chip"><span class="dot"></span>Why MemX</span>
      <div class="headline bahead">Stop texting yourself things<br>you'll <span class='hl'>never find</span> again.</div>
      <div class="sub basub">Your notes live in a dozen chats with yourself. MemX is the one private place that holds it all — and finds it in seconds.</div>
    </div>
    <div class="bapanels">
      {left_self}
      <div class="baarrow">&rarr;</div>
      {right_self}
    </div>
  </div>'''))

# 3. PARENT / DOSAGE
CARDS.append(("03_dosage", f'''<div class="stage brand docflowstage">
    <div class="dfcopy">
      {wordmark()}
      <span class="chip"><span class="dot"></span>For the 2am moments</span>
      <div class="headline dfhead">You need the dosage,<br>not a <span class='hl'>scavenger hunt</span>.</div>
      <div class="sub dfsub">The record's a photo, the dose is in an email. Snap it once — MemX keeps every detail one question away.</div>
    </div>
    <div class="dfflow">
      <div class="dfdoc">
        <div class="dfpaper">
          <div class="dfletter">
            <div class="dfclinic"><span class="dfcross">&#10010;</span>CityCare Pediatrics</div>
            <div class="dfclinic-sub">Dr. R. Menon, MD &middot; Child Health</div>
          </div>
          <div class="dfrule"></div>
          <div class="dfpat"><span>Patient: <b>Aarav (age 4)</b></span><span>12 Oct 2026</span></div>
          <div class="dfrx-body">
            <span class="dfrx">&#8478;</span>
            <div class="dfrx-lines">
              <div class="dfline hlx">Paracetamol 5&nbsp;ml — every 6 hrs if fever<span class="dfmark">found</span></div>
              <div class="dfline">Plenty of fluids, rest</div>
              <div class="dfline hlx">Flu vaccine — 2nd dose 30 Oct<span class="dfmark">found</span></div>
            </div>
          </div>
          <div class="dfsign">
            <svg width="132" height="38" viewBox="0 0 132 38" fill="none"><path d="M4 27 C 16 7, 26 7, 29 23 S 42 33, 51 17 66 8, 77 25 90 31, 110 12 122 7, 128 21" stroke="#2b3a55" stroke-width="2.3" stroke-linecap="round"/></svg>
            <div class="dfsign-name">Dr. R. Menon</div>
          </div>
        </div>
      </div>
      <div class="dfarrow">
        <div class="dfai"><img src="{LOGO}" alt="">MemX reads it</div>
        <div class="dfarr">&rarr;</div>
      </div>
      <div class="dfrem">
        <div class="dfrem-hd"><img class="logo" src="{LOGO}" alt="">Up&nbsp;next<span class="mauto">&#10022; auto</span></div>
        <div class="mrow"><span class="mbar bar-a"></span><div class="mrmid"><div class="mrtitle">Paracetamol 5ml</div><div class="mrsrc">if fever · every 6 hrs</div></div><div class="mrtime">now</div></div>
        <div class="mrow"><span class="mbar bar-b"></span><div class="mrmid"><div class="mrtitle">Flu vaccine — 2nd dose</div><div class="mrsrc">from prescription</div></div><div class="mrtime">30 Oct</div></div>
      </div>
    </div>
  </div>'''))

# 4. CLIENT-CALL live recording
CARDS.append(("04_client_call", f'''<div class="stage rev">
    <div class="snapwrap"><div class="snap"><div class="mscreen">
      <div class="rec-hd"><span class="rec-dot"></span><span class="rec-lbl">Recording</span><span class="rec-time">41:07</span></div>
      <div class="rec-sub">Live transcript · auto-detecting language</div>
      <div class="recwave">{wave([30,55,72,40,86,52,64,34,78,48,90,44,60,36,82,50,70,38,58,74,42,66,32,80,54,68,46,62,36,76])}</div>
      <div class="rec-tx">
        <div class="tline"><span class="sp">Client:</span> …so we can push the launch to the 14th, but the pricing stays.</div>
        <div class="tline live"><span class="sp">You:</span> Got it — I'll send the revised deck by Friday</div>
      </div>
      <div class="rec-chips"><span class="rec-chip">✓ Notes ready</span><span class="rec-chip">✓ Action items</span><span class="rec-chip">100+ languages</span></div>
    </div></div></div>
    {copy_block("After the call",
      "What did the client<br><span class='hl'>agree to?</span>",
      "MemX follows the whole call in 100+ languages and hands you <b>polished notes and action items</b> — talk freely, the note-taking is covered.")}
  </div>'''))

# 5. SMART REMINDERS (deadlines)
CARDS.append(("05_reminders", f'''<div class="stage rev">
    <div class="snapwrap"><div class="snap"><div class="mscreen">
      <div class="mtop"><img class="mlogo" src="{LOGO}"><span>Up next</span><span class="mauto">&#10022; auto</span></div>
      <div class="mrlist">
        <div class="mrow"><span class="mbar bar-a"></span><div class="mrmid"><div class="mrtitle">Pay Pacific Power bill</div><div class="mrsrc">from bill · due in 2 days</div></div><div class="mrtime">Thu</div></div>
        <div class="mrow"><span class="mbar bar-b"></span><div class="mrmid"><div class="mrtitle">Renew rental agreement</div><div class="mrsrc">auto-renews unless cancelled</div></div><div class="mrtime">31 Oct</div></div>
        <div class="mrow"><span class="mbar bar-c"></span><div class="mrmid"><div class="mrtitle">Amy's vaccination — 2nd dose</div><div class="mrsrc">from prescription</div></div><div class="mrtime">6 Nov</div></div>
      </div>
    </div></div></div>
    {copy_block("Smart reminders",
      "Deadlines don't<br>send <span class='hl'>warnings</span>.",
      "MemX reads the details you save and sets the reminder on its own — a bill, a renewal, a vaccination — then nudges you <b>before</b> it's due.")}
  </div>'''))

# 6. ASK, DON'T SEARCH
left_search = f'''<div class="snap bapanel"><div class="mscreen">
        <div class="msrchbox">{MAG_SVG}<span class="q">Samsung receipt</span><span class="cur"></span></div>
        <div class="mfile"><span class="mfic"></span><span class="mfnm">IMG_4382.HEIC</span></div>
        <div class="mfile"><span class="mfic"></span><span class="mfnm">scan_03.pdf</span></div>
        <div class="panelcap">Not what I'm looking for.</div>
      </div></div>'''
right_search = f'''<div class="snap bapanel"><div class="mscreen">
        <div class="mchat">
          <div class="bout">My Samsung TV is acting weird. Can you find the receipt and who to call?<span class="btime">now</span></div>
          <div class="bmemx">MemX</div>
          <div class="bans">Bought at <span class="bacc">Costco</span>, 25 Nov 2025 — under <b>1-yr warranty</b>. Call <span class="bacc">1-800-222-3333</span>.</div>
          <div class="bfrom"><span class="bfrom-ic">&#9635;</span>from <b>TV receipt · 25 Nov 2025</b></div>
        </div>
        <div class="panelcap good">Answered in 2s · Encrypted · access audited</div>
      </div></div>'''
CARDS.append(("06_ask_dont_search", f'''<div class="stage baflow">
    <div class="bacopy">
      {wordmark()}
      <span class="chip"><span class="dot"></span>Ask, don't dig</span>
      <div class="headline bahead">Go from searching<br>to simply <span class='hl'>asking</span>.</div>
      <div class="sub basub">MemX reads the text inside everything you save — one question replaces twenty minutes of scrolling.</div>
      <div class="statpill"><span class="snum">1.8 hrs</span><span class="stxt">a day is what knowledge workers spend just <b>searching for information</b>. &mdash; McKinsey</span></div>
    </div>
    <div class="bapanels">
      {left_search}
      <div class="baarrow">&rarr;</div>
      {right_search}
    </div>
  </div>'''))

# 7. PRIVACY
def acrow(title, sub):
    return f'''<div class="acrow"><span class="aclock">{LOCK_SVG}</span><div class="acmid"><div class="actitle">{title}</div><div class="acsub">{sub}</div></div><span class="acok">&#10003;</span></div>'''
CARDS.append(("07_privacy", f'''<div class="stage rev">
    <div class="snapwrap"><div class="snap"><div class="mscreen">
      <div class="mtop"><img class="mlogo" src="{LOGO}"><span>Access log</span><span class="mcount">only you</span></div>
      <div class="aclog">
        {acrow("Decrypted to answer you", "&ldquo;Samsung warranty?&rdquo; · today 9:41")}
        {acrow("Re-encrypted after answer", "held in the clear for 0.4s")}
        {acrow("New login — this device", "Pixel 8 · Bengaluru")}
      </div>
      <div class="acfoot"><span class="k">&#128274;</span>Encrypted at rest · every access is yours to see</div>
    </div></div></div>
    {copy_block("Private by design",
      "Your memories<br>are <span class='hl'>yours</span>.",
      "Encrypted at rest, decrypted only for the instant the AI answers you — and <b>every single access is logged</b> where you can see it.")}
  </div>'''))

# 8. DOWNLOAD CTA -- tilted phone (hosted image), badges, NO QR
CARDS.append(("08_cta", f'''<div class="stage">
    <div class="ctamedia">
      <img class="ctaphone" src="{TILT}" alt="MemX app">
    </div>
    <div class="copy">
      {wordmark()}
      <span class="chip"><span class="dot"></span>Free to start</span>
      <div class="headline">Stop remembering.<br>Start <span class='hl'>asking</span>.</div>
      <div class="sub">Voice notes, photos, docs &amp; deadlines — captured in seconds, recalled the moment you ask.</div>
      <div class="badges">
        <span class="badge">{DROID}Android</span>
        <span class="badge">{APPLE}iOS</span>
        <span class="badge wa">{WA}WhatsApp</span>
      </div>
    </div>
  </div>'''))

# ---------------- WRITE FILES ----------------
os.makedirs(os.path.join(HERE, "cards"), exist_ok=True)
for a in (LOGO, PHONE, TILT):
    src = os.path.join(HERE, a)
    if os.path.exists(src):
        shutil.copy(src, os.path.join(HERE, "cards", a))

labels = {
 "01_hook":"Card 1 · Hook","02_self_chat":"Card 2 · Self-chat (before→after)",
 "03_dosage":"Card 3 · Dosage / 2am","04_client_call":"Card 4 · Client call",
 "05_reminders":"Card 5 · Deadlines","06_ask_dont_search":"Card 6 · Ask, don't search",
 "07_privacy":"Card 7 · Privacy","08_cta":"Card 8 · Download CTA"}

for name, stage in CARDS:
    doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{HEAD}{EXTRA_CSS}</head>
<body class="render"><div class="exportframe">{stage}</div></body></html>"""
    open(os.path.join(HERE, "cards", f"{name}.html"), "w").write(doc)

frames = []
for name, stage in CARDS:
    frames.append(f'<div class="cardlabel">{labels[name]}</div>\n<div class="frame">{stage}</div>')
preview = f"""<!DOCTYPE html><html><head><meta charset="utf-8">{HEAD}{EXTRA_CSS}</head>
<body>
<div class="pagehead"><h1>MemX — Product Hunt gallery cards</h1>
<p>Apple-caliber light design carrying the launch stories. Product Hunt size (<code>1270×760</code>), shown scaled. Full-res exports in <code>cards/*.png</code>.</p></div>
{''.join(frames)}
</body></html>"""
open(os.path.join(HERE, "index.html"), "w").write(preview)
print("Built", len(CARDS), "cards + index.html")
