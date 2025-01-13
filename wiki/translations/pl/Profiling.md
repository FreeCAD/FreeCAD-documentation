# Profiling/pl
## Opis

Profilowanie kodu FreeCAD pomaga znaleźć wąskie gardła w algorytmach używanych do tworzenia lub manipulowania obiektami.

Do profilowania kodu [Python](Python/pl.md) należy użyć standardowego modułu `cProfile`, aby zdefiniować punkty początkowe i końcowe do profilowania w kodzie. 
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

Następnie zainstaluj i użyj `pyprof2calltree`, aby przekonwertować dane wyjściowe profilu na dane wejściowe cachegrind. 
```python
pyprof2calltree -i /tmp/profile.cprof -o /tmp/callgrind.out
```

Następnie zwizualizuj te informacje za pomocą `kcachegrind` dla systemu Linux lub `qcachegrind` dla systemu Windows. 
```python
kcachegrind /tmp/callgrind.out
```



## Zasoby

-   [Profilery Python](https://docs.python.org/3/library/profile.html), `cProfile` i `python`.
-   [pyprof2calltree](https://pypi.org/project/pyprof2calltree/) w PyPI; [pyprof2calltree](https://github.com/pwaller/pyprof2calltree/) repozytorium.
-   [Poradnik profilowania FreeCAD w Python](https://forum.freecadweb.org/viewtopic.php?f=10&t=44785).



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Profiling/pl
