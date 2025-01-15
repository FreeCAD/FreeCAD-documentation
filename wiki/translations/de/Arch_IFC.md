# Arch IFC/de
## Beschreibung

Der Arbeitsbereich <img alt="" src=images/Workbench_BIM.svg  style="width:24px;">[BIM](BIM_Workbench/de.md) (engl. Building Information Modeling - Bauwerksdatenmodellierung) unterstützt von Haus aus [Industry-Foundation-Classes (IFC)](https://de.wikipedia.org/wiki/Industry_Foundation_Classes) und stellt dafür auch Import- und Exportwerkzeuge zur Verfügung. Das IFC-Format ist ein ständig wachsendes, weit verbreitetes Format für den Datenaustausch zwischen [BIM](https://de.wikipedia.org/wiki/Building_Information_Modeling)-Anwendungen, das im Architektur- und im Bauingenieurwesen verwendet wird.

Weitere Informationen zum Umgang mit IFC-Dateien finden sich auf der Seite [NativeIFC](NativeIFC.md).



#### IfcOpenShell

Die gesamte IFC-Funktionalität hängt von der [IfcOpenShell](IfcOpenShell/de.md)-Bibliothek ab, die in einigen FreeCAD-Distributionen mitgeliefert wird. Eine einfache Möglichkeit zu prüfen, ob IfcOpenShell vorhanden ist, ist die Eingabe des Folgenden in der [Python-Konsole](Python_console/de.md):


```python
import ifcopenshell
```

Wenn keine Fehlermeldung erscheint, ist IfcOpenShell installiert, kann mit dem [Öffnen](Std_Open/de.md) oder [Importieren](Std_Import/de.md) von IFC-Dateien fortgefahren werden. Andernfalls muss man IfcOpenShell selbst installieren; auf der Seite [IfcOpenShell](IfcOpenShell/de.md) erfährt man mehr über diesen Vorgang.


**Note:**

Das Werkzeug **[<img src=images/BIM_Setup.svg style="width:16px"> [BIM Einrichten](BIM_Setup/de.md)** sucht auch nach IfcOpenShell und gibt eine Warnmeldung aus, wenn diese nicht installiert ist.



## Öffnen und Importieren 

Beginnend mit Version 1.0 öffnet und importiert FreeCAD IFC-Dateien eigenständig. Mehr dazu findet man auf der Seite [NativeIFC](NativeIFC/de.md).



### Ältere Import-Werkzeuge 



#### Das Arch-Import-Werkzeug 

Das originale IFC-Import-Werkzeug des Arbeitsbereichs Arch wurde in der FreeCAD-Version 1.0 deaktiviert, steht aber noch über Python zur Verfügung:


```python
from importers import importIFC
importIFC.open("C:\\Path\\To\\My\\File.ifc")
```

Alle [IfcProduct](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifckernel/lexical/ifcproduct.htm)-basierten Objekte aus IFC2x3 oder IFC4 Dateien werden in das FreeCAD-Dokument importiert. In den IFC-Voreinstellungen kannst du festlegen, wie die IFC-Objekte importiert werden:

-   **vollparametrische Arch-Objekte**, die Geometrie wird so weit wie möglich in FreeCAD editierbar sein
-   **nicht-parametrische Arch-Objekte**, die Objekte tragen IFC-Informationen und Eigenschaften, sind aber nicht editierbar
-   **nicht-parametrische Bauteilformen**, die Geometrie wird originalgetreu wiedergegeben, aber die IFC-Informationen werden verworfen
-   **eine Bauteilform pro Etage**, ein einziges Objekt, nur als Referenz

Jeder dieser Typen verliert einige Informationen gegenüber dem vorherigen, ist aber ressourcenschonender, was das Öffnen größerer Dateien ermöglicht. Ein letzter Typ erlaubt es, das Importieren von Arch-Objekten ganz zu verwerfen, was für strukturanalytische Modelle nützlich ist.

Wenn du versuchst, eine große Datei zu öffnen und FreeCAD zu lange für den Import braucht, versuche es normalerweise mit einem niedrigeren Importmodus.

IfcOpenShell unterstützt alle IFC2x3 und IFC4 Entitäten (IFC4-add1 und IFC4-add2 werden in v0.6 implementiert und sind möglicherweise verfügbar, wenn du dies liest), aber nicht alle können in [BIM](BIM_Workbench/de.md)-Objekte konvertiert werden, diejenigen, die nicht importiert werden können, werden als einfache [Part](Part_Workbench/de.md)-Formen importiert. Das IFC-Import-Programm importiert zunächst alle IFC-Entitäten, die von [IfcProduct](http://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproduct.htm) abgeleitet sind, d.h. im Grunde alle Objekte, aus denen ein Gebäude besteht, wie z.B. Wände oder Fenster oder Rohre. Alle anderen Entitäten, die von einem dieser Objekte benötigt werden, wie z. B. Extrusionsprofile oder Komponenten boolescher Operationen, werden nach Bedarf importiert.

Wenn ein Importmodus verwendet wird, der Arch Objekte verwendet, gleichgültig ob parametrisch oder nicht, tragen alle Objekte den vollständigen Satz von [IfcEigenschaften](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm), der an jedes Objekt angehängt ist, gruppiert nach Eigenschaftensatz.

Gebäudestrukturen wie Standorte, Gebäude und Stockwerke werden ebenfalls originalgetreu importiert, und die Struktur wird in FreeCAD korrekt nachgebildet. Gruppenstrukturen (mit IfcGroups) werden ebenfalls in FreeCAD importiert und gerendert und können mit Gebäudestrukturen kombiniert werden, z.B. mit Gruppen innerhalb von Stockwerken oder Stockwerken innerhalb von Gruppen.

[IfcAnnotation](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcproductextension/lexical/ifcannotation.htm)-Objekte werden ebenfalls importiert, genau wie gradlinige (linear) und gekrümmte (curve-based) [IfcStructuralItem](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralitem.htm) Entitäten.

Die in der IFC Datei angegebenen Größen werden **NICHT** importiert. Da die Geometrie jedoch vollständig in FreeCAD neu erstellt wird, sind die meisten Größen wie Länge, Fläche usw. für jedes Objekt leicht erhältlich.

Das Aktivieren von **show debug messages** in den IFC-Voreinstellungen wird einen Bericht ausgeben, wenn beim Import von IFC-Dateien Fehler auftreten.

**Hinweis**: Der BIM Arbeitsbereich verfügt über ein [IFC Explorer](BIM_IfcExplorer/de.md) Werkzeug , das dir erlaubt eine IFC Datei im schnellen Nur-Text Modus zu öffnen und nur die gewünschten Teile zu importieren.

#### The legacy importer 

In der Vergangenheit verfügte der Arbeitsbereich Arch über einen einfacheres IFC-Import-Werkzeug, das nicht von IfcOpenShell abhängig war. Dieses Legacy-Modul ist immer noch im Quellcode enthalten und kann über Python verwendet werden, wird aber gar nicht mehr empfohlen; es kann nur eine sehr kleine Teilmenge der IFC-Objekte importieren und sollte als völlig veraltet betrachtet werden.

The legacy importer can be used from Python:


```python
from importers import importIFClegacy
importIFClegacy.open("C:\\Path\\To\\My\\File.ifc")
```



## Export

Beim Exportieren in IFC Dateien werden alle ausgewählten Objekte und ihre Nachkommen exportiert. Alle Arch/BIM Objekte werden unterstützt, ebenso wie andere Objekte, die in anderen Arbeitsbereichen erstellt wurden. Die einzigen derzeit noch nicht vollständig unterstützten Objekte sind **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)**, **[<img src=images/Std_Part.svg style="width:16px"> [Std Parts](Std_Part/de.md)** und neue Strukturen wie **[<img src=images/Link.svg style="width:16px"> [Anwendungsverweise](Std_LinkMake/de.md)** und **[<img src=images/LinkGroup.svg style="width:16px"> VerweisGruppen**, so dass du diese noch etwas testen musst, wenn du sie verwenden möchtest. [Arch Referenzen](Arch_Reference/de.md) wird derzeit als `IfcBuildingElementProxies` exportiert.

Um einen ganzen Standort oder ein ganzes Gebäude oder ein ganzes Stockwerk oder eine Gruppe, die andere Objekte enthält, zu exportieren, ist es nur erforderlich, dieses Gebäude oder dieses Stockwerk oder diese Gruppe auszuwählen. Arch Objekte werden mit dem Typ exportiert, der in ihrer Eigenschaft \"IFC Type\" festgelegt ist. Ihre [IfcProperties](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm) werden ebenfalls exportiert, und wenn diese Objekte eine IFC UID aus einem früheren Import haben, wird dieselbe UID beim Export beibehalten. Objekte, die keine Arch Objekte sind, werden als [IfcBuildingElementProxy](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcsharedbldgelements/lexical/ifcbuildingelementproxy.htm) exportiert.

IFC Dateien werden als IFC2x3 oder IFC4 exportiert, abhängig von Ihrer Version von IfcOpenShell, die mit jedem der IFC Schemata kompiliert werden kann. Wenn du IfcOpenShell v0.6 oder höher verwendest, wird die in den Arch Einstellungen angegebene IFC Version verwendet.

Wenn die Form der exportierten Objekte auf einer Extrusion oder einer booleschen Operation basiert, werden die Operation und die Komponenten korrekt in die IFC exportiert. Wenn nicht, wird die Form des Objekts als [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4x1/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm) exportiert. Wenn die Form Kurven enthält, werden diese trianguliert. IfcOpenShell v0.5 oder höher verfügt jedoch über einen Serialisierer, der in den Import/Export → IFC Einstellungen aktiviert werden muss. Wenn dieser Serialisierer aktiviert ist, ist er in der Lage, sehr komplexe gekrümmte Objekte, wie z.B. solche, die auf NURBS basieren, zu exportieren und somit triangulierte Flächen zu vermeiden. Zum Zeitpunkt der Erstellung dieses Artikels unterstützen jedoch nur wenige andere BIM Anwendungen IFC NURBS Objekte, so dass ein wenig Testen empfohlen wird.



## Weitere Informationen 

-   [IfcOpenShell](IfcOpenShell/de.md), Weitere Informationen zum Installieren dieser Bibliothek.



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [BIM](Category_BIM.md) > Arch IFC/de
