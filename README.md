# vtt2text

[![vtt2text](https://img.shields.io/badge/pypi-vtt2text-brightgreen)](https://pypi.org/project/vtt2text/)
![Python](https://img.shields.io/badge/Python-3.6-blue.svg)
![MIT](https://img.shields.io/badge/license-MIT-important.svg)
![Size](https://img.shields.io/github/repo-size/vuanhtuan1012/vtt2text.svg)
![Contributors](https://img.shields.io/github/contributors/vuanhtuan1012/vtt2text.svg)

Small scripts to clean up the content of a subtitle file `.vtt`.

## Install

```
pip install vtt2text
```

## Usage

- `vtt2text.convert(filepath)`: return a clean text containing content of `vtt` file input.
- `vtt2text.tofile(filepath)`: save clean content to a text file. By default, the output file has extension `.txt` and the same name with the input file.

Before:

![vtt file](images/before.png)

After:

![txt file](images/after.png)
