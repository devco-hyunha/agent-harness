# AGENTS.md

이 문서는 agent-harness 저장소를 고치는 에이전트를 위한 규칙입니다. 이 저장소도 자기 하네스(harness/HARNESS.md)를 따릅니다.

## 정본 위치

- 하네스 설계 기록: harness/HARNESS.md
- 스킬: skills/<이름>/SKILL.md
- 핵심 규칙 템플릿: templates/AGENTS.harness.md, templates/CLAUDE.md
- 도구별 어댑터: adapters/claude, adapters/cursor
- 작업 문서: docs/tasks/

## 바꿀 때 함께 맞출 곳

HARNESS.md, 스킬, 핵심 규칙을 바꾸면 아래도 같이 확인합니다.

- README.md의 지원 도구 표
- templates/AGENTS.harness.md
- adapters/cursor/agent-harness.mdc (템플릿 본문과 같은 내용을 유지합니다.)
- adapters/claude/hooks.example.json
- 정본 규칙이 바뀌면 VERSION 파일의 버전을 올립니다.

## 스킬 형식

- Agent Skills 표준을 따릅니다. frontmatter에는 name과 description만 둡니다.
- name은 폴더명과 같고 소문자, 숫자, 하이픈만 씁니다. 정규식은 `^[a-z0-9]+(-[a-z0-9]+)*$`입니다.
- description은 1024자 이하입니다.
- 스킬 파일은 80줄 이하로 둡니다. dev-principles만 예외입니다.

## 언어 규칙

- 모든 문서는 한국어로 쓰고, 사용자 대상 문장은 존댓말로 씁니다.
- 코드, 경로, 명령, 식별자는 원문 그대로 둡니다.
- harness/, skills/, templates/, adapters/cursor/에는 특정 도구 전용 표현(Claude 고유 도구 이름, 개인 경로, 모델 이름)을 넣지 않습니다. 모델 이름 예시는 HARNESS.md 8절 표에만 둡니다.

## 검증 방법

변경 뒤 python -I로 아래를 확인합니다.

- 스킬 frontmatter: name이 폴더명과 같고 정규식에 맞으며, description이 1~1024자이고, 다른 필드가 없습니다.
- 금지 표현이 harness/, skills/, templates/, adapters/cursor/, adapters/claude/에 없습니다. 대상은 "C:\Users", "GLOBAL_HARNESS", "전역 하네스", "Agent 도구", "SendMessage"입니다. haiku, sonnet, opus는 HARNESS.md 8절 표에만 있어야 합니다.
- 스킬 줄 수가 80 이하(dev-principles 제외)이고 templates/AGENTS.harness.md가 40줄 이하입니다.
- adapters/claude/hooks.example.json이 json.load로 읽힙니다.

## 승인·안전 규칙

- 커밋, 푸시, 병합은 사용자가 허락한 뒤에만 합니다.
- 비밀 값과 .env는 넣지 않습니다.
- 리뷰 없이 PASS 처리하지 않습니다.
- 자세한 규칙은 harness/HARNESS.md 5절을 따릅니다.
