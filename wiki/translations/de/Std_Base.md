# <img alt="Symbol Std Basis" src=images/Freecad.svg  style="width:64px;"> Std Base/de






## Einleitung

**Std Basis** ist nicht wirklich ein Arbeitsbereich, sondern eher eine Kategorie von \'Standard\'-Befehlen und Werkzeugen, die in allen Arbeitsbereichen verwendet werden können.



## Werkzeuge

Die meisten **Std Basis**-Werkzeuge können aus dem [Standardmenü](Standard_Menu/de.md) erreicht werden. Diejenigen, die nur über eine Symbolleiste oder ein Kontextmenü zur Verfügung stehen, werden unten unter [Wekzeugleiste Struktur](#Wekzeugleiste_Struktur.md) und [Zusätzliche Werkzeuge](#Zusätzliche_Werkzeuge.md) aufgelistet.



### Standardmenü

Das Standardmenü setzt sich aus 7 Untermenüs zusammen. Jedes Untermenü hat eine eigene Seite. Einfach auf einen der untenstehenden Namen klicken.


{{StdMenu
|
[Datei](Std_File_Menu/de.md)
&nbsp;&nbsp;&nbsp;
[Bearbeiten](Std_Edit_Menu/de.md)
&nbsp;&nbsp;&nbsp;
[Ansicht](Std_View_Menu/de.md)
&nbsp;&nbsp;&nbsp;
[Werkzeuge](Std_Tools_Menu/de.md)
&nbsp;&nbsp;&nbsp;
[Makro](Std_Macro_Menu/de.md)
&nbsp;&nbsp;&nbsp;
[Fenster](Std_Windows_Menu/de.md)
&nbsp;&nbsp;&nbsp;
[Hilfe](Std_Help_Menu/de.md)
}}



### Werkzeugleiste Struktur 

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Baugruppe erstellen](Std_Part/de.md): Erzeugt eine neue Baugruppe und macht sie aktiv.

-   <img alt="" src=images/Part_CoordinateSystem.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create datums: 

  - <img alt="" src=images/Part_CoordinateSystem.svg  style="width:32px;"> [Create coordinate system](Part_CoordinateSystem.md): Creates a coordinate system object that can be attached to other objects. <small>(v1.1)</small> 

  - <img alt="" src=images/Part_DatumPlane.svg  style="width:32px;"> [Create datum plane](Part_DatumPlane.md): Creates a datum plane object that can be attached to other objects. <small>(v1.1)</small> 

  - <img alt="" src=images/Part_DatumLine.svg  style="width:32px;"> [Create datum line](Part_DatumLine.md): Creates a datum line object that can be attached to other objects. <small>(v1.1)</small> 

  - <img alt="" src=images/Part_DatumPoint.svg  style="width:32px;"> [Create datum point](Part_DatumPoint.md): Creates a datum point object that can be attached to other objects. <small>(v1.1)</small> 

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Gruppe erstellen](Std_Group/de.md): Legt eine neue Gruppe an.

-   <img alt="" src=images/Std_LinkMake.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Link tools:

  - <img alt="" src=images/Std_LinkMake.svg  style="width:32px;"> [Verknüpfung erstellen](Std_LinkMake/de.md): Erzeugt einen Link.

  - <img alt="" src=images/Std_LinkMakeRelative.svg  style="width:32px;"> [Unterverknüpfung erstellen](Std_LinkMakeRelative/de.md): Erstellt eine Verknüpfung von Unterobjekten oder Unterelementen.

  - <img alt="" src=images/Std_LinkReplace.svg  style="width:32px;"> [Durch Verknüpfung ersetzen](Std_LinkReplace/de.md): Ersetzt das/die Objekt(e) durch die neue(n) Verknüpfung(en).

  - <img alt="" src=images/Std_LinkUnlink.svg  style="width:32px;"> [Verknüpfung auflösen](Std_LinkUnlink/de.md): Ersetzt den/die Link(s) durch das/die verknüpfte(n) Objekt(e).

  - <img alt="" src=images/Std_LinkImport.svg  style="width:32px;"> [Verknüpfungen importieren](Std_LinkImport/de.md): Importiert den/die ausgewählten externen Link(s).

  - <img alt="" src=images/Std_LinkImportAll.svg  style="width:32px;"> [Alle Verknüpfungen importieren](Std_LinkImportAll/de.md): Importiert alle externen Link(s).

-   <img alt="" src=images/Std_VarSet.svg  style="width:32px;"> [Variablensatz erstellen](Std_VarSet/de.md): Erzeugt einen Satz von Eigenschaften, die als Variablen in [Ausdrücken](Expressions/de.md) verwendet werden können. {{Version/de|1.0}}



### Zusätzliche Werkzeuge 

-   <img alt="" src=images/Std_LinkMakeGroup.svg  style="width:32px;"> [Verknüpfungsgruppe erstellen](Std_LinkMakeGroup/de.md): Erzeugt eine Gruppe von Links.

-   [Ausdruck-Aktionen](Std_Expressions/de.md):

  - [Ausgewählte kopieren](Std_Expressions#Copy_selected/de.md): Kopiert die Ausdrucksdaten der ausgewählten Objekte in die Zwischenablage.

  - [Aktives Dokument kopieren](Std_Expressions#Copy_active_document/de.md): Kopiert die Ausdrucksdaten des aktiven Dokuments in die Zwischenablage.

  - [Alle Dokumente kopieren](Std_Expressions#Copy_all_documents/de.md): Kopiert die Ausdrucksdaten aus allen Dokumenten in die Zwischenablage.

  - [Einfügen](Std_Expressions#Paste/de.md): Fügt Ausdrucksdaten aus der Zwischenablage ein.

-   <img alt="" src=images/Part_SelectFilter.svg  style="width:" height="32px;"> <img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> [Auswahlfilter](Part_SelectFilter/de.md): {{Version/de|1.0}}

  - <img alt="" src=images/Vertex-selection.svg  style="width:32px;"> [Knotenauswahl](Part_SelectFilter/de#Knotenauswahl.md): Erlaubt nur die Auswahl von Eckpunkten.

  - <img alt="" src=images/Edge-selection.svg  style="width:32px;"> [Kantenauswahl](Part_SelectFilter/de#Kantenauswahl.md): Erlaubt nur die Auswahl von Kanten.

  - <img alt="" src=images/Face-selection.svg  style="width:32px;"> [Flächenauswahl](Part_SelectFilter/de#Flächenauswahl.md): Erlaubt nur die Auswahl von Flächen.

  - <img alt="" src=images/Clear-selection.svg  style="width:32px;"> [Alle Auswahlfilter gelöscht](Part_SelectFilter#All_selection_filters_cleared/de.md): Erlaubt die Auswahl aller Unterelemente.

-   <img alt="" src=images/Std_TreeSelectAllInstances.svg  style="width:32px;"> [Alle Instanzen auswählen](Std_TreeSelectAllInstances/de.md): Wählt alle Instanzen eines Objekts in der [Baumansicht](Tree_view/de.md) aus.

-   <img alt="" src=images/Std_ToggleFreeze.svg  style="width:32px;"> [Einfrieren umschalten](Std_ToggleFreeze/de.md): Schaltet den Einfrierzustand von Objekten um. {{Version/de|1.0}}



### Veraltete Werkzeuge 

-   <img alt="" src=images/View_Measure_Clear_All.svg  style="width:32px;"> [Messung löschen](View_Measure_Clear_All/de.md): Löscht [Part](Part_Workbench/de.md)-Messungen. Nicht verfügbar in {{VersionPlus/de|1.0}}. Stattdessen kann [Std Messen](Std_Measure/de.md) verwendet werden.

-   <img alt="" src=images/View_Measure_Toggle_All.svg  style="width:32px;"> [Messung umschalten](View_Measure_Toggle_All/de.md): Schaltet die Anzeige der Part-Messungen um. Nicht verfügbar in {{VersionPlus/de|1.0}}. Stattdessen kann [Std Messen](Std_Measure/de.md) verwendet werden.

-   <img alt="" src=images/Std_MeasureDistance.svg  style="width:32px;"> [Entfernung messen](Std_MeasureDistance/de.md): Erzeugt ein Objekt zum Messen und Anzeigen einer Entfernung. Nicht verfügbar in {{VersionPlus/de|1.0}}. Stattdessen kann [Std Messen](Std_Measure/de.md) verwendet werden.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Std Base/de
