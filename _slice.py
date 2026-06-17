import fitz, os, re, json

doc = fitz.open(r"d:\ah\swe\swe_at_google.2.pdf")
toc = doc.get_toc()

# find chapter-level entries: title like "Chapter N. Title"
chaps = []
for lvl, title, page in toc:
    m = re.match(r"Chapter (\d+)\.\s*(.+)", title)
    if m:
        chaps.append({"num": int(m.group(1)), "title": m.group(2).strip(), "start": page})

# end page = next chapter start - 1 ; last chapter ends before Afterword/Part V
# build list of "section boundary" pages from top-level + chapter starts
boundary_pages = sorted(set([page for lvl, title, page in toc if lvl <= 2]))

def next_boundary(after):
    for p in boundary_pages:
        if p > after:
            return p
    return doc.page_count + 1

for c in chaps:
    end = next_boundary(c["start"]) - 1
    c["end"] = end

os.makedirs(r"d:\ah\swe\chapters\raw", exist_ok=True)
index = []
for c in chaps:
    text = []
    for pno in range(c["start"], c["end"] + 1):
        if 1 <= pno <= doc.page_count:
            text.append(doc[pno - 1].get_text())
    body = "\n".join(text)
    fn = rf"d:\ah\swe\chapters\raw\ch{c['num']:02d}.txt"
    with open(fn, "w", encoding="utf-8") as f:
        f.write(f"# Chapter {c['num']}: {c['title']}\n# PDF pages {c['start']}-{c['end']}\n\n")
        f.write(body)
    index.append({"num": c["num"], "title": c["title"], "start": c["start"], "end": c["end"], "chars": len(body)})

with open(r"d:\ah\swe\chapters\raw\_index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=1)

for c in index:
    print(f"ch{c['num']:02d} p{c['start']}-{c['end']} {c['chars']:>6}c  {c['title']}")
