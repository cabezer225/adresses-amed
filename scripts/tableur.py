"""Minimal .xlsx writer and reader using only the standard library (no openpyxl on this Mac).

Writes a workbook Google Sheets can import (bold, frozen header row, column widths) and reads
back the .xlsx that Google Sheets exports.
"""
import re
import zipfile
from xml.sax.saxutils import escape

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"


def _col(i):
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


def _cell(ref, value, style):
    if value is None or value == "":
        return f'<c r="{ref}" s="{style}"/>'
    if isinstance(value, bool):
        value = "oui" if value else "non"
    if isinstance(value, (int, float)):
        return f'<c r="{ref}" s="{style}"><v>{value}</v></c>'
    text = escape(str(value)).replace("\n", "&#10;")
    return f'<c r="{ref}" t="inlineStr" s="{style}"><is><t xml:space="preserve">{text}</t></is></c>'


def ecrire_xlsx(path, feuilles):
    """feuilles: list of (name, rows, widths); rows[0] is the header row."""
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
            '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
            + "".join(f'<Override PartName="/xl/worksheets/sheet{i + 1}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(len(feuilles)))
            + "</Types>"))
        z.writestr("_rels/.rels", (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
            "</Relationships>"))
        z.writestr("xl/workbook.xml", (
            f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="{NS}" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>'
            + "".join(f'<sheet name="{escape(n)}" sheetId="{i + 1}" r:id="rId{i + 1}"/>' for i, (n, _, _) in enumerate(feuilles))
            + "</sheets></workbook>"))
        z.writestr("xl/_rels/workbook.xml.rels", (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            + "".join(f'<Relationship Id="rId{i + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i + 1}.xml"/>' for i in range(len(feuilles)))
            + f'<Relationship Id="rId{len(feuilles) + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
            "</Relationships>"))
        # Style 0: normal, wrapped. Style 1: bold header on a yellow fill.
        z.writestr("xl/styles.xml", (
            f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><styleSheet xmlns="{NS}">'
            '<fonts count="2"><font><sz val="11"/><name val="Arial"/></font><font><b/><sz val="11"/><name val="Arial"/></font></fonts>'
            '<fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill>'
            '<fill><patternFill patternType="solid"><fgColor rgb="FFFCE3A0"/></patternFill></fill></fills>'
            '<borders count="1"><border/></borders><cellStyleXfs count="1"><xf/></cellStyleXfs>'
            '<cellXfs count="2"><xf fontId="0" fillId="0" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>'
            '<xf fontId="1" fillId="2" applyFont="1" applyFill="1" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf></cellXfs>'
            "</styleSheet>"))
        for i, (_, rows, widths) in enumerate(feuilles):
            cols = "".join(f'<col min="{j + 1}" max="{j + 1}" width="{w}" customWidth="1"/>' for j, w in enumerate(widths))
            body = []
            for r, row in enumerate(rows):
                style = 1 if r == 0 else 0
                cells = "".join(_cell(f"{_col(c)}{r + 1}", v, style) for c, v in enumerate(row))
                body.append(f'<row r="{r + 1}">{cells}</row>')
            z.writestr(f"xl/worksheets/sheet{i + 1}.xml", (
                f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="{NS}">'
                '<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>'
                f"<cols>{cols}</cols><sheetData>{''.join(body)}</sheetData></worksheet>"))


def _text(el):
    return "".join(t.text or "" for t in el.iter(f"{{{NS}}}t"))


def lire_xlsx(path):
    """Return {sheet name: list of rows (lists of str)} from an .xlsx file."""
    import xml.etree.ElementTree as ET

    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        shared = []
        if "xl/sharedStrings.xml" in names:
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            shared = [_text(si) for si in root.findall(f"{{{NS}}}si")]
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        targets = {r.get("Id"): r.get("Target") for r in rels}
        out = {}
        for sh in wb.find(f"{{{NS}}}sheets"):
            rid = sh.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
            target = targets[rid].lstrip("/")
            target = target if target.startswith("xl/") else "xl/" + target
            root = ET.fromstring(z.read(target))
            rows = []
            for row in root.iter(f"{{{NS}}}row"):
                vals = {}
                for c in row.findall(f"{{{NS}}}c"):
                    col = re.match(r"[A-Z]+", c.get("r")).group(0)
                    idx = 0
                    for ch in col:
                        idx = idx * 26 + ord(ch) - 64
                    t = c.get("t")
                    v = c.find(f"{{{NS}}}v")
                    if t == "s" and v is not None:
                        val = shared[int(v.text)]
                    elif t == "inlineStr":
                        val = _text(c)
                    else:
                        val = v.text if v is not None else ""
                    vals[idx - 1] = val or ""
                width = max(vals) + 1 if vals else 0
                rows.append([vals.get(i, "") for i in range(width)])
            out[sh.get("name")] = rows
        return out
