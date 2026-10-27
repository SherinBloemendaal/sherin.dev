// sherin.dev: the install instrument, copy buttons, latest release numbers and section entrances.
// Every part is an enhancement: without this script the page shows the same content.

document.documentElement.classList.add("js");

const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// ---------- Install instrument ----------

function setUpInstrument(root) {
  const buttons = [...root.querySelectorAll("[data-app]")];
  const shell = root.querySelector("[data-command='shell'] pre");
  const windowsRow = root.querySelector("[data-command='windows']");
  const windows = windowsRow?.querySelector("pre");
  const note = root.querySelector(".note");
  let current = buttons.find((b) => b.getAttribute("aria-pressed") === "true")?.dataset.app ?? "tagwell";
  let timer = null;

  function show(app, animate) {
    const button = buttons.find((b) => b.dataset.app === app);
    if (!button) return;
    const install = { shell: button.dataset.shell, windows: button.dataset.windows, note: button.dataset.note };
    current = app;
    buttons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.app === app)));
    const apply = () => {
      shell.textContent = install.shell;
      if (windowsRow) {
        windowsRow.hidden = !install.windows;
        windows.textContent = install.windows ?? "";
      }
      note.innerHTML = install.note;
      shell.classList.remove("fading");
      windows?.classList.remove("fading");
    };
    if (animate && !reducedMotion) {
      shell.classList.add("fading");
      windows?.classList.add("fading");
      setTimeout(apply, 800);
    } else {
      apply();
    }
  }

  // The commands change slowly on their own until the visitor picks one.
  function cycle() {
    stop();
    if (reducedMotion || buttons.length < 2) return;
    timer = setInterval(() => {
      if (document.hidden) return;
      const index = buttons.findIndex((b) => b.dataset.app === current);
      show(buttons[(index + 1) % buttons.length].dataset.app, true);
    }, 6000);
  }
  function stop() {
    if (timer) clearInterval(timer);
    timer = null;
  }

  buttons.forEach((button) =>
    button.addEventListener("click", () => {
      stop();
      show(button.dataset.app, false);
    }),
  );
  root.addEventListener("pointerenter", stop);
  root.addEventListener("focusin", stop);
  cycle();
}

document.querySelectorAll("[data-instrument]").forEach(setUpInstrument);

// ---------- Copy buttons ----------

document.querySelectorAll(".command .copy").forEach((button) => {
  button.hidden = false;
  button.addEventListener("click", async () => {
    const text = button.closest(".command").querySelector("pre").textContent;
    try {
      await navigator.clipboard.writeText(text);
      button.textContent = "Copied";
    } catch {
      button.textContent = "Select and copy";
    }
    setTimeout(() => (button.textContent = "Copy"), 1600);
  });
});

// ---------- Ledger preview: the pointed-at app's own picture beside the list ----------

document.querySelectorAll(".ledger").forEach((ledger) => {
  const image = ledger.querySelector(".preview img");
  if (!image) return;
  let shown = image.getAttribute("src");
  const showFor = (link) => {
    const next = link.dataset.preview;
    if (!next || next === shown) return;
    shown = next;
    const swap = () => {
      image.src = next;
      image.classList.toggle("icon", next.endsWith(".png"));
      image.classList.remove("fading");
    };
    if (reducedMotion) {
      swap();
    } else {
      image.classList.add("fading");
      setTimeout(swap, 200);
    }
  };
  ledger.querySelectorAll("a").forEach((link) => {
    link.addEventListener("pointerenter", () => showFor(link));
    link.addEventListener("focus", () => showFor(link));
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
    versionSlots
      .filter((slot) => slot.dataset.version === repo)
      .forEach((slot) => {
        slot.textContent = tag;
        slot.hidden = false;
      });
  } catch {
    // Offline or rate limited: the page reads fine without the numbers.
  }
});

// ---------- Entrances ----------

const risers = [...document.querySelectorAll(".rise")];
if (reducedMotion || !("IntersectionObserver" in window)) {
  risers.forEach((el) => el.classList.add("in"));
} else {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in");
        observer.unobserve(entry.target);
      });
    },
    { rootMargin: "0px 0px -8% 0px" },
  );
  risers.forEach((el) => observer.observe(el));
}
