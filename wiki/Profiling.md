# Profiling
## Description

Profiling the code of FreeCAD helps find bottlenecks in the algorithms used to create or manipulate objects.

To profile [Python](Python.md) code use the standard  
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

Then install and use  
```python
pyprof2calltree -i /tmp/profile.cprof -o /tmp/callgrind.out
```

Then visualize this information with  
```python
kcachegrind /tmp/callgrind.out
```

## Resources

-   [The Python profilers](https://docs.python.org/3/library/profile.html), `cProfile` and `python`.
-   [pyprof2calltree](https://pypi.org/project/pyprof2calltree/) at PyPI; [pyprof2calltree](https://github.com/pwaller/pyprof2calltree/) repository.
-   [FreeCAD\'s Python profiling tutorial](https://forum.freecadweb.org/viewtopic.php?f=10&t=44785).



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Profiling
