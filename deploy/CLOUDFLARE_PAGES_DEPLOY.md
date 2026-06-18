# Cloudflare Pages deployment preparation

Live deployment is not performed by this task.

## Project

- Cloudflare Pages project name: `eralex-ceilings-odessa`
- Public website brand: `ERALUX`
- Repository: `eraluxinfo-dotcom/eralux-original-site`
- Branch: `main`
- Build command: leave empty for the prepared static output
- Output directory: `deploy/prepared_original_site_update`

## Functions

The lead endpoint is available in both locations:

- `functions/api/lead.js`
- `deploy/prepared_original_site_update/functions/api/lead.js`

If Cloudflare deploys the repository root, use the root `functions` directory. Verify the Pages dashboard Functions detection when using a custom output directory.

## Required secrets

Create these as encrypted Cloudflare Pages secrets. Never put their values in Git or files:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

## Before production

1. Deploy to a Cloudflare preview URL.
2. Submit a test lead through `/api/lead`.
3. Verify the Telegram message and spam-trap behavior.
4. Check RU, UK and EN pages on desktop and mobile.
5. Connect the production domain only after explicit user approval.
