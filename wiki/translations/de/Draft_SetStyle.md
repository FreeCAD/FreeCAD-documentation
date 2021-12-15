---
- GuiCommand:/de
   Name:Draft SetStyle
   Name/de:Draft StilFestlegen
   MenuLocation:Utilities → Stil festlegen
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Version:0.19
   SeeAlso:[Draft AnmerkungsStilEditor](Draft_AnnotationStyleEditor/de.md), [Draft AktuellenStilAnwenden](Draft_ApplyStyle/de.md)
---

# Draft SetStyle/de


</div>

## Beschreibung

Der <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Draft StilFestlegen**-Befehl legt die Standardstilvorgaben für neue Objekte fest.


<div class="mw-translate-fuzzy">

Dieser Befehl ist aktuell in Bearbeitung und sowohl die V0.19- als auch die V0.20-Version haben diverse Fehler.


</div>

![](images/Draft_SetStyle_taskpanel.png ) 
*Der Stileinstellungs-Aufgaben-Reiter*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Drücke die ![](images/Draft_tray_button_style.png )-Schaltfläche in der [Draft Ablage](Draft_Tray/de.md). Abhängig von den aktuellen Stileinstellungen kann diese Schaltfläche unterschiedlich aussehen.
    -   Wähle die **Utilities → <img src="images/Draft_SetStyle.svg" width=16px> Stil festlegen**-Option aus dem Menü.
2.  Der **Stileinstellungen**-Aufgaben-Reiter öffnet sich. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Ändere optional ein oder mehrere Einstellungen.
4.  Drücke die **OK**-Schaltfläche.
5.  Die Schaltfläche in der [Draft Ablage](Draft_Tray/de.md) wird aktualisiert.


</div>

## Optionen

-   From the dropdown list at the top of the task panel an exiting style can be selected. <small>(v0.20)</small> 
-   Press the {{button|<img src="images/Document-save.svg" width=16px> Save style}} button to save the style settings. <small>(v0.20)</small> 
-   In the **Lines and faces** section the following settings can be specified:
    -   
        **Line color**
        
        . This is also used for [Draft Labels](Draft_Label.md) and for the **Point Color** of objects.

    -   
        **Line width**
        
        . This is also used for [Draft Labels](Draft_Label.md).

    -   
        **Draw style**
        
        .

    -   
        **Display mode**
        
        .

    -   
        **Shape color**
        
        .

    -   
        **Transparency**
        
        .
-   In the **Annotations** section the following settings can be specified:
    -   
        **Text font**
        
        .

    -   
        **Text size**
        
        . This is in fact the line height, the letters are smaller.

    -   
        **Text spacing**
        
        . This is used for [Draft Dimensions](Draft_Dimension.md). It is the distance between the text and the dimension line. <small>(v0.20)</small> 

    -   
        **Text color**
        
        . This is also used for the **Line Color** of [Draft Dimensions](Draft_Dimension.md), which defines the color of the whole dimension including the text.

    -   
        **Line spacing**
        
        . This scale factor is applied to the line height. <small>(v0.20)</small> 

    -   
        **Arrow style**
        
        .

    -   
        **Arrow size**
        
        .

    -   
        **Show units**
        
        .

    -   
        **Unit override**
        
        .
-   Press the {{button|<img src="images/Draft_SetStyle.svg" width=16px> Selected}} button to apply the settings to selected objects or groups. <small>(v0.20)</small> 
-   Press the {{button|<img src="images/Draft_Text.svg" width=16px> Texts/dims}} button to apply the settings to all [Draft Texts](Draft_Text.md) and [Draft Dimensions](Draft_Dimension.md). <small>(v0.20)</small> 
-   Press the **Cancel** button to abort the command.

## Hinweise

-   Die Einstellungen für **Linienfarbe**, **Linienbreite** und **Formfarbe** werden nicht nur für Draft-Objekte verwendet, sondern auch für Objekte, die mit anderen Arbeitsbereiche erstellt werden.
-   Stile werden in einer Datei mit festgelegtem Namen gespeichert: {{FileName|StylePresets.json}}, die im FreeCAD-Benutzer-{{FileName|Draft}}-Verzeichnis abgelegt ist:
    -   Unter Linux ist es normalerweise {{FileName|/home/<username>/.FreeCAD/Draft/}}.
    -   Unter Windows ist es {{FileName|%APPDATA%\FreeCAD\Draft\}}, normalerweise {{FileName|C:\Users\<username>\Appdata\Roaming\FreeCAD\Draft\}}.
    -   Unter macOS ist es normalerweise {{FileName|/Users/<username>/Library/Preferences/FreeCAD/Draft/}}.

## Einstellungen

Siehe auch: [Einstellungseditor](Preferences_Editor/de.md) und [Entwurf Einstellungen](Draft_Preferences/de.md).

Die folgenden Einstellungen sind betroffen:

-   Linienfarbe: **Bearbeiten → Einstellungen... → Part design → Shape appearance → Default Shape view properties → Line color**.
-   Linienbreite: **Bearbeiten → Einstellungen... → Part design → Shape appearance → Default Shape view properties → Line width**.
-   Zeichenstil: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → Draft → DefaultDrawStyle**.
-   Anzeigenmodus: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → Draft → DefaultDisplayMode**.
-   Formfarbe: **Bearbeiten → Einstellungen... → Part design → Shape appearance → Default Shape view properties → Shape color**.
-   Transparenz: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → Draft → DefaultTransparency**.
-   Text-Schriftart: **Bearbeiten → Einstellungen... → Draft → Texte und Bemaßungen → Texteinstellungen → Schriftartfamilie**.
-   Schrifthöhe: **Bearbeiten → Einstellungen... → Draft → Texte und Bemaßungen → Texteinstellungen → Schriftgröße**.
-   Textabstand: **Bearbeiten → Einstellungen... → Draft → Texte und Bemaßungen → Bemaßungseinstellungen → Textabstand**.
-   Textfarbe: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → Draft → DefaultTextColor**.
-   Zeilenabstand: **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Mod → Draft → LineSpacing**.
-   Pfeilstil: **Bearbeiten → Einstellungen... → Draft → Texte und Bemaßungen → Bemaßungseinstellungen → Pfeil-Darstellung**.
-   Pfeilgröße: **Bearbeiten → Einstellungen... → Draft → Texte und Bemaßungen → Bemaßungseinstellungen → Pfeilgröße**.
-   Einheit anzeigen: **Bearbeiten → Einstellungen... → Draft → Texte und Bemaßungen → Bemaßungseinstellungen → Zeige Maße mit Maßeinheiten an**.
-   Einheit überschreiben: **Bearbeiten → Einstellungen... → Draft → Texte und Bemaßungen → Bemaßungseinstellungen → Einheit überschreiben**.

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/de
