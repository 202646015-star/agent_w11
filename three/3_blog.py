from pathlib import Path


def build_blog_series(base_dir: str = "blog_planning_series") -> None:
    """Create a blog series folder structure and write markdown files."""
    root = Path(base_dir)
    drafts_dir = root / "drafts"
    refs_dir = root / "references"

    # 하위폴더 포함 생성
    drafts_dir.mkdir(parents=True, exist_ok=True)
    refs_dir.mkdir(parents=True, exist_ok=True)

    links = [
        "https://blog.naver.com/resumet/224284263918",
        "https://blog.naver.com/schrblog/224173091886",
        "https://blog.naver.com/musthave007/224248958532",
    ]

    index_md = f"""# 블로그 3부작 기획안

아래 3개 레퍼런스 블로그를 참고해 시리즈 글을 기획합니다.

## 참고 링크
1. {links[0]}
2. {links[1]}
3. {links[2]}

## 시리즈 방향
- 대상 독자: 실무형 AI/데이터 작업을 처음 시작하는 학습자
- 톤앤매너: 친절한 설명 + 바로 실행 가능한 예시
- 구성 원칙: 개념 → 실습 → 확장 아이디어

## 포스트 구성

### Post 1. 왜 지금 물리 AI/자동화인가?
- 문제의식: 반복 작업과 데이터 기반 의사결정의 중요성
- 핵심 개념: 자동화 파이프라인, 재현 가능성, 문서화 습관
- 결과물: 실행 가능한 최소 자동화 스크립트 소개

### Post 2. 데이터 수집/가공 실전 패턴
- 문제의식: 데이터가 흩어져 있고 형식이 제각각인 상황
- 핵심 개념: 수집(Crawling/API), 정제, 저장 구조화
- 결과물: 폴더 구조 + CSV/JSON 관리 템플릿

### Post 3. 시각화와 인사이트 전달
- 문제의식: 분석 결과를 쉽게 전달하기 어려움
- 핵심 개념: 시각화 선택 기준, 스토리텔링, 리포트 자동화
- 결과물: 그래프 생성 및 공유 가능한 마크다운 리포트

## 발행 일정(예시)
- 1주차: Post 1 발행
- 2주차: Post 2 발행
- 3주차: Post 3 발행

## 체크리스트
- [ ] 각 글의 핵심 메시지 1문장 정리
- [ ] 코드/실습 예제 최소 1개 포함
- [ ] 마무리에 다음 글 예고 포함
"""

    post1_md = """# Post 1 초안: 왜 지금 물리 AI/자동화인가?

## 한 줄 요약
반복되는 작업을 자동화하고, 데이터 기반으로 의사결정을 돕는 능력은 이제 선택이 아니라 기본 역량입니다.

## 도입
공부나 프로젝트를 하다 보면, 매번 같은 정리 작업을 반복하게 됩니다.
예를 들어 파일 정리, 데이터 저장, 결과 문서 작성 같은 일은 작지만 꾸준히 시간을 소모합니다.

이 글에서는 **작은 자동화 습관이 어떻게 큰 생산성 차이**를 만드는지 이야기하고,
바로 실행할 수 있는 형태로 정리해보겠습니다.

## 왜 자동화가 중요한가?
1. **시간 절약**: 반복 작업을 코드로 치환하면, 중요한 문제 해결에 시간을 쓸 수 있습니다.
2. **실수 감소**: 수작업보다 같은 규칙을 일관되게 적용할 수 있습니다.
3. **재현 가능성**: 나중에 다시 실행해도 동일한 결과를 얻기 쉽습니다.
4. **협업 효율**: 폴더 구조와 문서 규칙이 있으면 팀원과 공유가 수월합니다.

## 이번 시리즈에서 다룰 것
- Post 1: 자동화의 필요성과 최소 실행 예시
- Post 2: 데이터 수집/가공 흐름 설계
- Post 3: 시각화 및 결과 전달 자동화

## 오늘의 최소 실천
오늘은 우선 아래 3가지만 실천해보면 충분합니다.

- 프로젝트 폴더를 목적별로 분리하기 (`drafts/`, `references/` 등)
- 작업 개요를 `index.md`로 남기기
- 첫 글 초안을 `post1.md`로 시작하기

작게 시작하되, 매번 반복 가능한 구조를 만드는 것이 핵심입니다.

## 마무리
자동화는 거창한 기술이 아니라, **반복되는 일을 코드로 남기는 습관**에서 시작됩니다.
다음 글에서는 실제로 데이터를 수집하고 정리할 때 어떤 구조로 작업하면 좋은지 실전 패턴을 다뤄보겠습니다.
"""

    (root / "index.md").write_text(index_md, encoding="utf-8")
    (root / "post1.md").write_text(post1_md, encoding="utf-8")

    # 참고 링크 원문 저장
    refs_text = "\n".join(f"- {url}" for url in links) + "\n"
    (refs_dir / "links.md").write_text("# 참고 링크\n\n" + refs_text, encoding="utf-8")

    print(f"완료: '{root}' 폴더 및 하위폴더/문서 생성")


if __name__ == "__main__":
    build_blog_series()
