# Arch IFC/de
{{TOCright}}

## Beschreibung

Die <img alt="" src=images/Workbench_Arch.svg  style="width:24px;">_ (engl. Building Information Modeling (kurz: BIM)) bietet einen [Industry Foundation Classes (IFC)](https://de.wikipedia.org/wiki/Industry_Foundation_Classes) Importeur und Exporteur. Das IFC Format ist ein ständig wachsendes, weit verbreitetes Format für den Datenaustausch zwischen [BIM](https://de.wikipedia.org/wiki/Building_Information_Modeling) (Bauwerksdatenmodellierung) Anwendungen, das in der Architektur und im Ingenieurwesen verwendet wird.

Sowohl der Importer als auch der Exporter hängen von der [IfcOpenShell](IfcOpenShell/de.md) Bibliothek ab, die in einigen FreeCAD Distributionen mitgeliefert wird. Eine einfache Möglichkeit zu prüfen, ob IfcOpenShell verfügbar ist, ist die Eingabe in der [Python Konsole](Python_console/de.md):


```python
import ifcopenshell
```

Wenn keine Fehlermeldung erscheint, ist IfcOpenShell installiert, und du kannst mit dem [Importieren](Std_Import/de.md) von IFC Dateien fortfahren. Andernfalls musst du IfcOpenShell selbst installieren; lies die [IfcOpenShell](IfcOpenShell/de.md) Seite, um mehr über diesen Vorgang zu erfahren.


**Note:**

Das **<img src=images/BIM_Setup.svg style="width:16px"> [BIM Einrichtung](BIM_Setup/de.md)**swerkzeug sucht auch nach IfcOpenShell und gibt eine Warnmeldung aus, wenn diese nicht installiert ist.


**Hinweis 2:**

in der Vergangenheit (2013) verfügte der Arch Arbeitsbereich über einen einfacheren IFC Importeur, der nicht von IfcOpenShell abhängig war. Dieses Legacy Modul ist immer noch im Quellcode enthalten, aber ab v0.19 wird es überhaupt nicht mehr empfohlen; es wird nur eine sehr kleine Teilmenge von IFC Objekten importieren können und sollte als völlig veraltet betrachtet werden.

## Importieren

Alle [IfcProduct](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifckernel/lexical/ifcproduct.htm)-basierten Objekte aus IFC2x3 oder IFC4 Dateien werden in das FreeCAD Dokument importiert. In den IFC Voreinstellungen kannst du festlegen, wie die IFC Objekte importiert werden:

-   **vollparametrische Arch Objekte**, die Geometrie wird so weit wie möglich in FreeCAD editierbar sein
-   **nicht-parametrische Arch Objekte**, die Objekte tragen IFC Informationen und Eigenschaften, sind aber nicht editierbar
-   **nicht-parametrische Bauteilformen**, die Geometrie wird originalgetreu wiedergegeben, aber die IFC Informationen werden verworfen
-   **eine Bauteilform pro Etage**, ein einziges Objekt, nur als Referenz

Jeder dieser Typen verliert einige Informationen gegenüber dem vorherigen, ist aber ressourcenschonender, was das Öffnen größerer Dateien ermöglicht. Ein letzter Typ erlaubt es, das Importieren von Arch Objekten ganz zu verwerfen, was für strukturanalytische Modelle nützlich ist.

Wenn du versuchst, eine große Datei zu öffnen und FreeCAD zu lange für den Import braucht, versuche es normalerweise mit einem niedrigeren Importmodus.

IfcOpenShell unterstützt alle IFC2x3 und IFC4 Entitäten (IFC4-add1 und IFC4-add2 werden in v0.6 implementiert und sind möglicherweise verfügbar, wenn du dies liest), aber nicht alle können in [Arch](Arch_Workbench/de.md)-Objekte konvertiert werden, diejenigen, die nicht importiert werden können, werden als einfache [Part](Part_Workbench/de.md) Formen importiert. Der IFC Importeur importiert zunächst alle IFC-Entitäten, die von [IfcProduct](http://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproduct.htm) abgeleitet sind, d.h. im Grunde alle Objekte, aus denen ein Gebäude besteht, wie z.B. Wände oder Fenster oder Rohre. Alle anderen Entitäten, die von einem dieser Objekte benötigt werden, wie z. B. Extrusionsprofile oder Komponenten boolescher Operationen, werden nach Bedarf importiert.

Wenn ein Importmodus verwendet wird, der Arch Objekte verwendet, gleichgültig ob parametrisch oder nicht, tragen alle Objekte den vollständigen Satz von [IfcEigenschaften](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm), der an jedes Objekt angehängt ist, gruppiert nach Eigenschaftensatz.

Gebäudestrukturen wie Standorte, Gebäude und Stockwerke werden ebenfalls originalgetreu importiert, und die Struktur wird in FreeCAD korrekt nachgebildet. Gruppenstrukturen (mit IfcGroups) werden ebenfalls in FreeCAD importiert und gerendert und können mit Gebäudestrukturen kombiniert werden, z.B. mit Gruppen innerhalb von Stockwerken oder Stockwerken innerhalb von Gruppen.

[IfcAnnotation](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcproductextension/lexical/ifcannotation.htm)-Objekte werden ebenfalls importiert, genau wie gradlinige (linear) und gekrümmte (curve-based) [IfcStructuralItem](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralitem.htm) Entitäten.

Die in der IFC Datei angegebenen Größen werden **NICHT** importiert. Da die Geometrie jedoch vollständig in FreeCAD neu erstellt wird, sind die meisten Größen wie Länge, Fläche usw. für jedes Objekt leicht erhältlich.

Das Aktivieren von **show debug messages** in den IFC-Voreinstellungen wird einen Bericht ausgeben, wenn beim Import von IFC-Dateien Fehler auftreten.

**Hinweis**: Der BIM Arbeitsbereich verfügt über ein [IFC Explorer](BIM_IfcExplorer/de.md) Werkzeug , das dir erlaubt eine IFC Datei im schnellen Nur-Text Modus zu öffnen und nur die gewünschten Teile zu importieren.

## Export

Beim Exportieren in IFC Dateien werden alle ausgewählten Objekte und ihre Nachkommen exportiert. Alle Arch/BIM Objekte werden unterstützt, ebenso wie andere Objekte, die in anderen Arbeitsbereichen erstellt wurden. Die einzigen derzeit noch nicht vollständig unterstützten Objekte sind **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/Std_Part.svg style="width:PartDesign Körper](PartDesign_Body/de.md)**, **_** und **[16px"> VerweisGruppen**, so dass du diese noch etwas testen musst, wenn du sie verwenden möchtest. [Arch Referenzen](Arch_Reference/de.md) wird derzeit als `IfcBuildingElementProxies` exportiert.

Um einen ganzen Standort oder ein ganzes Gebäude oder ein ganzes Stockwerk oder eine Gruppe, die andere Objekte enthält, zu exportieren, ist es nur erforderlich, dieses Gebäude oder dieses Stockwerk oder diese Gruppe auszuwählen. Arch Objekte werden mit dem Typ exportiert, der in ihrer Eigenschaft \"IFC Type\" festgelegt ist. Ihre [IfcProperties](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm) werden ebenfalls exportiert, und wenn diese Objekte eine IFC UID aus einem früheren Import haben, wird dieselbe UID beim Export beibehalten. Objekte, die keine Arch Objekte sind, werden als [IfcBuildingElementProxy](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcsharedbldgelements/lexical/ifcbuildingelementproxy.htm) exportiert.

IFC Dateien werden als IFC2x3 oder IFC4 exportiert, abhängig von Ihrer Version von IfcOpenShell, die mit jedem der IFC Schemata kompiliert werden kann. Wenn du IfcOpenShell v0.6 oder höher verwendest, wird die in den Arch Einstellungen angegebene IFC Version verwendet.

Wenn die Form der exportierten Objekte auf einer Extrusion oder einer booleschen Operation basiert, werden die Operation und die Komponenten korrekt in die IFC exportiert. Wenn nicht, wird die Form des Objekts als [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4x1/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm) exportiert. Wenn die Form Kurven enthält, werden diese trianguliert. IfcOpenShell v0.5 oder höher verfügt jedoch über einen Serialisierer, der in den Import/Export → IFC Einstellungen aktiviert werden muss. Wenn dieser Serialisierer aktiviert ist, ist er in der Lage, sehr komplexe gekrümmte Objekte, wie z.B. solche, die auf NURBS basieren, zu exportieren und somit triangulierte Flächen zu vermeiden. Zum Zeitpunkt der Erstellung dieses Artikels unterstützen jedoch nur wenige andere BIM Anwendungen IFC NURBS Objekte, so dass ein wenig Testen empfohlen wird.

## Weitere Informationen 

-   [IfcOpenShell](IfcOpenShell/de.md), Weitere Informationen zum Installieren dieser Bibliothek.





 

_

---
[documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Arch](Arch_Workbench.md) > Arch IFC/de
