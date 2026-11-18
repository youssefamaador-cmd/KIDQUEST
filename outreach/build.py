import csv, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from kidquest_prospects import KQ
try:
    from hse_prospects import HSE, hse_email
except ImportError:
    HSE, hse_email = [], None

SIG = "Best regards,\nYoussef Amaador\nKidQuest\nyoussef@amaador-hse.com"
OPT = "If you'd rather not hear from me again, just reply \"no thanks\" and I won't contact you further."

def kq_email(org, greet, hook, tie):
    subj = f"Certified gamified-learning training for {org}"
    body = f"""{greet},

{hook}

I'm Youssef from KidQuest. We run a short training for educators and club leaders on gamified learning: turning lessons into quests, levels and rewards that keep children engaged. Staff who complete it receive a KidQuest Certified Educator certificate. We also offer ready-made quest activity packs and personalised completion certificates children can earn.

{tie}

Would you be open to a 15-minute call, or shall I send over the course outline and pricing?

{SIG}

{OPT}"""
    return subj, body

rows = []
for org, em, reg, greet, hook, tie, src in KQ:
    s, b = kq_email(org, greet, hook, tie)
    rows.append(("KidQuest", org, reg, em, src, s, b))
for p in HSE:
    s, b = hse_email(p)
    rows.append(("HSE", p["org"], p["region"], p["email"], p["src"], s, b))

d = os.path.dirname(__file__)
with open(os.path.join(d, "outreach_emails.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["offer","organization","region","to","source_url","subject","body"]); w.writerows(rows)
with open(os.path.join(d, "outreach_emails.md"), "w") as f:
    f.write(f"# Outreach emails ({len(rows)})\n\nAll addresses were found published on each organization's own site (via domain-restricted search). Click the source link to confirm before sending.\n\n")
    for i, (off, org, reg, em, src, s, b) in enumerate(rows, 1):
        f.write(f"---\n\n## {i}. {org} ({off}, {reg})\n\n**To:** {em}  \n**Source:** {src}  \n**Subject:** {s}\n\n```\n{b}\n```\n\n")
print(len(rows), "emails")
