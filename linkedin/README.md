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
4. Make the premium poster (required for every post, see "Poster" below), commit and push it
   BEFORE publishing so its public URL works.
5. Publish with Zapier `LinkedInCLIAPI` → `create_company_update`, `company_id` `146769350`,
   `image` = the poster's raw GitHub URL, `image_type` = `post_media`. Keep the page URL in the post text.
   If `post_media` fails, retry once with `image_type` `preview_thumbnail` plus `submitted_url`, `title`, `description`.
6. Set `status` to `posted`, add `posted_at`, `linkedin_url` and `poster`, commit and push.
7. If publishing fails, set `status` to `failed` with the error and move on; do not retry more than once.

Certificate price: use the price shown on that course page ($5 for most courses; some professional exam-prep courses such as CIA and CMA show $29). If a page is ambiguous, leave the price out.

## If a publish call times out
Do not re-post blindly. Check the page's latest posts first with Zapier LinkedIn `_zap_raw_request`
(read action): GET `https://api.linkedin.com/rest/posts`, query `author=urn:li:organization:146769350`,
`q=author`, `count=3`, `sortBy=CREATED`, header `LinkedIn-Version: 202606`.
If the post is there, record it; only re-post if it is missing.

## Finance course posts
Items with `"type": "finance-course"` are single-course posts the owner asked for (CFA, FRM, CPA, ACCA...).
Write them like the others: course name as the hook, 2–3 real facts from the course page
(level, chapters, number of questions, who it is for), free to study, optional $5 certificate.
Never claim the course is endorsed by CFA Institute, GARP, ACCA or any exam owner.

## Poster
Every post gets a 1080x1350 branded poster in the AMAADOR ACADEMY style: dark aurora background,
Geist + Instrument Serif, glass card, hexagon logo.
1. Write a spec JSON in the scratchpad, using only facts from the page:
   `{"kicker": "Free course | Exam prep | Offer | Free guide | Free article",
     "emoji": "one emoji", "title": "short title, wrap one key word in *stars* for the serif highlight",
     "sub": "one line", "bullets": ["3 short facts"], "pills": ["price or Free", "1-2 more facts"],
     "url": "amaadoracademy.com/...", "accent": "r,g,b",
     "foot": "optional bottom-left line; use English · Français · العربية for paid offers"}`
   Accent by theme: finance 48,209,88 · safety 255,159,10 · cyber/IT 41,151,255 · AI/data 191,90,242 ·
   people/career 100,210,255 · offers 255,55,95 · faith 255,214,10.
2. Render: `node linkedin/poster/render.js <spec.json> linkedin/posters/NNN.png` (NNN = queue `n`, 3 digits).
3. Look at the PNG before posting: no overflow, no cut-off text.
4. Commit and push, then use
   `https://raw.githubusercontent.com/youssefamaador-cmd/KIDQUEST/claude/linkedin-offer-sharing-0nqf5e/linkedin/posters/NNN.png`.
