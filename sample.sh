#! /usr/bin/bash

ping epfl.ch -c 30 | cut " " -f 8 | cut "=" -f 2 | head -n 32 > samplertt.txt


