# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-01-27 07:50:00
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-01-27 07:59:01

import vtt2text


if __name__ == '__main__':
    filepath = "files/transports_en_commun.vtt"

    # get clean content
    content = vtt2text.convert(filepath)
    print(content)

    # save clean content to text file
    print()
    vtt2text.tofile(filepath)