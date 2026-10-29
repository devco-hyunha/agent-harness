# agent-harness

기획과 개발을 한 흐름으로 돕는 하네스를 여러 AI 코딩 도구에서 함께 쓰기 위한 저장소입니다. 요구 수렴, 작업 문서, 서브에이전트 위임, 리뷰, 상태 갱신을 같은 절차로 진행하도록 규칙과 스킬을 제공합니다.

## 구성

| 폴더 | 설명 |
|---|---|
| harness/ | 하네스 설계 기록(HARNESS.md). 정본입니다. |
| skills/ | Agent Skills 표준 스킬 6개: plan-harness, build-harness, review-harness, delegation-brief, proofread-harness, dev-principles |
| templates/ | 프로젝트에 넣는 핵심 규칙 블록(AGENTS.harness.md)과 CLAUDE.md 연결 파일 |
| adapters/ | 도구별 보조 파일. cursor는 규칙(.mdc) |

## 지원 도구

| 도구 | 규칙 파일 | 스킬 위치 |
|---|---|---|
| Claude Code | CLAUDE.md(@AGENTS.md 연결) 또는 AGENTS.md | .claude/skills, .agents/skills |
| Codex CLI | 프로젝트 AGENTS.md | .agents/skills |
| Cursor | 프로젝트 AGENTS.md, .cursor/rules/*.mdc | .agents/skills(Cursor는 .claude/skills도 읽음) |
| Gemini CLI | GEMINI.md, AGENTS.md는 settings.json context.fileName 설정 필요 | .agents/skills |
| Antigravity | 프로젝트 AGENTS.md | .agents/skills |
| GitHub Copilot | 프로젝트 AGENTS.md, .github/copilot-instructions.md | .agents/skills, .github/skills |

## AI 자동 적용

사용자가 "readme.md를 읽고 하네스를 적용해줘."라고 요청하면, 에이전트는 아래 순서를 따른다. 저장소 루트(이 README가 있는 곳)를 BASE, 적용받는 프로젝트 루트를 PROJ로 쓴다.

1. 자기 인식: 현재 도구가 지원 도구 표의 어떤 agent인지 확인한다. 표에 없는 도구에서는 공통 단계(3단계의 프로젝트 파일)만 적용하고 그 밖의 설정은 안내한다.
2. 계획 보고: 아래 단계에서 적용할 대상 파일과 설정 파일 편집 여부를 사용자에게 보고하고 승인을 받는다. 설정 파일(settings.json, AGENTS.md 병합 포함)을 편집할 때는 원본을 백업한 뒤 병합하고, 병합할 내용을 사용자에게 보여 확인한다.
3. 공통 파일 복사:
   - BASE/harness/HARNESS.md를 PROJ/harness/HARNESS.md에 복사한다.
   - BASE/skills/<스킬>를 PROJ/.agents/skills/<스킬>에 복사한다. Claude Code에서는 PROJ/.claude/skills/<스킬>에도 두도록 한다.
   - PROJ의 AGENTS.md에 templates/AGENTS.harness.md의 블록(agent-harness:begin~end)을 병합한다. AGENTS.md가 없으면 블록만으로 AGENTS.md를 만든다.
   - Claude Code에서는 templates/CLAUDE.md 내용(@AGENTS.md)으로 PROJ/CLAUDE.md를 만든다.
4. 도구별 설정 (2단계에서 승인받은 것만 실행):
   - Cursor: PROJ/.cursor/rules/agent-harness.mdc를 adapters/cursor/agent-harness.mdc에서 복사한다. 전역 User Rules는 settings.json의 user_rules에 templates/AGENTS.harness.md의 핵심 규칙이 들어 있는지 확인하고 없으면 병합한다.
   - Codex CLI: PROJ/AGENTS.md에 핵심 규칙 블록이 있는지 확인하고 없으면 병합한다.
   - Gemini CLI: settings.json의 context.fileName에 AGENTS.md가 포함되어 있는지 확인한다.
   - GitHub Copilot: PROJ/.github/copilot-instructions.md에 핵심 규칙을 병합하고, PROJ/.github/skills에 스킬을 복사한다.
   - Antigravity: PROJ/AGENTS.md와 PROJ/.agents/skills를 적용한다. 전역 규칙 경로는 공식 문서로 확인하지 못했으므로 사용자에게 직접 확인을 요청한다.
5. 검증과 보고: PROJ에 복사·병합된 파일이 실제로 존재하는지 확인하고, AGENTS.md 블록이 한 번만 들어 있는지 확인한다. PROJ/harness/HARNESS.md와 PROJ/.agents/skills가 하네스의 정본 위치가 된다. 사용자에게 적용한 위치를 목록으로 보고한다.

한계: Antigravity 전역 규칙 경로(~/.gemini/config/skills)와 Copilot CLI 경로는 공식 문서로 확인하지 못해 안내만 한다.

## 수동 설치

AI 자동 적용이 막힐 때 쓰는 폴백이다. GitHub에서 저장소를 내려받아 필요한 파일을 PROJ의 harness/, .agents/skills(도구별 스킬 위치)에 복사한다. 업데이트는 저장소를 다시 받아 같은 방식으로 복사하고, 제거는 복사한 파일을 직접 지운다.
