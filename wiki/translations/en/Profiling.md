# Profiling/en
## Description

Profiling the code of FreeCAD helps find bottlenecks in the algorithms used to create or manipulate objects.

To profile [Python](Python.md) code use the standard `cProfile` module to define start and end points to profile in the code. 
```python
import cProfile
pr = cProfile.Profile()
pr.enable()

# 
# Lines of code that you want to profile
# 

pr.disable()
pr.dump_stats("/tmp/profile.cprof")
```

Then install and use `pyprof2calltree` to convert the profile output into cachegrind input. 
```python
pyprof2calltree -i /tmp/profile.cprof -o /tmp/callgrind.out
```

Then visualize this information with `kcachegrind` for Linux or `qcachegrind` for Windows. 
```python
kcachegrind /tmp/callgrind.out
```

## Resources

-   [The Python profilers](https://docs.python.org/3/library/profile.html), `cProfile` and `python`.
-   [pyprof2calltree](https://pypi.org/project/pyprof2calltree/) at PyPI; [pyprof2calltree](https://github.com/pwaller/pyprof2calltree/) repository.
-   [FreeCAD\'s Python profiling tutorial](https://forum.freecadweb.org/viewtopic.php?f=10&t=44785).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Profiling/en
