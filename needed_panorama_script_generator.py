#!/usr/bin/python3
#
# MIT License
#
# Copyright (c) 2018 Nikhil Nayak
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import glob, os, subprocess, time

if __name__ == "__main__":
    for i in sorted([x[0] for x in os.walk('.')]):
        try:
            olddir = os.getcwd()
            os.chdir(i)
            print("Currently checking directory:  " + i)
            if len(glob.glob('*jpg') + glob.glob("*JPG")) > 0:
                print("  JPEG files found!", end=" ")
                if len(glob.glob("*pto")) > 0:
                    print("But there's an existing project file! Skipping...")
                else:
                    print("Creating new project script ...")
                    subprocess.call('panorama_script_generator.py', shell=True)
        finally:
            os.chdir(olddir)
            time.sleep(0.1)

