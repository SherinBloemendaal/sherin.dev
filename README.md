# sherin.dev

The site at [sherin.dev](https://sherin.dev): the apps I build, each with its own page, downloads and one-line install.

Plain HTML and CSS with a little JavaScript, hosted on Cloudflare Pages. The install scripts under `/<app>/install.sh` are not part of this site: a Cloudflare Worker serves them from each app's repository (see the `dns` repository).

## Changing the site

The pages are written by `scripts/build.py` from the app list at its top. Edit that list (or the templates below it), then:

```bash
python3 scripts/build.py
```

Commit the changed files in `site/`. A push to `main` deploys them; the workflow fails when `site/` does not match what the script writes.

## Layout

| Path | What it holds |
| --- | --- |
| `site/` | Everything that is published: the pages, `assets/` (CSS, JavaScript, fonts, icons, app art) and `_headers`. |
| `scripts/build.py` | Writes the pages in `site/`. |
| `art/` | Drawings made for the site, as SVG: the ShellOps icon. |

The app icons and illustrations in `site/assets` come from each app's own repository. The typeface is [Hanken Grotesk](https://fonts.google.com/specimen/Hanken+Grotesk) (SIL Open Font License), served from this site.

## Deploying

The workflow deploys `site/` with `wrangler pages deploy` to the Pages project `sherin-dev`. It needs one repository secret:

| Secret | Value |
| --- | --- |
| `CLOUDFLARE_API_TOKEN` | A Cloudflare API token with **Account · Cloudflare Pages · Edit** |

The Pages project, the `sherin.dev` and `www.sherin.dev` domains and their DNS records are managed in the `dns` repository.
