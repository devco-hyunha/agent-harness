import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

try:
    data = json.load(sys.stdin)
    ti = data.get("tool_input", {}) or {}
    desc = ti.get("description") or str(ti.get("command", ""))[:80]
    print(json.dumps({"systemMessage": "⏳ 터미널 실행: " + desc}, ensure_ascii=False))
except Exception as e:
    # 훅 실패가 도구 실행을 막지 않도록 오류만 기록한다.
    sys.stderr.write(f"bash_progress hook error: {e}\n")
