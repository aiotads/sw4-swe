import fitz, re, json
doc = fitz.open(r"d:\ah\swe\swe_at_google.2.pdf")
idx = json.load(open(r"d:\ah\swe\chapters\raw\_index.json", encoding="utf-8"))

# figure-caption references per chapter, and embedded raster image count per page range
for c in idx:
    pages = range(c["start"], c["end"]+1)
    caps = set()
    imgs = 0
    for p in pages:
        page = doc[p-1]
        txt = page.get_text()
        for m in re.finditer(r"Figure\s+(\d+-\d+)", txt):
            caps.add(m.group(1))
        imgs += len(page.get_images(full=True))
    caps = sorted(caps, key=lambda s:(int(s.split('-')[0]), int(s.split('-')[1])))
    print(f"ch{c['num']:02d}  figs={len(caps):2d}  rasterimgs={imgs:3d}  {caps}")
