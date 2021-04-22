# voc

MS VOLT command line tools.


## voc_extract

Extract a VOLT project file (.vtp) from a font.

```bash
$ voc_extract TTF_PATH [OUT_PATH]
```

If `OUT_PATH` is not specified, the output file name is constructed by replacing the TTF file suffix by `vtp`.


## voc_merge

Extract a VOLT project file (.vtp) from a font.

```bash
$ voc_merge TTF_PATH VTP_PATH [TTF_OUT_PATH]
```

If `TTF_OUT_PATH` is not specified, the original font file is overwritten.
