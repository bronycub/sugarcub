#!/usr/bin/env bash

[[ $# -eq 0 ]] && docker run -v $(pwd)/shared:/shared -i -t --name console --rm sugarcub-console

[[ $# -eq 0 ]] || docker run -v $(pwd)/shared:/shared -i --name console --rm sugarcub-console -c "$*"
