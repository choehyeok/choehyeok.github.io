import glob, os, re, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = open(os.path.join(ROOT, '_thumb', 'template.html'), encoding='utf-8').read()
DEF = {'badge': '당일·익일 정산', 'title1': '', 'title2': '', 'sub': '', 'amount': '1,250,000', 'chip': '오늘 입금', 'toast': '매출 정산이 입금됐어요'}

def meta(path):
    t = open(path, encoding='utf-8').read().split('---')[1]
    d = dict(DEF)
    for k in DEF:
        m = re.search(r'^thumb_%s:\s*"?(.*?)"?\s*$' % k, t, re.M)
        if m: d[k] = m.group(1)
    return d if d['title1'] else None

os.makedirs(os.path.join(ROOT, 'img'), exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1200, 'height': 630})
    for f in sorted(glob.glob(os.path.join(ROOT, '_posts', '*.md'))):
        slug = re.sub(r'^\d{4}-\d\d-\d\d-', '', os.path.basename(f))[:-3]
        out = os.path.join(ROOT, 'img', slug + '.png')
        d = meta(f)
        if not d or (os.path.exists(out) and '--force' not in sys.argv): continue
        html = TPL
        for k, v in d.items(): html = html.replace('{{%s}}' % k, v)
        tmp = os.path.join(ROOT, '_thumb', '_tmp.html')
        open(tmp, 'w', encoding='utf-8').write(html)
        pg.goto('file://' + tmp); pg.wait_for_timeout(400)
        pg.screenshot(path=out); print('rendered', out)
    b.close()
