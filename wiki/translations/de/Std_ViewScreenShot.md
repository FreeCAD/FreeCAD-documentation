---
 GuiCommand:
   Name: Std ViewScreenShot
   Name/de: Std AnsichtAufnehmen
   MenuLocation: Werkzeuge , Bildinhalt speichern...
   Workbenches: Alle
   SeeAlso: Std_Print/de, Std_PrintPdf/de, Macro_Copy3DViewToClipboard, Macro_Screen_Wiki/de, Macro_Snip/de
---

# Std ViewScreenShot/de



## Beschreibung

Der **Std AnsichtAufnehmen** Befehl öffnet ein Dialogfeld, um eine Bilddatei, einen Bildschirmfoto, von der aktiven [3D-Ansicht](3D_view/de.md) zu erstellen.

<img alt="" src=images/Save_picture.png  style="width:800px;"> 
*Das Dialogfeld Bildinhalt speichern nach Drücken der Schaltfläche Erweitert*



## Anwendung

1.  Wähle die **Werkzeuge → <img src="images/Std_ViewScreenShot.svg" width=16px> Bild speichern...** Option aus dem Menü.
2.  Es öffnet sich das Dialogfeld Bildinhalt speichern.
3.  Wahlweise die Schaltfläche **Erweitert** drücken, um ein zusätzlichen Bereich im Dialogfeld einzublenden. Für weitere Informationen siehe [Optionen](#Optionen.md).
4.  Wahlweise nach dem richtigen Ordner suchen.
5.  Einen Dateinamen eingeben und den Dateityp auswählen.
6.  Die Schaltfläche **Speichern** drücken, um die Bilddatei zu erstellen und das Dialogfeld zu schließen.



## Optionen



#### Bildabmessungen

1.  Wähle eine Standardgröße aus der Auswahlliste **Standardauflösungen**. Oder gib **Breite** und **Höhe** für eine benutzerdefinierte Größe an.
2.  Klicke optional auf eine **Seitenverhältnis**-Schaltfläche , um das Verhältnis von Breite zu Höhe des Bildes festzulegen. Wenn das Eingabefeld **Breite** den Fokus hat, ändert sich die Höhe des Bildes und umgekehrt.



### Bildeigenschaften

#\* Wähle eine Option aus der **Hintergrund** Aufklappliste:

#\* {{Value|Aktuell}} Diese Option verwendet tWerthe Hintergrund der 3D Ansicht.

#\* {{Value|Weiß}}

#\* {{Value|Schwarz}}

#\* {{Value|Durchsichtig}} Nicht alle Bildformate unterstützen Transparenz.

1.  Wähle eine Option aus der **Erstellungsmethode** Aufklappliste:
    -   
        {{Value|Offscreen (Neu)}}
        
        Dies ist die Standardmethode. Diese Methode unterstützt [anti-aliasing](https://en.wikipedia.org/wiki/Multisample_anti-aliasing). *Technische Informationen: Die wichtigsten Klassen für diese Methode sind Qt\'s QOffscreenSurface und QOpenGLFramebufferObject.*

    -   
        {{Value|Offscreen (Alt)}}
        
        Diese Methode funktioniert auf vielen modernen Linux Systemen nicht, da sie sich auf den Grafiktreiber verlässt. Diese Methode unterstützt kein Anti-Aliasing. *Technische Informationen: Dies ist eine echte Offscreen Rendering Methode, die nur Funktionen aus der Coin3d Bibliothek verwendet.*

    -   
        {{Value|Bildpuffer (benutzerdefiniert)}}
        
        Diese Methode unterstützt Anti-Aliasing. *Technische Informationen: Wenn Anti-Aliasing ausgeschaltet ist, liest diese Methode das Bild direkt aus dem Grafik Renderer, ansonsten rendert sie in einen Bildpuffer und holt sich das Bild von dort. Der Schlüsselteil dieser Methode ist Qt\'s QOpenGLFramebufferObject Klasse.*

    -   
        {{Value|Bildpuffer (wie bestehend)}}
        
        Diese Methode verwendet die gleichen Techniken wie **Bildpuffer (benutzerdefiniert)**. Sie unterstützt auch Anti-Aliasing, hat aber einige Einschränkungen in Bezug auf benutzerdefinierte Größen und verwendet immer den aktuellen Hintergrund der 3D Ansicht.



### Kommentar zum Bild 

1.  Wähle die Option {{RadioButton|TRUE|MIBA Informationen einfügen}}, um [MIBA](MIBA.md)-Informationen in die Datei einzufügen. Nicht alle Bildformate unterstützen dies.
2.  Oder wähle die Option {{RadioButton|TRUE|Kommentar einfügen}} und gib einen Kommentar in das Textfeld ein, um einen Kommentar in die Datei einzubetten. Dies wird nicht von allen Bildformaten unterstützt.
3.  Aktiviere das Kontrollkästchen {{CheckBox|TRUE|Wasserzeichen einfügen}}, um ein Wasserzeichen hinzuzufügen. Das Wasserzeichen wird in der unteren linken Ecke des Bildes platziert und besteht aus dem FreeCAD-Logo und dem Namen über der FreeCAD-Haupt-URL: [www.freecadweb.org](http://www.freecadweb.org).



## Hinweise

-   Die Anzahl der verfügbaren Bilddateiformate kann je nach Betriebssystem variieren.
-   Einige OpenGL-Treiber lassen keine Renderings über einer bestimmten Maximalgröße zu.



## Einstellungen

-   Der Hintergrund der 3D-Ansicht kann in den Voreinstellungen geändert werden: **Bearbeiten → Einstellungen... → Anzeige → Farben → Hintergrundfarbe**. Siehe [Voreinstellungseditor](Preferences_Editor/de#Farben.md).
-   Um das Anti Aliasing der 3D-Ansicht zu ändern: **Bearbeiten → Einstellungen... → Anzeige → 3D-Viewer → Rendern → Kantenglättung**. Siehe [Voreinstellungseditor](Preferences_Editor/de#3D-Ansicht.md).



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



---
⏵ [documentation index](../README.md) > Std ViewScreenShot/de
