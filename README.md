# GTL
GTL (or Generatore Tipografico di Libertà) is a Python set of libraries for the creation of generative fonts.<br />

The program generate a typeface (.ufo) from a "lazy-discrete" description (for each letter) and a set of instructions to "translate" the "brutal-discrete" description (a syntax).

With this tool you can create lazy-discrete-typefaces (saving a lot of time!).
We believe this is the best brutal ruled-based-typography development tool. 

Most important thing: credits to [Daniele Capo](http://www.danielecapo.com/). He had the original idea about this project - mine is a further development.
<br />
<br />

# WHAT DOES IT DO?

```
........        ...0#1...
........        ..#...#..
.#####..        ..#...#..
.#...#..        ..#...#..
.....#..        ..2###1..
.#####..        ..#...#..
.#...#..        ..#...#..
.####.#.        .##...##.
........        .........
........        .........

```

The program takes many txt files (for each letter) and transforms them (parsing) into an .ufo typeface.
For each symbol in the txt file the programm will do something.
So you can create a syntax to use many different symbols to describe you design into the txt files.

The program works quickly and allow you to operate in a smart way that anyone can approach.

## Install guide
GTL requires [Python](https://www.python.org/) 3.4 or later.

### 1. Virtual Environment creation
First of all, it is strongly recommended to create a Python Virtual Enviroment for the installation of all the needed libraries.

Create a folder where you want (e.g. I usually store all my environments in ```Documents/PythonEnvironments/```).

Then open to the terminal and input
```
# (change <DIR> with the path of your folder)
python3 -m venv <DIR>
```
to create the virtual environment.<br />
To activate it run
```
# On macOS
source <DIR>/bin/activate

# On Windows
<DIR>\Scripts\activate
```
(To exit from the environment, anytime, just enter ```deactivate```.)

### 2. Installing fontParts
[FontParts](https://fontparts.readthedocs.io/) is the core library over which the GTL has been built. To install it (while the virtual environment is active) type in terminal
```
pip install fontParts==0.8.7
```
FontParts is still in development, and newer version are already out. For the moment, the GTL has been tested only on the 0.8.7 version.

### 3. Setting up the workspace
Download the master folder anywhere and you're ready to start!
<br />
<br />

## How it works (Folders Architecture)
```
– GTL                                   // CORE FOLDER, don't touch
– GTL_main.py                           // the file to run
– GTL_syntax.py                         // parameters and functions
– LICENSE                               // …
– README.md                             // …
– TEST_LETTERS                          // LETTER STRUCTURES FOLDER (TXT FILES FOR EACH LETTER)
```
### 1. Syntax
the structure of the syntax is: 

# string : (function, properties)

**string**            = a glyph used in the txt files to describe something
**function**          = what the program has to do when meets the string
**properties**        = some function parameters 

At the top of Syntax file you will find the constants:

**CONSTANTS ORIENTATIONS = ["NW", "NE", "SW", "SE"]**

### 2. Input typologies
All properties could accept 2 different typologies of input:

#### a single value
    — int             1
    — float           3.14
    — string          "NW", "NE", "SE", SW" (only if possible)
    
#### a couple of values ("a tuple")
    — range           ("RANGE", [2, 21])                  // only 2 elements
    — choice          ("CHOICE", [2, 23, 7 , 32, 21])     // how many elements do you want 

In every function you can use the input you want.

For example:
**"scale_x":1** or **"scale_x":1.5** or **"scale_x":("RANGE", [1, 5])** or **"scale_x":("CHOICE", [1, 5, 10, 25])**

### 3. Functions and Properties

**do_nothing**          = it does nothing
  — "null"              = the only avaible value is "null"            

**rectangle**           = it draws a rectangle filling the cell
  — "scale_x":1         = horizontal scale factor
  — "scale_y":1         = vertical scale factor
  — "rotation":0        = rotation degrees

**ellipse**
  — "scale_x":1         = horizontal scale factor
  — "scale_y":1         = vertical scale factor
  — "rotation":0        = rotation degree
  — "squaring":.56      = squaring degree of the ellipse (0 < X < 1 for ellipses)
  
**ellipse_quarter**
  — "scale_x":1         = horizontal scale factor
  — "scale_y":1         = vertical scale factor
  — "rotation":0        = rotation degrees
  — "squaring":.56      = squaring degree of the ellipse (0 < X < 1 for ellipses)
  – "orientation":"NW"  = orientation of the quarter (**use only constants**)

**random_function**
  — "functions":        = a list of tuple, with 2 arguments: "the function" and "the properties".

### 4. Anatomy of a txt-letter file

```
A

...0#1...
..#...#..
..#...#..
..#...#..
..2###1..
..#...#..
..#...#..
.##...##.
.........
.........
```

At the top, first of all, you need to insert the unicode name for the glyph.
After an empty row.

The number of the rows for each letter of the alphabet should be the same.
In the same letter, the number of the columns for each row must be the same.
In different letters you can use different widths (columns number)
If you need more kinds of marker you can edit the syntax, setting them.

## How to generate the font (this is the magic!)

### 1. Edit GTL_main.py setting the variables
```
# Path of folder containing glyphs txt
txt_path = "/path/to/folder/of/letters"

# Path of output font
out_path = "/path/to/folder/of/font.ufo" // (important: remember to use the .ufo extension!)

# Set glyphs'baseline row (counting from bottom of txt)
gly_baseline = 2

# Set box size
box = 100, 100

# Set number of box sub-units for recursive functions
box_col = 1
box_row = 1

```

### 2. Terminal instructions to make magic happens

after you activate the virual environment

```
# On macOS
source <DIR>/bin/activate

# On Windows
<DIR>\Scripts\activate
```

type **python3 /path/to/GTL_main.py**

now… enjoy! ;) 
