# text coverage excludes known empty pages when page extraction is disabled

Reproduced with official CLI 1.3.10 on macOS arm64.

All modes extract identical text and count 3 source pages. Default/false return pages 1 and 3 and report coverage 1. Explicit true includes page 2 and reports 0.6666667. Default omits metadata.pages; explicit false/true retain the full metadata inventory.

## Reproduce

From this directory:

```sh
xberg extract fixtures/empty-middle.pdf --config configs/default.json --format json --no-cache true --ocr false
xberg extract fixtures/empty-middle.pdf --config configs/false.json --format json --no-cache true --ocr false
xberg extract fixtures/empty-middle.pdf --config configs/true.json --format json --no-cache true --ocr false
```

## Source

Synthetic three-page PDF: text, empty page, text. Generated with the included make_fixture.py using built-in Helvetica.

PDF SHA-256:

```text
b0d8f99827326da9140c22c7f1ab3f03754c125b25105e0a8432699773c36cca  fixtures/empty-middle.pdf
```
