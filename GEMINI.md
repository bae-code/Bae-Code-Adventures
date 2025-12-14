# General GitHub Rules

- **Language**: All GitHub-related activities, including commit messages, Pull Request titles and descriptions, and comments, must be written in **Korean**.

---
# Create Branch Rules

- **Remote Push**: 브랜치를 만들면 항상 리모트에 푸시해야 합니다.

---
# Commit Rules

- print 와 같은 디버깅 요소가 포함된 경우 제거 요청을 해야합니다.


# Commit Message Rules

- **Prefix**: All commit messages must start with one of the following prefixes:
  - `[feat]`: 새로운 기능 추가 (A new feature)
  - `[fix]`: 버그 수정 (A bug fix)
  - `[docs]`: 문서 변경 (Documentation changes)
  - `[test]`: 테스트 코드 관련 변경 (Adding missing tests or correcting existing tests)
  - `[refactor]`: 코드 리팩토링 (A code change that neither fixes a bug nor adds a feature)

- **Granularity**: Commits should be as granular as possible. Each commit should represent a single logical change.

---

# Pull Request (PR) Rules

When creating a Pull Request, please adhere to the following guidelines to ensure clarity and a smooth review process.

## 1. PR Title

The PR title should be clear and concise, following the same prefix rules as commit messages, and must be in **Korean**.

- **Example**: `[feat]: 사용자 인증 기능 추가`

## 2. PR Description (Template)

Use the following template in your PR description. The description must be in **Korean**.

```markdown
## 📝 Description

변경 사항에 대한 요약과 해결된 이슈 번호를 포함해주세요. 관련된 동기나 컨텍스트도 함께 제공해주세요.

- Closes #(이슈_번호)

## ✨ 주요 변경 사항

- 변경점 1
- 변경점 2
- 변경점 3

## ✅ 체크리스트

- [ ] 제 코드는 이 프로젝트의 스타일 가이드라인을 따릅니다.
- [ ] 제 코드에 대한 자체 검토를 수행했습니다.
- [ ] 이해하기 어려운 부분에 주석을 추가했습니다.
- [ ] 문서에 관련된 변경 사항을 만들었습니다.
- [ ] 제 변경 사항으로 인해 새로운 경고가 발생하지 않습니다.
- [ ] 제 수정 사항이 효과적이거나 기능이 작동함을 증명하는 테스트를 추가했습니다.
- [ ] 새로운 테스트와 기존 테스트 모두 제 변경 사항으로 로컬에서 통과합니다.
```

## 3. 리뷰 절차
- **리뷰어 지정**: PR에 최소 한 명 이상의 리뷰어를 지정하세요.
- **피드백 반영**: 리뷰어의 모든 코멘트와 피드백을 반영하세요.
- **머지**: PR이 승인되면 메인 브랜치로 머지할 수 있습니다.
