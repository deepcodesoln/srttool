# srttool

A tool for working with SRT subtitle files (primarily Japanese subtitles); this
tool converts SRT files into other forms for study.

# Usage

Python3.9+ is required.

`python3 srttool.py -h`

# Development

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
pre-commit install
```

Note that these requirements are only for development; they are not needed to
simply use the tool.

## Testing

`python3 -m unittest`

## Documentation

`sphinx-build -EW docs/source docs/build`

# License

MIT license.
