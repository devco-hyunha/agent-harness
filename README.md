# agent-harness

기획과 개발을 한 흐름으로 돕는 하네스를 여러 AI 코딩 도구에서 함께 쓰기 위한 저장소입니다. 요구 수렴, 작업 문서, 서브에이전트 위임, 독립 리뷰, 상태 갱신을 같은 절차로 진행하도록 규칙과 스킬을 제공합니다.

## 구성

| 폴더·파일 | 설명 |
|---|---|
| harness/ | 하네스 설계 기록(HARNESS.md). 정본입니다. |
| skills/ | Agent Skills 표준 스킬 7개: plan-harness, build-harness, review-harness, delegation-brief, proofread-harness, eli5-clarity, dev-principles |
| templates/ | 프로젝트에 넣는 핵심 규칙 블록(AGENTS.harness.md)과 CLAUDE.md 연결 파일 |
| adapters/ | 도구별 보조 파일. cursor는 규칙(.mdc) 2개: agent-harness.mdc(AGENTS.md 브리지), tool-call.mdc(도구 호출 보정) |
| VERSION | 하네스 버전. 적용받는 프로젝트에는 harness/VERSION으로 복사합니다. |
| .gitattributes | `* text=auto eol=lf`. 줄바꿈 차이로 생기는 가짜 변경을 막습니다. |

## 지원 도구

주력 도구 4개의 기준입니다. 정본은 harness/HARNESS.md 2절입니다.

| 도구 | 규칙 파일 | 스킬 위치 | 서브에이전트 |
|---|---|---|---|
| Claude Code | CLAUDE.md(@AGENTS.md 연결) | .claude/skills | 서브에이전트를 열 수 있고 모델 단계를 지정합니다. |
| Cursor | AGENTS.md, .cursor/rules/*.mdc(어댑터) | .agents/skills(.claude/skills도 읽음) | 서브에이전트를 열 수 있고 모델을 지정합니다. |
| Codex | AGENTS.md | .agents/skills | 도구가 지원하는 방식을 따릅니다. 없으면 메인이 단계별로 진행하고 리뷰는 새 대화에서 합니다. |
| OpenCode | AGENTS.md(있으면 CLAUDE.md는 읽지 않음) | .agents/skills만 복사 권장 | 위와 같습니다. |

- OpenCode는 .agents/skills와 .claude/skills를 모두 탐색합니다. 이름 충돌 경고를 피하려면 .agents/skills에만 복사합니다.
- 서브에이전트 지원과 모델 지정은 도구와 버전마다 다릅니다. 호출 전에 도구 schema로 확인합니다.

보조 도구입니다.

| 도구 | 규칙 파일 | 스킬 위치 |
|---|---|---|
| Gemini CLI | GEMINI.md, AGENTS.md는 settings.json context.fileName 설정 필요 | .agents/skills |
| Antigravity | 프로젝트 AGENTS.md | .agents/skills |
| GitHub Copilot | 프로젝트 AGENTS.md, .github/copilot-instructions.md | .agents/skills, .github/skills |

## 베이스 + 프로젝트 오버레이

결론: 하네스는 읽기 전용 베이스이고, 프로젝트 고유 규칙은 한 곳에만 둡니다. 업데이트해도 고유 규칙이 남습니다.

- 마커 불변: AGENTS.md의 `<!-- agent-harness:begin -->`~`<!-- agent-harness:end -->` 블록과 harness/HARNESS.md는 직접 고치지 않습니다.
- 프로젝트 오버레이: 고유 규칙과 예외는 마커 바깥의 `## 프로젝트 오버레이` 절(분량이 크면 docs/PROJECT_RULES.md 링크 한 줄)에 둡니다.
- 안전 규칙 충돌: 더 엄격한 규칙은 오버레이가 우선합니다. 완화하는 규칙은 `[안전 예외 승인: N번]`을 명시한 때만 허용합니다.
- 버전과 줄바꿈: harness/VERSION과 .gitattributes(`eol=lf`)를 함께 둡니다.

## AI 자동 적용

사용자가 "readme.md를 읽고 하네스를 적용해줘."라고 요청하면, 에이전트는 서브에이전트를 열지 않고 메인이 직접 아래 순서를 따른다(Fast-track). 저장소 루트(이 README가 있는 곳)를 BASE, 적용받는 프로젝트 루트를 PROJ로 쓴다.

1. 자기 인식: 현재 도구가 지원 도구 표의 어떤 agent인지 확인한다. 표에 없는 도구에서는 공통 단계(3단계의 프로젝트 파일)만 적용하고 그 밖의 설정은 안내한다.
2. 계획 보고: 아래 단계에서 적용할 대상 파일과 설정 파일 편집 여부를 사용자에게 보고하고 승인을 받는다. 설정 파일(settings.json, AGENTS.md 병합 포함)을 편집할 때는 원본을 백업한 뒤 병합하고, 병합할 내용을 사용자에게 보여 확인한다.
3. 공통 파일 복사:
   - BASE/harness/HARNESS.md를 PROJ/harness/HARNESS.md에 복사한다. BASE/VERSION은 PROJ/harness/VERSION에 복사한다.
   - BASE/.gitattributes를 PROJ/.gitattributes에 적용한다. PROJ에 이미 있으면 `* text=auto eol=lf` 줄만 병합한다.
   - BASE/skills/<스킬>를 PROJ/.agents/skills/<스킬>에 복사한다. Claude Code에서는 PROJ/.claude/skills/<스킬>에 둔다. OpenCode에서는 .agents/skills만 둔다.
   - PROJ의 AGENTS.md에 templates/AGENTS.harness.md의 블록(agent-harness:begin~end)을 병합한다. AGENTS.md가 없으면 블록만으로 AGENTS.md를 만든다.
   - Claude Code에서는 templates/CLAUDE.md 내용(@AGENTS.md)으로 PROJ/CLAUDE.md를 만든다.
4. 도구별 설정 (2단계에서 승인받은 것만 실행):
   - Cursor: PROJ/.cursor/rules/에 adapters/cursor/agent-harness.mdc와 adapters/cursor/tool-call.mdc를 복사한다. 전역 User Rules는 settings.json의 user_rules에 templates/AGENTS.harness.md의 핵심 규칙이 들어 있는지 확인하고 없으면 병합한다.
   - Codex·OpenCode: PROJ/AGENTS.md에 핵심 규칙 블록이 있는지 확인하고 없으면 병합한다.
   - Gemini CLI: settings.json의 context.fileName에 AGENTS.md가 포함되어 있는지 확인한다.
   - GitHub Copilot: PROJ/.github/copilot-instructions.md에 핵심 규칙을 병합하고, PROJ/.github/skills에 스킬을 복사한다.
   - Antigravity: PROJ/AGENTS.md와 PROJ/.agents/skills를 적용한다. 전역 규칙 경로는 공식 문서로 확인하지 못했으므로 사용자에게 직접 확인을 요청한다.
5. 검증과 보고: PROJ에 복사·병합된 파일이 실제로 존재하는지 확인하고, AGENTS.md 블록이 한 번만 들어 있는지 확인한다. 사용자에게 적용한 위치를 목록으로 보고한다.

한계: Antigravity 전역 규칙 경로(~/.gemini/config/skills)와 Copilot CLI 경로는 공식 문서로 확인하지 못해 안내만 한다.

## 업데이트 (보존 방식)

이미 하네스를 쓰는 프로젝트를 갱신할 때는 서브에이전트나 별도 리뷰 세션을 열지 않고 메인이 직접 아래만 바꾸며(Fast-track), 프로젝트 고유 규칙은 건드리지 않는다.

1. 갱신 대상: AGENTS.md의 마커 블록, harness/HARNESS.md, 스킬 폴더, harness/VERSION, .cursor/rules의 어댑터 2개.
2. 보존 대상: 마커 바깥의 `## 프로젝트 오버레이` 절과 docs/PROJECT_RULES.md. 읽기만 하고 수정·삭제하지 않는다.
3. 블록 갱신은 begin~end 사이만 통째로 교체한다. 마커가 없으면 파일 끝에 새 블록을 추가한다.
4. 갱신 전 오버레이 안의 완화 규칙에 `[안전 예외 승인: N번]`이 있는지 확인하고, 없으면 사용자에게 보고한다.
5. 갱신 뒤 harness/VERSION이 BASE/VERSION과 같은지, 오버레이 절이 그대로인지 확인해 보고한다.

## 수동 설치

AI 자동 적용이 막힐 때 쓰는 폴백이다. GitHub에서 저장소를 내려받아 필요한 파일을 PROJ의 harness/, .agents/skills(도구별 스킬 위치), harness/VERSION에 복사한다. 업데이트는 위 "업데이트 (보존 방식)"을 따르고, 제거는 복사한 파일을 직접 지운다.
