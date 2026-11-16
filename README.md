# Obsidian AI Knowledge Base Site

Quartz builds the Markdown notes and attachments in `content/` into a public website. GitHub Actions publishes the result to GitHub Pages after every push to `main`.

The original Obsidian Vault and its private backup repository are separate from this public site repository. The local sync script copies publishable note files from the Vault into `content/` and pushes updates. Hidden plugin settings, AI sessions, caches, and local records are excluded.

To preview locally, run `npm ci` and `npx quartz build --serve` from this repository.
