#!/usr/bin/env python3
"""Writes the static pages of sherin.dev from the app list below.

The output (site/index.html, site/404.html and one folder per app) is committed, so deploying needs no build step.
Run it after changing an app:  python3 scripts/build.py
"""

import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
GITHUB = "https://github.com/SherinBloemendaal"
YEAR = 2026


def release(repo: str, name: str) -> str:
    return f"https://github.com/{repo}/releases/latest/download/{name}"


APPS = [
    {
        "slug": "tagwell",
        "name": "Tagwell",
        "kind": "MP3 tag editor",
        "where": "macOS",
        "repo": "SherinBloemendaal/tagwell",
        "title": "Tagwell: MP3 tags, nothing else.",
        "lead": "A small, native Mac app for editing the tags of one MP3 or hundreds at once. "
        "It writes only the fields you change; the audio and the rest of the tag stay exactly as they were.",
        "primary": ("Download for Mac", release("SherinBloemendaal/tagwell", "Tagwell.dmg")),
        "install": "tagwell",
        "art": "tagwell-how-it-works",
        "art_alt": "What a save touches: changed fields are rewritten, the rest of the tag is kept byte for byte, "
        "the audio is never touched, and an ID3v1 tag is kept in sync",
        "points": [
            ("Only what you changed is written.", "MusicBrainz IDs, iTunes data, lyrics and ratings stay byte for byte, and the tag keeps its ID3 version."),
            ("Bulk edit.", "Select a hundred files and set the artist, album, year or cover art once. Number tracks or turn file names into titles in one click."),
            ("Artist folders.", "Drag files onto an artist in the sidebar to set their artist. Saved artists come back as suggestions, so a name is spelled the same everywhere."),
            ("Cover art from YouTube.", "Search for the track and pick a thumbnail, or let Tagwell find the video in a yt-dlp file name. Cropped to a square by default."),
            ("Rename on save, if you want.", "Files can take the name Artist - Title. An existing file is never overwritten."),
            ("Safe saves.", "Files are written in the background with a progress window, next to the original and swapped in, so a failed save never leaves a broken MP3."),
        ],
        "downloads": [
            ("Mac, Apple Silicon and Intel", "Tagwell.dmg", release("SherinBloemendaal/tagwell", "Tagwell.dmg")),
            ("The app on its own", "Tagwell.zip", release("SherinBloemendaal/tagwell", "Tagwell.zip")),
            ("Checksums", "SHA256SUMS", release("SherinBloemendaal/tagwell", "SHA256SUMS")),
        ],
        "facts": [
            ("Needs", "macOS 15 or later"),
            ("Runs on", "Apple Silicon and Intel"),
            ("Written in", "Swift and SwiftUI"),
            ("Licence", "MIT"),
        ],
    },
    {
        "slug": "moire",
        "name": "Moire",
        "kind": "Compare text, files and folders",
        "where": "macOS",
        "repo": "SherinBloemendaal/moire",
        "title": "Moire shows what changed.",
        "lead": "A native Mac app for comparing text, files and folders. Lines line up across both sides, "
        "and the exact words that changed are marked.",
        "primary": ("Download for Mac", release("SherinBloemendaal/moire", "Moire.dmg")),
        "install": "moire",
        "art": "moire-preview",
        "art_alt": "Moire comparing two versions of a Swift file side by side, with the changed words marked",
        "points": [
            ("Side by side or unified.", "Changed lines sit next to their new version, with the changed words marked."),
            ("Copy changes across.", "Take a change from either side; saving keeps the file's own encoding and line endings."),
            ("Jump between changes", "with the keyboard, or click a mark in the change map beside the scroll bar."),
            ("Paste or type.", "No files needed: paste two snippets and the comparison updates as you type."),
            ("Compare folders.", "Every file in both folders is compared by its contents; double-click one to see what changed."),
            ("Fast on big files.", "Myers' algorithm in linear space, the idea behind git diff, off the main thread."),
        ],
        "downloads": [
            ("Mac, Apple Silicon and Intel", "Moire.dmg", release("SherinBloemendaal/moire", "Moire.dmg")),
            ("The app on its own", "Moire.zip", release("SherinBloemendaal/moire", "Moire.zip")),
            ("Checksums", "SHA256SUMS", release("SherinBloemendaal/moire", "SHA256SUMS")),
        ],
        "facts": [
            ("Needs", "macOS 15 or later"),
            ("Runs on", "Apple Silicon and Intel"),
            ("Written in", "Swift and SwiftUI"),
            ("Licence", "MIT"),
        ],
    },
    {
        "slug": "varve",
        "name": "Varve",
        "kind": "Database manager",
        "where": "macOS, Windows, Linux",
        "repo": "getvarve/varve",
        "site": "https://varve.app",
        "title": "Varve: calm database work.",
        "lead": "One desktop app for PostgreSQL, MySQL, MariaDB and Redis, careful around production: "
        "environment tags, read-only connections and a plan to review before every change.",
        "primary": ("See the downloads", "#downloads"),
        "install": "varve",
        "art": "varve-banner",
        "art_alt": "Varve: a calm desktop manager for PostgreSQL, MySQL, MariaDB and Redis",
        "points": [
            ("Every engine, fully.", "Materialized views, partitions, events, system-versioned tables and Redis streams, each in its own place."),
            ("Safe around production.", "Environment tags, read-only connections, a plan before every structure change and a confirmation before destructive statements."),
            ("Quiet by design.", "A dense, calm interface where colour only means something: production is red, and nothing else is."),
            ("Secrets stay local.", "Passwords and SSH passphrases live in your system keychain; your queries only travel to your own servers."),
            ("Fast where it counts.", "A Rust core with native drivers, cancellable queries and a grid that stays smooth on large results."),
        ],
        "downloads": [
            ("Mac, Apple Silicon", "varve-macos-arm64.dmg", release("getvarve/varve", "varve-macos-arm64.dmg")),
            ("Mac, Intel", "varve-macos-x64.dmg", release("getvarve/varve", "varve-macos-x64.dmg")),
            ("Windows installer", "varve-windows-x64-setup.exe", release("getvarve/varve", "varve-windows-x64-setup.exe")),
            ("Windows, for administrators", "varve-windows-x64.msi", release("getvarve/varve", "varve-windows-x64.msi")),
            ("Linux x64, AppImage", "varve-linux-x64.AppImage", release("getvarve/varve", "varve-linux-x64.AppImage")),
            ("Linux x64, Debian and Ubuntu", "varve-linux-x64.deb", release("getvarve/varve", "varve-linux-x64.deb")),
            ("Linux arm64, AppImage", "varve-linux-arm64.AppImage", release("getvarve/varve", "varve-linux-arm64.AppImage")),
            ("Linux arm64, Debian and Ubuntu", "varve-linux-arm64.deb", release("getvarve/varve", "varve-linux-arm64.deb")),
        ],
        "facts": [
            ("Runs on", "macOS, Windows and Linux"),
            ("Linux needs", "glibc 2.35 or newer (Ubuntu 22.04, Debian 12, Fedora 36)"),
            ("Written in", "Rust, with a Vue interface"),
            ("Licence", "Apache-2.0 for Varve Community"),
        ],
    },
    {
        "slug": "chatkeep",
        "name": "Chatkeep",
        "kind": "Keeps AI chats with moved projects",
        "where": "Command line",
        "repo": "SherinBloemendaal/chatkeep",
        "title": "Chatkeep: your chats move along.",
        "lead": "A command-line tool for Cursor and Claude Code. Move or rename a project folder, "
        "and its chat history comes along to the new place.",
        "primary": ("Install", "#install"),
        "install": "chatkeep",
        "art": "chatkeep-how-it-works",
        "art_alt": "chatkeep mv rewrites the local references of Cursor and Claude Code so chats follow a moved folder",
        "points": [
            ("Chats follow the folder.", "chatkeep mv rewrites the local references, so the history reattaches at the new path."),
            ("One command, both tools.", "List, move, copy, split, combine, export and import chats for Cursor and Claude Code alike."),
            ("Safe writes.", "It refuses while the tool still uses the chats, keeps an undo journal, and -n previews first."),
            ("Queue for later.", "A command that has to wait goes into a queue that runs once the tool is closed."),
            ("Local only.", "It never contacts the servers of Cursor or Anthropic."),
        ],
        "downloads": [
            ("Mac, Apple Silicon", "chatkeep-aarch64-apple-darwin.tar.gz", release("SherinBloemendaal/chatkeep", "chatkeep-aarch64-apple-darwin.tar.gz")),
            ("Mac, Intel", "chatkeep-x86_64-apple-darwin.tar.gz", release("SherinBloemendaal/chatkeep", "chatkeep-x86_64-apple-darwin.tar.gz")),
            ("Linux x64", "chatkeep-x86_64-unknown-linux-gnu.tar.gz", release("SherinBloemendaal/chatkeep", "chatkeep-x86_64-unknown-linux-gnu.tar.gz")),
            ("Linux arm64", "chatkeep-aarch64-unknown-linux-gnu.tar.gz", release("SherinBloemendaal/chatkeep", "chatkeep-aarch64-unknown-linux-gnu.tar.gz")),
            ("Windows x64", "chatkeep-x86_64-pc-windows-msvc.zip", release("SherinBloemendaal/chatkeep", "chatkeep-x86_64-pc-windows-msvc.zip")),
        ],
        "facts": [
            ("Runs on", "macOS, Linux and Windows"),
            ("Works with", "Cursor and Claude Code"),
            ("Written in", "Rust"),
            ("Licence", "MIT"),
        ],
    },
    {
        "slug": "shellops",
        "name": "ShellOps",
        "kind": "Docker Compose and PHP from the shell",
        "where": "Command line",
        "repo": "SherinBloemendaal/shellops-cli",
        "title": "ShellOps: Compose from the shell.",
        "lead": "so finds the project's git root, loads its .env, and turns Docker Compose, PHP tooling, "
        "database resets and releases into one short command each.",
        "primary": ("Source on GitHub", "https://github.com/SherinBloemendaal/shellops-cli"),
        "unreleased": "The first release is not published yet. The install command appears here as soon as it is.",
        "art": "shellops-how-it-works",
        "art_alt": "so reads compose.yml, .env and Dockerfiles at the git root, then runs Docker, PHP tooling, "
        "database, cache, release and alias commands",
        "points": [
            ("Knows your project.", "It finds the git root, loads .env, and picks dev or prod from APP_ENV."),
            ("One short command per chore.", "Compose, image builds, PHP tooling, database resets and caches."),
            ("Guarded releases.", "so release requires HEAD to match origin, pushes branch and tag together, and drafts the release notes."),
            ("Signed aliases.", "Shared shortcuts are signed with your SSH key and only run for others once they trust them."),
            ("Verified updates.", "so update checks SHA256SUMS before it replaces the binary."),
        ],
        "facts": [
            ("Runs on", "macOS and Linux"),
            ("For", "projects with a compose.yml at the git root"),
            ("Written in", "Rust"),
            ("Status", "Not released yet"),
        ],
    },
    {
        "slug": "tresso",
        "name": "Tresso",
        "kind": "Email client: do, hand over, know",
        "where": "Web, desktop, mobile",
        "repo": "gettresso/tresso",
        "title": "Tresso: do, hand over or know.",
        "lead": "An email client built around one idea: every email is something to do, to hand over, "
        "or to know. Open source and self-hostable, for the web, the desktop and your phone.",
        "primary": ("See the downloads", "#downloads"),
        "install": "tresso",
        "points": [
            ("Do.", "The email becomes a todo, linked to it, with a due date when there is one. Complete the todo and the email archives itself."),
            ("Hand over.", "It goes to someone else with a note and a due date, and waits in Waiting on until they finish it."),
            ("Know.", "It lands in the daily brief, cleared with one click on Noted."),
            ("One inbox for every account,", "grouped into smart inboxes for todos, notifications, newsletters and invitations, plus your own."),
            ("Triage mode.", "One email at a time, settled with D, H or K."),
            ("Everywhere.", "Web, desktop and mobile, with notifications only for mail that needs you."),
        ],
        "downloads": [
            ("Mac, Apple Silicon and Intel", "tresso-macos-universal.dmg", release("gettresso/tresso", "tresso-macos-universal.dmg")),
            ("Windows installer", "tresso-windows-x64-setup.exe", release("gettresso/tresso", "tresso-windows-x64-setup.exe")),
            ("Windows, for administrators", "tresso-windows-x64.msi", release("gettresso/tresso", "tresso-windows-x64.msi")),
            ("Linux x64, AppImage", "tresso-linux-x86_64.AppImage", release("gettresso/tresso", "tresso-linux-x86_64.AppImage")),
            ("Linux x64, Debian and Ubuntu", "tresso-linux-x86_64.deb", release("gettresso/tresso", "tresso-linux-x86_64.deb")),
            ("Linux arm64, AppImage", "tresso-linux-aarch64.AppImage", release("gettresso/tresso", "tresso-linux-aarch64.AppImage")),
            ("Linux arm64, Debian and Ubuntu", "tresso-linux-aarch64.deb", release("gettresso/tresso", "tresso-linux-aarch64.deb")),
            ("Checksums", "SHA256SUMS", release("gettresso/tresso", "SHA256SUMS")),
        ],
        "facts": [
            ("Runs on", "Web, desktop (Tauri) and mobile (Expo)"),
            ("Desktop app for", "macOS, Windows and Linux"),
            ("Hosting", "Self-hostable with Docker"),
            ("Licence", "AGPL-3.0"),
            ("Status", "Early: the first releases are out, the mobile app is not yet"),
        ],
    },
    {
        "slug": "eb-sessions",
        "name": "EB Sessions",
        "kind": "Chrome extension for e-Boekhouden",
        "where": "Chrome",
        "title": "EB Sessions: e-Boekhouden without the login friction.",
        "lead": "A Chrome extension for the Dutch bookkeeping app e-Boekhouden.nl. Switch between administrations in one click, "
        "log in with 1Password, and get a login dialog instead of a lost page when a session expires.",
        "primary": ("What it does", "#points"),
        "unreleased": "Not released yet, and not on the Chrome Web Store. An unofficial tool, not made by or affiliated with e-Boekhouden.nl.",
        "points": [
            ("One click between administrations.", "Every administration you logged in to stays one click away, and all e-Boekhouden tabs move over. No logging out and in."),
            ("1Password on the login page.", "The login form moves out of e-Boekhouden's old frameset, so 1Password's inline menu works. Passwords never touch the extension."),
            ("Expired? Log in where you are.", "A login dialog over the page instead of the login screen, and afterwards you are back where you were."),
            ("A calmer design, if you want it.", "One switch turns on redesigned screens for logging in, importing bank lines, invoices, subscriptions and the archive."),
            ("It never books for you.", "It only changes how pages look and work in your own browser. Every save and every submit is your own click."),
        ],
        "facts": [
            ("Runs in", "Chrome and other Chromium browsers"),
            ("Works with", "e-Boekhouden.nl"),
            ("Written in", "JavaScript"),
            ("Status", "Not released yet"),
        ],
    },
    {
        "slug": "webra",
        "name": "WebRA",
        "kind": "Real-time strategy in the browser",
        "where": "Browser",
        "title": "WebRA: strategy in a browser tab.",
        "lead": "A strategy game inspired by Command & Conquer: Red Alert and the open-source OpenRA engine, "
        "written in Rust and WebAssembly with WebGPU graphics. Nothing to install.",
        "primary": ("Play at webra.sherin.dev", "https://webra.sherin.dev/"),
        "points": [
            ("Campaign.", "The Allied and Soviet missions with their maps, rules and scripts."),
            ("Skirmish for 2 to 8 players,", "free for all or in teams, against AI that plays OpenRA's own bots."),
            ("Online multiplayer.", "Host a public or private game, with spectators, reconnecting and rematches."),
            ("Replays,", "recorded for every game and kept in your account."),
            ("Map editor,", "in the browser and on phones, and OpenRA maps can be imported."),
        ],
        "facts": [
            ("Plays in", "A browser with WebGPU"),
            ("Account", "Needed to play"),
            ("Written in", "Rust and WebAssembly"),
            ("Source", "Not public yet"),
        ],
    },
]

INSTALL_APPS = ["tagwell", "moire", "varve", "chatkeep", "tresso"]
INSTALL_COMMANDS = {
    "tagwell": ("curl -fsSL https://sherin.dev/tagwell/install.sh | bash", None),
    "moire": ("curl -fsSL https://sherin.dev/moire/install.sh | bash", None),
    "varve": ("curl -fsSL https://sherin.dev/varve/install.sh | bash", 'powershell -c "irm https://sherin.dev/varve/install.ps1|iex"'),
    "chatkeep": ("curl -fsSL https://sherin.dev/chatkeep/install.sh | bash", 'powershell -c "irm https://sherin.dev/chatkeep/install.ps1|iex"'),
    "tresso": ("curl -fsSL https://sherin.dev/tresso/install.sh | bash", 'powershell -c "irm https://sherin.dev/tresso/install.ps1|iex"'),
}
# What each installer prints on a Mac, step by step (see the app's install.sh).
INSTALL_STEPS = {
    "tagwell": [("Download", "Tagwell.zip"), ("Checksum", "SHA-256 matches SHA256SUMS"), ("Installed", "/Applications/Tagwell.app")],
    "moire": [("Download", "Moire.zip"), ("Checksum", "SHA-256 matches SHA256SUMS"), ("Installed", "/Applications/Moire.app")],
    "varve": [("Download", "varve-macos-arm64.app.tar.gz"), ("Checksum", "SHA-256 matches SHA256SUMS"), ("Installed", "/Applications/Varve Community.app")],
    "chatkeep": [("Download", "chatkeep-aarch64-apple-darwin.tar.gz"), ("Checksum", "SHA-256 matches SHA256SUMS"), ("Installed", "~/.chatkeep/bin/chatkeep")],
    "tresso": [("Download", "tresso-macos-universal.app.tar.gz"), ("Checksum", "SHA-256 matches SHA256SUMS"), ("Installed", "/Applications/Tresso.app")],
}
INSTALL_NOTES = {
    "tagwell": 'Installs Tagwell.app for macOS 15 or later. <a href="/tagwell/">About Tagwell</a>',
    "moire": 'Installs Moire.app for macOS 15 or later. <a href="/moire/">About Moire</a>',
    "varve": 'macOS and Linux above, Windows below. <a href="/varve/">About Varve</a>',
    "chatkeep": 'macOS and Linux above, Windows below. <a href="/chatkeep/">About Chatkeep</a>',
    "tresso": 'The desktop app: macOS and Linux above, Windows below. <a href="/tresso/">About Tresso</a>',
}

# Which languages each app is written in, and its licence, for the record tiles on the front page.
WRITTEN_IN = [
    ("Swift", ["Tagwell", "Moire"]),
    ("Rust", ["Varve", "Chatkeep", "ShellOps", "WebRA"]),
    ("TypeScript and Vue", ["Varve", "Tresso"]),
    ("PHP and Go", ["Tresso"]),
    ("JavaScript", ["EB Sessions"]),
]
LICENCES = [
    ("MIT", ["Tagwell", "Moire", "Chatkeep"]),
    ("Apache-2.0", ["Varve Community"]),
    ("AGPL-3.0", ["Tresso"]),
]


def e(text: str) -> str:
    return escape(text, quote=True)


def page(title: str, description: str, path: str, body: str, theme: str = "#0b0c0e", glow: str = "") -> str:
    # Soft lights behind the glass tiles: every app's colour on the home page, one app's on its own page.
    lights = f'<div class="glow{f" {glow}" if glow else ""}" aria-hidden="true"><i></i><i></i><i></i><i></i></div>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="https://sherin.dev{path}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="https://sherin.dev{path}">
<meta name="theme-color" content="{theme}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/hanken-grotesk.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/site.js" defer></script>
</head>
<body>
{lights}
<a class="skip" href="#main">Skip to content</a>
<main id="main" class="board">
{body}
</main>
{footer()}
</body>
</html>
"""


def band(text: str, colour: str, label: str) -> str:
    # The name is set wider than its tile, so both ends are cut off by the edges.
    return f"""<header class="tile band {colour} rise" aria-label="{e(label)}">
  <p aria-hidden="true">{e(text)}</p>
</header>"""


def nav(links: list[tuple[str, str]]) -> str:
    items = "\n".join(f'  <a class="tile navlink rise" href="{e(href)}">{e(text)}</a>' for text, href in links)
    return f'<nav class="navrow" aria-label="Site">\n{items}\n</nav>'


def footer() -> str:
    # The closing wordmark: one block per letter, each in the colour of an app.
    colours = [a["slug"] for a in APPS]
    blocks = "".join(f'<span class="block c-{colours[i % len(colours)]} h{i % 3}">{ch}</span>' for i, ch in enumerate("SHERIN"))
    apps = "\n      ".join(f'<li><a href="/{a["slug"]}/">{e(a["name"])}</a></li>' for a in APPS)
    return f"""<footer class="board footer">
  <a class="tile mark" href="/" aria-label="sherin.dev, all apps">{blocks}</a>
  <div class="tile foot-apps">
    <p class="small">The apps</p>
    <ul>
      {apps}
    </ul>
  </div>
  <div class="tile foot-me">
    <p class="small">Made by</p>
    <p>Sherin Bloemendaal</p>
    <p><a href="{GITHUB}">github.com/SherinBloemendaal</a></p>
  </div>
  <div class="tile foot-end">
    <p class="small">{YEAR} · No cookies, no tracking</p>
    <a class="button" href="#main">Back to the top</a>
  </div>
</footer>"""


def instrument(apps: list[str], selected: str, on_app_page: bool = False) -> str:
    # The commands live on the buttons, so the script and the pages share one source.
    buttons = "".join(
        f'<button type="button" data-app="{a}" data-shell="{e(INSTALL_COMMANDS[a][0])}" data-windows="{e(INSTALL_COMMANDS[a][1] or "")}" '
        f'data-note="{e(INSTALL_NOTES[a])}" data-steps="{e(json.dumps(INSTALL_STEPS[a]))}" aria-pressed="{str(a == selected).lower()}">{e(next(x["name"] for x in APPS if x["slug"] == a))}</button>'
        for a in apps
    )
    shell, windows = INSTALL_COMMANDS[selected]
    picker = f'<div class="apps" role="group" aria-label="App to install">{buttons}</div>' if len(apps) > 1 else ""
    windows_row = (
        f'<div class="command" data-command="windows"{"" if windows else " hidden"}><pre><code>{e(windows or "")}</code></pre>'
        '<button class="copy" type="button" hidden>Copy</button></div>'
        if any(INSTALL_COMMANDS[a][1] for a in apps)
        else ""
    )
    note = INSTALL_NOTES[selected].split(" <a ")[0] if on_app_page else INSTALL_NOTES[selected]
    heading = "Install in one line" if not on_app_page else f"Install {next(x['name'] for x in APPS if x['slug'] == selected)}"
    return f"""<section class="tile install c-{selected} rise" id="install" aria-labelledby="install-title" data-ui data-instrument>
  <h2 id="install-title" class="small">{e(heading)}</h2>
  {picker}
  <div class="command" data-command="shell"><pre><code>{e(shell)}</code></pre><button class="copy" type="button" hidden>Copy</button></div>
  {windows_row}
  <ol class="steps" aria-label="What the installer does on a Mac">
{steps(selected)}
  </ol>
  <p class="note">{note}</p>
</section>"""


def steps(app: str) -> str:
    return "\n".join(f'    <li><span>{e(k)}</span>{e(v)}</li>' for k, v in INSTALL_STEPS[app])


def art(a: dict, cls: str) -> str:
    # The README illustrations are drawn for a light page, so they sit on a light tile of their own.
    return f"""<figure class="tile paper {cls} rise">
  <img src="/assets/art/{a['art']}-light.svg" alt="{e(a['art_alt'])}" width="1200" height="600" loading="lazy">
</figure>"""


def version(a: dict) -> str:
    return f'<span class="version" data-version="{a["repo"]}" hidden></span>' if a.get("repo") and a.get("downloads") else ""


def app_tile(a: dict, size: str) -> str:
    status = "Not released yet" if a.get("unreleased") else ("Plays in the browser" if a["slug"] == "webra" else "")
    status_line = f'<span class="status">{e(status)}</span>' if status else version(a)
    picture = (
        f'<span class="peek"><img src="/assets/art/{a["art"]}-light.svg" alt="" width="1200" height="600" loading="lazy"></span>'
        if a.get("art") and size in ("large", "tall")
        else ""
    )
    return f"""<a class="tile app {size} c-{a['slug']} rise" href="/{a['slug']}/">
  <img class="icon" src="/assets/icons/{a['slug']}.png" alt="" width="128" height="128" loading="lazy">
  <span class="name">{e(a['name'])}</span>
  <span class="kind">{e(a['kind'])}</span>
  <span class="meta">{e(a['where'])} {status_line}</span>
  {picture}
</a>"""


def downloads_list(apps: list[dict], open_first: bool = True) -> str:
    bars = []
    for i, a in enumerate(apps):
        if a.get("downloads"):
            rows = "\n".join(f'      <li><span>{e(label)}</span><a href="{e(url)}">{e(file)}</a></li>' for label, file, url in a["downloads"])
        elif a["slug"] == "webra":
            rows = '      <li><span>Plays in the browser</span><a href="https://webra.sherin.dev/">webra.sherin.dev</a></li>'
        elif not a.get("repo"):
            rows = f'      <li><span>Not released yet</span><a href="/{a["slug"]}/">About {e(a["name"])}</a></li>'
        else:
            rows = f'      <li><span>Not released yet</span><a href="https://github.com/{a["repo"]}">Source on GitHub</a></li>'
        bars.append(
            f"""  <details class="bar"{" open" if open_first and i == 0 else ""}>
    <summary><img src="/assets/icons/{a['slug']}.png" alt="" width="24" height="24" loading="lazy"><span>{e(a['name'])}</span>{version(a)}</summary>
    <ul>
{rows}
    </ul>
  </details>"""
        )
    return "\n".join(bars)


def record(title: str, rows: list[tuple[str, list[str]]], cls: str) -> str:
    items = "\n".join(f"    <div><dt>{e(k)}</dt><dd>{e(', '.join(v))}</dd></div>" for k, v in rows)
    return f"""<section class="tile record {cls} rise" aria-label="{e(title)}">
  <p class="small">{e(title)}</p>
  <dl>
{items}
  </dl>
</section>"""


def marquee(words: list[str], colour: str = "") -> str:
    run = "".join(f"<span>{e(w)}</span>" for w in words)
    return f"""<div class="tile marquee{f' one {colour}' if colour else ''}" aria-hidden="true">
  <div class="track">{run}{run}</div>
</div>"""


def home() -> str:
    by_slug = {a["slug"]: a for a in APPS}
    tiles = "\n".join(
        app_tile(by_slug[slug], size)
        for slug, size in [
            ("tagwell", "large"),
            ("moire", "tall"),
            ("varve", "tall"),
            ("chatkeep", "large"),
            ("shellops", "tall"),
            ("tresso", "tall"),
            ("eb-sessions", "wide"),
            ("webra", "wide"),
        ]
    )
    body = f"""{band("Sherin Bloemendaal", "c-ink", "Sherin Bloemendaal")}
{nav([("The apps", "#apps"), ("Install", "#install"), ("Downloads", "#downloads"), ("GitHub", GITHUB)])}

<section class="tile statement rise" aria-labelledby="title">
  <h1 id="title">Eight apps I build and use myself.</h1>
  <p>Two Mac apps, a database manager, two command-line tools, an email client, a browser extension for bookkeeping and a strategy game. Most of them are open source, and most install with one line.</p>
</section>
{instrument(INSTALL_APPS, "tagwell")}

<h2 class="sr-only" id="apps">The apps</h2>
{tiles}

{marquee([a["name"] for a in APPS])}

<section class="tile downloads rise" id="downloads" aria-labelledby="downloads-title">
  <h2 id="downloads-title" class="giant">Downloads</h2>
{downloads_list(APPS)}
</section>
{record("Written in", WRITTEN_IN, "written")}
{record("Licence", LICENCES, "licence")}
<section class="tile why rise" aria-label="Why these apps">
  <p>Each app started as something I needed myself. They stay small on purpose, and most are open source, so you can read what an app does before you run it.</p>
</section>"""
    return page(
        "Sherin Bloemendaal: apps",
        "Apps by Sherin Bloemendaal: Tagwell, Moire, Varve, Chatkeep, ShellOps, Tresso, EB Sessions and WebRA, with downloads and one-line installs.",
        "/",
        body,
    )


def app_page(a: dict) -> str:
    primary_label, primary_url = a["primary"]
    links = [("All apps", "/")]
    if a.get("install"):
        links.append(("Install", "#install"))
    elif a["slug"] == "webra":
        links.append(("Play", "https://webra.sherin.dev/"))
    else:
        links.append(("What it does", "#points"))
    links.append(("Downloads", "#downloads") if a.get("downloads") else ("Details", "#details"))
    if a.get("site"):
        links.append((a["site"].removeprefix("https://"), a["site"]))
    elif a.get("repo"):
        links.append(("GitHub", f"https://github.com/{a['repo']}"))
    else:
        links.append(("GitHub", GITHUB))

    action = instrument([a["install"]], a["install"], on_app_page=True) if a.get("install") else ""
    unreleased = f'<p class="unreleased">{e(a["unreleased"])}</p>' if a.get("unreleased") else ""
    picture = art(a, "art") if a.get("art") else f'<div class="tile art-icon c-{a["slug"]} rise"><img src="/assets/icons/{a["slug"]}.png" alt="" width="256" height="256" loading="lazy"></div>'

    points = "\n".join(
        f"""<div class="tile point rise">
  <p class="lead-line">{e(title)}</p>
  <p>{e(text)}</p>
</div>"""
        for title, text in a["points"]
    )

    downloads = ""
    if a.get("downloads"):
        rows = "\n".join(f'    <li><span>{e(label)}</span><a href="{e(url)}">{e(file)}</a></li>' for label, file, url in a["downloads"])
        downloads = f"""<section class="tile downloads rise" id="downloads" aria-labelledby="downloads-title">
  <h2 id="downloads-title" class="giant">Downloads</h2>
  <p class="small">Latest release {version(a)}</p>
  <ul class="files">
{rows}
  </ul>
</section>"""

    facts = list(a["facts"])
    if a.get("repo"):
        facts.append(("Source", f"github.com/{a['repo']}"))
    fact_tiles = "\n".join(
        f"""<div class="tile fact rise">
  <p class="small">{e(k)}</p>
  <p>{f'<a href="https://{e(v)}">{e(v)}</a>' if v.startswith("github.com/") else e(v)}</p>
</div>"""
        for k, v in facts
    )

    body = f"""{band(a["name"], f"c-{a['slug']}", a["name"])}
{nav(links)}

<section class="tile statement rise" aria-labelledby="title">
  <img class="icon" src="/assets/icons/{a['slug']}.png" alt="{e(a['name'])} icon" width="128" height="128">
  <h1 id="title">{e(a['title'])}</h1>
  <p>{e(a['lead'])}</p>
  <p class="actions"><a class="button c-{a['slug']}" href="{e(primary_url)}">{e(primary_label)}</a></p>
  {unreleased}
</section>
{action}
{picture}

<h2 class="sr-only" id="points">What it does</h2>
{points}

{downloads}
<h2 class="sr-only" id="details">Details</h2>
{fact_tiles}

{marquee([a["name"]] * 6, f"c-{a['slug']}")}"""
    return page(f"{a['name']}: {a['kind']}", a["lead"], f"/{a['slug']}/", body, glow=f"c-{a['slug']}")


def not_found() -> str:
    body = f"""{band("Not found", "c-ink", "Not found")}
{nav([("All apps", "/"), ("Install", "/#install"), ("Downloads", "/#downloads"), ("GitHub", GITHUB)])}
<section class="tile statement rise" aria-labelledby="title">
  <h1 id="title">This page does not exist.</h1>
  <p>It may have moved. Every app is on the front page.</p>
  <p class="actions"><a class="button c-tagwell" href="/">All apps</a></p>
</section>"""
    return page("Not found: sherin.dev", "This page does not exist.", "/404", body)


def main() -> None:
    (SITE / "index.html").write_text(home())
    (SITE / "404.html").write_text(not_found())
    for a in APPS:
        folder = SITE / a["slug"]
        folder.mkdir(exist_ok=True)
        (folder / "index.html").write_text(app_page(a))
    print(f"Wrote index.html and {len(APPS)} app pages")


if __name__ == "__main__":
    main()
