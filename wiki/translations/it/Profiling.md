# Profiling/it
## Descrizione

La profilazione del codice di FreeCAD aiuta a trovare i colli di bottiglia negli algoritmi utilizzati per creare o manipolare oggetti.

Per profilare il codice [Python](Python/it.md) usare il modulo standard `cProfile` per definire i punti di inizio e fine del profilo nel codice. 
```python
import cProfile
pr = cProfile.Profile()
pr.enable()

# --------------------------------------
# Lines of code that you want to profile
# --------------------------------------

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


{{Powerdocnavi

}} 

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Profiling/it
