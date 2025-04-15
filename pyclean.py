#!/usr/bin/env python3
import os
import sys
import shutil

def clean(path="."):
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if name == "__pycache__":
                full_path = os.path.join(root, name)
                shutil.rmtree(full_path)
                print(f"Deleted: {full_path}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    clean(target)
