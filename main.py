# Connor Luckett
import argparse
import os

import ezdxf
import numpy as np
import pandas as pd


def main():
    # Parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--input',
        type=str,
        help="Path to DAT file",
    )
    parser.add_argument(
        '-o',
        '--output',
        default=os.getcwd(),
        type=str,
        help="Output directory to place the DXF file",
    )
    parser.add_argument(
        '-s',
        '--scale',
        default=1,
        type=float,
        help="Chord length of airfoil (AutoCAD is unit-agnostic)",
    )
    args = parser.parse_args()

    # Get the file's name and location and units to be used
    input_path = args.input
    output_dir = args.output
    scale = args.scale

    # Check that the inputs are valid
    assert os.path.isfile(input_path), "File does not exist"
    assert scale > 0, "Scale must be greater than 0"
    assert os.path.isdir(output_dir), "Output path must be a directory"

    # Good to go!
    print("Reading in {} with scale {}".format(input_path, scale))

    # Load the file
    coord_df = pd.read_csv(input_path, sep=r"\s+", header=None, skiprows=1, dtype=np.float64)
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
    output_file = '{}.dxf'.format(os.path.splitext(os.path.basename(input_path))[0])
    output_path = os.path.join(output_dir, output_file)
    print("Saving as: {}".format(output_path))
    dxf.saveas(output_path)


if __name__ == '__main__':
    main()
