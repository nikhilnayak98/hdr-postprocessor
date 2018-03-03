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

from __future__ import print_function
import datetime, os, sys
import text_handling

# Can set the starting level above zero explicitly when debugging.
verbosity_level = 0


class Logger(object):
    # An abstract logger class that encapsulates settings and behavior.
    def __init__(self, name="default logger", logfile_paths=None):
        # Set up the logger object. If LOGFILE_PATHS is specified, a log file is opened
        # and kept at each location in the list.

        self.width = text_handling.terminal_width()
        self.name = name
        self.output_destinations = [ sys.stdout ]
        if logfile_paths is None:
            self.logfile_paths = [][:]
        elif isinstance(logfile_paths, (list, tuple)):
            self.logfile_paths = logfile_paths
        else:
            self.logfile_paths = [ logfile_paths ]
        for logfile_path in self.logfile_paths:
            new_log_file = open(logfile_path, mode='wt', buffering=1)
            self.output_destinations += [ new_log_file ]
            new_log_file.write('Hello, traveler. This is the beginning of a log file called: "%s".\n' % self.name)
            new_log_file.write('Some basic system info about the host machine: %s\n' % str(os.uname()))
            new_log_file.write('This log was begun %s\n\n\n\n' % datetime.datetime.now().strftime('%A, %d %B %Y at %H:%M'))
            self.width = -1

    def __del__(self):
        # Clean up. More specifically: close any open files that aren't standard
        # streams.

        if sys is not None:
            for dest in self.output_destinations:
                if dest not in [sys.stdout, sys.stderr, sys.stdin]:
                    dest.close()

    def log_it(self, message, minimum_level=1):
        # Add a message to the log if the current verbosity_level is at least the minimum_level of the message.
        if verbosity_level >= 6:    # set verbosity to at least 6 to get this message output in the debug log
            self.log_it("\nDEBUGGING: function log_it() called", 1)
        if verbosity_level >= minimum_level:
            for dest in self.output_destinations:
                print('\n'.join(text_handling._get_wrapped_lines(message)), file=dest)

the_logger = Logger()


def log_it(message, minimum_level=1):
    # Convenience function to wrap the automatically created default Logger object.
    the_logger.log_it(message, minimum_level)
