---
- GuiCommand:/de
   Name:PartDesign SubShapeBinder
   Name/de:PartDesign UnterFormBinder
   Workbenches:[PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)
   MenuLocation:Part Design → Erstellen eines Unterobjekt-Formbinders
   Version:0.19
   SeeAlso:[PartDesign FormBinder](PartDesign_ShapeBinder/de.md), [PartDesign Klon](PartDesign_Clone/de.md)
---

## Beschreibung

Ein [PartDesign UnterFormBinder](PartDesign_SubShapeBinder/de.md) importiert ein Element aus einem anderen Körper in den aktiven [Körper](PartDesign_Body/de.md). Es kann die [Form](Shape/de.md) eines anderen Objekts übernehmen oder an ein oder mehrere Objekte oder Unterelemente (Kanten oder Flächen) eines anderen Objekts \"gebunden\" werden.


<div class="mw-translate-fuzzy">

Dann kann das resultierende Binderobjekt verschoben oder zur Durchführung erweiterter Operationen wie [boolesche](PartDesign_Boolean/de.md) oder [Polster](PartDesign_Pad/de.md) verwendet werden.


</div>

Es kann auch an Objekte binden, die innerhalb von [Std Parts](Std_Part/de.md) verschachtelt sind, und es verfolgt die relative Platzierung dieser Merkmale. Dies ist im Zusammenhang mit der Erstellung von [Baugruppen](Assembly/de.md) nützlich, da der Anwender oft auf [Formelemente](PartDesign_Feature/de.md) verweisen muss, die bereits korrekt in einer anderen Unterbaugruppe platziert sind.

<img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width:" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width:" height="300px;">


*Links: zwei Körper, die in zwei separaten [Körpern](PartDesign_Body/de.md) erzeugt wurden. Rechts: zwei UnterFormBinder, die aus dem ersten Körper extrahiert, in den zweiten Körper importiert und an eine andere Position verschoben wurden.*

<img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width:" height="300px;"> 
*Die beiden UnterFormBinder werden verwendet, um einen [booleschen Schnitt](PartDesign_Boolean/de.md) und ein [Polster](PartDesign_Pad/de.md), mit dem zweiten Körper, zu erstellen.*

## Anwendung

1.  Beginne mit einem bereits positionierten **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/PartDesign_AdditivePrism.svg style="width:Körper](PartDesign_Body/de.md)**, der ein einzelnes [Formelement](PartDesign_Feature/de.md), z. B., ein **[16px">  [AdditivesPrisma](PartDesign_AdditivePrism/de.md)** enthält.
2.  Erstelle einen zweiten **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/PartDesign_AdditiveBox.svg style="width:Körper](PartDesign_Body/de.md)**, der ein einzelnes [Formelement](PartDesign_Feature/de.md), z. B., ein **[16px"> [AdditiverQuader](PartDesign_AdditiveBox/de.md)**. Dies wird der aktive Körper sein.
3.  Wähle den gesamten ersten Körper aus und drücke **<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [UnterFormBinder](PartDesign_SubShapeBinder/de.md)**.
4.  Ändere die Eigenschaften dieses Binderobjekts, zum Beispiel seine Positionierung.
5.  Verwende es mit einer anderen Aktion, wie z.B. **<img src=images/PartDesign_Boolean.svg style="width:16px"> [Boolesche](PartDesign_Boolean/de.md)**.

## Eigenschaften

Der [UnterFormBinder](PartDesign_SubShapeBinder/de.md) ist abgeleitet von [Part Formelement](Part_Feature/de.md) (`Part::Feature` Klasse). Zusätzlich zu den in [Part Formelement](Part_Feature/de.md) aufgelisteten Eigenschaften sind die folgenden Eigenschaften im [Eigenschaftseditor](property_editor/de.md) verfügbar.

### Daten


{{TitleProperty|Base}}

-    **Unterstützung|XVerknüpfungUnterListe|ausgeblendet**: Unterstützung für die Geometrie.

-    **Verschmelzen|Bool**: wenn es {`True` ist, werden die verknüpften Volumenkörperformen verschmolzen.

-    **Flächen erstellen|Bool**: Wenn der Wert `True` ist, wird eine Fläche für die verknüpften Drahtobjekte erstellt.

-    **Kindobjekte beanspruchen|EigenschaftBool**: Wenn der Wert `True` ist, werden die verknüpften Objekte in der [Baumansicht](Tree_view/de.md) als Kindobjekte beansprucht.

-    **Relativ|Bool**: wenn es`True` ist, ermöglicht es die relative Verknüpfung von Unterobjekten.

-    **Bindungsmodus|Aufzählung**: Bindungsmodus, {{Wert|Synchronisiert}}, {{Wert|Eingefroren}}, {{Wert|Abgehängt}}.

-    **Teilweise laden|Bool**}: wenn es `True` ist, ermöglicht es Objekte teilweise zu Laden.

-    **Kontext|XVerknüpfung|ausgeblendet**: Containerobjekt dieses Binderobjekts.

-    **_Version|Integer|ausgeblendet**: Version dieses Objekttyps.

-    **Form|PartForm|ausgeblendet**: [Part TopoForm](Part_TopoShape/de.md) dieses Objekttyps.


{{TitleProperty|Cache}}

-    {{PropertyData/de|Körper|Matrix|ausgeblendet}}: Einheitenmatrix dieses Objekts.

### Ansicht

Siehe [Part Formelement](Part_Feature/de.md).

## Verweise

-   [New Sublink Link Feature](https://forum.freecadweb.org/viewtopic.php?t=41450), Gebrauchserklärung mit Video.





{{PartDesign Tools navi

}} 
