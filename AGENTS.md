# AGENTS.md

이 문서는 agent-harness 저장소 규칙입니다. 하네스(harness/HARNESS.md)를 따르며 핵심 규칙 블록은 맨 아래에 있습니다.

## 정본 위치

- 하네스 설계 기록: harness/HARNESS.md
- 스킬: skills/<이름>/SKILL.md
- 핵심 규칙 템플릿: templates/AGENTS.harness.md, templates/CLAUDE.md
- Cursor 어댑터: adapters/cursor/agent-harness.mdc, adapters/cursor/tool-call.mdc
- 줄바꿈 표준: .gitattributes (LF)
- 작업 문서: docs/tasks/ (기획용 하나로 단일화, 별도 brief 금지)
- 문서 색인: docs/INDEX.md

## 바꿀 때 함께 맞출 곳

- skills/ → .agents/skills/, .claude/skills/ (3벌 바이트 동일)
- templates/AGENTS.harness.md ↔ 이 파일의 마커 블록 (바이트 동일)
- adapters/cursor/*.mdc ↔ .cursor/rules/*.mdc (바이트 동일)
- README.md의 지원 도구 표, harness/HARNESS.md 2절
- 정본 규칙이 바뀌면 VERSION을 커밋하는 시점에 올립니다.

## 스킬 형식

- Agent Skills 표준을 따릅니다. frontmatter에는 name과 description만 둡니다.
- name은 폴더명과 같고 `^[a-z0-9]+(-[a-z0-9]+)*$`에 맞습니다.
- description은 1024자 이하입니다.
- 스킬 파일은 80줄 이하, 3,500자 이하입니다. dev-principles만 예외입니다.

## 언어 규칙

- 응답·문서·주석·커밋 메시지는 사용자 언어와 존댓말로 쓰고 eli5-clarity를 항상 적용합니다(harness/HARNESS.md 1절).
- 코드, 경로, 명령, 식별자는 원문 그대로 둡니다.
- harness/, skills/, templates/, adapters/cursor/에는 특정 도구 전용 표현(개인 경로, 모델 이름)을 넣지 않습니다. 모델 이름 예시는 HARNESS.md 8절 표에만 둡니다.
- 스킬 지시문은 간결한 서술체로, 사용자에게 띄우는 문장은 존댓말과 eli5-clarity로 씁니다.

## 검증 방법

변경 뒤 `python -I -c` 인라인으로만 확인합니다. 임시 스크립트(_verify*.py 등)는 만들지 않습니다.

1. 스킬 frontmatter: name이 폴더명과 같고 정규식에 맞으며, description이 1~1024자이고 다른 필드가 없습니다.
2. 금지 표현이 harness/, skills/, templates/, adapters/cursor/, docs/에 0건입니다. 이 파일도 검사 대상이라 두 조각으로 적습니다: `C:`+`\Users`, `GLOBAL_`+`HARNESS`, `전역 `+`하네스`, `Agent `+`도구`, `Send`+`Message`. 모델 이름 3종(`hai`+`ku`, `son`+`net`, `op`+`us`)은 HARNESS.md 8절 표에만 둡니다.
3. 스킬 80줄·3,500자 이하(dev-principles 제외), templates/AGENTS.harness.md 40줄 이하, 어댑터 .mdc 글자 수 상한(agent-harness 600, tool-call 700), 상시 로드(AGENTS.md+.cursor/rules/*.mdc 글자 합) 5,089자 이하를 지킵니다.
4. 해시 일치: 스킬 3벌, 템플릿 ↔ 이 파일 마커 블록, 어댑터 ↔ .cursor/rules 사본.
5. 깨진 문자(U+FFFD)와 허용 외 한자·일본어가 0건입니다.

## 승인·안전 규칙

- 커밋·푸시·병합은 사용자 허락 후에만 하며, 비밀 값·.env 금지, 리뷰 없이 PASS 금지입니다(상세: harness/HARNESS.md 5절).

<!-- agent-harness:begin -->
## 기획·개발 하네스 핵심 규칙

정본은 harness/HARNESS.md입니다. 스킬: plan-harness, build-harness, review-harness, delegation-brief, proofread-harness, eli5-clarity, dev-principles

### 공통 규칙 (메인·서브·리뷰 전원 필수, HARNESS.md 1절)
- 사용자 언어·존댓말·eli5-clarity(결론 먼저, 짧게, 용어 첫 등장 풀이)를 응답·서브 지시와 보고·문서·코드 주석과 독스트링·커밋 메시지에 씁니다.
- 한자·외국어 서술과 깨진 글자(U+FFFD)를 쓰지 않습니다.
- 코드·경로·명령·식별자·인용은 원문 그대로 둡니다.
- 마커 블록과 harness/HARNESS.md는 읽기 전용이라 고치지 않습니다.
- 프로젝트 규칙은 마커 바깥 `## 프로젝트 오버레이`(또는 docs/PROJECT_RULES.md)에 둡니다.
- 더 엄격한 오버레이가 우선하고, 완화는 `[안전 예외 승인: N번]`을 명시한 때만 허용합니다.
- harness/VERSION과 .gitattributes(`eol=lf`)를 함께 둡니다.

### 부모(메인) 세션 규칙 (HARNESS.md 3절)
- 메인은 기획 수렴·승인 요청·작업 문서 결정·위임 지시·최종 보고만 합니다.
- 허락 후 메인이 한 줄 명령(git status·log·diff, 커밋, 푸시, python -I -c)을 실행합니다.
- 표준은 구현 서브 → 독립 리뷰 서브 2단계입니다.
- Fast-track(단일 파일·20줄 이하 단순 수정 또는 하네스 설치·업데이트 동기화, 보안·비가역 제외)은 서브 없이 메인이 직접 처리하고 인라인 검증·셀프 체크로 PASS합니다.
- 서브 호출 전 도구 schema와 delegation-brief를 읽고, 모든 서브 프롬프트에 개발 하네스([앞: 가드레일 6줄(harness/HARNESS.md·AGENTS.md·dev-principles 전 항목(2~11절 전체) 경로 포함)] → [작업 문서 경로·작업 번호] → [끝: 자기점검 4줄], 500자 이하)를 전달합니다.
- 긴 출력은 로그 파일+한 줄 요약, 보고는 결과1줄/불릿≤5/경로/다음1줄입니다.

### 자식(구현·리뷰 서브) 세션 규칙 (HARNESS.md 3·6·7절)
- 전달받은 가드레일과 세 문서(harness/HARNESS.md·AGENTS.md·dev-principles)를 먼저 읽고 준수합니다. 본문은 다시 적지 않습니다.
- 구현·보정 서브는 지정 문서·파일만 읽고 바로 고치며, 주석 eli5-clarity를 지키고 -c 검증과 dev-principles 전 항목(2~11절 전체) 준수·확인을 보고합니다.
- 리뷰 서브는 맥락 없는 새 세션에서 검증 재실행·산출물 확인·7대 체크리스트(주석·언어 순수성)·dev-principles 전 항목(2~11절 전체) 준수·확인 후 판정합니다.

### 승인·안전 6원칙 (전원 필수, HARNESS.md 5절)
1. 기획 승인 전 코드를 쓰지 않습니다.
2. 구현 중 멈춤은 새 권한·비가역(파일 삭제 포함)·보안·제품 결과 변경·동일 지적 보정 2회 후 미달뿐입니다. 파일 삭제 요청·수행·보고 시 해당 파일이 무엇인지, 삭제 이유와 근거가 무엇인지 반드시 설명합니다.
3. 커밋·푸시·병합은 사용자 허락이 필요합니다(오버레이 명시 예외 제외).
4. 비밀 값·.env를 커밋·로그에 남기지 않습니다.
5. 리뷰 없이 PASS하지 않습니다. 표준은 독립 리뷰 세션, Fast-track은 메인 셀프 체크가 판정합니다.
6. 요청받지 않은 코드·미지시 파일·임시 검증 스크립트(_verify*.py)를 만들지 않습니다. 검증은 -c 인라인만 씁니다.
<!-- agent-harness:end -->
