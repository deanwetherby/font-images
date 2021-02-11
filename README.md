# Font Image Generator

Creates single character images for the provided font file.

![alt text](https://github.com/deanwetherby/font-images/raw/master/black_animated.gif "Font with dark background")
![alt text](https://github.com/deanwetherby/font-images/raw/master/white_animated.gif "Font with light background")


## Installation instructions

Clone this repo. Create a local virtual environment. Install dependencies.

```
$ git clone https://github.com/deanwetherby/font-images.git
$ cd font-images
$ python3 -m venv --prompt font venv
$ source venv/bin/activate
(font) $ python -m pip install --upgrade pip
(font) $ python -m pip install -r requirements.txt
```

## Usage

```
(venv) $ python generate.py -h
usage: generate.py [-h] [-f FONT] [-s SIZE] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -f FONT, --font FONT  True Type Font file (.ttf)
  -s SIZE, --size SIZE  Character image size
  -o OUTPUT, --output OUTPUT
                        Output folder to place character images
```

## Examples

```
(font) $ python generate.py --font Erebor.ttf --output ./output

```
