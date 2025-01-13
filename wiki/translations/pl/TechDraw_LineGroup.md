# TechDraw LineGroup/pl
## Opis

Grupy linii służą do kontrolowania wyglądu różnych typów linii.



## Użycie

1.  Przejdź do zakładki preferencji *[Adnotacja](TechDraw_Preferences/pl#Adnotacje.md)*.
2.  Wybierz w polu **Szerokość linii w grupie** grupę linii. Są to grupy zdefiniowane w pliku csv definicji *LineGroup*.

Aby zmienić plik definicji LineGroups

1.  Przejdź do zakładki preferencji *[Ogólne](TechDraw_Preferences/pl#Ogólne.md)*.
2.  Wybierz w polu **Plik grupy linii** plik definicji grupy linii.



## Dostosowywanie grup linii 

Jeśli masz uprawnienia do zapisu, możesz edytować `LineGroup.csv`, aby dodać własne grupy linii.

Plik ten zazwyczaj znajduje się w:


```python
$INSTALL_DIR/Mod/TechDraw/LineGroup/LineGroup.csv
```

Gdzie `$INSTALL_DIR` to katalog, w którym zainstalowano FreeCAD, na przykład:


```python
/usr/share/freecad/Mod/TechDraw/LineGroup/LineGroup.csv
```

Możesz określić swoje ulubione ustawienia domyślne w [ustawieniach](TechDraw_Preferences/pl.md).



## Ścieżka pliku LineGroup 

-   **Windows**: `C:\Program Files\FreeCAD\data\Mod\TechDraw\LineGroup\`
-   **Mac**: `/Applications/FreeCAD.app/Contents/Mod/TechDraw/LineGroup/`
-   **Linux**: `/usr/share/freecad/Mod/TechDraw/LineGroup/`
    -   **freecad-daily PPA**: `/usr/share/freecad-daily/Mod/TechDraw/LineGroup/`
    -   **snap package**: `/snap/freecad/current/usr/share/Mod/TechDraw/LineGroup`

Uwaga: Dodano nową preferencję, aby umożliwić korzystanie z własnego pliku LineGroup.


```python
;FreeCAD LineGroup Definitions
;Format: *GroupName,thin,graphic,thick,extra
;thin: hidden lines
;graphic: dimensions, centerlines
;thick: visible lines
;extra: not implemented
```


```python
*FC 0.25mm,0.13,0.18,0.25,0.50
*FC 0.35mm,0.18,0.25,0.35,0.70
*FC 0.50mm,0.25,0.35,0.50,1.0
*FC 0.70mm,0.35,0.50,0.70,1.4
*FC 1.00mm,0.50,0.70,1.00,2.00
```



## Uwagi

-   Szerokość linii w środowisku pracy Rysunek Techniczny jest zawsze określana w mm, nawet w przypadku korzystania z innych systemów jednostek.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LineGroup/pl
