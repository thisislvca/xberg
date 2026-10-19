#!/usr/bin/env python3
"""Deterministic synthetic PDF; no third-party package or embedded font needed."""
from pathlib import Path


def fixture_bytes():
    objects = [b'<< /Type /Catalog /Pages 2 0 R >>',
               b'<< /Type /Pages /Count 3 /Kids [4 0 R 6 0 R 8 0 R] >>',
               b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>']
    for i, text in enumerate(['First page body.', '', 'Last page body.']):
        stream = (f'BT /F1 16 Tf 40 100 Td ({text}) Tj ET\n' if text else '').encode('ascii')
        objects.append(f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 200] /Resources << /Font << /F1 3 0 R >> >> /Contents {5+i*2} 0 R >>'.encode())
        objects.append(f'<< /Length {len(stream)} >>\nstream\n'.encode()+stream+b'endstream')
    out = bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
    offsets = [0]
    for n, obj in enumerate(objects, 1):
        offsets.append(len(out))
        out.extend(f'{n} 0 obj\n'.encode()+obj+b'\nendobj\n')
    xref = len(out)
    out.extend(f'xref\n0 {len(offsets)}\n0000000000 65535 f \n'.encode())
    for offset in offsets[1:]:
        out.extend(f'{offset:010d} 00000 n \n'.encode())
    out.extend(f'trailer\n<< /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode())
    return bytes(out)

if __name__ == '__main__':
    (Path(__file__).resolve().parent/'fixtures/empty-middle.pdf').write_bytes(fixture_bytes())
