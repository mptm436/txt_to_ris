# Kindle Clippings to Zotero Converter

A Python script to convert Kindle highlights and annotations into Zotero-compatible RIS format.

## Features

- Converts Kindle's `My Clippings.txt` to Zotero-readable RIS format
- Preserves book metadata (title, author)
- Maintains highlight dates and content
- Groups multiple highlights under their original books
- Generates ready-to-import files for Zotero reference management

## Requirements

- Python 3.6 or newer
- Kindle `My Clippings.txt` file
- Zotero installed (desktop version recommended)

## Installation

1. Clone the repository or download the script:

```bash
git clone https://github.com/mptm436/txt_to_ris.git
```

2. Navigate to the project directory:

```bash
cd txt_to_ris
```

## Usage

1. Export your Kindle clippings:

   - Connect Kindle to computer
   - Copy `My Clippings.txt` from Kindle's documents folder to the project directory

2. Run the converter:

```bash
python3 txt_to_ris.py
```

3. Import to Zotero:
   - Open Zotero
   - `File → Import...`
   - Select the generated `Kindle_Clippings.ris` file
   - Choose destination collection/folder

## File Structure

```
.
├── kindle_to_zotero.py    # Main conversion script
├── My Clippings.txt       # Input file from Kindle (not included)
├── Kindle_Clippings.ris   # Generated output file
├── README.md              # This documentation
└── requirements.txt       # Python version requirements
```

## Example

**Input (My Clippings.txt):**

```
The Art of War (Sun Tzu)
- Your Highlight on Page 3 | Added on Wednesday, January 1, 12:00:00 AM
Know yourself and you will win all battles
==========
```

**Output in Zotero:**

```
Type: Book
Title: The Art of War
Author: Sun Tzu
Notes:
- Highlight 1 (Wednesday, January 1, 12:00:00 AM): Know yourself and...
```

## Limitations

- Requires consistent Kindle clipping format
- Non-English characters might need special handling
- Complex book titles with parentheses may require manual adjustment

## Contributing

Contributions are welcome! Please open an issue or PR for:

- Additional format support (BibTeX, CSV)
- Enhanced metadata parsing
- Error handling improvements

## License

MIT License - See [LICENSE](LICENSE) for details

---

**Version:** 1.0.0  
**Last Updated:** October 2023
