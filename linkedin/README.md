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
