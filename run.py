#!/usr/bin/python

import os
import subprocess

subprocess.check_call(["git", "diff-tree", "--no-commit-id", "--name-only",
                       "-r", "%s" % os.environ['ghprbActualCommit']])
