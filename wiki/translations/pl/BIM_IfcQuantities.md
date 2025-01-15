---
 GuiCommand:
   Name: BIM IfcQuantities
   Name/pl: BIM: Menadżer ilości IFC
   MenuLocation: Zarządzanie , Menadżer ilości IFC
   Workbenches: BIM Workbench/pl
   SeeAlso: 
---

# BIM IfcQuantities/pl



## Opis

**Menedżer ilości IFC** umożliwia sprawdzenie \"jawnych ilości\" dołączonych do obiektów, które mają zostać wyeksportowane do IFC.

<img alt="" src=images/BIM_ifcquantities_screenshot.png  style="width:600px;"> 
*Menadżer ilości IFC.*

Format IFC pozwala na uwzględnienie, dla dowolnego obiektu, jawnych wielkości, które mogą być takie jak \"Szerokość\", \"Wysokość\" lub \"Powierzchnia\". Nie ma standardu określającego, który typ obiektu musi zawierać dany rodzaj wielkości, a także nie ma gwarancji, że takie jawne wielkości faktycznie odzwierciedlają geometrię obiektu. Innymi słowy, wielkości te mogą mieć błędne wartości lub nawet kłamać. Ściana może mieć geometrię sześcianu o długości 10 metrów, ale może mieć dołączoną wartość \"Długość\" równą 8 metrów.

Ideą ilości jawnych jest udostępnienie ich aplikacjom, które nie są w stanie odczytać geometrii, takim jak arkusze kalkulacyjne. Taka aplikacja, czytając plik IFC z jawnymi wielkościami, nadal może uzyskać pojęcie o wymiarach obiektu i wykorzystać je na przykład do obliczeń ilościowych.

Domyślnie podczas eksportowania pliku IFC z FreeCAD nie są eksportowane żadne jawne ilości. Dzięki menedżerowi ilości IFC możesz zaznaczyć, które ilości powinny zostać wyeksportowane i sprawdzić ich wartości. Znaki ostrzegawcze będą wyświetlane obok wartości zerowych, powiadamiając o możliwych problemach, które można naprawić przed eksportem.

Można również użyć menedżera ilości, aby zmienić lub naprawić rzeczywiste wartości *wysokości*, *szerokości* i *długości* obiektów. Wpłynie to jednak na geometrię obiektu w FreeCAD.



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM IfcQuantities/pl
