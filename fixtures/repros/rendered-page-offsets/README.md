# formatted output keeps page-byte ranges from an earlier plain representation

Reproduced with official CLI 1.3.10 on macOS arm64.

Markdown content is 925 UTF-8 bytes, but its page ranges remain `[0,321)` and `[323,644)`. Page 2 selects page 1's footer and excludes its own. The plain-text control has correct ranges.

## Reproduce

From this directory:

```sh
xberg extract synthetic-prices.pdf --config configs/markdown.json --format json
xberg extract synthetic-prices.pdf --config configs/plain.json --format json
```

## Source

Synthetic two-page native-text PDF, with an identical table and different page footers. Built-in Helvetica fonts; no external document content.

PDF SHA-256:

```text
451d79cdbec543d95d4f8b1d24577345fcc0f20000381524a08cf1d2bcab0ad8  synthetic-prices.pdf
```
