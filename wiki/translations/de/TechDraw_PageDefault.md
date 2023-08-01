---
- GuiCommand:
   Name: TechDraw PageDefault
   Name/de: TechDraw Standardseite
   MenuLocation: TechDraw - Page - Neues Zeichnungsblatt aus der Standardvorlage erstellen
   Workbenches: [TechDraw](TechDraw_Workbench/de.md)
   SeeAlso: [TechDraw Seitenvorlage](TechDraw_PageTemplate/de.md), [TechDraw Vorlagen](TechDraw_Templates/de.md)
---

# TechDraw PageDefault/de



## Beschreibung

Das Werkzeug **TechDraw Standardseite** erstellt ein neues Page-Objekt (Zeichnungsblatt) unter Verwendung der in den [TechDraw-Einstellungen](TechDraw_Preferences/de.md) festgelegten Standardvorlage.

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Eine Vorlage, die mit TechDraw geliefert wird: A4_LandscapeTD.svg*



## Anwendung

1.  Ein aktives Dokument muss vorhanden sein.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_PageDefault.svg" width=16px> [Neues Zeichnungsblatt aus der Standardvorlage erstellen](TechDraw_PageDefault/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Page → <img src="images/TechDraw_PageDefault.svg" width=16px> Neues Zeichnungsblatt aus der Standardvorlage erstellen** auswählen.



## Hinweise

-   Wenn das Zeichnungsblatt mit »nicht aktuell halten« markiert ist, ob durch seine {{PropertyData/de|Keep Updated}}, die Menüoption **Toggle Keep Updated** im Kontextmenü seines Fensters, (die Menüoption **Automatisches Aktualisieren umschalten** in seinem Kontextmenü in der Baumansicht), oder durch den entsprechend gesetzten Wert unter Einstellungen, wird es Änderungen des 3D-Modells ignorieren. Dies kann zu ungewöhnlichen Darstellungen führen (fehlende Geometrien, fehlende Maßzahlen usw.). Diese werden korrigiert, sobald die Seite mit dem Werkzeug [Seite neu zeichnen](TechDraw_RedrawPage/de.md) aktualisiert wird. Die Zeichnung wird mit diesem Symbol <img alt="" src=images/TechDraw_Tree_Page_Unsync.png  style="width:24px;"> in der [Baumansicht](Tree_view/de.md) angezeigt, solange die Aktualisierung ausgesetzt ist. Diese Einstellung beeinflusst auch den Startprozess. Wenn eine Seite mit »nicht aktuell halten« markiert ist, wird sie beim Programmstart nicht dargestellt.

Wenn in der Konfigurationsdatei `user.cfg` keine Standardvorlage angegeben ist, wird das Werkzeug folgendes versuchen:

:   
    
```python
    $INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    





:   wobei `$INSTALL_DIR` das Verzeichnis ist, in welchem FreeCAD installiert wurde. Das kann z.B. so aussehen:





:   
    
```python
    /usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    



## Eigenschaften



### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|Projection Type}}: Standardprojektionsart (erster oder dritter Winkel) dieser Seite.


{{TitleProperty|Page properties}}

-    {{PropertyData/de|Projektionstyp}}: Standard Projektionstyp (erster oder dritter Winkel) für diese Seite.

-    {{PropertyData/de|Aktualisiert halten}}: Falls false, wird die Seite nicht mit Änderungen am 3D Modell aktualisiert. Nützlich für komplizierte/langsame Zeichnungen. Siehe Anmerkungen.

-    {{PropertyData/de|Vorlage}}: Ein Verweis auf das [Vorlagen](TechDraw_Templates/de.md)-Objekt dieser Seite.

-    {{PropertyData/de|Ansichten}}: Eine Liste von Verweisen auf die Ansichten auf dieser Seite.

-    {{PropertyData/de|Maßstab}}: Standardmaßstab für Ansichten auf dieser Seite.

-    {{PropertyData/de|Next Balloon Index}}: Autonummerierung für Balloons.



### Ansicht


{{TitleProperty|Grid}}

-    {{PropertyView/de|Show Grid}}: Zeigt ein Raster über dieser Seite an. {{Version/de|0.20}}

-    {{PropertyView/de|Grid Spacing}}: Abstand zwischen den Rasterlinien. {{Version/de|0.20}}



## Skripten

Siehe [TechDraw Seitenvorlage](TechDraw_PageTemplate/de#Skripten.md).





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageDefault/de
