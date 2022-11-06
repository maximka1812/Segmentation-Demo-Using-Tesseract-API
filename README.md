<h1 align="center">Tesseract API Page Segmentation Example</h1>

  <p align="center">
    Python3 script to show ability to use Tesseract OCR page segmentation !
    <br />
    </p>

## About 

Simple demo of page segmentation using Tesseract API, can be used for different purposes, not necessary OCR!

## Installing requirements

Install tesserocr library and binaries through https://github.com/simonflueckiger/tesserocr-windows_build

It contains ready to install wheels (use "pip install wheels" if they are not installed!).

All you need to do is type pip install https://github.com/simonflueckiger/tesserocr-windows_build/releases/download/tesserocr-v2.5.2-tesseract-4.1.1/tesserocr-2.5.2-cp38-cp38-win_amd64.whl

After this you need to download training data for languages you use from https://github.com/tesseract-ocr/tessdata/ 

It'll show you proper path where to put them as you try to run it without proper trainign data!
   
## Usage

   On Windows just run seg.bat with argument containing image file

## Notes

For now it is just bare demo showing you how to use API (large part comes from Stackoverflow answer).