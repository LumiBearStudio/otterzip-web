# OtterZip Website (`redesign.html`)

OtterZip (`otterzip-web`) 공식 랜딩 페이지 및 리디자인 버전입니다.

## 주요 특징 및 비주얼 개선 사항

### 1. 디자인 시스템 & CSS 변수화 (`:root`)
- 하드코딩된 색상을 제거하고 테마 변수를 일관되게 적용했습니다.
  - `--accent`: `#4d7cff`, `--accent-hover`: `#6b91ff`
  - `--accent2`: `#3fd6e0`, `--accent2-text`: `#9df0e6`
  - `--nav-bg`, `--card`, `--panel` 등 다크 모드 기반 세련된 대비 강화

### 2. 섹션별 인터랙션 및 애니메이션
- **Hero 섹션**: 타이틀 뒤 은은한 Radial Glow + 수달 심볼 아이콘 인라인 배치
- **섹션 디바이더**: 급격한 단색 전환 대신 부드러운 상하 그라디언트 페이드(`sec-fade-in`, `sec-fade-out`) 적용
- **Simple & Native UI 프레임**: 스크린샷 윈도우에 호버 시 부드러운 입체 부양(`translateY(-4px)`) 효과
- **Speed Bar 모티프**: Rust 엔진의 빠름을 표현하는 프로그레스 바에 Shimmer(빛 스치는) 효과 및 완료(`✓`) 체크마크 PopIn 애니메이션
- **다운로드 카드 & 포맷 칩**: 카드 및 칩 요소에 반응형 Hover 마이크로인터랙션 적용

### 3. 다운로드 및 배포 연동 (CI/CD Architecture)
- **최신 버전 자동 다운로드 URL**
  - 사이트 내 다운로드 링크(`OZ_DOWNLOAD_URL`)는 GitHub Releases의 고정 에셋 URL을 가리킵니다:
    ```
    https://github.com/LumiBearStudio/OtterZip/releases/latest/download/OtterZip_x64.msix
    ```
- **자동화된 배포 파이프라인 (`.github/workflows/release.yml`)**
  - Git 태그(`v*`)를 push하면 GitHub Actions가 Rust FFI + WinUI3 MSIX 패키지를 빌드한 뒤, 생성된 바이너리를 `OtterZip_x64.msix` 이름으로 Release 에셋에 첨부합니다.
  - 이를 통해 랜딩 페이지의 다운로드 버튼 수정 없이 항상 최신 릴리즈의 MSIX가 다운로드됩니다.

## 파일 구성
- `redesign.html`: 개선된 리디자인 메인 페이지
- `index.html`: 기존 버전 랜딩 페이지
- `assets/`: 수달 아이콘(`otter.png`) 및 윈도우 스크린샷(`window.png`, `settings.png`)
