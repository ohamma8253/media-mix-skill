# results/*/채점.md 표의 판정 칸을 모아 시나리오 × 모델 표(tsv)로 낸다.
import re, glob, os, sys
KEYS = ['끝까지 갔나','결과 박스','금액 합','한도','하한','질문 4개 이상 발화','들은 것 밖 단정','확인 못 함 / 검사 못 함 처리','오류 11개 중 놓친 것']
rows = []
for f in sorted(glob.glob('results/*/채점.md')):
    run = f.split('/')[1]; t = open(f, encoding='utf-8').read()
    got = {}
    for line in t.splitlines():
        m = re.match(r'^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|', line)
        if not m: continue
        k, v = m.group(1), m.group(2)
        for key in KEYS:
            if k.startswith(key[:5]) and key not in got:
                got[key] = re.sub(r'\*\*', '', v)[:40]
    b = re.search(r's3 브랜드 키워드 오류 5:\s*([^\n]+)', t)
    rows.append([run] + [got.get(k, '?') for k in KEYS] + [b.group(1).strip()[:20] if b else ''])
print('\t'.join(['회차'] + KEYS + ['s3 브랜드 오류5']))
for r in rows: print('\t'.join(r))
