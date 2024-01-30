# Partial State Machine Generator

Webservers need to parse specifically encoded input. The input follows
a normal format that can easily parsed by a stack machine. It either is
encoded in ascii or compressed ascii. Both forms can be decoded by a
stack machine built against their gramars.

This project is meant to generate efficient stack machine parses with
input that can be stopped mid read. This is critical as data is read 
in chunks across the network.

In order to support both formats, the end implementation will need to 
treat the states from binary rather than from characters only. The
current implementation uses only characters.

## Input

The main way currently proposed as input is by hand encoding the 
statemachine by using python and the library's public api. With the focus
primarily being generatoring http 1/2/3 REQUEST headers and frames. 
Therefore, reading a grammar is not necessarily required. 

## Speed

The state machines will be reduced to the minimal versions.

## Correctness

Hard tests and fuzzing

## Output

The ultimate output will be optimized c++ code that can be injected into a cmake
build system. This could should be optimized to minimize cache misses and be able
to stop and start parsing from any place in the input.

