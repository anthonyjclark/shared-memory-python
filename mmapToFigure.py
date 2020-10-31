#!/usr/bin/env python3

from argparse import ArgumentParser
from mmap import mmap
from time import time

import cv2
import numpy as np

arg_parser = ArgumentParser("Get images from camera and write to mmap file.")
arg_parser.add_argument("filename", help="Name of mmap file")
arg_parser.add_argument("camera", type=int, help="Camera index")
arg_parser.add_argument("width", type=int, help="Image width")
arg_parser.add_argument("height", type=int, help="Image height")
args = arg_parser.parse_args()

file_bytes = args.width * args.height * 3
image_shape = (args.height, args.width, 3)

# # Create initial file
# with open(filename, "wb") as mem_file:
#     for i in range(n):
#         mem_file.write(b"0")

with open(args.filename, "r+b") as mem_file:

    with mmap(mem_file.fileno(), file_bytes) as mem:

        while True:
            # Read image from shared mmap
            start = time()
            mem.seek(0)
            buf = mem.read(file_bytes)
            img = np.frombuffer(buf, dtype=np.uint8).reshape(image_shape)
            stop = time()

            print(f"Time to read: {(stop - start) * 1000:.2f} ms")
            cv2.imshow("Image", img)

            key = cv2.waitKey(1) & 0xFF
            key = chr(key)
            if key.lower() == "q":
                break

cv2.destroyAllWindows()
