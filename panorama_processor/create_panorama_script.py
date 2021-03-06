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
#
# This quick hack writes a bash script that uses the PTTools to stitch a
# panorama from all photos in the current directory. It assumes that all of the
# photos are JPGs in the current directory, and that all of the JPGs in the
# current directory are photos for the panorama. 
#
# A short (i.e., non-comprehensive) list of choices the output script makes for
# you would include:
#     * using CPFind as the control point detector;
#     * continuously overwriting the same project file instead of leaving
#       multiple project files behind to allow for problem tracing;
#     * treating the first file (according to standard lexicographic sort by
#       filename) as the reference (or "anchor") image for the purposes of both
#       position and exposure, which often winds up not being the best choice;
#     * assuming that the input images are taken with a rectilinear lens;
#     * running Celeste;
#     * running CPFind's version of Celeste instead of Celeste standalone;
#     * using the --multirow match detection algorithm, which is generally
#       pretty good, but which is not perfect for all possible scenarios, and
#       which does unnecessary work in single-row panoramas, sometimes causing
#       problems on its own;
#     * running CPClean with default parameters;
#     * automatically optimizing control points, which is almost certainly a
#       good idea in most, but not all, cases;
#     * trying to find a suitable projection type, which is often basically
#       successful but rarely makes the absolute best possible choice;  
#     * doing photometric optimization, which wastes time if the shots were
#       manually shot at the same exposure;
#     * trying to find vertical control points, which is often successful and
#       frequently a good idea, though the process can go astray;
#     * automatically calculating ostensibly optimal canvas and crop sizes; and
#     * using hugin_executor as the stitching program (PTBatchGUI might also be
#      used for this purpose).

import os, glob, subprocess

import postprocessor as pprocessor

the_files = sorted(list(set(glob.glob('*JPG') + glob.glob('*jpg'))))
the_files_list = ' '.join(the_files)
project_file = the_files[0] + ".pto"
if the_files:
    the_script = """#!/usr/bin/env bash
pto_gen -o %s %s
""" % (project_file, the_files_list)
    
    the_script = the_script + """
cpfind --multirow --celeste -o %s %s
cpclean -o %s %s
linefind -o %s %s
autooptimiser -a -l -s -m -o %s %s
pano_modify --canvas=AUTO --crop=AUTO -o %s %s
# hugin_executor -s %s                              # Uncomment to stitch the panorama immediately
""" % tuple([project_file] * 11)
    
    script_file_name = os.path.splitext(the_files[0])[0] + '-pano.SH'
    with open(script_file_name, mode='w') as script_file:
        script_file.write(''.join(the_script))
    
    os.chmod(script_file_name, os.stat(script_file_name).st_mode | 0o111)    # or, in Bash, "chmod a+x SCRIPT_FILE_NAME"
    
    # pprocessor.run_shell_scripts()    # uncomment this line to automatically run all scripts in the directory.
else:
    raise IndexError('You must call panorama_script_generator.py in a folder with at least one .jpg or .JPG file;\n   current working directory is %s' % os.getcwd())