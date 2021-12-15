# TechDraw LineGroup/fr
{{TOCright}}

## Présentation

Les Groupes de lignes sont utilisés pour contrôler l\'apparence de différents types de lignes.

### Utilisation

1.  Allez dans l\'onglet des préférences *[Annotation](TechDraw_Preferences/fr#Annotation.md)*.
2.  Sélectionnez dans le champ **Line Width Group** un LineGroup. Ce sont les groupes définis dans le fichier csv de définition LineGroup.

Pour modifier le fichier de définition LineGroups

1.  Allez dans l\'onglet des préférences *[Généralités](TechDraw_Preferences/fr#G.C3.A9n.C3.A9ralit.C3.A9s.md)*.
2.  Sélectionnez dans le champ **Line Group File** un fichier de définition LineGroup.

### Personnaliser les groupes de lignes 

Si vous avez les droits en écriture, vous pouvez éditer `LineGroup.csv` pour ajouter vos propres groupes de lignes.

Ce fichier est généralement dans:


```python
$INSTALL_DIR/Mod/TechDraw/LineGroup/LineGroup.csv
```

Où `$INSTALL_DIR` est le dossier d\'installation de FreeCAD, par exemple


```python
/usr/share/freecad/Mod/TechDraw/LineGroup/LineGroup.csv
```

Vous pouvez spécifier vos valeurs préférées par défaut dans [TechDraw Préférences](TechDraw_Preferences/fr.md).

## Chemin de LineGroup 

-   **Windows**: `C:\Program Files\FreeCAD\data\Mod\TechDraw\LineGroup\`
-   **Mac**: `/Applications/FreeCAD.app/Contents/Mod/TechDraw/LineGroup/`
-   **Linux**: `/usr/share/freecad/Mod/TechDraw/LineGroup/`
    -   ***freecad-daily PPA***: `/usr/share/freecad-daily/Mod/TechDraw/LineGroup/`

Remarque: une nouvelle préférence a été ajoutée pour vous permettre d\'utiliser votre propre fichier personnel LineGroup.


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

## Remarque

-   La largeur de trait dans TechDraw est toujours en mm, même lorsque vous utilisez d\'autres systèmes d\'unités.





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LineGroup/fr
