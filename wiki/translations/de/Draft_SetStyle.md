---
 GuiCommand:
   Name: Draft SetStyle
   Name/de: Draft StilFestlegen
   MenuLocation: Dienstprogramme , Stil festlegen
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   Shortcut: **S** **S**
   Version: 0.19
   SeeAlso: Draft_AnnotationStyleEditor/de, Draft_ApplyStyle/de
---

# Draft SetStyle/de



## Beschreibung

Der <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Draft StilFestlegen**-Befehl legt die Standardstilvorgaben für neue Objekte fest.

<img alt="" src=images/Draft_SetStyle_Taskpanel.png  style="width:" height="550px;"> 
*Der Stileinstellungs-Aufgaben-Reiter*



## Anwendung

1.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Die Schaltfläche ![](images/Draft_tray_button_style.png ) in der [Draft Ablage](Draft_Tray/de.md). Abhängig von den aktuellen Stileinstellungen kann diese Schaltfläche unterschiedlich aussehen.
    -   Den Menüeintrag **Dienstprogramme → <img src="images/Draft_SetStyle.svg" width=16px> Stil festlegen** auswählen.
    -   Das Tastaturkürzel **S** dann **S**.
2.  Der Aufgaben-Bereich **Stileinstellungen** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Wahlweise eine oder mehrere Einstellungen ändern.
4.  Die Schaltfläche **OK** drücken, um die Einstellungen zu sichern.
5.  Die Schaltfläche in der [Draft Ablage](Draft_Tray/de.md) wird aktualisiert.



## Optionen

-   From the dropdown list at the top of the task panel an exiting style preset can be selected.
-   Press the **<img src="images/Document-save.svg" width=16px>** button to save the current style settings as a preset.
-   In the **Shapes** section the following settings can be specified:
    -   
        **Shape color**
        
        .

    -   
        **Transparency**
        
        .

    -   
        **Line color**
        
        .

    -   
        **Line width**
        
        .

    -   
        **Point color**
        
        . <small>(v0.22)</small> 

    -   
        **Point size**
        
        . <small>(v0.22)</small> 

    -   
        **Draw style**
        
        .

    -   
        **Display mode**
        
        .
-   The settings in the **Annotations** section apply to [Draft Texts](Draft_Text.md), [Draft Dimensions](Draft_Dimension.md) and [Draft Labels](Draft_Label.md). The following settings can be specified (see [Draft Text](Draft_Text#View.md) for details):
    -   
        **Text color**
        
        .

    -   
        **Font name**
        
        .

    -   
        **Font size**
        
        . This is in fact the default line height, the letters are smaller.

    -   
        **Line spacing**
        
        . Not used for dimensions.

    -   
        **Scale multiplier**
        
        . This is the inverse of the scale set in the [Draft annotation scale widget](Draft_annotation_scale_widget.md). If the scale is {{value|1:100}} the multiplier is {{Value|100}}. <small>(v0.22)</small> 
-   In the **Dimensions** section the following settings can be specified (see [Draft Dimension](Draft_Dimension#View.md) for details):
    -   
        **Line and arrow color**
        
        . <small>(v0.22)</small> 

    -   
        **Line width**
        
        . <small>(v0.22)</small> 

    -   
        **Arrow type**
        
        .

    -   
        **Arrow size**
        
        .

    -   
        **Show unit**
        
        .

    -   
        **Unit override**
        
        .

    -   
        **Dim overshoot**
        
        . <small>(v0.21)</small> 

    -   
        **Ext lines**
        
        . <small>(v0.21)</small> 

    -   
        **Ext overshoot**
        
        . <small>(v0.21)</small> 

    -   
        **Text spacing**
        
        .
-   Press the **<img src="images/Draft_SetStyle.svg" width=16px> Selected** button to apply the settings to selected objects or groups. Objects can be selected while the task panel is open.
-   Press the **<img src="images/Draft_Text.svg" width=16px> Annotations** button to apply the settings to all [Draft Texts](Draft_Text.md), [Draft Dimensions](Draft_Dimension.md) and [Draft Labels](Draft_Label.md) in the current document. <small>(v0.21)</small> 
-   Press the **Cancel** button to finish the command without saving the settings.



## Hinweise

-   Die Einstellungen im Abschnitt **Formen**, außer **Darstellungsart** und **Anzeigemodus**, werden nicht nur für Draft-Objekte verwendet, sondern auch für Objekte, die mit anderen Arbeitsbereiche erstellt werden.
-   Alle Einstellungen, außer **Darstellungsart** und **Anzeigemodus**, können auch in den Voreinstellungen angepasst werden. Siehe [PartDesign-Einstellungen](PartDesign_Preferences/de#Formdarstellung.md) und [Draft-Einstellungen](Draft_Preferences/de#Texte_und_Bemaßungen.md).
-   Stile werden in einer Datei mit festgelegtem Namen gespeichert: **StylePresets.json**, die im **Draft**-Verzeichnis des FreeCAD-Anwenders abgelegt ist:
    -   Unter Linux ist es normalerweise **/home/<username>/.local/share/FreeCAD/Draft/**.
    -   Unter Windows ist es **%APPDATA%\FreeCAD\Draft\**, normalerweise **C:\Users\<username>\Appdata\Roaming\FreeCAD\Draft\**.
    -   Unter macOS ist es normalerweise **/Users/<username>/Library/Preferences/FreeCAD/Draft/**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/de
