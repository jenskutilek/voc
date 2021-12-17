# voc

MS VOLT command line tools. Extract and merge VOLT project files (.vtp), e.g. if you prefer to edit them in a standalone text editor.


## voc_extract

Extract a VOLT project file (.vtp) from a font.

```bash
$ voc_extract TTF_PATH [OUT_PATH]
```

If `OUT_PATH` is not specified, the output file name is constructed by replacing the TTF file suffix by `vtp`.


## voc_merge

Merge a VOLT project file (.vtp) into a font. Existing VOLT data in the font is overwritten.

```bash
$ voc_merge TTF_PATH VTP_PATH [TTF_OUT_PATH]
```

If `TTF_OUT_PATH` is not specified, the original font file is overwritten.

## voc_parse

Parse a VOLT project file (.vtp) using fontTools.voltLib. This can be used as a syntax check. It doesn't compile the project.

```bash
$ voc_parse VTP_PATH
```

## voc_ship

Remove VOLT and VTT source data from a font.

```bash
$ voc_ship TTF_PATH [TTF_OUT_PATH]
```

If `TTF_OUT_PATH` is not specified, the original font file is overwritten.

## voc_encode

Experimental. Add a Unicode value for a glyph in VOLT source data. The cmap table is not actually changed by this command, you still have to open the font in VOLT and compile the project.

```bash
$ voc_encode GLYPH_NAME UNICODE_VALUE TTF_PATH [TTF_PATH]
```

The Unicode value should be specified as `U+` followed by a hexadecimal number. The DEF_GLYPH line will always specify the glyph as "BASE" at the moment.
