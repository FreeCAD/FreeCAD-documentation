---
- GuiCommand:/de
   Name:TechDraw PageDefault
   Name/de:TechDraw Standardseite
   MenuLocation:TechDraw → Neues Zeichnungsblatt aus der Standardvorlage erstellen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Seitenvorlage](TechDraw_PageTemplate/de.md), [TechDraw Vorlagen](TechDraw_Templates/de.md)
---

# TechDraw PageDefault/de

## Beschreibung

Das Werkzeug Standardseite erstellt ein neues Page-Objekt (Zeichnungsblatt) unter Verwendung der in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) festgelegten Standardvorlage.

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Eine Vorlage, die mit TechDraw geliefert wird: A4 im Querformat, mit editierbaren Textfeldern*

## Anwendung

-   Die Schaltfläche **<img src="images/TechDraw_PageDefault.svg" width=16px> [Neues Zeichnungsblatt aus der Standardvorlage erstellen](TechDraw_PageDefault/de.md)** drücken. (Ein aktives Dokument muss vorhanden sein).

## Hinweise

-   Wenn die Seite mit »nicht aktuell halten« markiert ist, ob durch die Eigenschaft »KeepUpdated« oder durch den entsprechend gesetzten Wert unter Einstellungen, wird sie Änderungen des 3D-Modells ignorieren. Dies kann zu ungewöhnlichen Darstellungen führen (fehlende Geometrien, fehlende Maßzahlen usw.). Diese werden korrigiert, sobald die Seite mit dem Werkzeug [Seite neu zeichnen](TechDraw_RedrawPage/de.md) aktualisiert wird. Die Zeichnung wird mit diesem Symbol <img alt="" src=images/TechDraw_Tree_Page_Unsync.png  style="width:24px;"> im Baum angezeigt, solange die Aktualisierung ausgesetzt ist. Diese Einstellung beeinflusst auch den Startprozess. Wenn die Seite mit »nicht aktuell halten« markiert ist, wird sie beim Programmstart nicht dargestellt.

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

-    {{PropertyView/de|Show Grid}}: Zeigt ein Raster über dieser Seite an. <small>(v0.20)</small> 

-    {{PropertyView/de|Grid Spacing}}: Abstand zwischen den Rasterlinien in mm. <small>(v0.20)</small> 

## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Standardseite kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden: 
```python
page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
template = FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
template.Template = templateFileSpec
page.Template = FreeCAD.ActiveDocument.Template
```

-   Erstellt eine neue Seite im aktuellen Dokument

### Editierbare Textfelder 


**Siehe auch:**

[TechDraw Vorlagen](TechDraw_Templates/de.md) für mehr Informationen zur Erstellung von Vorlagen.

Sobald eine neue Seite erzeugt wurde, enthält ihr Attribut `Template` ein Wörterbuch (Dictionary-Objekt) `EditableTexts` mit den Namen der editierbaren Felder (Keys) und ihren Textinhalten (Values). Dieses Wörterbuch kann in eine Variable kopiert, geändert und dann erneut dem Attribut `EditableTexts` zugewiesen werden, um die Änderungen anzusehen.


```python
page = FreeCAD.ActiveDocument.Page
texts = page.Template.EditableTexts

for key, value in texts.items():
    print("{0} = {1}".format(key, value))

texts["FC-Title"] = "The title of my page"
page.Template.EditableTexts = texts
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageDefault/de
