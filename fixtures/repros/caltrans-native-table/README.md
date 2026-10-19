# native row clustering rejects a complete item schedule as single-row fragments

Reproduced with official CLI 1.3.10 on macOS arm64.

Page 3 should yield its seven-column item schedule. It returns zero tables while retaining all 25 item/code/bid/amount associations in text. Page 8 is a positive control and returns a 34-by-9 native table.

## Reproduce

From this directory:

```sh
xberg extract fixtures/caltrans-p3.pdf --config config.json --format json --no-cache true --ocr false --layout false --pdf-backend native --pdf-extract-tables true --extract-pages true
xberg extract fixtures/caltrans-p8.pdf --config config.json --format json --no-cache true --ocr false --layout false --pdf-backend native --pdf-extract-tables true --extract-pages true
```

## Source

Physical pages 3 and 8 copied without content changes from Caltrans 08-1M0804: https://ppmoe.dot.ca.gov/api/x_cado2_contractor/public_attachment_downloader_api/55ed8ed447041b5006b0f5d4116d4326

PDF SHA-256:

```text
74c9f4dee4d3e79eb22decbcd7cc35e39f8215f7d0405bc921722e32e93ed103  fixtures/caltrans-p3.pdf
4198ef086cd69299647ef98ab7f81b780f3cace0d13c1931e5f9d98234e73b03  fixtures/caltrans-p8.pdf
```
