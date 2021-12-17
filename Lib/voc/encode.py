from fontTools.ttLib import TTFont
from voc import set_TSIV
from sys import argv


def encode_glyph(ttf_path: str, glyph_name: str, unicode: str):
    font = TTFont(ttf_path)
    go = font.getGlyphOrder()
    if glyph_name not in go:
        font.close()
        print(f"Glyph '{glyph_name}' not in font, skipping.")
        return

    if unicode.startswith("U+"):
        try:
            unicode_number = int(unicode[2:], 16)
        except:
            font.close()
            print(
                f"Could not parse Unicode value '{glyph_name}', "
                "it must start with 'U+' followed by the value as "
                "a hexadecimal number."
            )
            return

        tsiv = font["TSIV"]
        data = tsiv.data.decode()
        # data = data.split("\0")
        lines = data.splitlines()
        seen_glyph_def = False
        for i, line in enumerate(lines):
            if line.strip().startswith("DEF_GLYPH"):
                seen_glyph_def = True
                continue

            if not seen_glyph_def:
                continue

            index = go.index(glyph_name)
            entry = (
                f'DEF_GLYPH "{glyph_name}" ID {index} '
                f"UNICODE {unicode_number} TYPE BASE END_GLYPH"
            )
            lines.insert(i, entry)
            print(f"Inserting entry at line {i}: \n    {entry}")
            set_TSIV(tsiv, lines)
            font.save(ttf_path)
            break

    font.close()


def encode():
    # Encode a glyph in the VOLT source
    # cmd line interface
    num_args = len(argv)
    if num_args < 3:
        print("Encode a glyph in the VOLT source.")
        print(f"Usage: {argv[0]} GLYPHNAME UNICODE TTF_PATH [TTF_PATH]")
        print(f"Example: {argv[0]} a U+0065 MyFont1.ttf MyFont2.ttf")
    else:
        glyph_name, unicode = argv[1:3]
        font_paths = argv[3:]
        for font_path in font_paths:
            print(font_path)
            encode_glyph(font_path, glyph_name, unicode)
