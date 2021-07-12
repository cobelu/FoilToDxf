# Connor Luckett
import argparse
from enum import Enum

import ezdxf
import pandas as pd


def main():
    # Parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str)
    parser.add_argument('-s', '--scale', default=1, type=float)
    args = parser.parse_args()
    # Get the file's name and location and units to be used
    filename = args.file
    scale = args.scale
    # Load the file
    coord_df = pd.read_csv(filename, sep='\t', header=None, skiprows=1)
    # Scale it
    coord_df = coord_df * scale
    # Add a column of zeros to fool AutoCAD (AutoCAD is such a jerk)
    coord_df[2] = 0
    # Convert the dataframe to tuples for drawing
    coords = list(coord_df.itertuples(index=False, name=None))
    # Initialize the DXF file
    dxf = ezdxf.new(dxfversion='AC1027')
    # Create a model space
    msp = dxf.modelspace()
    # Add a spline
    msp.add_spline(coords)
    # Close off the airfoil
    first = coords[0]
    last = coords[-1]
    msp.add_line(first, last)
    # Save as a DXF
    out_filename = filename.split('.')[0]
    dxf.saveas('{0}.dxf'.format(out_filename))


if __name__ == '__main__':
    main()
