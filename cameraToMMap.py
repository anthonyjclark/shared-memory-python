#!/usr/bin/env python3

from argparse import ArgumentParser
from mmap import mmap, PROT_WRITE
from time import time
import cv2

arg_parser = ArgumentParser("Get images from camera and write to mmap file.")
arg_parser.add_argument("filename", help="Name of mmap file")
arg_parser.add_argument("camera", type=int, help="Camera index")
arg_parser.add_argument("width", type=int, help="Image width")
arg_parser.add_argument("height", type=int, help="Image height")
args = arg_parser.parse_args()

file_bytes = args.width * args.height * 3
cap = cv2.VideoCapture(args.camera)

with open(args.filename, "r+b") as mem_file:

    with mmap(mem_file.fileno(), file_bytes, prot=PROT_WRITE) as mem:

        try:

            while True:
                ret, img = cap.read()
                if not ret:
                    print("Could not read from camera.")
                    break

                img = cv2.resize(img, (args.width, args.height))

                # Write image to mmap file
                start = time()
                buf = img.tobytes()
                mem.seek(0)
                mem.write(buf)
                mem.flush()
                stop = time()

                print(f"Time to write: {(stop - start) * 1000:.2f} ms")

        except KeyboardInterrupt:
            pass

cap.release()
