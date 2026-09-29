# notes-to-markdown

Summary:
The "notes-to-markdown" repository provides a Node.js script designed to convert Standard Notes backup files into Markdown format. This enables users to utilize their notes across different file management systems that support Markdown. The conversion process extracts only the "title" and "text" properties from each note within the Standard Notes backup file, which is typically obtained by downloading an unencrypted copy of your data through the Standard Notes Desktop application.

Prerequisites include having a local, unencrypted version of your Standard Notes data downloaded to a folder on your computer. The README outlines step-by-step instructions for downloading this data via the Standard Notes desktop app, including visual guidance with screenshots.

Installation involves cloning the repository, installing its dependencies using npm, placing the specific backup file (`Standard Notes Backup and Import File txt.txt`) into the project's `src` directory, and executing the script with `node index.js`. The resulting Markdown files are generated in an output folder named `./out`.

KEYWORDS:
standard notes markdown conversion node js software utility backup file processing title text properties data import
