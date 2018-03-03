#!/usr/bin python3
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

# This quick hack makes an HDR script from all JPG photos in the current 
# directory. Then it runs it. It assumes that all of the photos are JPGs in the
# current directory, that all of the JPGs in the current directory are photos for
# the project, and that there are no other .SH files in the current directory.


import os, glob, subprocess

import postprocessor as pprocessor
import hdr_script_generator as cHs

the_files = sorted(glob.glob('*JPG') + glob.glob('*jpg'))
if len(the_files) > 0:
    cHs.create_script_from_file_list(the_files)
    pprocessor.run_shell_scripts()
else:
    raise IndexError('You must call main_jpg.py in a folder with at least one *jpg or *JPG file;\n   current working directory is %s' % os.getcwd())