#!/usr/bin/env python3
"""Writes the static pages of sherin.dev from the app list below.

The output (site/index.html, site/404.html and one folder per app) is committed, so deploying needs no build step.
Run it after changing an app:  python3 scripts/build.py
"""

import hashlib
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
GITHUB = "https://github.com/SherinBloemendaal"
YEAR = 2026


def release(repo: str, name: str) -> str:
    return f"https://github.com/{repo}/releases/latest/download/{name}"


def mac(app: str, kind: str = "mac") -> str:
    """The Mac download of an app. Its DMG carries the version in its name, so no fixed file name
    exists; the install Worker (the `dns` repository) redirects this path to the latest one."""
    return f"/{app}/download/{kind}"


APPS = [
    {
        "slug": "tagwell",
        "name": "Tagwell",
        "kind": "MP3 tag editor",
        "where": "macOS",
        "lang": "Swift",
        "repo": "SherinBloemendaal/tagwell",
        "title": "Tagwell: MP3 tags, nothing else.",
        "lead": "A small, native Mac app for editing the tags of one MP3 or hundreds at once. "
        "It writes only the fields you change; the audio and the rest of the tag stay exactly as they were.",
        "primary": ("Download for Mac", mac("tagwell")),
        "install": "tagwell",
        "points": [
            ("Only what you changed is written.", "MusicBrainz IDs, iTunes data, lyrics and ratings stay byte for byte, and the tag keeps its ID3 version."),
            ("Bulk edit.", "Select a hundred files and set the artist, album, year or cover art once. Number tracks or turn file names into titles in one click."),
            ("Artist folders.", "Drag files onto an artist in the sidebar to set their artist. Saved artists come back as suggestions, so a name is spelled the same everywhere."),
            ("Cover art from YouTube.", "Search for the track and pick a thumbnail, or let Tagwell find the video in a yt-dlp file name. Cropped to a square by default."),
            ("Rename on save, if you want.", "Files can take the name Artist - Title. An existing file is never overwritten."),
            ("Safe saves.", "Files are written in the background with a progress window, next to the original and swapped in, so a failed save never leaves a broken MP3."),
        ],
        "downloads": [
            ("Mac, Apple Silicon and Intel", "Tagwell for Mac (.dmg)", mac("tagwell")),
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
        "lang": "Swift",
        "repo": "SherinBloemendaal/moire",
        "title": "Moire shows what changed.",
        "lead": "A native Mac app for comparing text, files and folders. Lines line up across both sides, "
        "and the exact words that changed are marked.",
        "primary": ("Download for Mac", mac("moire")),
        "install": "moire",
        "points": [
            ("Side by side or unified.", "Changed lines sit next to their new version, with the changed words marked."),
            ("Copy changes across.", "Take a change from either side; saving keeps the file's own encoding and line endings."),
            ("Jump between changes", "with the keyboard, or click a mark in the change map beside the scroll bar."),
            ("Paste or type.", "No files needed: paste two snippets and the comparison updates as you type."),
            ("Compare folders.", "Every file in both folders is compared by its contents; double-click one to see what changed."),
            ("Fast on big files.", "Myers' algorithm in linear space, the idea behind git diff, off the main thread."),
        ],
        "downloads": [
            ("Mac, Apple Silicon and Intel", "Moire for Mac (.dmg)", mac("moire")),
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
        "lang": "Rust, Vue",
        "repo": "getvarve/varve",
        "site": "https://getvarve.com",
        "title": "Varve: calm database work.",
        "lead": "One desktop app for PostgreSQL, MySQL, MariaDB and Redis, careful around production: "
        "environment tags, read-only connections and a plan to review before every change.",
        "primary": ("See the downloads", "#downloads"),
        "install": "varve",
        "points": [
            ("Every engine, fully.", "Materialized views, partitions, events, system-versioned tables and Redis streams, each in its own place."),
            ("Safe around production.", "Environment tags, read-only connections, a plan before every structure change and a confirmation before destructive statements."),
            ("Quiet by design.", "A dense, calm interface where colour only means something: production is red, and nothing else is."),
            ("Secrets stay local.", "Passwords and SSH passphrases live in your system keychain; your queries only travel to your own servers."),
            ("Fast where it counts.", "A Rust core with native drivers, cancellable queries and a grid that stays smooth on large results."),
        ],
        "downloads": [
            ("Mac, Apple Silicon", "Varve for Mac, Apple Silicon (.dmg)", mac("varve", "mac-arm64")),
            ("Mac, Intel", "Varve for Mac, Intel (.dmg)", mac("varve", "mac-x64")),
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
        "lang": "Rust",
        "repo": "SherinBloemendaal/chatkeep",
        "title": "Chatkeep: your chats move along.",
        "lead": "A command-line tool for Cursor and Claude Code. Move or rename a project folder, "
        "and its chat history comes along to the new place.",
        "primary": ("Install", "#install"),
        "install": "chatkeep",
        "points": [
            ("Chats follow the folder.", "chatkeep mv rewrites the local references, so the history reattaches at the new path."),
            ("One command, both tools.", "List, move, copy, split, combine, export and import chats for Cursor and Claude Code alike."),
            ("Safe writes.", "It refuses while the tool still uses the chats, keeps an undo journal, and -n previews first."),
            ("Queue for later.", "A command that has to wait goes into a queue that runs once the tool is closed."),
            ("Local only.", "It never contacts the servers of Cursor or Anthropic."),
        ],
        "downloads": [
            ("Mac app, Apple Silicon and Intel", "Chatkeep for Mac (.dmg)", mac("chatkeep")),
            ("Command line, Mac, Apple Silicon", "chatkeep-aarch64-apple-darwin.tar.gz", release("SherinBloemendaal/chatkeep", "chatkeep-aarch64-apple-darwin.tar.gz")),
            ("Command line, Mac, Intel", "chatkeep-x86_64-apple-darwin.tar.gz", release("SherinBloemendaal/chatkeep", "chatkeep-x86_64-apple-darwin.tar.gz")),
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
        "lang": "Rust",
        "repo": "SherinBloemendaal/shellops-cli",
        "title": "ShellOps: Compose from the shell.",
        "lead": "so finds the project's git root, loads its .env, and turns Docker Compose, PHP tooling, "
        "database resets and releases into one short command each.",
        "primary": ("Source on GitHub", "https://github.com/SherinBloemendaal/shellops-cli"),
        "unreleased": "The first release is not published yet. The install command appears here as soon as it is.",
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
        "lang": "TypeScript, PHP, Go",
        "repo": "gettresso/tresso",
        "site": "https://gettresso.com",
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
            ("Mac, Apple Silicon and Intel", "Tresso for Mac (.dmg)", mac("tresso")),
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
        "lang": "TypeScript",
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
            ("Written in", "TypeScript"),
            ("Status", "Not released yet"),
        ],
    },
    {
        "slug": "eb-mcp",
        "name": "EB MCP",
        "kind": "e-Boekhouden for AI clients",
        "where": "macOS, Windows",
        "lang": "Rust, TypeScript",
        "title": "EB MCP: your bookkeeping, readable for AI.",
        "repo": "SherinBloemendaal/eboekhouden-mcp",
        "lead": "A menu-bar app that signs in to the Dutch bookkeeping app e-Boekhouden.nl and lets Claude, Cursor and other AI clients "
        "work with your administration through a local MCP server. Read only, unless you turn writing on for an account.",
        "primary": ("Download for Mac", mac("eb-mcp")),
        "notice": "An unofficial tool, not made by or affiliated with e-Boekhouden.nl.",
        "points": [
            ("Signs in out of sight.", "You add an account once, with the password in 1Password or your Keychain. EB MCP fills e-Boekhouden's own login page in the background and asks for your two-step code in its own field."),
            ("Read only, until you say otherwise.", "Tools for relations, entries, open items, the ledger, balance sheet, profit and loss, VAT, hours and the digital archive. Writing is off for every account until you turn it on, and can wait for your approval per change."),
            ("Local and locked down.", "The server listens on 127.0.0.1 only, behind a token, and refuses any website. Sessions live in memory and end when you quit."),
            ("See every call.", "A request log shows each AI question next to the e-Boekhouden calls it caused, with cookies and tokens masked, and a dashboard of the traffic."),
            ("One click to connect.", "Writes the entry into Claude's or Cursor's config after you saw exactly what changes, with a backup first."),
        ],
        "facts": [
            ("Runs on", "macOS (menu bar) and Windows (system tray)"),
            ("Works with", "e-Boekhouden.nl, Claude, Cursor and other MCP clients"),
            ("Written in", "Rust (Tauri) and TypeScript"),
        ],
        "downloads": [
            ("Mac, Apple Silicon and Intel", "EB MCP for Mac (.dmg)", mac("eb-mcp")),
            ("Windows installer", "eb-mcp-windows-x64-setup.exe", release("SherinBloemendaal/eboekhouden-mcp", "eb-mcp-windows-x64-setup.exe")),
            ("Windows, for administrators", "eb-mcp-windows-x64.msi", release("SherinBloemendaal/eboekhouden-mcp", "eb-mcp-windows-x64.msi")),
            ("Checksums", "SHA256SUMS", release("SherinBloemendaal/eboekhouden-mcp", "SHA256SUMS")),
        ],
    },
    {
        "slug": "webra",
        "name": "WebRA",
        "kind": "Real-time strategy in the browser",
        "where": "Browser",
        "lang": "Rust, WebAssembly",
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

def e(text: str) -> str:
    return escape(text, quote=True)


def asset(name: str) -> str:
    # The file's hash in the URL, so a changed stylesheet or script is never taken from an old cache.
    digest = hashlib.sha256((SITE / "assets" / name).read_bytes()).hexdigest()[:10]
    return f"/assets/{name}?v={digest}"


DOWNLOAD_ICON = (
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>'
)


def page(
    title: str,
    description: str,
    path: str,
    body: str,
    crumb: str = "",
    links: list[tuple[str, str]] | None = None,
    back: bool = False,
) -> str:
    links = links or [("apps", "/#apps"), ("install", "/#install"), ("github", GITHUB)]
    items = "\n".join(f'    <a href="{e(href)}">{e(text)}</a>' for text, href in links)
    trail = f'<span class="crumb"><span aria-hidden="true"> / </span>{e(crumb)}</span>' if crumb else ""
    start = '<a href="/">← all apps</a>' if back else "<span>Sherin Bloemendaal</span>"
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
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#fbfbf9" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#111214" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/ibm-plex-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/ibm-plex-mono-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{asset('site.css')}">
<script src="{asset('site.js')}" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="wrap">
<header class="top">
  <p class="brand"><a href="/"><span class="accent">~/</span>sherin.dev</a>{trail}</p>
  <nav aria-label="Site">
{items}
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  {start}
  <span>© {YEAR} · no cookies, no tracking · <a href="{GITHUB}">github.com/SherinBloemendaal</a></span>
</footer>
</div>
</body>
</html>
"""


def prompt(text: str) -> str:
    # site.js types the line out once; without it the line is simply there.
    return (
        f'<p class="prompt"><span class="sr-only">{e(text)}</span>'
        f'<span aria-hidden="true"><span data-type>{e(text)}</span><span class="cursor">▍</span></span></p>'
    )


def label(text: str, ident: str) -> str:
    return f'<h2 class="label" id="{ident}"><span aria-hidden="true">## </span>{e(text)}</h2>'


def command(kind: str, text: str, ps1: str, hidden: bool = False) -> str:
    return (
        f'<div class="cmd{" sub" if kind == "windows" else ""}" data-command="{kind}"{" hidden" if hidden else ""}>'
        f'<code><span class="ps1" aria-hidden="true">{e(ps1)}</span><span class="text">{e(text)}</span></code>'
        '<button class="copy" type="button" hidden><span>copy</span></button></div>'
    )


def output(app: str) -> str:
    # What the installer prints on a Mac, replayed line by line by site.js.
    lines = "\n".join(
        f'    <li class="line"><span class="mark" aria-hidden="true">{"→" if k == "Download" else "✓"}</span>'
        f'<span class="key">{e(k.lower())}</span><span>{e(v)}</span></li>'
        for k, v in INSTALL_STEPS[app]
    )
    return f'<ol class="out" aria-label="What the installer prints on a Mac" data-reveal>\n{lines}\n  </ol>'


def installer(apps: list[str], selected: str, on_app_page: bool = False) -> str:
    # The commands live on the buttons, so the script and the pages share one source.
    buttons = "".join(
        f'<button type="button" data-app="{a}" data-shell="{e(INSTALL_COMMANDS[a][0])}" data-windows="{e(INSTALL_COMMANDS[a][1] or "")}" '
        f'data-note="{e(INSTALL_NOTES[a])}" aria-pressed="{str(a == selected).lower()}">{a}</button>'
        for a in apps
    )
    shell, windows = INSTALL_COMMANDS[selected]
    tabs = f'<div class="tabs" role="group" aria-label="App to install">{buttons}</div>' if len(apps) > 1 else ""
    windows_row = command("windows", windows or "", "PS> ", hidden=not windows) if any(INSTALL_COMMANDS[a][1] for a in apps) else ""
    if on_app_page:
        after = f'{output(selected)}\n  <p class="note">{INSTALL_NOTES[selected].split(" <a ")[0]}</p>'
    else:
        after = f'<p class="note">Checks the SHA-256 against SHA256SUMS before it installs. <span data-install-note>{INSTALL_NOTES[selected]}</span></p>'
    return f"""<div class="panel" data-installer>
  {tabs}
  {command("shell", shell, "$ ")}
  {windows_row}
  {after}
</div>"""


def status(a: dict) -> str:
    if a.get("unreleased"):
        return '<span class="status off">not yet</span>'
    if a["slug"] == "webra":
        return '<span class="status">playable</span>'
    # site.js swaps in the latest release tag from GitHub.
    return f'<span class="status" data-version="{a["repo"]}">released</span>'


def app_row(a: dict) -> str:
    return f"""      <tr>
        <th scope="row"><a href="/{a['slug']}/">{a['slug']}</a></th>
        <td>{e(a['kind'])}</td>
        <td class="dim">{e(a['where'])}</td>
        <td class="dim">{e(a['lang'])}</td>
        <td class="end">{status(a)}</td>
      </tr>"""


def home() -> str:
    rows = "\n".join(app_row(a) for a in APPS)
    body = f"""<section class="hero">
  {prompt("# sherin bloemendaal")}
  <h1>Small tools I build, with the source, the downloads and a one-line install.</h1>
  <p class="lead">I am a programmer. These are my own apps: native Mac apps in Swift, command-line tools in Rust, and desktop apps for every platform.</p>
</section>

<section class="block" id="install" aria-labelledby="install-title">
  {label("install", "install-title")}
  {installer(INSTALL_APPS, "tagwell")}
</section>

<section class="block" id="apps" aria-labelledby="apps-title">
  {label("apps", "apps-title")}
  <div class="scroll" tabindex="0" role="region" aria-labelledby="apps-title" data-reveal>
  <table class="apps">
    <thead>
      <tr><th scope="col">name</th><th scope="col">what it is</th><th scope="col">runs on</th><th scope="col">written in</th><th scope="col" class="end">status</th></tr>
    </thead>
    <tbody>
{rows}
    </tbody>
  </table>
  </div>
</section>"""
    return page(
        "Sherin Bloemendaal: apps",
        "Apps by Sherin Bloemendaal: Tagwell, Moire, Varve, Chatkeep, ShellOps, Tresso, EB Sessions, EB MCP and WebRA, with downloads and one-line installs.",
        "/",
        body,
    )


def fact_value(value: str) -> str:
    return f'<a href="https://{e(value)}">{e(value)}</a>' if value.startswith("github.com/") else e(value)


def app_page(a: dict) -> str:
    primary_label, primary_url = a["primary"]
    source = f"https://github.com/{a['repo']}" if a.get("repo") else ""
    links = [("apps", "/#apps")]
    if a.get("site"):
        links.append(("website", a["site"]))
    if source:
        links.append(("source", source))

    facts = list(a["facts"])
    licence = dict(facts).get("Licence")
    meta = [a["kind"], a["where"], a["lang"]] + ([licence] if licence else [])
    meta_line = '<span aria-hidden="true">·</span>'.join(f"<span>{e(m)}</span>" for m in meta)

    icon = DOWNLOAD_ICON if primary_label.startswith("Download") else ""
    actions = [f'<a class="button primary" href="{e(primary_url)}">{icon}{e(primary_label)}</a>']
    if source and primary_url != source:
        actions.append(f'<a class="button" href="{e(source)}">View source</a>')
    # A released app can carry a notice too, such as a disclaimer.
    note = a.get("unreleased") or a.get("notice")
    unreleased = f'\n  <p class="notice">{e(note)}</p>' if note else ""

    install = ""
    if a.get("install"):
        install = f"""
<section class="block" id="install" aria-labelledby="install-title">
  {label("install", "install-title")}
  {installer([a["install"]], a["install"], on_app_page=True)}
</section>
"""

    points = "\n".join(f"    <li><strong>{e(title)}</strong> {e(text)}</li>" for title, text in a["points"])

    downloads = ""
    if a.get("downloads"):
        rows = "\n".join(
            f'      <tr><td>{e(text)}</td><td class="end"><a class="file" href="{e(url)}">{e(file)}</a></td></tr>'
            for text, file, url in a["downloads"]
        )
        downloads = f"""
<section class="block" id="downloads" aria-labelledby="downloads-title">
  {label("downloads", "downloads-title")}
  <div class="scroll" tabindex="0" role="region" aria-labelledby="downloads-title">
  <table class="files">
    <tbody>
{rows}
    </tbody>
  </table>
  </div>
</section>
"""

    if source:
        facts.append(("Source", source.removeprefix("https://")))
    fact_items = "\n".join(f"    <div><dt>{e(k)}</dt><dd>{fact_value(v)}</dd></div>" for k, v in facts)

    body = f"""<section class="hero app">
  <p class="meta">{meta_line}</p>
  <h1>{e(a['name'])}</h1>
  <p class="lead">{e(a['lead'])}</p>{unreleased}
  <p class="actions">{"".join(actions)}</p>
</section>
{install}
<section class="block" id="points" aria-labelledby="points-title">
  {label("what it does", "points-title")}
  <ul class="points">
{points}
  </ul>
</section>
{downloads}
<section class="block" id="details" aria-labelledby="details-title">
  {label("facts", "details-title")}
  <dl class="facts">
{fact_items}
  </dl>
</section>"""
    return page(f"{a['name']}: {a['kind']}", a["lead"], f"/{a['slug']}/", body, crumb=a["slug"], links=links, back=True)


def not_found() -> str:
    body = f"""<section class="hero">
  {prompt("# 404")}
  <h1>This page does not exist.</h1>
  <p class="lead">It may have moved. Every app is on the front page.</p>
  <p class="actions"><a class="button primary" href="/">All apps</a></p>
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
