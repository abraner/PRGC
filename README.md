# PRGC Live Golf Scorecard

Django web app for **Pine Ridge Golf Club** outing scoring: check-in, pairing, live hole-by-hole score entry, leaderboards, and end-of-round handicap/quota updates.

**Live site (typical):** `https://abraner.pythonanywhere.com`  
**Code:** `golf_project/` (Django project + `scorecard` app)  
**Repo:** https://github.com/abraner/PRGC

---

## What it does

| Role | What they use |
|------|----------------|
| **Staff / outing admin** | Control panel to set the game format, check players in, build teams/squads, assign shotgun holes, and watch the leaderboard |
| **Players / captains** | Log in, open a live scorecard, enter scores hole by hole, view the leaderboard |

Supported formats:

1. **18-Hole Individual Gross/Net** — stroke play; net uses player Handicap  
2. **18-Hole Men's League** — net stroke play + skins / closest-to-pin notes; updates Handicap after the round  
3. **18-Hole Individual Chicago Points** — points vs personal quota (`chicago_points_18`)  
4. **9-Hole Team Chicago** — squads; group points vs combined quotas; shotgun start  
5. **9-Hole Women's League** — 9-hole stroke play using Ladies League Handicap  
6. **9-Hole Scramble** — captain enters one team score per hole; leaderboard is one row per squad  

---

## Main screens

| URL | Who | Purpose |
|-----|-----|---------|
| `/login/` | Everyone | Sign in |
| `/admin-dashboard/` | Staff | Outing control panel |
| `/play/` | Players | Live scorecard (auto-routes by format; shotgun start when set) |
| `/leaderboard/` | Everyone | Live standings (use `?format=...` when needed) |
| `/admin-dashboard/all-members/` | Staff | Member list / edit players |
| `/register/` | Public | Register a scoring login (if enabled) |

---

## Admin: run an outing (typical day)

### 1. Open the control panel
1. Log in with a **staff** account.  
2. Go to **`/admin-dashboard/`**.

### 2. Choose the game format
Use **Set Active Game Format** and pick today’s format.  
The dashboard pairing tools change based on scramble / Team Chicago vs individual formats.

### 3. Check players in
1. Mark members as **Playing Today**.  
2. For scramble / Team Chicago: mark **captains** and set **cart / riding partners** if you use auto-pairing.  
3. Adjust handicaps or Chicago quotas on the member/edit screens as needed.

### 4. Build groups (team formats)
**Scramble or Team Chicago:**
1. Choose target team size if prompted.  
2. Use **auto-generate squads** (points-balanced for Team Chicago; scramble pairing from captains/cart links).  
3. Or create / edit a squad **manually**.  
4. Assign each squad a **starting hole** (shotgun).  
5. Dismantle a squad if you need to redo one team.

**Individual formats:** players usually don’t need squads; they score under their own name.

### 5. During play
- Players open **`/play/`** and enter scores.  
- Staff can open the **leaderboard** from the dashboard.  
- Scramble: only the **captain** (or staff) enters the team stroke total; teammates see the card read-only.  
- Scramble scorecard shows a live **To Par** total as scores are chosen.

### 6. End of round (staff, once)
On the leaderboard, staff get an update button (once per round; then it locks):

| Format | Button | Writes to |
|--------|--------|-----------|
| 18-Hole Chicago | Update Next-Round Quotas | `chicago_points_18` |
| 9-Hole Team Chicago | Update Next-Round Quotas | Team Chicago / related quotas |
| Women's League | Update Ladies Handicaps | `ladies_league_handicap` |
| Men's League / 18 Gross-Net | Update Player Handicaps | `handicap` |

Handicap rule used for men’s / 18 individual:  
`new = old + (net − par) × 0.8` (clamped 0–36).

### 7. Reset for the next outing
Use the dashboard **reset / clear round** actions carefully (clears the active round session and check-in flags). Prefer finishing quota/handicap updates first when prompted.

---

## Player: how to score

1. Log in at `/login/` (account must be linked to a **Player** record).  
2. Open **`/play/`**.  
3. Enter **gross strokes** for the hole (dropdown).  
4. Use **Prev / Next** (or **Finish** on the last hole).  
5. Open **Leaderboard** anytime to see standings.

### Format notes for players

- **Chicago (18 or Team 9):** scorecard shows quota / points needed and running points (8 eagle+, 4 birdie, 2 par, 1 bogey).  
- **Scramble:** captain enters one score for the team; card lists captain + teammates and running to-par.  
- **Shotgun:** `/play/` sends you to your squad’s starting hole and walks the 9-hole loop in course order.

---

## Leaderboard basics

- **Individual formats:** one row per player (gross, net/points, to-par or points net).  
- **Team Chicago:** one row per squad; captain labeled; partners listed under; **Points Net +/-** vs group quota.  
- **Scramble:** one row per squad; captain on top; teammates underneath; **team** gross / to-par only (not summed per player).  
- Financial summary card shows entry / pool style totals when the format uses them.  
- Men’s league can show skins winners / closest-to-pin notes when filled in.

---

## Staff tips

- Link each login **User** to a **Player** (member edit / admin) or captains won’t see their scramble roster.  
- Use a staff login to test any squad’s scramble card (`?squad=` picker on the scramble scorecard).  
- After deploying code to PythonAnywhere: `git pull`, then reload the web app. Run `migrate` only when new migrations ship.  
- Secrets (MySQL password, etc.) belong in `golf_project/golf_project/local_settings.py` (not committed). See `local_settings.example.py`.

---

## Local development (optional)

```bash
cd golf_project
# Create local_settings.py from the example and set MySQL + SECRET_KEY
python -m venv ../.venv
# activate venv, then:
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # staff user for admin-dashboard
python manage.py runserver
```

Open `http://127.0.0.1:8000/login/`.

---

## Deploy notes (PythonAnywhere)

1. Code under `~/PRGC4` (git clone of this repo).  
2. `local_settings.py` with PA MySQL host/user/password and DB name.  
3. `ALLOWED_HOSTS` includes `abraner.pythonanywhere.com` (already in project settings).  
4. Web app points at `golf_project` WSGI / virtualenv.  
5. After pull: reload web app; run `python manage.py migrate` when schema changes.

---

## Quick reference — Chicago points

| Score vs par | Points |
|--------------|--------|
| Eagle or better | 8 |
| Birdie | 4 |
| Par | 2 |
| Bogey | 1 |
| Double bogey+ | 0 |

9-hole Team Chicago **points needed** ≈ half of 18-hole Chicago quota, rounded up.
