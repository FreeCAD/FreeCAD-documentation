---
 GuiCommand:Addon
   Name: BIM IfcProperties
   Name/pl: BIM: Edytuj właściwości IFC
   Workbenches: Image:IFC.svg BIM Workbench/pl
   Addon: BIM
   MenuLocation: Zarządzaj , Edytuj właściwości IFC
   SeeAlso: BIM IfcElements/pl,BIM IfcQuantities/pl
---

# BIM IfcProperties/pl



## Opis

<img alt="" src=images/BIM_ifcproperties_screenshot.png  style="width:1024px;">

Menedżer właściwości IFC umożliwia edycję właściwości IFC jednego wybranego obiektu, wielu wybranych obiektów lub wszystkich obiektów dokumentu. Właściwości IFC to informacje dołączone do poszczególnych obiektów. Mogą być one dołączane tylko do [obiektów BIM](BIM_Workbench/pl.md), więc każdy obiekt nie będący obiektem BIM musi najpierw zostać przekonwertowany na obiekt BIM za pomocą opcji w menu **3D/BIM -> Komponent**, zanim będzie mógł przechowywać właściwości IFC.

Właściwości IFC mogą być niestandardowe, tzn. można zdefiniować dla nich własną nazwę i wartość, lub mogą być zgodne z gotowym schematem zdefiniowanym przez standard IFC. Właściwości te są zdefiniowane w *Zestawach właściwości* i są zwykle udostępniane dla najpopularniejszych typów IFC. Na przykład zestaw właściwości **Pset_BeamCommon** jest przeznaczony do dołączania do belek. Predefiniowane zestawy właściwości zazwyczaj zawierają zwykłe właściwości, które schemat IFC zdefiniował dla określonego typu. Na przykład zestaw Pset_WallCommon, który powinien być dołączony do ścian, zawiera właściwości określające, czy ściana jest nośna, zewnętrzna czy wewnętrzna.

Można tworzyć własne właściwości i zestawy właściwości i przypisywać je do dowolnego obiektu. W schemacie IFC nie ma wymogu dodawania predefiniowanych zestawów właściwości dla typowych typów ani żadnych ograniczeń dotyczących dodawania niestandardowych właściwości. Jest to decyzja pozostawiona użytkownikom. Zazwyczaj, podczas pracy w zespole, kwestie te są ustalane wraz z innymi wymaganiami BIM, aby upewnić się, że wszystkie tworzone modele BIM spełniają te same wymagania.



### Definiowanie własnych zestawów właściwości 

Dostępne zestawy właściwości, które są wstępnie zdefiniowane w standardzie IFC, są przechowywane w pliku [csv dołączonym do FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/Presets/pset_definitions.csv). Można również dodać niestandardowy plik csv z własnymi zestawami właściwości. Plik ten musi mieć nazwę CustomPsets.csv i być umieszczony w katalogu \$USERAPPDATA/BIM

Folder \$USERAPPDATA zależy od platformy/systemu operacyjnego *(zazwyczaj \$HOME/.FreeCAD na linux/mac, /users/YOUR USER/Application Data/roaming/FreeCAD na windows)* i można go również znaleźć wpisując go w konsoli Python:

FreeCAD.getUserAppDataDir()

Wewnątrz pliku CSV każdy wiersz reprezentuje inny zestaw właściwości, zaczynając od nazwy zestawu i dowolnej liczby par Nazwa;Typ, definiujących nazwę właściwości i jej [typ](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/Presets/ifc_types_IFC4.json). Na przykład:

Pset_FreeCAD;Name;IfcLabel;Version;IfcReal

zdefiniowałby zestaw właściwości o nazwie \"FreeCAD\" *(przedrostek Pset\_ nie jest obowiązkowy, ale jest powszechną praktyką)*, który zawiera dwie właściwości: jedną o nazwie \"Name\", którą jest IfcLabel *(fragment tekstu)*, a drugą o nazwie \"Version\", która jest IfcReal *(wartość liczbowa z miejscami dziesiętnymi)*.



---
⏵ [documentation index](../README.md) > BIM IfcProperties/pl
