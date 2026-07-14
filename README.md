# OtterZip website

Landing page for **OtterZip**, a quiet, no-clutter archive tool for Windows.
Deployed to `otterzip-web` (GitHub Pages).

- Live: https://lumibearstudio.github.io/otterzip-web/
- Microsoft Store: https://apps.microsoft.com/detail/9NWQNGGSWJCL

## Files
- `index.html` — the landing page. Dark theme, 10-language i18n with browser
  auto-detection (`data-i18n` + a JS dictionary), scroll-reveal, and the
  Windows Store deep link on Windows.
- `install.html` — bilingual (KO/EN) install guide for the direct download.
- `assets/` — otter icon + app screenshots.

## Downloads (two channels, same app)
- **Microsoft Store** — one-click install + automatic updates. Primary CTA.
- **Direct download** — free `OtterZip_x64_installer.zip` from GitHub Releases.

### How the direct download works
The download button points at a **stable** GitHub Releases asset:

```
https://github.com/LumiBearStudio/OtterZip/releases/latest/download/OtterZip_x64_installer.zip
```

The bundle contains the **signed** `.msix`, the **public `.cer`**, and
`Install.ps1`. Because it is self-signed (not Store-signed), the user runs
`Install.ps1` once, which registers our publisher certificate (a UAC prompt)
and installs the app. See `install.html`.

The bundle is built **locally** — a CI-built MSIX is unsigned and omits the C++
shell extension, so it cannot be a real release:

```
pwsh tools/dev-cert.ps1          # once, per machine: self-signed publisher cert
build-msix.bat --sideload        # builds shell + signs + writes the installer zip
gh release create v<ver> AppPackages/VER_<ver>/OtterZip_x64_installer.zip --generate-notes
```

`.github/workflows/release.yml` is a manual compile smoke-check only; it does
not publish releases.

© 2026 LumiBear Studio
