# Profiling/de
## Beschreibung

Das Profilieren des Codes von FreeCAD hilft Flaschenhälse in den Algorithmen zu finden, die zur Erstellung oder Bearbeitung von Objekten verwendet werden.

Zum Profilieren des [Python](Python/de.md)-Codes, wird das Standardmodul `cProfile` verwendet, um Start- und Endpunkte der Profilierung im Code zu definieren. 
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

Dann wird `pyprof2calltree` installiert und ausgeführt, um die Ausgabe der Profilierung in eine Eingabe für cachegrind umzuwandeln. 
```python
pyprof2calltree -i /tmp/profile.cprof -o /tmp/callgrind.out
```

Danach wird diese Information mit `kcachegrind` für Linux oder `qcachegrind` für Windows angezeigt. 
```python
kcachegrind /tmp/callgrind.out
```



## Ressourcen

-   [The Python profilers](https://docs.python.org/3/library/profile.html), `cProfile` and `python`.
-   [pyprof2calltree](https://pypi.org/project/pyprof2calltree/) at PyPI; [pyprof2calltree](https://github.com/pwaller/pyprof2calltree/) repository.
-   [FreeCAD\'s Python profiling tutorial](https://forum.freecadweb.org/viewtopic.php?f=10&t=44785).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Profiling/de
