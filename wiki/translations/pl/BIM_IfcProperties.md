---
 GuiCommand:
   Name: BIM IfcProperties
   Name/pl: BIM: Edytuj właściwości IFC
   MenuLocation: Zarządzanie , Edytuj właściwości IFC
   Workbenches: BIM_Workbench/pl
   SeeAlso: 
---

# BIM IfcProperties/pl



## Opis

**Menedżer właściwości IFC** umożliwia edycję właściwości IFC jednego wybranego obiektu, wielu wybranych obiektów lub wszystkich obiektów dokumentu. Właściwości IFC to informacje dołączone do poszczególnych obiektów. Mogą być one dołączane tylko do [obiektów BIM](BIM_Workbench/pl.md), więc każdy obiekt nie będący obiektem BIM musi najpierw zostać przekonwertowany na obiekt BIM za pomocą narzędzia [Komponent](Arch_Component/pl.md), zanim będzie mógł przechowywać właściwości IFC.

<img alt="" src=images/BIM_ifcproperties_screenshot.png  style="width:1024px;"> 
*Menedżer właściwości IFC*

Właściwości IFC mogą być niestandardowe, tzn. można zdefiniować dla nich własną nazwę i wartość, lub mogą być zgodne z gotowym schematem zdefiniowanym przez standard IFC. Właściwości te są zdefiniowane w *Zestawach właściwości* i są zwykle udostępniane dla najpopularniejszych typów IFC. Na przykład zestaw właściwości **Pset_BeamCommon** jest przeznaczony do dołączania do belek. Predefiniowane zestawy właściwości zazwyczaj zawierają zwykłe właściwości, które schemat IFC zdefiniował dla określonego typu. Na przykład zestaw Pset_WallCommon, który powinien być dołączony do ścian, zawiera właściwości określające, czy ściana jest nośna, zewnętrzna czy wewnętrzna.

Można tworzyć własne właściwości i zestawy właściwości i przypisywać je do dowolnego obiektu. W schemacie IFC nie ma wymogu dodawania predefiniowanych zestawów właściwości dla typowych typów ani żadnych ograniczeń dotyczących dodawania niestandardowych właściwości. Jest to decyzja pozostawiona użytkownikom. Zazwyczaj, podczas pracy w zespole, kwestie te są ustalane wraz z innymi wymaganiami BIM, aby upewnić się, że wszystkie tworzone modele BIM spełniają te same wymagania.



### Definiowanie własnych zestawów właściwości 

Dostępne zestawy predefiniowanych właściwości są przechowywane w katalogu zasobów FreeCAD, który można znaleźć wprowadzając poniższy kod do [konsoli Pythona](Python_console/pl.md):


```python
FreeCAD.getResourceDir()
```

Predefiniowane zestawy właściwości znajdują się w **/Mod/BIM/Presets/pset_definitions.csv**.

Wewnątrz pliku CSV każdy wiersz reprezentuje inny zestaw właściwości, zaczynając od nazwy zestawu i dowolnej liczby par Nazwa;Typ, definiujących nazwę właściwości i jej typ. Na przykład:


{{Code|lang=text|code=
Pset_FreeCAD;Name;IfcLabel;Version;IfcReal
}}

To zdefiniowałoby zestaw właściwości o nazwie \"FreeCAD\" *(przedrostek \"Pset\_\" nie jest obowiązkowy, ale jest powszechną praktyką)*, który zawiera dwie właściwości: jedną o nazwie \"Name\", którą jest IfcLabel *(fragment tekstu)*, a drugą o nazwie \"Version\", która jest IfcReal *(wartość liczbowa z miejscami dziesiętnymi)*.

Możesz dodać własny plik csv z twoimi zestawami właściwości. Ten plik musi być nazwany CustomPsets.csv i umieszczony w **$USERAPPDATA/BIM**.

Folder **$USERAPPDATA** zależy od platformy/systemu operacyjnego:

-   na Windows jest to zwykle: **%APPDATA%/FreeCAD**
-   na Linux jest to zwykle: **$HOME/.FreeCAD**
-   na macOS jest to zwykle: **$HOME/Library/Preferences/FreeCAD**

Może być też znaleziony poprzez wpisanie tego w konsoli Pythona:


```python
FreeCAD.getUserAppDataDir()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM IfcProperties/pl
