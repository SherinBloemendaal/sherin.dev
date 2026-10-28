#!/usr/bin/env python3
"""Writes the static pages of sherin.dev from the app list below.

The output (site/index.html, site/404.html and one folder per app) is committed, so deploying needs no build step.
Run it after changing an app:  python3 scripts/build.py
"""

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
INSTALL_NOTES = {
    "tagwell": 'Installs Tagwell.app for macOS 15 or later. <a href="/tagwell/">About Tagwell</a>',
    "moire": 'Installs Moire.app for macOS 15 or later. <a href="/moire/">About Moire</a>',
    "varve": 'macOS and Linux above, Windows below. <a href="/varve/">About Varve</a>',
    "chatkeep": 'macOS and Linux above, Windows below. <a href="/chatkeep/">About Chatkeep</a>',
    "tresso": 'The desktop app: macOS and Linux above, Windows below. <a href="/tresso/">About Tresso</a>',
}

MARK = (
    '<svg viewBox="0 0 22 22" aria-hidden="true"><rect width="22" height="22" rx="5" fill="#1f3038"/>'
    '<path d="M6.5 8 L10 11 L6.5 14" fill="none" stroke="#5fd0db" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
    '<rect x="11.5" y="13.2" width="5" height="1.8" rx=".9" fill="#e8eef1"/></svg>'
)


def e(text: str) -> str:
    return escape(text, quote=True)


def page(title: str, description: str, path: str, body: str, corner: tuple[str, str]) -> str:
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
<meta name="theme-color" content="#f7f9fa">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/switzer-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/switzer-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="column"><a class="wordmark" href="/">{MARK}<span>sherin.dev</span></a></div>
  <a class="corner" href="{e(corner[1])}">{e(corner[0])}</a>
</header>
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
"""


def footer() -> str:
    links = "\n    ".join(f'<a href="/{a["slug"]}/">{e(a["name"])}</a>' for a in APPS)
    return f"""<footer class="footer">
  <p>Apps by Sherin Bloemendaal</p>
  <nav aria-label="Apps">
    {links}
    <a href="{GITHUB}">GitHub</a>
  </nav>
  <p class="end">{YEAR} · No cookies, no tracking</p>
</footer>"""


def instrument(apps: list[str], selected: str, on_app_page: bool = False) -> str:
    # The commands live on the buttons, so the script and the pages share one source.
    buttons = "".join(
        f'<button type="button" data-app="{a}" data-shell="{e(INSTALL_COMMANDS[a][0])}" data-windows="{e(INSTALL_COMMANDS[a][1] or "")}" '
        f'data-note="{e(INSTALL_NOTES[a])}" aria-pressed="{str(a == selected).lower()}">{e(next(x["name"] for x in APPS if x["slug"] == a))}</button>'
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
    return f"""<div class="instrument rise" style="--i:4" id="install" data-ui data-instrument>
  {picker}
  <div class="command" data-command="shell"><pre><code>{e(shell)}</code></pre><button class="copy" type="button" hidden>Copy</button></div>
  {windows_row}
  <p class="note">{INSTALL_NOTES[selected].split(" <a ")[0] if on_app_page else INSTALL_NOTES[selected]}</p>
</div>"""


def picture(name: str, alt: str) -> str:
    # The site is light only, so the README art is too.
    return f"""<figure class="figure rise">
  <img src="/assets/art/{name}-light.svg" alt="{e(alt)}" width="1200" height="600" loading="lazy">
</figure>"""


def preview(a: dict) -> str:
    """The picture shown beside the app list: the app's own README art, or its icon when it has none."""
    return f"/assets/art/{a['art']}-light.svg" if a.get("art") else f"/assets/icons/{a['slug']}.png"


def home() -> str:
    ledger = "\n".join(
        f"""    <li><a href="/{a['slug']}/" data-preview="{preview(a)}">
      <span class="name"><img src="/assets/icons/{a['slug']}.png" alt="" width="28" height="28" loading="lazy">{e(a['name'])}</span>
      <span class="kind">{e(a['kind'])}</span>
      <span class="where">{e(a['where'])}</span>
    </a></li>"""
        for a in APPS
    )

    groups = []
    for a in APPS:
        icon = f'<img src="/assets/icons/{a["slug"]}.png" alt="" width="16" height="16" loading="lazy">'
        version = f' <span data-version="{a["repo"]}" hidden></span>' if a.get("repo") and a.get("downloads") else ""
        if a.get("downloads"):
            rows = "\n".join(
                f'      <li><span>{e(label)}</span><a href="{e(url)}">{e(file)}</a></li>' for label, file, url in a["downloads"][:4] if file != "SHA256SUMS"
            )
            more = (
                f'\n      <li><span>Everything else</span><a href="/{a["slug"]}/#downloads">All downloads</a></li>'
                if len([d for d in a["downloads"] if d[1] != "SHA256SUMS"]) > 4
                else ""
            )
        elif a["slug"] == "webra":
            rows = '      <li><span>Plays in the browser</span><a href="https://webra.sherin.dev/">webra.sherin.dev</a></li>'
            more = ""
        else:
            rows = f'      <li><span>Not released yet</span><a href="https://github.com/{a["repo"]}">Source on GitHub</a></li>'
            more = ""
        groups.append(
            f"""  <div class="group rise">
    <p>{icon}<a href="/{a['slug']}/">{e(a['name'])}</a>{version}</p>
    <ul>
{rows}{more}
    </ul>
  </div>"""
        )

    body = f"""<section class="hero column" aria-labelledby="title">
  <h1 id="title" class="rise" style="--i:0">Apps I build and use myself.</h1>
  <p class="lead rise" style="--i:1">I'm Sherin Bloemendaal. These are my own apps: two for the Mac, a database manager, two command-line tools, an email client and a strategy game. Most install with one line.</p>
  <div class="actions rise" style="--i:2">
    <a class="button" href="#apps">See the apps</a>
    <a class="textlink" href="{GITHUB}">GitHub <span aria-hidden="true">→</span></a>
  </div>
  {instrument(INSTALL_APPS, "tagwell")}
</section>

<section class="section column" id="apps" aria-labelledby="apps-title">
  <h2 id="apps-title" class="rise">The apps</h2>
  <ul class="ledger rise">
{ledger}
    <li class="preview" aria-hidden="true"><img src="{preview(APPS[0])}" alt="" width="480" height="240"></li>
  </ul>
</section>

<section class="section column rows" id="downloads" aria-labelledby="downloads-title">
  <h2 id="downloads-title" class="rise">Downloads</h2>
{chr(10).join(groups)}
</section>

<section class="section about" aria-label="About">
  <dl class="rise">
    <div><dt>Made by</dt><dd>Sherin Bloemendaal</dd></div>
    <div><dt>Code</dt><dd><a href="{GITHUB}">github.com/SherinBloemendaal</a></dd></div>
    <div><dt>Licences</dt><dd>MIT, Apache-2.0, AGPL-3.0</dd></div>
  </dl>
  <p class="statement rise">Each app here started as something I needed myself. They stay small on purpose and do one job well, and most of them are open source, so you can read exactly what an app does before you run it.</p>
  <div class="record rise">
    <div>
      <p>Written in</p>
      <ul>
        <li><span>Tagwell, Moire</span><span>Swift</span></li>
        <li><span>Varve, Chatkeep, ShellOps</span><span>Rust</span></li>
        <li><span>Tresso</span><span>TypeScript, PHP, Go</span></li>
        <li><span>WebRA</span><span>Rust, WebAssembly</span></li>
      </ul>
    </div>
    <div>
      <p>Licence</p>
      <ul>
        <li><span>Tagwell, Moire, Chatkeep</span><span>MIT</span></li>
        <li><span>Varve Community</span><span>Apache-2.0</span></li>
        <li><span>Tresso</span><span>AGPL-3.0</span></li>
      </ul>
    </div>
  </div>
</section>"""
    return page(
        "Sherin Bloemendaal: apps",
        "Apps by Sherin Bloemendaal: Tagwell, Moire, Varve, Chatkeep, ShellOps, Tresso and WebRA, with downloads and one-line installs.",
        "/",
        body,
        ("GitHub", GITHUB),
    )


def app_page(a: dict) -> str:
    primary_label, primary_url = a["primary"]
    links = []
    if a.get("site"):
        links.append(f'<a class="textlink" href="{e(a["site"])}">{e(a["site"].removeprefix("https://"))} <span aria-hidden="true">→</span></a>')
    if a.get("repo") and primary_url != f"https://github.com/{a['repo']}":
        links.append(f'<a class="textlink" href="https://github.com/{a["repo"]}">Source on GitHub <span aria-hidden="true">→</span></a>')

    if a.get("install"):
        demo = instrument([a["install"]], a["install"], on_app_page=True)
    else:
        demo = ""
    unreleased = f'\n  <p class="unreleased rise" style="--i:4">{e(a["unreleased"])}</p>' if a.get("unreleased") else ""
    art = picture(a["art"], a["art_alt"]) if a.get("art") else ""

    points = "\n".join(f"    <li><strong>{e(title)}</strong> {e(text)}</li>" for title, text in a["points"])

    downloads = ""
    if a.get("downloads"):
        version = f' <span data-version="{a["repo"]}" hidden></span>' if a.get("repo") else ""
        rows = "\n".join(f'      <li><span>{e(label)}</span><a href="{e(url)}">{e(file)}</a></li>' for label, file, url in a["downloads"])
        downloads = f"""
<section class="section column rows" id="downloads" aria-labelledby="downloads-title">
  <h2 id="downloads-title" class="rise">Downloads</h2>
  <div class="group rise">
    <p>Latest release{version}</p>
    <ul>
{rows}
    </ul>
  </div>
</section>"""

    facts = "\n".join(f"    <dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in a["facts"])
    source = f'\n    <dt>Source</dt><dd><a href="https://github.com/{a["repo"]}">github.com/{a["repo"]}</a></dd>' if a.get("repo") else ""

    body = f"""<section class="hero app column" aria-labelledby="title">
  <div class="app-head rise" style="--i:0"><img src="/assets/icons/{a['slug']}.png" alt="{e(a['name'])} icon" width="72" height="72"></div>
  <h1 id="title" class="rise" style="--i:1">{e(a['title'])}</h1>
  <p class="lead rise" style="--i:2">{e(a['lead'])}</p>
  <div class="actions rise" style="--i:3">
    <a class="button" href="{e(primary_url)}">{e(primary_label)}</a>
    {" ".join(links)}
  </div>
  {demo}{unreleased}
  {art}
</section>

<section class="section column" aria-labelledby="points-title">
  <h2 id="points-title" class="rise">What it does</h2>
  <ul class="points rise">
{points}
  </ul>
</section>
{downloads}
<section class="section column" aria-labelledby="facts-title">
  <h2 id="facts-title" class="rise">Details</h2>
  <dl class="facts rise">
{facts}{source}
  </dl>
</section>"""
    corner = (f"{a['name']} on GitHub", f"https://github.com/{a['repo']}") if a.get("repo") else ("All apps", "/")
    return page(f"{a['name']}: {a['kind']}", a["lead"], f"/{a['slug']}/", body, corner)


def not_found() -> str:
    body = f"""<section class="hero column" aria-labelledby="title">
  <h1 id="title">This page does not exist.</h1>
  <p class="lead">It may have moved. Every app is listed on the front page.</p>
  <div class="actions">
    <a class="button" href="/">All apps</a>
    <a class="textlink" href="{GITHUB}">GitHub <span aria-hidden="true">→</span></a>
  </div>
</section>"""
    return page("Not found: sherin.dev", "This page does not exist.", "/404", body, ("GitHub", GITHUB))


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
