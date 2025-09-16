#!/usr/bin/env python
# Code by Lachlan Marnoch, 20XX

import os

import template as template

description = """
Does something cool.
"""


def main(
        output_dir: str,
        input_dir: str
):
    print("Template script running.")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description=description
    )

    parser.add_argument(
        "-o",
        help="Path to output directory.",
        type=str,
        default="./output"
    )
    parser.add_argument(
        "-i",
        help="Path to directory containing input files.",
        type=str,
        default="./input"
    )

    args = parser.parse_args()
    output_path = args.o
    input_path = args.i
    main(
        output_dir=output_path,
        input_dir=input_path
    )
