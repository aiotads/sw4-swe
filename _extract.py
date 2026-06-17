import fitz, json, os

doc = fitz.open(r"d:\ah\swe\swe_at_google.2.pdf")
os.makedirs(r"d:\ah\swe\_pages", exist_ok=True)

toc = doc.get_toc()
with open(r"d:\ah\swe\_pages\toc.txt", "w", encoding="utf-8") as f:
    f.write(f"PAGES: {doc.page_count}\n")
    for lvl, title, page in toc:
        f.write(f"{'  '*(lvl-1)}[{page}] {title}\n")

# also json toc for programmatic slicing
with open(r"d:\ah\swe\_pages\toc.json", "w", encoding="utf-8") as f:
    json.dump(toc, f, ensure_ascii=False, indent=1)

allpages = []
for page in doc:
    allpages.append(page.get_text())
with open(r"d:\ah\swe\_pages\full.txt", "w", encoding="utf-8") as f:
    for i, t in enumerate(allpages):
        f.write(f"\n\n========== PAGE {i+1} ==========\n")
        f.write(t)

with open(r"d:\ah\swe\_pages\done.txt", "w", encoding="utf-8") as f:
    f.write(f"OK pages={doc.page_count} chars={sum(len(t) for t in allpages)} toc_entries={len(toc)}")
print("done")
