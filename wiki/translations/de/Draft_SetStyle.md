---
 GuiCommand:
   Name: Draft SetStyle
   Name/de: Draft StilFestlegen
   MenuLocation: Dienstprogramme , Stil festlegen
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Shortcut: Draft: **S** **S**
   Version: 0.19
   SeeAlso: Draft_AnnotationStyleEditor/de, Draft_ApplyStyle/de
---

# Draft SetStyle/de



## Beschreibung

Der <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> **Draft StilFestlegen**-Befehl legt die Standardstilvorgaben für neue Objekte fest.

<img alt="" src=images/Draft_SetStyle_Taskpanel_Tab_Shape.png  style="width:" height="500px;"> <img alt="" src=images/Draft_SetStyle_Taskpanel_Tab_Annotation.png  style="width:" height="500px;"> 
*Die beiden Reiter ({{Version/de|1.0*) der Aufgaben-Tafel Stileinstellungen }}



## Anwendung

1.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Die Schaltfläche ![](images/Draft_tray_button_style.png ) in der [Draft Ablage](Draft_Tray/de.md). Abhängig von den aktuellen Stileinstellungen kann diese Schaltfläche unterschiedlich aussehen.
    -   [Draft](Draft_Workbench/de.md): Den Menüeintrag **Dienstprogramme → <img src="images/Draft_SetStyle.svg" width=16px> Stil festlegen** auswählen oder die Menüoption im Kontextmenü der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Draft: Das Tastaturkürzel **S** dann **S**.
2.  Der Aufgaben-Bereich **Stileinstellungen** wird geöffnet. Siehe [Optionen](#Optionen.md) für weitere Informationen.
3.  Wahlweise eine oder mehrere Einstellungen ändern.
4.  Die Schaltfläche **OK** drücken, um die Einstellungen zu sichern.
5.  Die Schaltfläche in der [Draft Ablage](Draft_Tray/de.md) wird aktualisiert.



## Optionen

-   Aus der herunter geklappten Liste oben im Task Fenster kann ein vorhandener voreingestellter Stil ausgewählt werden.
-   Drücke die **<img src="images/Document-save.svg" width=16px>** Schaltfläche um die aktuellen Stil Einstellungen als Voreinstellung festzulegen.
-   Im **Form** Reiter können die folgenden Einstellungen festgelegt werden:
    -   
        **Erscheinungsbild der Form**
        
        -   
            **Formfarbe**
            
            .

        -   
            **Umgebungsfarbe**
            
            . <small>(v1.0)</small> 

        -   
            **Emmissionsfarbe**
            
            . <small>(v1.0)</small> 

        -   
            **Glanzfarbe**
            
            . <small>(v1.0)</small> 

        -   
            **Formtransparenz**
            
            .

        -   
            **Glanzstärke**
            
            . <small>(v1.0)</small> 

    -   
        **Andere**
        
        -   
            **Linienfarbe**
            
            .

        -   
            **Linienbreite**
            
            .

        -   
            **Punktfarbe**
            
            . <small>(v1.0)</small> 

        -   
            **Punktgröße**
            
            . <small>(v1.0)</small> 

        -   
            **Darstellungsart**
            
            .

        -   
            **Anzeigemodus**
            
            .
-   Die Einstellungen im **Anmerkungen** Reiter wirken auf [Draft Texte](Draft_Text/de.md), [Draft Maße](Draft_Dimension/de.md) and [Draft Hinweise](Draft_Label/de.md). Die folgenden Einstellungen können festgelegt werden (Details siehe [Draft Text](Draft_Text/de#Ansicht.md) und [Draft Maße](Draft_Dimension/de#Ansicht.md)):
    -   
        **Texte**
        
        -   
            **Schriftname**
            
            .

        -   
            **Schriftgröße**
            
            . Das ist die Standard Linienhöhe, die Buchstaben sind kleiner.

        -   
            **Faktor für den Zeilenabstand**
            
            . Wird bei Maßen nicht verwendet.

        -   
            **Skalenfaktor**
            
            . Dies ist die Umkehrung des Maßstabes der in [Draft Beschriftungsmaßstab Widget](Draft_annotation_scale_widget/de.md) gesetzt ist. Wenn der Maßstab {{value|1:100}} ist, ist der Multiplizierer {{value|100}}. <small>(v1.0)</small> 

        -   
            **Textfarbe**
            
            .

    -   
        **Linien und Pfeile**
        
        -   
            **Linienbreite**
            
            . <small>(v1.0)</small> 

        -   
            **Pfeiltyp**
            
            .

        -   
            **Pfeilgröße**
            
            .

        -   
            **Linien- und Pfeilfarbe**
            
            . <small>(v1.0)</small> 

    -   
        **Maße**
        
        -   
            **Einheit anzeigen**
            
            .

        -   
            **Einheit überschreiben**
            
            .

        -   
            **Maßlinienüberstand**
            
            . <small>(v0.21)</small> 

        -   
            **Länge der Maßhilfslinie**
            
            . <small>(v0.21)</small> 

        -   
            **Maßhilfslinienüberstand**
            
            . <small>(v0.21)</small> 

        -   
            **Textabstand**
            
            .
-   Drücke die **<img src="images/Draft_SetStyle.svg" width=16px> Ausgewählt** Schaltfläche um die Festlegungen auf ausgewählte Objekte oder Gruppen zuzuweisen. Objekte können ausgewählt werden, so lange das Task Fenster offen ist.
-   Drücke die **<img src="images/Draft_Text.svg" width=16px> Anmerkungen** Schaltfläche um die Festlegungen auf alle [Draft Texte](Draft_Text/de.md), [Draft Maße](Draft_Dimension/de.md) and [Draft Hinweise](Draft_Label/de.md) im aktuellen Dokument anzuwenden. <small>(v0.21)</small> 
-   Drücke die **Abbrechen** Schaltfläche um den Befehl ohne Speicherung der Einstellungen zu beenden.



## Hinweise

-   Die Einstellungen im Reiter **Formen**, außer **Darstellungsart** und **Anzeigemodus**, werden nicht nur für Draft-Objekte verwendet, sondern auch für Objekte, die mit anderen Arbeitsbereiche erstellt werden.
-   Alle Einstellungen, außer **Darstellungsart** und **Anzeigemodus**, können auch in den Voreinstellungen angepasst werden. Siehe [PartDesign-Einstellungen](PartDesign_Preferences/de#Formdarstellung.md) und [Draft-Einstellungen](Draft_Preferences/de#Texte_und_Bemaßungen.md).
-   Stile werden in einer Datei mit festgelegtem Namen gespeichert: **StylePresets.json**, die im **Draft**-Verzeichnis des FreeCAD-Anwenders abgelegt ist:
    -   Unter Linux ist es normalerweise **/home/<username>/.local/share/FreeCAD/Draft/**.
    -   Unter Windows ist es **%APPDATA%\FreeCAD\Draft\**, normalerweise **C:\Users\<username>\Appdata\Roaming\FreeCAD\Draft\**.
    -   Unter macOS ist es normalerweise **/Users/<username>/Library/Preferences/FreeCAD/Draft/**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SetStyle/de
