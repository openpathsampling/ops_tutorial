#!/bin/bash

openpathsampling pathsampling shooting_setup.nc -o 2_way.nc \
    --scheme 2_way -n 200
openpathsampling pathsampling shooting_setup.nc -o biased.nc \
    --scheme biased_shooting -n 200
