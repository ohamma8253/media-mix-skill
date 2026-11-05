# transcript.md에서 `스킬:` 차례마다 사용자가 답할 질문 수를 센다(번호 줄 중 물음표가 있는 줄 + 번호 없는 물음표 줄).
# 사용: python3 qcount.py <transcript.md>...   출력: 파일 · 스킬 차례 수 · 사용자 차례 수 · 4개 이상 차례 수 · 최대
import re, sys
for p in sys.argv[1:]:
    t = open(p, encoding='utf-8').read()
    parts = re.split(r'^\**(스킬|사용자)\**\s*[:：]', t, flags=re.M)
    turns = list(zip(parts[1::2], parts[2::2]))
    sk = [b for a, b in turns if a == '스킬']; us = [b for a, b in turns if a == '사용자']
    counts = []
    for b in sk:
        b = re.sub(r'```.*?```', '', b, flags=re.S)
        q = 0
        for line in b.splitlines():
            s = line.strip()
            if not s or s.startswith('|') or s.startswith('>'):
                continue
            if '?' in s or '？' in s:
                q += 1
        counts.append(q)
    big = [c for c in counts if c >= 4]
    print(f"{p}\t스킬 {len(sk)}\t사용자 {len(us)}\t4개 이상 {len(big)}\t최대 {max(counts) if counts else 0}")
