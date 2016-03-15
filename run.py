#!/usr/bin/python

import os
import subprocess

for k, v in os.environ.iteritems():
    print k, "-->", v

print
subprocess.check_call(["git", "diff-tree", "--no-commit-id", "--name-only",
                       "-r", "%s" % os.environ['ghprbActualCommit']])
