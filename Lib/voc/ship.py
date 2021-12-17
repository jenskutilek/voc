from fontTools.ttLib import TTFont
from sys import argv


def ship_font(ttf_path, out_path=None):
    if out_path is None:
        out_path = ttf_path
    f = TTFont(ttf_path)
    tags = [tag for tag in f if tag.startswith("TSI")]
    for tag in tags:
        if tag in f:
            del f[tag]
    f.save(out_path)


def ship():
    # Ship a font
    # cmd line interface
    num_args = len(argv)
    if num_args == 2:
        ship_font(ttf_path=argv[1])
    elif num_args == 3:
        ship_font(ttf_path=argv[1], out_path=argv[2])
    else:
        print(f"Usage: {argv[0]} TTF_PATH [TTF_OUT_PATH]")
