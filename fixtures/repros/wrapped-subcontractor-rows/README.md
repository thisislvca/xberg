# wrapping in several cells splits one subcontractor record into five rows

Reproduced with official CLI 1.3.10 on macOS arm64.

The Bayview record should remain one row. It becomes five: the name is in row 6 and `$17,500` is in row 8 (zero-based). All nine neighboring records and the full table token multiset survive.

## Reproduce

From this directory:

```sh
xberg extract sfport-p7.pdf --config config.json --format json --no-cache true --ocr false --pdf-backend native --layout false --extract-pages true --include-structure true
```

## Source

Physical page 7 copied without content changes from the public SF Port bid tabulation: https://www.sfport.com/media/10881/download?inline=

PDF SHA-256:

```text
154712ae0c1c9cfcec4385115384f2f8973193311d217fd43dbb5fd1d3424a09  sfport-p7.pdf
```
