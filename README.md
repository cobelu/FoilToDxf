# FoilToDxf

Do you have an airfoil coordinate (.dat) file that you would like to convert into a DXF?
I do, so I wrote this script.

## Usage

### Parameters

* `-i`/`--input` - Path to .DAT file
* `-o`/`--output` - Path to output directory
* `-s`/`--scale` - Scale of airfoil (AutoCAD is units-agnostic)
* `-h`/`--help` - Display help

Note that DXF doesn't have a true unit decsription _per se_. 
Rather, you actually select your units when you import the file.
Thus, specifying a scale of 54 means you would be wanting to import the airfoil with a chord of 54 mm, 54 in, etc.
The default ouput directory is your current working directory.

### Examples

* `python main.py -i some_airfoil.dat -s 54`
    * Produces a DXF file from an airfoil named "some_airfoil.dat" in the current directory with a chord length of 54. 
* `python main.py -i some_airfoil.dat -o ../dxfs/ -s 48`
