# Phonetisaurus G2P Scripts

This directory contains a set of scripts and a web demo interface for the Phonetisaurus Grapheme-to-Phoneme (G2P) conversion tool. The G2P process converts words from their written form into a phonetic representation. These tools are designed for use with Python 3 and the Phonetisaurus G2P model.

## Contents

- `g2pserver.py`: A Python 3 server script that provides a web service for G2P conversion.
- `phoneticize.py`: A Python 3 script for converting individual words or a list of words from a file to their phonetic representations.
- `demo.html`: A web interface for submitting words to the G2P service and receiving phonetic conversions.
- `words.list`: An example text file containing words to be converted using the `phoneticize.py` script.

## Requirements

- Python 3.x
- Phonetisaurus G2P model files
- Bottle web framework (for `g2pserver.py`)

Ensure all dependencies are installed using pip:

\```sh
pip install phonetisaurus bottle
\```

## Usage

### g2pserver.py

Start the G2P web service:

\```sh
python g2pserver.py --model path/to/your/model.fst
\```

### phoneticize.py

Convert a single word:

\```sh
python phoneticize.py --model path/to/your/model.fst --word "test"
\```

Convert a list of words from a file:

\```sh
python phoneticize.py --model path/to/your/model.fst --wlist words.list
\```

### Using the Web Interface

1. Ensure the `g2pserver.py` is running.
2. Open `demo.html` in a web browser.
3. Enter words (one per line) in the text area.
4. Click "Convert" to see the phonetic representations.

## Features

- **G2P Conversion**: Convert written words to phonetic representations using a state-of-the-art model.
- **Batch Processing**: Process multiple words at once through the command-line tool or the web interface.
- **Web Interface**: A user-friendly way to perform G2P conversion without the need for command-line interaction.

## Customization

- The server address and port can be customized in the `g2pserver.py` script and the `demo.html` file to match your deployment environment.

## License

[Specify License Here]

## Acknowledgements

This tool is built using the Phonetisaurus G2P library. For more information about Phonetisaurus and its capabilities, visit the [official repository](https://github.com/AdolfVonKleist/Phonetisaurus).