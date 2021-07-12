# FoilToDxf

Do you have an airfoil coordinate (.dat) file that you would like to convert into a DXF?
I do, so I wrote this script.

## Usage

### Parameters

* `-f`/`--file` - Location of .dat file.
* `-s`/`--scale` - Scale of airfoil.

Note that DXF doesn't have a true unit decsription per se. 
Rather, you actually select your units when you import the file.
Thus, specifying a scale of 54 means you would be wanting to import the airfoil with a chord of 54 mm, 54 in, etc.

At the present time, the outputs get dumped to the main directory.

### Example

* `python main.py -f some_airfoil.dat -s 54`
    * Produces a DXF file from an airfoil named "some_airfoil.dat" in the current directory with a chord length of 54. 
