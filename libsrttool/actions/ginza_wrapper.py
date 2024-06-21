"""
A wrapper around invoking the ginza tool, emitting spaCy-like JSON.
Ginza: https://github.com/megagonlabs/ginza
"""

import argparse
import glob
import json
import os
import shlex
import subprocess
import sys


def extend_cli(sp: argparse._SubParsersAction):
    """
    Extend a CLI with an interface for this module.

    Args:
        sp: The subparsers object on a CLI to extend. This function adds and
            configures one or more new subparsers.
    """
    parser = sp.add_parser(
        "ginza_wrapper",
        help="invoke ginza, processing one or more dialog files; output spaCy JSON",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--dialog_file",
        help="pathname of dialog file to process",
    )
    group.add_argument(
        "--dialog_dir",
        help="pathname of a directory containing dialog files to process",
    )
    parser.add_argument(
        "output_pathname",
        help="the pathname to write the JSON file(s) to",
    )
    parser.set_defaults(func=main)


def run_ginza(dialog: str) -> str:
    """
    Run the ginza tool on some content.

    Args:
        dialog: Dialog to pass to ginza for processing.
    Returns:
        The JSON content returned by ginza as a string.
    """
    r = subprocess.run(
        ["ginza", "-f", "json"], input=dialog, text=True, capture_output=True
    )
    if r.returncode != 0:
        print("ginza failed", file=sys.stderr)
        print(f"stderr: {r.stderr}", file=sys.stderr)
        # TODO(orphen) early-exit hack; handle this more cleanly.
        sys.exit(1)
    return r.stdout


def main(args: argparse.Namespace) -> int:
    files = []
    if args.dialog_file:
        if not os.path.isfile(args.dialog_file):
            print(f"{args.dialog_file} must be an ordinary file", file=sys.stderr)
            return 1
        files = [args.dialog_file]
    else:  # args.dialog_dir
        if not os.path.isdir(args.dialog_dir):
            print(f"{args.dialog_dir} must be a directory", file=sys.stderr)
            return 1
        files = glob.glob(os.path.join(args.dialog_dir, "*.txt"))

    if not os.path.exists(args.output_pathname):
        os.makedirs(args.output_pathname, exist_ok=True)

    # Check that ginza is accessible.
    r = subprocess.run(["ginza", "-h"], text=True, capture_output=True)
    if r.returncode != 0:
        print("Failed to run `ginza`.", file=sys.stderr)
        print(f"stderr: {r.stderr}", file=sys.stderr)
        return 1

    print(f"Processing {len(files)} files.")
    for i, f in enumerate(files):
        with open(f, "r") as dialog_file:
            # Join dialog naively with sentence-ending punctuation. If we instead join
            # with a newline, ginza will emit invalid JSON if it happens to process just
            # that newline.
            dialog = "。".join(dialog_file.readlines())
        ginza_json = run_ginza(dialog)
        output_file_base = os.path.basename(f)
        output_file = os.path.splitext(output_file_base)[0] + ".json"
        output_pathname = os.path.join(args.output_pathname, output_file)
        with open(output_pathname, "w") as json_file:
            some_json = json.loads(ginza_json)
            json.dump(some_json, json_file)

        print(f"({i}) {f}: done")

    return 0
