# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-01-27 07:02:40
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-01-27 07:57:58

import re
from os.path import splitext
from os.path import exists


def convert(filepath: str) -> str:
    """Convert content of a subtitle file (vtt) to string

    Args:
        filepath (str): path to vtt file

    Returns:
        str: clean content
    """
    # read file content
    with open(filepath, "r", encoding="utf-8") as fp:
        content = fp.read()

    # remove header & empty lines
    lines = [line for line in content.split("\n") if line]
    lines = lines[1:]

    # remove indexes
    lines = [lines[i] for i in range(len(lines)) if not lines[i].isdigit()]

    # remove times
    pattern = r"^\d{2}:\d{2}:\d{2}.\d{3}.*\d{2}:\d{2}:\d{2}.\d{3}$"
    lines = [lines[i] for i in range(len(lines))
             if not re.match(pattern, lines[i])]

    content = " ".join(lines)
    # remove duplicate spaces
    pattern = r"\s{2,}"
    content = re.sub(pattern, r" ", content)

    # add space after punctuation marks if it doesn't exist
    pattern = r"([\.!?])(\w)"
    content = re.sub(pattern, r"\1 \2", content)

    return content


def tofile(file_in: str, file_out=None):
    """Save content of a subtitle file to text file

    Args:
        file_in (str): path to vtt file
        file_out (None, optional): Description
    """
    # set default filename
    if not file_out:
        filename = splitext(file_in)[0]
        file_out = filename + ".txt"
        i = 0
        while exists(file_out):
            i += 1
            file_out = "%s_%s.txt" % (filename, i)

    content = convert(file_in)
    with open(file_out, "w+", encoding="utf-8") as fp:
        fp.write(content)
    print("clean content is written to file: %s" % file_out)
