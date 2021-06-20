#!/bin/bash

for iface in 0 1 2 3 4; do
    echo "SAMPLING INTERFACE ${iface}"
    openpathsampling equilibrate parallel_setup.nc -o equil_${iface}.nc \
        --scheme scheme_${iface} --extra-steps 5 # user does 50
    openpathsampling pathsampling equil_${iface}.nc -o scheme_${iface}.nc \
        -n 300
done

echo "SAAMPLING RETIS"
openpathsampling equilibrate parallel_setup.nc -o equil_retis.nc \
    --scheme retis --extra-steps 5  # user does 50
openpathsampling pathsampling equil_retis.nc -o retis.nc -n 2850
