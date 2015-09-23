#!/bin/bash
import os
import sys


environment = os.environ
environment_variable = sys.argv[1]

print(environment[environment_variable])
