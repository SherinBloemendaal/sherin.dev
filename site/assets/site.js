// sherin.dev: the typed prompt, install tabs, copy buttons, latest release numbers and reveals.
// Every part is an enhancement: without this script the page shows the same content.

const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// Restarts a short fade by switching between two identical animations.
function fade(el, a, b) {
  const next = el.classList.contains(a) ? b : a;
  el.classList.remove(a, b);
  el.classList.add(next);
}

// ---------- Typed prompt ----------

document.querySelectorAll("[data-type]").forEach((el) => {
  if (reducedMotion) return;
  const cursor = el.parentElement.querySelector(".cursor");
  const text = el.textContent;
  let typed = 0;
  el.textContent = "";
  const timer = setInterval(() => {
    typed += 1;
    el.textContent = text.slice(0, typed);
    if (typed < text.length) return;
    clearInterval(timer);
    cursor?.classList.add("blink");
  }, 35);
});

// ---------- Install tabs ----------

document.querySelectorAll("[data-installer]").forEach((root) => {
  const buttons = [...root.querySelectorAll("[data-app]")];
  const shell = root.querySelector("[data-command='shell'] .text");
  const windowsRow = root.querySelector("[data-command='windows']");
  const windows = windowsRow?.querySelector(".text");
  const note = root.querySelector("[data-install-note]");

  buttons.forEach((button) =>
    button.addEventListener("click", () => {
      if (button.getAttribute("aria-pressed") === "true") return;
      buttons.forEach((b) => b.setAttribute("aria-pressed", String(b === button)));
      shell.textContent = button.dataset.shell;
      fade(shell, "swap-a", "swap-b");
      if (windowsRow) {
        windowsRow.hidden = !button.dataset.windows;
        windows.textContent = button.dataset.windows;
        fade(windows, "swap-a", "swap-b");
      }
      // The notes are written by scripts/build.py, so they are trusted markup.
      if (note) note.innerHTML = button.dataset.note;
    }),
  );
});

// ---------- Copy buttons ----------

document.querySelectorAll(".cmd .copy").forEach((button) => {
  const label = button.querySelector("span");
  let timer = null;
  const say = (text) => {
    if (label.textContent === text) return;
    label.textContent = text;
    fade(label, "lab-a", "lab-b");
  };
  button.hidden = false;
  button.addEventListener("click", async () => {
    const text = button.closest(".cmd").querySelector(".text").textContent;
    try {
      await navigator.clipboard.writeText(text);
      say("copied ✓");
    } catch {
      say("select and copy");
    }
    clearTimeout(timer);
    timer = setTimeout(() => say("copy"), 1500);
  });
});

// ---------- Latest release numbers from GitHub ----------

async function latestVersion(repo) {
  const key = `release:${repo}`;
  try {
    const cached = sessionStorage.getItem(key);
    if (cached) return cached;
  } catch {}
  const response = await fetch(`https://api.github.com/repos/${repo}/releases/latest`, {
    headers: { Accept: "application/vnd.github+json" },
  });
  if (!response.ok) return null;
  const tag = (await response.json()).tag_name;
  try {
    sessionStorage.setItem(key, tag);
  } catch {}
  return tag;
}

const versionSlots = [...document.querySelectorAll("[data-version]")];
const repos = [...new Set(versionSlots.map((slot) => slot.dataset.version))];
repos.forEach(async (repo) => {
  try {
    const tag = await latestVersion(repo);
    if (!tag) return;
    versionSlots.filter((slot) => slot.dataset.version === repo).forEach((slot) => (slot.textContent = tag));
  } catch {
    // Offline or rate limited: "released" stays, which is still true.
  }
});

// ---------- Reveals: the apps table and the installer output, once ----------

if (!reducedMotion && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.replace("will-reveal", "is-in");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.2 },
  );
  document.querySelectorAll("[data-reveal]").forEach((el) => {
    el.classList.add("will-reveal");
    observer.observe(el);
  });
}
