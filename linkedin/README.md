# AMAADOR LinkedIn posting queue

`queue.json` lists every AMAADOR ACADEMY offer, training field and article to share on the
AMAADOR LinkedIn company page (page id `146769350`), one post at a time, 9 per day.

## Each run
1. Take the lowest `n` with `"status": "pending"`.
2. Read its page (`url`) for 2–3 concrete facts: price, what is included, who it is for, deadline.
3. Write the post (English, max ~1,000 characters):
   - Hook line with one emoji.
   - 2–3 short lines or ✅ bullets with real facts from the page. Never invent prices or claims.
   - Call to action + full page URL.
   - 3–5 hashtags, always including `#AmaadorAcademy`.
   - No parentheses or other LinkedIn reserved characters `( ) [ ] { } < > | * _ ~ @`.
4. Publish with Zapier `LinkedInCLIAPI` → `create_company_update`, `company_id` `146769350`,
   `submitted_url` = page URL, `title` = page title, `description` = short summary.
5. Set `status` to `posted`, add `posted_at` and `linkedin_url`, commit and push.
6. If publishing fails, set `status` to `failed` with the error and move on; do not retry more than once.

Certificate price: use $5 per course (homepage and Offers page).
