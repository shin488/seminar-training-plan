from weasyprint import HTML
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = script_dir + '/images/'
pdf_path = os.path.join(script_dir, 'seminar-plan.pdf')

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;600;700&display=swap');
@page { size: A4 portrait; margin: 14mm 12mm; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Noto Sans JP', sans-serif; font-size: 9pt; line-height: 1.5; color: #1a1a2e; }
h2 { font-size: 14pt; font-weight: 700; margin: 12pt 0 4pt; color: #1a1a2e; }
h2 .en { display: block; font-size: 8pt; font-weight: 500; color: #4f46e5; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 2pt; }
h3 { font-size: 10pt; font-weight: 700; margin-bottom: 3pt; }
h4 { font-size: 9pt; font-weight: 700; margin-bottom: 3pt; }
p { font-size: 8pt; color: #4a4e6a; margin-bottom: 3pt; }
.desc { font-size: 8.5pt; color: #4a4e6a; margin-bottom: 8pt; }
ul { margin: 2pt 0 2pt 12pt; }
li { font-size: 8pt; color: #4a4e6a; margin-bottom: 1.5pt; }
td { vertical-align: top; }
.tag { display: inline-block; font-size: 7pt; padding: 1.5pt 5pt; border-radius: 3pt; margin: 1pt 1.5pt; background: #eef2ff; color: #4f46e5; }
.tag-warm { background: #fffbeb; color: #92400e; }
.card { border: 1px solid #d0d0d0; border-radius: 6pt; padding: 8pt; margin-bottom: 4pt; }
.purpose-card { color: #fff; border-radius: 8pt; padding: 10pt; min-height: 55pt; }
.purpose-card p { color: rgba(255,255,255,0.8); }
.purpose-card .num { font-size: 28pt; font-weight: 700; opacity: 0.15; float: right; line-height: 1; }
.purpose-card h3 { font-size: 14pt; }
.flow-item { display: inline-block; font-size: 8pt; padding: 3pt 8pt; border: 1px solid #d0d0d0; border-radius: 4pt; background: #fff; margin: 1pt; }
.flow-arrow { display: inline-block; font-size: 9pt; color: #4f46e5; font-weight: 700; margin: 0 1pt; }
.day-badge { color: #fff; font-size: 9pt; font-weight: 700; padding: 6pt 10pt; letter-spacing: 0.5pt; }
.day1 { background: linear-gradient(135deg, #4f46e5, #06b6d4); }
.day2 { background: linear-gradient(135deg, #7c3aed, #a855f7); }
.tl-time { font-size: 7pt; font-weight: 600; color: #4f46e5; white-space: nowrap; padding-top: 1pt; }
.tl-body strong { font-size: 8pt; display: block; }
.tl-body p { font-size: 6.5pt; color: #8b8fa8; margin-bottom: 0; }
.tl-hl { background: #eef2ff; border-radius: 3pt; }
.tl-green { background: #f0fdf4; border-radius: 3pt; }
.budget-row { border-bottom: 1px solid #f0f1f6; padding: 5pt 0; font-size: 9pt; }
.budget-total { background: #eef2ff; font-weight: 700; color: #4f46e5; border-radius: 3pt; }
.spot-img { width: 100%; border-radius: 4pt; }
.spot-name { font-size: 7.5pt; font-weight: 600; }
.spot-dist { font-size: 6.5pt; color: #8b8fa8; }
.map-img { width: 100%; border-radius: 4pt; border: 1px solid #d0d0d0; }
.border-top-ai { border-top: 2.5pt solid #6366f1; }
.border-top-iot { border-top: 2.5pt solid #0d9488; }
.border-top-dx { border-top: 2.5pt solid #e11d48; }
"""

def img(name):
    return f'{img_dir}{name}'

def row_3cols(c1, c2, c3, widths='30%,30%,30%'):
    return f'''<table width="100%" cellpadding="0" cellspacing="4pt" style="table-layout:fixed;">
<tr>
<td width="{widths.split(',')[0]}">{c1}</td>
<td width="{widths.split(',')[1]}">{c2}</td>
<td width="{widths.split(',')[2]}">{c3}</td>
</tr></table>'''

def row_2cols(c1, c2, w1='48%', w2='48%'):
    return f'''<table width="100%" cellpadding="0" cellspacing="4pt" style="table-layout:fixed;">
<tr>
<td width="{w1}">{c1}</td>
<td width="{w2}">{c2}</td>
</tr></table>'''

def row_1col(c1):
    return f'<div style="margin-bottom:4pt">{c1}</div>'

purpose_ai = '<div class="purpose-card" style="background:#6366f1"><span class="num">01</span><h3>AI</h3><p>人工知能技術の実践的活用</p></div>'
purpose_iot = '<div class="purpose-card" style="background:#0d9488"><span class="num">02</span><h3>IoT</h3><p>データ収集と可視化</p></div>'
purpose_dx = '<div class="purpose-card" style="background:#e11d48"><span class="num">03</span><h3>DX</h3><p>デジタルトランスフォーメーション推進</p></div>'

ai_cards = row_2cols(
    '<div class="card"><h4>画像認識・外観検査</h4><p>カメラで製品の傷や欠陥を自動検出。人の目による検査との違いを学べる。</p></div>',
    '<div class="card"><h4>異常検知</h4><p>機械の振動や温度の変化から故障の兆候を検出。</p></div>'
) + row_2cols(
    '<div class="card"><h4>需要予測・在庫管理</h4><p>過去のデータを分析し、生産量や在庫を最適化。</p></div>',
    '<div class="card"><h4>ディープラーニング応用</h4><p>品質管理や検査工程での活用事例。</p></div>'
)

iot_sensor = '<div class="card"><h4>センサーによるデータ収集</h4><div><span class="tag">🌡 温度</span><span class="tag">💧 湿度</span><span class="tag">📳 振動</span><span class="tag">⏲ 圧力</span><span class="tag">⚡ 電力使用量</span></div></div>'
iot_comm = '<div class="card"><h4>省電力無線通信</h4><p>LPWAなどの省電力無線通信。</p></div>'
iot_rfid = '<div class="card"><h4>RFID管理</h4><p>RFIDによる部品・製品管理。</p></div>'
iot_flow = '<div class="card" style="background:#eef2ff;border-color:#e0e7ff"><h4>IoTデバイスの仕組み</h4><div style="text-align:center;margin-top:4pt"><span class="flow-item">センサー</span><span class="flow-arrow">→</span><span class="flow-item">ゲートウェイ</span><span class="flow-arrow">→</span><span class="flow-item">クラウド</span><span class="flow-arrow">→</span><span class="flow-item">可視化</span></div></div>'

dx_rows = ''
dx_items = [
    ('01', '生産ラインの見える化', '稼働率のリアルタイム表示'),
    ('02', '生産工程の効率化', ''),
    ('03', 'データ活用による経営改善', ''),
    ('04', '人手不足への対応', ''),
    ('05', 'ペーパーレス化・デジタル化', ''),
]
for num, title, desc in dx_items:
    d = f'<p>{desc}</p>' if desc else ''
    dx_rows += f'<tr><td style="font-size:11pt;font-weight:700;color:#d0d0d0;width:24pt;text-align:right;padding-right:4pt">{num}</td><td><strong>{title}</strong>{d}</td></tr>'

facility_exhibit = f'''<div class="card" style="padding:0;overflow:hidden">
<img src="{img('facility-exhibit.jpg')}" style="width:100%;height:55pt;object-fit:cover;display:block">
<div style="padding:6pt"><span class="tag">展示体験室</span><h4>最新技術を体験</h4><p>民間企業15社のブースで、プレス加工機の見える化、生産ラインIoT、AI画像検査など最新のIoT技術を体験。</p></div></div>'''
facility_workshop = f'''<div class="card" style="padding:0;overflow:hidden">
<img src="{img('facility-workshop.jpg')}" style="width:100%;height:55pt;object-fit:cover;display:block">
<div style="padding:6pt"><span class="tag">IoT研修室</span><h4>ワークショップ実習</h4><p>Raspberry Pi + Node-REDを用いたIoT実習やAI活用ビッグデータ解析など。</p></div></div>'''
facility_tags = '<div class="card"><h4>主な展示内容</h4><div><span class="tag tag-warm">プレス機の稼働状況見える化</span><span class="tag tag-warm">生産ラインの稼働管理</span><span class="tag tag-warm">工作機械の遠隔監視</span><span class="tag tag-warm">AI画像自動監視</span><span class="tag tag-warm">RFID部品管理</span><span class="tag tag-warm">LPWAセンサーデバイス</span><span class="tag tag-warm">電動サーボプレスIoT化</span><span class="tag tag-warm">エネルギー消費量の見える化</span></div></div>'

def schedule_row(time, title, desc='', hl='', green=''):
    cls = ' tl-hl' if hl else (' tl-green' if green else '')
    d = f'<p>{desc}</p>' if desc else ''
    return f'<tr><td class="tl-time" style="padding:2pt 3pt 2pt 0">{time}</td><td style="padding:2pt 3pt"><div class="card{cls}" style="margin:0;padding:3pt 5pt"><strong>{title}</strong>{d}</div></td></tr>'

day1_rows = ''
day1_items = [
    ('9:00', '受付・オリエンテーション', '研修の概要説明、チーム編成'),
    ('9:30', '展示体験室ツアー', '15社の最新IoT機器を実際に見学・体験'),
    ('10:30', 'IoT基礎講義', 'センサー、通信技術、クラウド連携の基礎知識'),
    ('12:00', '昼食', ''),
    ('13:00', '実習（Raspberry Pi + Node-RED）', 'センサーデータの収集・可視化を手を動かして体験', True, False),
    ('15:00', '実習まとめ・質疑応答', ''),
    ('16:00', 'チェックイン・自由時間', ''),
    ('17:00', '牧ヶ谷湧水公園', '徒歩5〜10分。湧水や緑を楽しむ', False, True),
    ('17:30', '光鏡院', '徒歩5分。地域の歴史と文化を感じる寺院', False, True),
    ('18:00', '千手寺', '徒歩5分。静かな境内を散策', False, True),
    ('19:00〜', '夕食・宿泊', ''),
]
for item in day1_items:
    if len(item) == 5:
        day1_rows += schedule_row(*item)
    else:
        day1_rows += schedule_row(item[0], item[1], item[2])

day2_rows = ''
day2_items = [
    ('8:00', 'チェックアウト', ''),
    ('9:00', '静岡県美術館', '駅前再開発ビル「Cenova」内', False, True),
    ('10:30', '駿府城公園', '家康ゆかりの城址。天守台や石垣を散策', False, True),
    ('12:00', '昼食', '静岡せいか・うなぎ等を味わう'),
    ('13:30', '三保松原', '車で約30分。日本三景の一つ', False, True),
    ('15:30', '清水港周辺散策', '海沿いを歩きながら現地の雰囲気を楽しむ', False, True),
    ('16:30', '静岡駅へ戻る', 'バスまたはタクシーで約30分'),
    ('17:00', 'お土産選び・散策', '静岡駅周辺で土産物店を回る'),
    ('19:00', '新幹線で帰路', '静岡駅よりお好きな方向へ出発', True, False),
]
for item in day2_items:
    if len(item) == 5:
        day2_rows += schedule_row(*item)
    else:
        day2_rows += schedule_row(item[0], item[1], item[2])

outcomes_ai = '''<div class="card border-top-ai"><h4 style="color:#6366f1">AI</h4><ul>
<li>画像認識・外観検査の仕組みを理解できる</li>
<li>異常検知の基本概念と活用方法を学べる</li>
<li>需要予測のデータ分析手法を把握できる</li>
<li>ディープラーニングの製造業応用を知ることができる</li></ul></div>'''
outcomes_iot = '''<div class="card border-top-iot"><h4 style="color:#0d9488">IoT</h4><ul>
<li>センサーからクラウドまでのデータフローを理解できる</li>
<li>Raspberry Pi + Node-REDでの実装を体験できる</li>
<li>LPWAなどの省電力無線通信の特徴を学べる</li>
<li>自社工場でのIoT導入イメージを具体化できる</li></ul></div>'''
outcomes_dx = '''<div class="card border-top-dx"><h4 style="color:#e11d48">DX</h4><ul>
<li>生産ラインの見える化手法を学べる</li>
<li>データ活用による経営改善の考え方を理解できる</li>
<li>人手不足・ペーパーレス化の具体的対応を知ることができる</li>
<li>自社の課題を明確化する力が身につく</li></ul></div>'''

def spot_cell(img_name, name, dist):
    return f'''<td style="text-align:center;padding:2pt">
<img src="{img(img_name)}" class="spot-img" style="height:45pt">
<div class="spot-dist">{dist}</div>
<div class="spot-name">{name}</div></td>'''

spots_row1 = row_3cols(
    spot_cell('spot-yusui.jpg', '牧ヶ谷湧水公園', '徒歩5〜10分'),
    spot_cell('spot-kojinguin.jpg', '光鏡院', '徒歩5分'),
    spot_cell('spot-senjuji.jpg', '千手寺', '徒歩5分'),
)
spots_row2 = row_3cols(
    spot_cell('spot-museum.jpg', '静岡県美術館', '駅前'),
    spot_cell('spot-castle.jpg', '駿府城公園', '徒歩15分'),
    spot_cell('spot-fuji.jpg', '三保松原', '車で約30分'),
)

access_left = '''<div class="card">
<div style="margin-bottom:5pt"><span style="font-size:7pt;font-weight:600;color:#8b8fa8;letter-spacing:1pt;text-transform:uppercase">所在地</span><p>〒421-1298 静岡県静岡市葵区牧ヶ谷2078<br>（静岡県工業技術研究所内）</p></div>
<div style="margin-bottom:5pt"><span style="font-size:7pt;font-weight:600;color:#8b8fa8;letter-spacing:1pt;text-transform:uppercase">電話番号</span><p>054-278-3027</p></div>
<div style="margin-bottom:5pt"><span style="font-size:7pt;font-weight:600;color:#8b8fa8;letter-spacing:1pt;text-transform:uppercase">メール</span><p>sk-kd@pref.shizuoka.lg.jp</p></div>
<div><span style="font-size:7pt;font-weight:600;color:#8b8fa8;letter-spacing:1pt;text-transform:uppercase">開所時間</span><p>平日 9:00〜17:00</p></div></div>'''

access_right = '''<div class="card"><h4>交通手段</h4>
<div style="margin-bottom:5pt"><strong>🚄 新幹線</strong><p>東海道新幹線「静岡駅」下車</p></div>
<div style="margin-bottom:5pt"><strong>🚌 バス</strong><p>しずてつジャストライン「県工業技術研究所」下車 徒歩約3分</p></div>
<div><strong>🚗 車</strong><p>東名高速道路「静岡IC」から約20分<br>牧ヶ谷ICから約5分</p></div></div>'''

budget_rows = '''<div class="card" style="padding:0;overflow:hidden">
<div class="budget-row" style="padding:5pt 10pt">🚄 交通費<span style="float:right">￥13,000</span></div>
<div class="budget-row" style="padding:5pt 10pt">🏨 宿泊費<span style="float:right">￥5,000〜10,000</span></div>
<div class="budget-row" style="padding:5pt 10pt">🍜 その他<span style="float:right">￥7,000〜12,000</span></div>
<div class="budget-row budget-total" style="padding:6pt 10pt">合計<span style="float:right">￥25,000〜30,000</span></div></div>'''

body = f'''<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8"><style>{CSS}</style></head>
<body>

<h2>研修の目的</h2>
{row_3cols(purpose_ai, purpose_iot, purpose_dx)}

<h2><span class="en">AI</span>人工知能</h2>
{ai_cards}

<h2><span class="en">IoT</span>モノのインターネット</h2>
{row_1col(iot_sensor)}
{row_2cols(iot_comm, iot_rfid)}
{row_1col(iot_flow)}

<h2><span class="en">DX</span>デジタルトランスフォーメーション</h2>
<table width="100%" cellpadding="0" cellspacing="0"><tbody>
{dx_rows}</tbody></table>

<h2><span class="en">Facility</span>施設紹介</h2>
<p class="desc">静岡県AI・IoT推進ラボは、県内の中小企業へのIoT導入支援拠点として、静岡県工業技術研究所内に設置されています。</p>
{row_2cols(facility_exhibit, facility_workshop)}
{row_1col(facility_tags)}

<h2><span class="en">Schedule</span>1泊2日スケジュール</h2>
<p class="desc">実習と観光を両立する、充実した2日間</p>
<table width="100%" cellpadding="0" cellspacing="4pt" style="table-layout:fixed"><tr>
<td width="48%" style="vertical-align:top">
<div class="day-badge day1">DAY 1 — 実習 &amp; 観光</div>
<table width="100%" cellpadding="0" cellspacing="0"><tbody>{day1_rows}</tbody></table>
</td>
<td width="48%" style="vertical-align:top">
<div class="day-badge day2">DAY 2 — 観光 &amp; 帰路</div>
<table width="100%" cellpadding="0" cellspacing="0"><tbody>{day2_rows}</tbody></table>
</td></tr></table>

<h2><span class="en">Outcomes</span>学習成果</h2>
<p class="desc">この研修を通じて得られる知識とスキル</p>
{row_3cols(outcomes_ai, outcomes_iot, outcomes_dx)}

<h2><span class="en">Sightseeing</span>観光スポット</h2>
<p class="desc">研修の合間に、牧ヶ谷の自然と文化を</p>
{spots_row1}
{spots_row2}

<h2><span class="en">Access</span>アクセス</h2>
{row_2cols(access_left, access_right)}
<img src="{img('map-static.png')}" class="map-img" style="margin-top:4pt">

<h2><span class="en">Budget</span>予算（概算）</h2>
{budget_rows}

</body></html>'''

HTML(string=body, base_url=script_dir + '/').write_pdf(pdf_path, presentational_hints=True)
print(f'PDF generated: {pdf_path}')
