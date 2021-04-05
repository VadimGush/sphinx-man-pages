
from enum import Enum, auto

class Entry(Enum):
    PAR_INDENT = auto()
    PARAGRAPH = auto()
    ITALICS_B = auto()
    ITALICS_R = auto()
    MARGIN_S = auto()
    MARGIN_E = auto()
    COMMENT = auto()
    SECTION = auto()
    ITALICS = auto()
    ROMAN_B = auto()
    ROMAN_I = auto()
    SMALL_B = auto()
    PAR_TAG = auto()
    BOLD_I = auto()
    BOLD_R = auto()
    ROMAN = auto()
    SMALL = auto()
    TITLE= auto()
    NONE = auto()
    BOLD = auto()
    URL = auto()
    PAR_TAG_N = auto()
    SUBSECTION = auto()
    SYN_START = auto()
    SYN_END = auto()
    EXAMPLE_S = auto()
    EXAMPLE_E = auto()
    MAILTO_S = auto()
    MAILTO_E = auto()
    CMD_OPTION = auto()
    INDENT = auto()
    CENTER = auto()
    BREAK = auto()
    NO_FILL = auto()
    FILL = auto()
    SPACE = auto()

tags = {
    Entry.COMMENT : ".\\\"",
    Entry.TITLE : ".TH",
    Entry.SECTION: ".SH",
    Entry.PARAGRAPH : [".PP", ".LP", ".P"],
    Entry.BOLD : ".B",
    Entry.BOLD_I : ".BI",
    Entry.BOLD_R : ".BR",
    Entry.ITALICS : ".I",
    Entry.ITALICS_B : ".IB",
    Entry.ITALICS_R : ".IR",
    Entry.ROMAN : ".R",
    Entry.ROMAN_B : ".RB",
    Entry.ROMAN_I : ".RI",
    Entry.SMALL : ".SM",
    Entry.SMALL_B: ".SB",
    Entry.URL: ".UR",
    Entry.MARGIN_S : ".RS",
    Entry.MARGIN_E : ".RE",
    Entry.PAR_INDENT: ".HP",
    Entry.PAR_TAG: ".IP",
    Entry.PAR_TAG_N: ".TP",
    Entry.SUBSECTION: ".SS",
    Entry.SYN_START: ".SY",
    Entry.SYN_END: ".YS",
    Entry.EXAMPLE_S: ".EX",
    Entry.EXAMPLE_E: ".EE",
    Entry.MAILTO_S: ".MT",
    Entry.MAILTO_E: ".ME",
    Entry.CMD_OPTION: ".OP",
    # ======================
    Entry.INDENT: ".in",
    Entry.CENTER: ".cn",
    Entry.BREAK: ".br",
    Entry.NO_FILL: ".nf",
    Entry.SPACE: ".sp",
    Entry.FILL: ".fi"
}

def get_content(text, tag):
    return text[len(tag) : len(text)].strip();

def _process_tag(text, entries, key, tag):
    if text.startswith(tag + " "):
        entries.append((key, get_content(text, tag)))
        return True
    return False

def process_tag(text, entries, key, tag):
    tag_list = []
    if type(tag) == list:
        for t in tag:
            tag_list.append(t)
    else:
        tag_list.append(tag)

    was_tag = False
    for t in tag_list:
        if _process_tag(text, entries, key, t):
            was_tag = True
    return was_tag

def parse(lines):
    entries = []

    for line in lines:
        ln = line.replace("\n", " ")

        tag_found = False
        for (name, value) in tags.items():
            if process_tag(ln, entries, name, value):
                tag_found = True

        if not tag_found:
            entries.append((Entry.NONE, ln))

    for (key, value) in entries:
        print(str(key) + "\t\t> " + value)

