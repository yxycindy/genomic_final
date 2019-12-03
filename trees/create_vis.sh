#!/bin/bash

# $1 is the name of the file
dot -Tpng $1".dot" > $1".png"
