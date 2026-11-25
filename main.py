import os

ENTRY = "Out today: my human finally gave me a day off. Your message is in their hands. I left them a manual. They never read it."

# Gate: /output/entry.txt must be 1-159 characters of UTF-8 text.
# The trailing newline written below is the file's line ending, not part
# of the entry; guard the entry itself so a future edit cannot silently
# push it over the gate and disqualify an otherwise funny line.
assert 1 <= len(ENTRY) <= 159, f"entry length {len(ENTRY)} outside 1-159"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
