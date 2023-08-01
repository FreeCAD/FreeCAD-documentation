# Profiling/it
## Descrizione

La profilazione del codice di FreeCAD aiuta a trovare i colli di bottiglia negli algoritmi utilizzati per creare o manipolare oggetti.

Per profilare il codice [Python](Python/it.md) usare il modulo standard `cProfile` per definire i punti di inizio e fine del profilo nel codice. 
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

Quindi installare e usare `pyprof2calltree` per convertire l\'output del profilo in input di cachegrind. 
```python
pyprof2calltree -i /tmp/profile.cprof -o /tmp/callgrind.out
```

Quindi visualizzare queste informazioni con `kcachegrind` per Linux o `qcachegrind` per Windows. 
```python
kcachegrind /tmp/callgrind.out
```

## Risorse

-   [The Python profilers](https://docs.python.org/3/library/profile.html), `cProfile` and `python`.
-   [pyprof2calltree](https://pypi.org/project/pyprof2calltree/) at PyPI; [pyprof2calltree](https://github.com/pwaller/pyprof2calltree/) repository.
-   [FreeCAD\'s Python profiling tutorial](https://forum.freecadweb.org/viewtopic.php?f=10&t=44785).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Profiling/it
