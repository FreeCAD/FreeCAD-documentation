# Compiling (Speeding up)/hr






{{TOCright}}

## Pregled

FreeCAD is a large application that may take from 10 minutes to one hour to compile completely from source. This depends primarily on the CPU that you have, and the number of cores that are used in the compilation process. Here are some tips to shorten that process and make build times shorter.

## CCache

Install `ccache` to cache builds.

## Disable modules 

When using `cmake` to configure the build, you can disable the compilation of certain workbenches that you may not need at the moment. This is useful if you only need to test a few workbenches.

For example, to avoid building the FEM and Mesh workbenches:


```python
cmake -DBUILD_FEM=OFF -DBUILD_MESH=OFF ../freecad-source
```

Use `cmake-gui`, `cmake-curses-gui`, or `cmake-qt-gui` to display all the possible variables that can be edited in the configuration; using these interfaces you can easily switch on or off different workbenches.

## Number of jobs in parallel 

After configuring with `cmake`, the `make` program launches the actual C++ compiler to work on the source code files. You can speed up compilation by working on various files at the same time. This is achieved with the `-j` option of `make`, which denotes the number of \"jobs\" or compilation commands that are run simultaneously. This option is an integer number.

Run four compilation commands in parallel:


```python
make -j4
```

Compile as many files in parallel as the number of CPU cores in your system. This is useful if you have many cores and want to use them all to compile the software.


{{code|code=
make -j$(nproc)
}}

Compile as many files in parallel as the number of CPU cores in your system, minus two. Use this so that your system is still responsive to do some other task; for example, two cores will allow you to use a browser, while the rest of the cores keep compiling the software on the background.


{{code|code=
make -j$(nproc --ignore=2)
}}

## distcc

The `distcc` program can be used to perform distributed compilation of C and C++ code across several machines in a network.







[Category:Developer\_Documentation](Category:Developer_Documentation.md) [Category:Developer](Category:Developer.md)
