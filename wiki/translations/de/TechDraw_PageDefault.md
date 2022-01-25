---
- GuiCommand:/de
   Name:TechDraw PageDefault
   Name/de:TechDraw StandardSeite
   MenuLocation:TechDraw → Einfügen Standard Seite
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw SeitenVorlage einfügen](TechDraw_PageTemplate/de.md), [TechDraw Vorlagen](TechDraw_Templates/de.md)
---

# TechDraw PageDefault/de

## Beschreibung

Das Neue Standard Werkzeug erstellt ein neues Seitenobjekt unter Verwendung der Vorlagendatei, die in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) festgelegt ist.

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Standardvorlage, die mit TechDraw geliefert wird: A4 im Querformat, mit editierbaren Textfeldern*

## Anwendung

-   Drücke die **<img src="images/TechDraw_PageDefault.svg" width=16px> [Standardseite einfügen](TechDraw_PageDefault/de.md)**-Schaltfläche. (Ein aktives Dokument muss vorhanden sein).

## Hinweise

-   Wenn in der Zeichnung die Eigenschaft »KeepUpdated« auf »False« gesetzt wird oder die TechDraw Einstellung »Seiten aktuell halten« deaktiviert ist, wird die Zeichnung bei einer 3D-Modelländerung nicht aktualisiert. Es kann dann vorkommen, dass Hinweise zu fehlenden Geometrien oder Bemaßungen usw. aufploppen. Sobald die Seite aktualisiert wird, sollten die Fehler behoben sein. Die Zeichnung wird mit diesem Symbol <img alt="" src=images/TechDraw_Tree_Page_Unsync.png  style="width:32px;"> im Baum anzeigen, wenn die Aktualisierung ausgesetzt ist. Diese Einstellung beeinflusst auch den Startprozess. Wenn die Seite als »Seiten nicht aktuell halten« markiert ist, wird sie nicht beim Programmstart gezeichnet.

Wenn die Standardvorlage nicht in der Konfigurationsdatei `user.cfg` angegeben ist, wird das Werkzeug versuchen die Vorlage A4-Querformat zu öffnen und folgenden Pfad verwenden. 
```python
$INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
```

wobei `$INSTALL_DIR` das Verzeichnis ist, in welchem FreeCAD installiert wurde. Das kann z.B. so aussehen 
```python
/usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
```

## Eigenschaften

-    **Projektionstyp**: Standard Projektionstyp (erster oder dritter Winkel) für diese Seite.

-    **Aktualisiert halten**: Falls false, wird die Seite nicht mit Änderungen am 3D Modell aktualisiert. Nützlich für komplizierte/langsame Zeichnungen. Siehe Anmerkungen.

-    **Vorlage**: Ein Verweis auf das [Vorlagen](TechDraw_Templates/de.md) Objekt dieser Seite.

-    **Ansichten**: Eine Liste von Verweisen auf die Ansichten auf dieser Seite.

-    **Maßstab**: Standardmaßstab für Ansichten auf dieser Seite.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Neue Standard Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden: 
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

Sobald eine neue Seite erzeugt wurde, enthalten ihre `Vorlagen` Attribute ein `EditierbareTexte` Wörterbuch mit den Namen der bearbeitbaren Felder (Tasten) und ihren textlichen Werte. Kopiere dieses Wörterbuch in eine Variable, führe Änderungen durch und weise dann das Wörterbuch erneut dem `EditierbareTexte` Attribut zu, um die Änderungen zu sehen.


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
