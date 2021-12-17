import codecs

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables.T_S_I_V_ import table_T_S_I_V_
from fontTools.voltLib.parser import Parser
from sys import argv


def set_TSIV(table, lines: list):
    table.data = ("\r" + "\r".join([line.strip() for line in lines]) + "\r").encode()


def extract_vtp(ttf_path, out_path=None):
    font = TTFont(ttf_path)
    tsiv = font["TSIV"]

    if out_path is None:
        out_path = ttf_path.rsplit(".", 1)[0] + ".vtp"

    data = tsiv.data.decode()
    data = data.split('\0')
    with codecs.open(out_path, "wb", "utf-8") as f:
        f.write("\r")  # VOLT exports with empty line at the beginning
        for line in data:
            line = line.strip()
            if line:
                f.write(line)
        f.write("\r\r")

    font.close()


def merge_vtp(ttf_path, vtp_path, out_path=None):
    font = TTFont(ttf_path)

    if out_path is None:
        # Overwrite the input font
        out_path = ttf_path

    tsiv = table_T_S_I_V_("TSIV")

    with codecs.open(vtp_path, "rb", "utf-8") as f:
        lines = f.readlines()

    set_TSIV(tsiv, lines)
    font["TSIV"] = tsiv

    font.save(out_path)
    font.close()


def parse_vtp(vtp_path):
    parser = Parser(vtp_path)
    parser.parse()
    # for glyph, anchor in parser.anchors_.items():
    #     print(glyph, anchor)


def extract():
    # Extract a project file from a font
    # cmd line interface
    num_args = len(argv)
    if num_args == 2:
        extract_vtp(ttf_path=argv[1])
    elif num_args == 3:
        extract_vtp(ttf_path=argv[1], out_path=argv[2])
    else:
        print(f"Usage: {argv[0]} TTF_PATH [OUT_PATH]")


def merge():
    # Merge a project file into a font
    # cmd line interface
    num_args = len(argv)
    if num_args == 3:
        merge_vtp(ttf_path=argv[1], vtp_path=argv[2])
    elif num_args == 4:
        merge_vtp(ttf_path=argv[1], vtp_path=argv[2], out_path=argv[3])
    else:
        print(f"Usage: {argv[0]} TTF_PATH VTP_PATH [TTF_OUT_PATH]")


def parse():
    # Parse a project file
    # cmd line interface
    num_args = len(argv)
    if num_args == 2:
        parse_vtp(vtp_path=argv[1])
    else:
        print(f"Usage: {argv[0]} VTP_PATH")
