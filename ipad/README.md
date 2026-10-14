# iPad apps

Two single-file web apps. Neither needs a build step or a server of its own.

| App | File | What it does |
| --- | --- | --- |
| Think Aloud Coach | `coach/index.html` | Listens while you explain a coding problem out loud, flags techniques and mistakes as you say them, and asks Claude for a verdict, explanation, pseudocode and Python code. |
| Pocket Ledger | `index.html` | Touch-friendly version of `account.py`, with the `test_account.py` cases run in the page. |

## Running on an iPad

Safari only allows speech recognition on pages served over HTTPS, so host the files rather than opening them from the Files app:

1. In the repo's GitHub settings, open **Pages** and publish from this branch (folder `/`).
2. On the iPad, open `https://<user>.github.io/interview_prep/ipad/coach/` in Safari.
3. Tap **Share → Add to Home Screen** so it opens full screen like an app.
4. The first time you tap **Start listening**, allow the microphone and speech recognition.

## Showing it on a monitor

Connect the iPad with a USB-C to HDMI/DisplayPort cable or adapter (or AirPlay to a TV or Mac).
The screen is mirrored by default. On iPads that support Stage Manager, turn it on in
Control Center to use the monitor as a separate, larger screen. The coach switches to a
three-column layout at widths of 1200px and up; **Large text** makes it readable from further away.

## Claude reviews

- Opened from claude.ai, the coach uses your Claude account. No key is needed.
- Hosted anywhere else, paste an Anthropic API key under **Claude connection**. The key is stored
  only in that browser's local storage. Calls go straight from the iPad to the Anthropic API
  (model `claude-opus-5-5`) and are billed to that key.

The live hints are keyword matches, so they are quick but simple: saying "I won't use nested loops"
still flags nested loops. Claude's review reads the whole transcript and handles context like that.
