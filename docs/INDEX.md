# 문서 색인

결론: 이 저장소의 정본은 harness/·skills/·templates/·adapters/에 있고, docs/tasks/에는 작업 이력만 쌓입니다.

## 저장소 문서 구조
| 위치 | 내용 |
| --- | --- |
| AGENTS.md | 저장소 유지 규칙과 하네스 핵심 규칙 |
| harness/HARNESS.md | 하네스 설계 기록(정본) |
| skills/<이름>/SKILL.md | 스킬 정본 7종 (사본: .agents/skills, .claude/skills) |
| templates/ | 소비 프로젝트에 복사하는 핵심 규칙 템플릿 |
| adapters/cursor/ | Cursor 전용 규칙 어댑터 |
| docs/tasks/ | 작업 문서(기획용 하나로 단일화). 과거 위임 문서(brief)는 이력으로만 보존 |
| docs/INDEX.md | 이 색인 |

## 파일 이름 규칙
- 기획용 작업 문서: `<순번>-<작업명>.md`
- 위임용 작업 문서(brief): 단일 작업 문서 체제로 통합됨. 새로 만들지 않고, 과거 파일(`<순번>-<작업명>.brief-<번호>.md`, 초기 `<순번>-brief-<번호>.md`)은 이력으로 보존합니다.
- 상태 표기: planned → in-progress → done. 대체된 문서는 superseded, 보관만 하는 문서는 archived.

## 작업 이력 (docs/tasks/)
위임 문서(brief) 열의 파일은 모두 '단일 작업 문서 체제로 통합됨' 이전의 이력입니다.

| 순번 | 작업 | 기획 문서 | 위임 문서(brief, 이력) | 상태 |
| --- | --- | --- | --- | --- |
| 01 | 하네스 패키지 저장소 구성 | 01-package.md | 01-package.brief-01.md | done |
| 01 | strata-shift 하네스 이식 | 01-strata-shift-harness-sync.md | - | superseded (16번으로 통합) |
| 02 | README AI 자동 적용 | 02-ai-auto-apply.md | 02-ai-auto-apply.brief-01.md | done |
| 02 | 파일 단일 책임·테스트 배치 공통 규칙 | 02-common-file-srp-test-placement.md | 02-common-file-srp-test-placement.brief-1.md | done |
| 03 | 하네스 경로 프로젝트 기준화 | 03-project-paths.md | 03-project-paths.brief-01.md | done |
| 04 | 코드 생성 금지 규칙 | 04-no-code-gen.md | 04-no-code-gen.brief-01.md | done |
| 05 | adapters/claude 제거 | 05-remove-adapter-claude.md | 05-brief-01.md | done |
| 06 | 이 저장소 자기 적용 | 06-project-apply.md | 06-brief-01.md, 06-brief-02.md | done |
| 07 | 리뷰 위임 프롬프트 보정 | 07-review-prompt.md | - | done |
| 08 | 단순 위임 기준 추가 | 08-simple-delegation.md | - | done |
| 09 | 브리프 출력 규칙 추가 | 09-brief-output.md | - | done |
| 10 | 리뷰 minor 5건 보정 | 10-review-minor.md | - | done |
| 11 | 브리프의 하네스 준수·언어 고정 | 11-brief-harness-language.md | - | done |
| 12 | 위임 프롬프트에 하네스 주입 | 12-harness-injection.md | 12-harness-injection.brief-01.md | done |
| 12 | 위임 브리프 초안(보관) | 12.new-delegation-brief.md | - | archived |
| 13 | 사용자 언어·존댓말·eli5 명확성 | 13-user-language-eli5-clarity.md | - | done |
| 14 | 대화·컨텍스트 효율 | 14-conversation-context-efficiency.md | - | done |
| 15 | eli5-clarity 스킬 정본 | 15-eli5-clarity-skill.md | - | done |
| 16 | 하네스 전체 점검·리밸런싱 | 16-harness-rebalancing.md | 16-harness-rebalancing.brief-01.md, brief-02.md, brief-03.md | done |
| 17 | 서브에이전트 개발 하네스 전달 강제 | 17-subagent-harness-delivery.md | - | done |
| 18 | 재사용 사다리·의존성 절제·호출부 확인 | 18-reuse-ladder-and-caller-check.md | - | done |

## 16번 작업 단위
- 작업 1: 정본·템플릿·어댑터·README 개편 (brief-01, 단일 작업 문서 체제로 통합됨)
- 작업 2: 스킬 7종 개편과 3벌 동기화 (brief-02, 단일 작업 문서 체제로 통합됨)
- 작업 3: docs/tasks 정리와 이 색인 신설 (brief-03, 단일 작업 문서 체제로 통합됨)
- 작업 4: 통합 인라인 검증과 전체 리뷰
- 작업 5: 추가 요구 반영 (공통·부모·자식 역할 구분, 단일 작업 문서와 포인터 샌드위치, 코드 주석 eli5-clarity, 조건부 리서치)

## 17번 작업 단위
- 작업 1: 부모 세션 하네스 주입 의무화, dev-principles 전 항목(2~11절 전체) 전달 통일, 파일 삭제 시 대상·이유·근거 설명 강제

## 18번 작업 단위
- 작업 1: 재사용 사다리와 소수 줄용 새 의존성 금지를 `dev-principles` 3절에 반영하고 3벌 동기화
- 작업 2: 버그 수정·심볼 변경 시 호출부 검색·공유 코드 한곳 수정·범위 밖 보고를 `dev-principles` 11절에 반영하고 색인에 18번 추가
- 작업 3: 재사용 사다리 1단계(생략 선언)를 제거해 4단계로 줄이고, 작업 회피·파일 몰아넣기 금지를 3절·4절에 명시하며, 11절에 범위 밖 호출부 후속 작업 이관을 반영
