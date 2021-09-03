---
- GuiCommand:/de
   Name:Std ViewScreenShot
   Name/de:Std AnsichtBildschirmFoto
   MenuLocation:Werkzeuge → Bild speichern...
   Workbenches:Alle
   SeeAlso:[Std Druck](Std_Print/de.md), [Std DruckePdf](Std_PrintPdf/de.md)
---

## Beschreibung

Der **Std AnsichtBildschirmFoto** Befehl öffnet ein Dialogfeld, um eine Bilddatei, einen Bildschirmfoto, von der aktiven [3D Ansicht](3D_view/de.md) zu erstellen.

<img alt="" src=images/Save_picture.png  style="width:800px;"> 
*Das Bild speichern  Dialogfeld nach Drücken der Erweiterten Schaltfläche*

## Anwendung

1.  Wähle die **Werkzeuge → <img src="images/Std_ViewScreenShot.svg" width=16px> Bild speichern...** Option aus dem Menü.
2.  Es öffnet sich das Dialogfeld Bild speichern.
3.  Drücke optional die **Erweitert** Schaltfläche, um ein zusätzliches Feld im Dialogfeld einzublenden. Für weitere Informationen siehe [Optionen](#Options.md).
4.  Suche optional nach dem richtigen Ordner.
5.  Gib einen Dateinamen ein und wähle den Dateityp.
6.  Drücke die **Speichern** Schaltfläche, um die Bilddatei zu erstellen und das Dialogfeld zu schließen.

## Optionen

#### Bild Abmessungen 

1.  Wähle eine Standardgröße aus der **Standardgrößen** Auswahlliste . Oder gib die **Breite** und **Höhe** für eine benutzerdefinierte Größe an.
2.  Klicke optional auf die **Seitenverhältnis** Schaltfläche , um das Verhältnis von Breite zu Höhe des Bildes festzulegen. Wenn das Eingabefeld **Breite** den Fokus hat, ändert sich die Höhe des Bildes und umgekehrt.

### Bildeigenschaften

\#\* Wähle eine Option aus der **Hintergrund** Aufklappliste:

\#\* {{Value|Aktuell}} Diese Option verwendet tWerthe Hintergrund der 3D Ansicht.

\#\* {{Value|Weiß}}

\#\* {{Value|Schwarz}}

\#\* {{Value|Transparent}} Nicht alle Bildformate unterstützen Transparenz.

1.  Wähle eine Option aus der **Erstellungsmethode** Aufklappliste:
    -   
        {{Value|Offscreen (Neu)}}
        
        Dies ist die Standardmethode. Diese Methode unterstützt [anti-aliasing](https://en.wikipedia.org/wiki/Multisample_anti-aliasing). *Technische Informationen: Die wichtigsten Klassen für diese Methode sind Qt\'s QOffscreenSurface und QOpenGLFramebufferObject.*

    -   
        {{Value|Offscreen (Alt)}}
        
        Diese Methode funktioniert auf vielen modernen Linux Systemen nicht, da sie sich auf den Grafiktreiber verlässt. Diese Methode unterstützt kein Anti-Aliasing. *Technische Informationen: Dies ist eine echte Offscreen Rendering Methode, die nur Funktionen aus der Coin3d Bibliothek verwendet.*

    -   
        {{Value|Framebuffer (custom)}}
        
        Diese Methode unterstützt Anti-Aliasing. *Technische Informationen: Wenn Anti-Aliasing ausgeschaltet ist, liest diese Methode das Bild direkt aus dem Grafik Renderer, ansonsten rendert sie in einen Framebuffer und holt sich das Bild von dort. Der Schlüsselteil dieser Methode ist Qt\'s QOpenGLFramebufferObject Klasse.*

    -   
        {{Value|Framebuffer (as is)}}
        
        Diese Methode verwendet die gleichen Techniken wie **Framebuffer (custom)**. Sie unterstützt auch Anti-Aliasing, hat aber einige Einschränkungen in Bezug auf benutzerdefinierte Größen und verwendet immer den aktuellen Hintergrund der 3D Ansicht.

### Bildkommentar

1.  Wähle die {{RadioButton|TRUE|MIBA einfügen}} Option, um [MIBA](MIBA.md) Informationen in die Datei einzufügen. Nicht alle Bildformate unterstützen dies.
2.  Oder wähle die {{RadioButton|TRUE|Kommentar einfügen}} Option und gib einen Kommentar in das Textfeld ein, um einen Kommentar in die Datei einzubetten. Dies wird nicht von allen Bildformaten unterstützt.
3.  Aktiviere das {{CheckBox|TRUE|Wasserzeichen einfügen}} Kontrollkästchen, um ein Wasserzeichen hinzuzufügen. Das Wasserzeichen wird in der unteren linken Ecke des Bildes platziert und besteht aus dem FreeCAD Logo und dem Namen über der FreeCAD Haupt URL: [www.freecadweb.org](http://www.freecadweb.org).

## Hinweise

-   Die Anzahl der verfügbaren Bilddateiformate kann je nach Betriebssystem variieren.
-   Einige OpenGL Treiber lassen keine Renderings über einer bestimmten Maximalgröße zu.

## Einstellungen

-   Der Hintergrund der 3D Ansicht kann in den Voreinstellungen geändert werden: **Bearbeiten → Voreinstellungen... → Anzeige → Farben → Hintergrundfarbe**. Siehe [Einstellungseditor](Preferences_Editor/de#Farben.md).
-   Um das Anti Aliasing der 3D Ansicht zu ändern: **Bearbeiten → Voreinstellungen... → Anzeige → 3D Ansicht → Rendering → Anti-Aliasing**. Siehe [Einstellungseditor](Preferences_Editor/de#3D_View.md).

## Skripten

Es ist möglich, Bildschirmfotos mit Python Code zu erstellen.


```python
Gui.ActiveDocument.ActiveView.saveImage('C:/temp/test.png',1656,783,'Current')
```

Dieses Skript speichert eine Reihe von Bildschirmfotos in verschiedenen Größen und aus verschiedenen Richtungen. Der Kameratyp, orthografisch oder perspektivisch, wird ebenfalls geändert.


```python
import Part, PartGui
# Loading test part
Part.open('C:/Documents and Settings/jriegel/My Documents/Projects/FreeCAD/data/Blade.stp')
OutDir = 'C:/temp/'
 
# Creating images with different Views, Cameras and sizes
for p in ['PerspectiveCamera','OrthographicCamera']:
    Gui.SendMsgToActiveView(p)
    for f in ['ViewAxo','ViewFront','ViewTop']:
        Gui.SendMsgToActiveView(f)
        for x,y in [[500,500],[1000,3000],[3000,1000],[3000,3000],[8000,8000]]:
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + 'Blade_' + p +'_' + f + '_' + x + '_' + y + '.jpg',x,y,'White')
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + 'Blade_' + p +'_' + f + '_' + x + '_' + y + '.png',x,y,'Transparent')

# Close active document
App.closeDocument(App.ActiveDocument.Name)
```





{{Std Base navi

}}  
