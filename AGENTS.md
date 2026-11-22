# AGENTS.md

이 문서는 agent-harness 저장소 규칙입니다. 정본·절차는 harness/HARNESS.md, 핵심 규칙은 아래 마커 블록입니다.

## 정본·동기화

- 정본: harness/HARNESS.md, skills/, templates/, adapters/cursor/, .gitattributes(LF). docs/INDEX.md는 로컬 작업 색인(원격 미포함)·docs는 빈 골격.
- 동기화: skills→.agents/.claude(3벌 동일), templates/AGENTS.harness.md↔마커, adapters↔.cursor/rules, README 지원 표↔HARNESS 2절. VERSION은 커밋 시.

## 스킬·언어·검증

- frontmatter는 name·description만. name=폴더명·^[a-z0-9]+(-[a-z0-9]+)*$, description 1~1024자. 스킬 ≤80줄·≤3,500자. 잎(leaves/*.md)은 스킬 아님(자동 부착 금지).
- 응답·문서·커밋은 사용자 언어·존댓말·eli5-clarity, 코드 주석은 쉬운 명사형 한 줄(HARNESS 1절). 코드·경로·명령·식별자는 원문. harness/, skills/, templates/에는 도구 전용 표현·개인 경로 금지. adapters/는 도구 연결용이라 도구명·경로 예외 허용(모델 이름 예시는 HARNESS 8절 표만).
- 검증은 python -I -c만(임시 _verify*.py 금지). (1) frontmatter (2) 금지 표현 0건(이 파일도 대상; C:+\Users, GLOBAL_+HARNESS, 전역 +하네스, Agent +도구, Send+Message; 모델명 3종 hai+ku/son+et/op+us는 8절만) (3) 줄·글자 상한·상시합≤5089 (4) 해시 3벌·템플릿 마커 구간·어댑터 (5) U+FFFD·허용 외 한자·일본어 0.
- 커밋·푸시·병합은 허락 후. 비밀·.env 금지. 리뷰 없이 PASS 금지(HARNESS 5절).

## 프로젝트 오버레이

- 질문: 필요할 때까지 배치로 이어서(개수는 끝 아님). 선택지 제한 없음. 답 후 즉시 구현 금지. 「가정」=잡무·비결정만.
- 문서: 수정 시 연결 문서 검색→추가·수정·삭제(또는 즉시 후속=같은 번호·다음 턴 전). 반영 목록 필수. 한쪽만이면 PASS 금지.
- 주석만: 주석·독스트링만·동작/API 불변이면 코드 리뷰 대신 언어·eli5·연쇄. Fast-track→메인 셀프, 아니면 독립 주석 전용. 리뷰 없이 PASS 금지. .md만은 문서 연쇄+문서 리뷰.

<!-- agent-harness:begin -->
## 기획·개발 하네스 핵심 규칙

정본은 harness/HARNESS.md입니다. 스킬: harness-router, plan-harness, project-plan-harness, build-harness, review-harness, delegation-brief, proofread-harness, eli5-clarity, dev-principles. 분기: harness-router → playbooks 경로만. 절차 장문은 플레이북·HARNESS(3·6·7절). 서브 위임 시 자기점검에 하네스 준수 칸 필수(delegation-brief).

### 공통 핵심 (전원 필수, HARNESS.md 1절)
- 요청이 오면 harness-router로 플레이북 하나를 고르고 그 경로만 읽습니다. 동시 둘 이상 서브 금지·순차 허용.
- 판단 정본(하네스·오버레이·기획/작업 문서·해당 플레이북/SKILL)은 메인이 직접 읽고, 잡음 절약은 대량 검색·긴 로그·리서치에만 둡니다.
- 사용자 언어·eli5-clarity를 씁니다. 존댓말=응답·서브 지시·보고·문서·커밋. 코드 주석·독스트링=쉬운 명사형 한 줄(eli5 정본).
- 한자·외국어 서술과 깨진 글자(U+FFFD)를 쓰지 않습니다.
- 코드·경로·명령·식별자·인용은 원문 그대로 둡니다.
- 마커 블록과 harness/HARNESS.md는 읽기 전용이라 고치지 않습니다.
- 프로젝트 규칙은 마커 바깥 `## 프로젝트 오버레이`(또는 docs/PROJECT_RULES.md)에 둡니다.
- 더 엄격한 오버레이가 우선하고, 완화는 `[안전 예외 승인: N번]`을 명시한 때만 허용합니다.
- harness/VERSION과 .gitattributes(`eol=lf`)를 함께 둡니다.

### 승인·안전 6원칙 (전원 필수, HARNESS.md 5절)
1. 기획 승인 전 코드를 쓰지 않습니다.
2. 구현 중 멈춤은 새 권한·비가역(파일 삭제 포함)·보안·제품 결과 변경·동일 지적 보정 2회 후 미달뿐입니다. 파일 삭제 요청·수행·보고 시 해당 파일이 무엇인지, 삭제 이유와 근거가 무엇인지 반드시 설명합니다.
3. 커밋·푸시·병합은 사용자 허락이 필요합니다(오버레이 명시 예외 제외).
4. 비밀 값·.env를 커밋·로그에 남기지 않습니다.
5. 리뷰 없이 PASS하지 않습니다. 표준은 독립 리뷰 세션, Fast-track은 메인 셀프 체크가 판정합니다.
6. 요청받지 않은 코드·미지시 파일·임시 검증 스크립트(_verify*.py)를 만들지 않습니다. 검증은 -c 인라인만 씁니다.
<!-- agent-harness:end -->



