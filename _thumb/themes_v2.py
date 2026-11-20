# 테마 렌더러 v2: thumb_theme 이 있는 front matter 에서만 사용 (없으면 기존 render.py 방식)
# 글 하나의 이미지 3장은 같은 theme 로 통일, 글끼리는 theme 를 다르게.
import html as _h

THEMES = {
 't1': dict(bg='#eef4ff', ink='#0f172a', ac='#2563eb', ac2='#93b4f5', mu='#475569', card='#ffffff', on='#ffffff'),   # 라이트 블루
 't2': dict(bg='#fff1dc', ink='#3b1d0a', ac='#ea580c', ac2='#fbbf24', mu='#7c4a1d', card='#ffffff', on='#ffffff'),   # 웜 크림 오렌지
 't3': dict(bg='#09090b', ink='#ffffff', ac='#f59e0b', ac2='#d4d4d8', mu='#a1a1aa', card='#18181b', on='#111111'),   # 다크 앰버
 't4': dict(bg='#e6fbf3', ink='#064e3b', ac='#059669', ac2='#6ee7b7', mu='#3f6f5e', card='#ffffff', on='#ffffff'),   # 민트 그린
 't5': dict(bg='#0b1b3a', ink='#ffffff', ac='#e5b84b', ac2='#9fb3d9', mu='#9fb3d9', card='#13264f', on='#0b1b3a'),   # 네이비 골드
 't6': dict(bg='#ffeef3', ink='#4a1230', ac='#e11d74', ac2='#f9a8c9', mu='#8a4b69', card='#ffffff', on='#ffffff'),   # 소프트 핑크
 't7': dict(bg='#1e1147', ink='#ffffff', ac='#a78bfa', ac2='#6d4de0', mu='#c4b5fd', card='#2b1b66', on='#1e1147'),   # 퍼플
 't8': dict(bg='#ffffff', ink='#111111', ac='#111111', ac2='#9ca3af', mu='#6b7280', card='#f3f4f6', on='#ffffff'),   # 모노 화이트
 't9': dict(bg='#fde047', ink='#1c1917', ac='#1c1917', ac2='#ca8a04', mu='#57534e', card='#fffbeb', on='#fde047'),   # 옐로
 't10': dict(bg='#14301f', ink='#f0fdf4', ac='#86efac', ac2='#4ade80', mu='#a7d7b8', card='#1d4430', on='#14301f'),   # 포레스트
 't11': dict(bg='#fff0ec', ink='#3a0f0a', ac='#ef4444', ac2='#fca5a5', mu='#8a3f37', card='#ffffff', on='#ffffff'),   # 코랄 레드
 't12': dict(bg='#e8edf3', ink='#1f2a37', ac='#3b6ea8', ac2='#9db8d6', mu='#52616f', card='#ffffff', on='#ffffff'),   # 슬레이트
}
CSS = "*{margin:0;box-sizing:border-box}body{font-family:'Noto Sans CJK KR','Noto Sans KR','Apple SD Gothic Neo',sans-serif}.f{position:relative;overflow:hidden}.b{font-weight:900}"
e = _h.escape
def lines(s): return e(s).replace('/', '<br>')          # 줄바꿈은 / 로
def parts(s): return [x.strip() for x in s.split('|')]

def _phone(t, d):
    amt = d.get('i2') or '50,000'
    return ("<div style='position:absolute;left:790px;top:70px;width:330px;height:640px;border-radius:52px;background:#0f172a;padding:14px;transform:rotate(8deg);box-shadow:0 30px 60px rgba(0,0,0,.35)'>"
      "<div style='width:100%%;height:100%%;border-radius:40px;background:#fff;padding:34px 24px;color:#111'>"
      "<div style='font-size:22px;color:#64748b;font-weight:700'>결제 금액</div><div class='b' style='font-size:54px;margin:4px 0 22px'>%s원</div>"
      "<div style='background:#f1f5f9;border-radius:16px;padding:16px 18px;font-size:22px;font-weight:700;line-height:1.7'><span style='color:#64748b'>상품</span> %s<br><span style='color:#64748b'>수단</span> 신용·체크카드</div>"
      "<div class='b' style='margin-top:26px;background:%s;color:%s;border-radius:18px;text-align:center;padding:22px;font-size:28px'>카드로 결제하기</div>"
      "<div style='margin-top:18px;text-align:center;font-size:18px;color:#94a3b8;font-weight:700'>예시 화면</div></div></div>") % (e(amt), e(d.get('i1') or '레슨 1회'), t['ac'] if t['ac'] != '#111111' else '#111', t['on'] if t['ac'] != '#111111' else '#fff')

def _chat(t, d):
    return ("<div style='position:absolute;right:56px;top:64px;width:470px'>"
      "<div style='background:#fff;border-radius:34px 34px 34px 8px;padding:26px 30px;font-size:32px;font-weight:700;color:#222;box-shadow:0 8px 24px rgba(0,0,0,.12)'>%s</div>"
      "<div style='margin:22px 0 0 60px;background:#fde047;border-radius:34px 34px 8px 34px;padding:26px 30px;box-shadow:0 8px 24px rgba(0,0,0,.12)'><div style='font-size:24px;font-weight:800;color:#713f12'>결제 링크</div><div class='b' style='font-size:44px;color:#111;margin:4px 0 10px'>%s원</div><div style='background:#111;color:#fff;border-radius:16px;text-align:center;padding:14px;font-size:28px;font-weight:800'>카드로 결제하기</div></div>"
      "<div style='margin-top:22px;background:#fff;border-radius:34px 34px 34px 8px;padding:22px 30px;font-size:32px;font-weight:700;color:#222;box-shadow:0 8px 24px rgba(0,0,0,.12)'>%s</div></div>") % (e(d.get('i1') or '결제 링크 보내드려요'), e(d.get('i2') or '50,000'), e(d.get('i3') or '결제했어요 👍'))

def thumb(t, d):
    L = d.get('layout') or 'plain'
    title = lines(d['title1'] + ('/' + d['title2'] if d['title2'] else ''))
    badge = e(d['badge'])
    if L == 'phone':
        body = ("<div style='position:absolute;left:64px;top:56px;background:%s;color:%s;font-weight:900;font-size:34px;padding:8px 28px;border-radius:99px'>%s</div>"
                "<div class='b' style='position:absolute;left:64px;top:170px;font-size:100px;line-height:1.15;color:%s;letter-spacing:-3px'>%s</div>%s") % (t['ac'], t['on'], badge, t['ink'], title, _phone(t, d))
    elif L == 'chat':
        body = ("<div class='b' style='position:absolute;left:64px;top:60px;font-size:92px;line-height:1.15;color:%s;letter-spacing:-3px'>%s</div>%s") % (t['ink'], title, _chat(t, d))
    elif L == 'bignum':
        big = e(d['amount'] or '1'); unit = e(d['chip'] or '시간')
        body = ("<div style='position:absolute;left:64px;top:52px;color:%s;font-weight:900;font-size:36px'>%s</div>"
                "<div class='b' style='position:absolute;left:52px;top:100px;font-size:300px;line-height:1;color:%s;letter-spacing:-12px'>%s<span style='font-size:150px;letter-spacing:-4px'>%s</span></div>"
                "<div class='b' style='position:absolute;left:64px;bottom:50px;font-size:78px;color:%s;letter-spacing:-2px'>%s</div>"
                "<div style='position:absolute;right:64px;bottom:62px;font-size:30px;color:%s;font-weight:700;text-align:right;line-height:1.5'>%s</div>") % (t['ac'], badge, t['ink'], big, unit, t['ac'], lines(d['title1']), t['mu'], lines(d['sub']))
    else:  # plain: 큰 제목 + 하단 정보 칩
        body = ("<div style='position:absolute;left:64px;top:52px;background:%s;color:%s;font-weight:900;font-size:34px;padding:8px 28px;border-radius:99px'>%s</div>"
                "<div style='position:absolute;right:64px;top:62px;font-weight:700;font-size:30px;color:%s'>tycoonkr.com</div>"
                "<div class='b' style='position:absolute;left:64px;top:170px;font-size:128px;line-height:1.1;color:%s;letter-spacing:-4px'>%s</div>"
                "<div style='position:absolute;left:64px;bottom:50px;background:%s;color:%s;font-weight:800;font-size:42px;padding:14px 28px;border-radius:18px'>%s</div>") % (t['ac'], t['on'], badge, t['mu'], t['ink'], title, t['card'], t['ink'], e(d['sub']))
    return 1200, 630, body

def card(t, d):
    L = d.get('layout') or 'rows'
    items = [d[k] for k in ('i1', 'i2', 'i3', 'i4') if d.get(k)]
    head = ("<div style='font-size:36px;font-weight:900;color:%s'>%s</div><div class='b' style='font-size:82px;color:%s;line-height:1.15;margin-top:8px'>%s</div>") % (t['ac'], e(d['badge']), t['ink'], lines(d['title1'] + ('/' + d['title2'] if d['title2'] else '')))
    foot = ("<div style='position:absolute;left:70px;right:70px;bottom:46px;font-size:30px;font-weight:700;color:%s'>%s</div>" % (t['mu'], e(d['sub']))) if d['sub'] else ''
    if L == 'steps':
        rows = ''
        for i, it in enumerate(items):
            a = parts(it); sub = a[1] if len(a) > 1 else ''
            line = '' if i == len(items) - 1 else "<div style='width:10px;height:78px;background:%s;opacity:.3'></div>" % t['ac']
            rows += ("<div style='display:flex;gap:36px;align-items:flex-start'><div style='display:flex;flex-direction:column;align-items:center'><div class='b' style='width:112px;height:112px;border-radius:50%%;background:%s;color:%s;font-size:56px;display:flex;align-items:center;justify-content:center'>%d</div>%s</div>"
                     "<div style='padding-top:6px'><div class='b' style='font-size:68px;color:%s'>%s</div><div style='font-size:36px;font-weight:700;color:%s;margin-top:8px'>%s</div></div></div>") % (t['ac'], t['on'], i + 1, line, t['ink'], e(a[0]), t['mu'], e(sub))
        body = "<div style='position:absolute;left:70px;top:64px;right:70px'>%s<div style='margin-top:40px'>%s</div></div>%s" % (head, rows, foot)
    elif L == 'bars':   # i = 이름|설명|길이(10~100)
        rows = ''
        for it in items:
            a = parts(it); w = int(a[2]) if len(a) > 2 else 50
            rows += ("<div style='margin-top:34px'><div style='display:flex;align-items:baseline;gap:20px'><div class='b' style='font-size:60px;color:%s'>%s</div><div style='font-size:34px;font-weight:700;color:%s'>%s</div></div>"
                     "<div style='margin-top:14px;height:86px;border-radius:43px;background:%s;position:relative'><div style='position:absolute;left:0;top:0;height:100%%;width:%d%%;background:%s;border-radius:43px;display:flex;align-items:center;justify-content:flex-end;padding-right:30px;color:%s;font-weight:900;font-size:36px'>입금</div></div></div>") % (t['ink'], e(a[0]), t['mu'], e(a[1] if len(a) > 1 else ''), t['card'], w, t['ac'], t['on'])
        body = "<div style='position:absolute;left:70px;right:70px;top:64px'>%s<div style='margin-top:10px'>%s</div></div>%s" % (head, rows, foot)
    elif L == 'panels':  # i = 제목|설명
        pans = ''
        cols = [t['ac'], t['ink'], t['ac2']]
        for i, it in enumerate(items[:3]):
            a = parts(it); bg = cols[i]
            fg = t['on'] if bg == t['ac'] else (t['bg'] if bg == t['ink'] else t['ink'])
            pans += ("<div style='flex:1;background:%s;border-radius:36px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;color:%s;padding:20px;text-align:center'><div class='b' style='font-size:64px'>%s</div><div style='font-size:34px;font-weight:700;opacity:.9'>%s</div></div>") % (bg, fg, e(a[0]), e(a[1] if len(a) > 1 else ''))
        body = "<div style='position:absolute;inset:48px;display:flex;flex-direction:column;gap:22px'><div style='padding:6px 16px'>%s</div><div style='display:flex;flex-direction:column;gap:22px;flex:1'>%s</div></div>" % (head, pans)
    else:  # rows: 번호 + 한 줄 카드
        rows = ''
        for i, it in enumerate(items):
            a = parts(it)
            rows += ("<div style='background:%s;border-radius:30px;padding:0 36px;height:210px;display:flex;align-items:center;gap:34px;box-shadow:0 10px 0 rgba(0,0,0,.12)'><div class='b' style='font-size:110px;color:%s;width:76px;text-align:center'>%d</div><div><div class='b' style='font-size:48px;color:%s;line-height:1.2'>%s</div><div style='font-size:32px;font-weight:700;color:%s;margin-top:6px'>%s</div></div></div>") % (t['card'], t['ac'], i + 1, t['ink'], e(a[0]), t['mu'], e(a[1] if len(a) > 1 else ''))
        body = "<div style='position:absolute;left:64px;right:64px;top:60px'>%s</div><div style='position:absolute;left:64px;right:64px;top:300px;display:flex;flex-direction:column;gap:20px'>%s</div>%s" % (head, rows, foot)
    return 1080, 1080, body

def build(d):
    """d: front matter dict (render.py meta). 반환 (w,h,html). tall(핀)은 card 와 같은 구도를 세로로 늘려 사용."""
    t = THEMES.get(d.get('theme') or 't1', THEMES['t1'])
    size = d.get('size')
    if size in ('sq', 'tall'):
        w, h, body = card(t, d)
        if size == 'tall': w, h = 1000, 1500; body = "<div style='transform:scale(.925);transform-origin:0 0;position:absolute;left:0;top:0;width:1080px;height:1080px'>%s</div>" % body
    else:
        w, h, body = thumb(t, d)
    doc = "<style>%s</style><div class='f' style='width:%dpx;height:%dpx;background:%s'>%s</div>" % (CSS, w, h, t['bg'], body)
    return w, h, doc
