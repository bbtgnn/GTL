# GTL

The GTL (or Generatore Tipografico di Libertà) is a Python library for the creation of generative fonts.

Foremost thing: huge credits to [Daniele Capo](http://www.danielecapo.com/). He's the designer of the original project - this repository is in some ways a branch and a departure from his idea.

And thanks also to  all the XYZ2018 partecipants: Micol Salomone, Giovanni Abbatepaolo, Roberto Ciarambino, Alberto Guerra, Greta Capozzi, Enzo Di Gioia, Elsa Moro, Giulio Galli, Alessandra Del Nero, Vittorio Veronesi, Mattia Bressan, Marco Napoletano, Dania Menafra, Laura Laricchiuta, Roberto Lenza, Eleonora Cappuccio, Marco Balestra, Lucien Haba, Ass Diop Faty, Matija Grgič.

</br>
</br>
</br>

---
## 0 - What does it do

The GTL takes as input

 - a **structure** - ASCII-like drawings of glyphs
```
.........     ........
...O##...     ........
..O...#..     ........
..O...#..     .#O##O..
..#...O..     .#...#..
..O#O##..     .....O..
..#...#..     .#O#O#..
..#...O..     .#...#..
.#O...##.     .O#O#.#.
.........     ........
```

- a **syntax** - a set of instructions
```
. -> draw a white space
# -> draw a rectangle
O -> draw a circle
```
and by combining the inputs generates an actual, usable font:

![https://raw.githubusercontent.com/bbtgnn/GTL/master/readme_images/Aa.png](https://raw.githubusercontent.com/bbtgnn/GTL/master/readme_images/Aa.png)
The GTL is the perfect tool for the development of lazy-brutal-discrete typefaces, allowing for a fast and flexible drawing process: just by changing the syntax is it possible to generate endless variations for the same letter structure!

The GTL is meant to be used by everyone. If you're curious, let's dive in!

</br>
</br>
</br>

---
## 1 - Install guide
The GTL requires [Python](https://www.python.org/). It has been tested only on Python 3.7.4, but should work on other versions as well (if not, stick with 3.7.4).

</br>

---
### 1.1 - Virtual Environment creation
It is strongly recommended to create a Python Virtual Enviroment for the installation of all the needed libraries and the usage of the GTL.

\-
#### 1.1.1 - Folder creation
Create a folder anywhere you want.

\-
#### 1.1.2 - Virtual Environment creation
Open the terminal and input
```
python3 -m venv <DIR>
```
where ```<DIR>``` is the full path of the created folder. For example:
```
python3 -m venv /Users/username/Desktop/venv_gtl
```

\-
#### 1.1.3 - Virtual Environment activation
The virtual enviroment needs to be activated *each time* you want to use the GTL. To do it, run in the terminal
```
# On macOS
source <DIR>/bin/activate

# On Windows
<DIR>\Scripts\activate
```
e.g.
```
source /Users/username/Desktop/venv_gtl/bin/activate
```
(To exit from the environment anytime just enter ```deactivate``` or close the terminal.)

</br>

---
### 1.2 - Installing fontParts
[FontParts](https://fontparts.readthedocs.io/) is the core library over which the GTL has been built. To install it - **while the virtual environment is active** - run in terminal
```
pip install fontParts==0.8.7
```
FontParts is still in development, and newer version are already out. As of today, the GTL has been tested only on the 0.8.7 version.

</br>

---
### 1.3 - Setting up the workspace
Download this master folder anywhere. This is the folder architecture:
```
.
│
├── GTL                  # CORE FOLDER, don't touch
│   └── ...
│
├── GTL_syntax.py        # Here you'll set the syntax
├── GTL_params.py        # Here you'll set some minor (but important) parameters
├── GTL_main.py          # This is the file to run to generate the font
│
├── LICENSE              # …
├── README.md            # …
│
└── test_letters         # Here's a sample of some letters ready to use
    └── ...
```

</br>
</br>
</br>

---
## 2 - How it works

### 2.1 - Drawing the letters

First of all, you have to design the letter structure!
Each letter should be drawn in a separate **.TXT file**. The file should look like this:
```
A               # LINE 1 ━ glyph name
                # LINE 2 ━ empty line
...##O...       # LINE 3 ┓
..#...#..	  .      ┃
..#...#..	  .      ┃
..#...#..	  .      ┃
..O####..	  .      ┣ glyph structure
..#...O..	  .      ┃   
..#...O..	  .      ┃
.O#...##.	  .      ┃
.........       # LINE N ┛
```
**Important notes about the glyph name**
- The glyph name **is not** the glyph itself: for example, the name for ```à``` is ```agrave```. You can search the glyph in this [reference table](https://github.com/bbtgnn/AGLFN-table/blob/master/AGLFN-table.tsv) and get its name from ```Glyph name``` column.
- If a glyph is not in the provided table you can give it a random name. **Only letters** (A-Z, a-z) are accepted.

**Important notes about the glyph structure**
- For each letter of the font - the number of the rows **must** be the same.
- In the same letter - all the rows **must** have the same length.
- It's important to have at least one **empty** column for each side, to give glyphs some margin.

Other things
-  Glyphs from the same font can have different widths (a different row length).
- You can use all the symbols you want in the glyph structure. The more the symbols, the more will be possible to create complex designs and behaviours. 
- Remember that the _space_ is also a glyph.

Once you've drawn all the glyphs, store them in a folder.

</br>

---
### 2.2 - Syntax

Once you've designed the letters (or, if you're lazy, decided to use the sample letters in the master folder) it's time to define the **syntax**.

\-

So open ```GTL_syntax.py``` with a *code editor* and scroll all the way down: you'll find this
```
syntax = {
    # Add instructions here
}
```
Each symbol used in the glyph structure needs an **instruction**: the GTL needs to know what to do when it reads each symbol found in the glyph structure.

An instruction looks like this:
```
"character": (function, function_properties),		# the comma is important
```
- **character** - here goes the symbol you used in the description 
- **function** - here you tell the GTL what to do when it reads that character
- **function_properties** - here you set some parameters to modify the behaviour of the function

**Before continuing, please check the section [Functions and Properties](#functions-and-properties) to see the complete list of Functions and Functions Properties**

\-
#### Example
Let's now say you decided that you want to draw a rectangle each time there's a ```#``` in the glyph structure. According to what we said before, we need a *symbol*, a *function* and *function_properties*. Symbol and function we have (respectively ```#``` and ```rectangle```). But we do not have any *function_properties*! We'll have to *write* this one.

For the moment, the syntax looks like this
```
syntax = {
    "#": (rectangle, ?),
}
```

\-
#### Writing a property

As you might have noticed, in the ```GTL_syntax.py``` file, above the syntax, there's a section called ```Properties```: there'll go our code.

We start by creating the "container" of the properties.
```
container = {
}
```
Since we will have different properties, it's good practice to give the container an appropriate name:
```
p_rectangle = {			# "p" is short for "properties"
}
```
Then, we add the corresponding properties for the function we chose. Since we chose the rectangle, we copy and paste its properties from the [section below](#functions-and-properties), enclosing them between quotes and adding a colon and a comma after it.
```
p_rectangle = {
    "scale_x": ,
    "scale_y": ,
    "rotation": ,
}
```
Then we have to add the values. Let's say we do not want to scale the rectangle, but we want to give it a random rotation each time it gets drawn. So the properties will look like this:
```
p_rectangle = {
    "scale_x": 1,		# Scaling by 1 means no change
    "scale_y": 1,		# Scaling by 1 means no change
    "rotation": (0, 360),	# A random angle between 0 and 360 will be chosen
}
```
And now that we have our property, we can write the instruction!
```
syntax = {
    "#": (rectangle, p_rectangle),
}
```
At this point, you just need to add an instruction for each symbol you used in the glyphs structures and you're good to go!

\-

**Extra tip**</br>
The property for the function ```do_nothing``` looks like this: ```p_do_nothing = {}```.
Since the function does nothing, the container for its properties is empty.

</br>

---
### 2.3 - How to generate the font (Where the magic happens!)

#### 2.3.1 - Edit GTL_params.py
Next (and almost final) step: you need to edit the ```GTL_params.py``` file by adding all the requested variables.
```
## PATHS

# Path of folder containing glyphs txt
txt_path = "path/to/txt/files"

# Path of folder of output font
out_path = "path/to/chosen/folder"
```
```
## FONT INFO

# Font name (anything you like: Sator, Avocado, etc)
font_name = "Tenet"

# Style name (Regular, Bold, Rectangular, Dizzy, etc)
style_name = "Regular"
```
```
## FONT METRICS
# For the font metrics section, you just have to count the rows as shown in this example:
```
![https://raw.githubusercontent.com/bbtgnn/GTL/master/readme_images/metrics.png](https://raw.githubusercontent.com/bbtgnn/GTL/master/readme_images/metrics.png)
```
## BOX PROPERTIES

# FLOAT - Set box width ratio (width_ratio=1 for square proportions)
width_ratio = 1
```
![https://raw.githubusercontent.com/bbtgnn/GTL/master/readme_images/width_ratio.png](https://raw.githubusercontent.com/bbtgnn/GTL/master/readme_images/width_ratio.png)
```
# (INT, INT) - Set box layout (e.g. box_layout = (1,1))
box_layout = 1,1
```
![https://raw.githubusercontent.com/bbtgnn/GTL/master/readme_images/box_layout.png](https://raw.githubusercontent.com/bbtgnn/GTL/master/readme_images/box_layout.png)

\-
#### 2.3.2 - Terminal instructions to make magic happen

Activate the Virtual Environment

```
# On macOS
source <DIR>/bin/activate

# On Windows
<DIR>\Scripts\activate
```
Run
```
python3 /path/to/GTL_main.py
```

aaand… enjoy! :) 

(The font will be saved both as UFO format: to make it fully usable you have to export it as OTF file from a font editor such as [FontForge](https://fontforge.org/en-US/).)

</br>
</br>
</br>

---
## Functions and properties

Here's a  list of all the available functions and their properties.
```
function	| function description
    - property	    | property description
```
```
p_do_nothing    | does nothing
    - [has no properties]

p_rectangle     | draws a rectangle
    - scale_x       | horizontal scale factor
    - scale_y       | vertical   scale factor
    - rotation      | rotation (in degrees)

p_ellipse       | draws an ellipse
    - scale_x       | "
    - scale_y       | "
    - rotation      | "
    - squaring      | squaring degree of the curve

ellipse_quarter | draws an ellipse quarter
    - scale_x       | "
    - scale_y       | "
    - rotation      | "
    - squaring      | "
    - orientation   | orientation of the quarter

random_function | executes a random function chosen between the ones provided
    - function_properties_list
                    | a list of function-properties couples
```
And this is a list of possible values for each property:
```
properties
	- data type					data example
```
```
scale_x, scale_y, rotation, squaring
	- an integer number (int)			1
	- a floating point number (float)		3.14
	- a range of int and/or float			(-3.14, 9)
	- a list  of int and/or float			[0, 9.32, -12, 4.3]

orientation
	- an orientation (str)				"NW" or "NE" or "SW" or "SE"
	- a list of orientations			["NW", "NE", "SE"]

function_properties_list
	- a list of function-properties couples		[(f1, f1_prop), (f2, f2_prop), …]
```	
**Important notes**
 - In case of **range** values, will be chosen a random number between the extremes.
 - In case of **list** values, will be chosen a random value from the ones in the list.

Also remember:
- **Lists** are always enclosed in **squared brackets**.
- **Ranges** and **couples** are always enclosed in **round brackets**.
