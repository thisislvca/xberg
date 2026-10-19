# Tesseract SelfCorrecting skips PDF display-rotation restoration under default PSM

Reproduced with official CLI 1.3.10 on macOS arm64.

With single-stage Tesseract, Concord default/false omit `BID TABULATION`; true retains it. The compensated synthetic page loses its heading with false and retains it with true. The upright synthetic control retains it with false.

## Reproduce

From this directory:

```sh
xberg extract fixtures/concord-airport-page29.pdf --config configs/default.json --format json --log-level error
xberg extract fixtures/concord-airport-page29.pdf --config configs/false.json --format json --log-level error
xberg extract fixtures/concord-airport-page29.pdf --config configs/true.json --format json --log-level error
xberg extract fixtures/control-image-p270-m90.pdf --config configs/false.json --format json --log-level error
xberg extract fixtures/control-image-p270-m90.pdf --config configs/true.json --format json --log-level error
xberg extract fixtures/control-image-p0-m0.pdf --config configs/false.json --format json --log-level error
```

## Source

Public Concord agenda, physical page 29: https://concordnc.gov/Portals/0/Concord/Departments/Clerk/Council%20Agenda/14698/2025-03-131111.pdf?ver=-JripFv8DxCm1Z0_iAJY8g%3D%3D

The two image-only controls contain synthetic English text. Both display upright: p270/m90 combines a clockwise 270-degree image rotation with PDF /Rotate 90; p0/m0 has neither rotation.

PDF SHA-256:

```text
39b3053d4d5a58781e1a6f559081923cf39ef96546676982f65a9c8599c3f951  fixtures/concord-airport-page29.pdf
0a9ef1b3129ee7daf23786135c27a5742cee1184c584744811448cec238ab509  fixtures/control-image-p0-m0.pdf
ebb37209e509dbfa8ae8be282edee55ffebd71d896ec8afcde8074c6762b1348  fixtures/control-image-p270-m90.pdf
```
