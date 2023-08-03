---
 GuiCommand:
   Name: Part JoinEmbed
   Name/pl: Część: Osadź obiekt
   MenuLocation: Część , Połącz , Osadź obiekt
   Workbenches: Part_Workbench/pl
   Version: 0.16
   SeeAlso: Part_JoinConnect/pl, Part_JoinCutout/pl, Part_Boolean/pl, Part_Thickness/pl
---

# Part JoinEmbed/pl



## Opis

Narzędzie **Osadź** umożliwia umieszczenie obiektu ze ściankami *(np. rury)* w innym obiekcie ze ściankami.

![600px](images/JoinFeatures_Embed.png)



## Użycie

1.  Wybierz najpierw obiekt bazowy, a następnie obiekt, który ma zostać osadzony. Kolejność wyboru jest ważna. Wystarczy wybrać jeden kształt podrzędny każdego obiektu *(np. ściany)*.
2.  Wywołaj polecenie Osadź obiekt.

Tworzony jest obiekt środowiska Część CechaPołączenia z ustawionym trybem \"Osadź\". Oryginalne obiekty są ukryte, a wynik osadzenia jest wyświetlany w oknie widoku 3D.



## Właściwości


{{TitleProperty|Podstawa}}

-    **Baza**: Odniesienie do obiektu bazowego *(tego, w którym ma zostać osadzony inny obiekt)*. Obiekt powinien być pojedynczą bryłą.

-    **Narzędzie**: Odniesienie do obiektu narzędzia (obiektu, który ma zostać osadzony). Obiekt może być pojedynczą bryłą lub [prawidłowym złożeniem](Part_Compound.md) brył.

-    **Tryb**: Tryb działania, równy **Osadź** *(Zmiana, która przekształci narzędzie w inne Part_JoinXXX)*. Wartość **obejdź** może być użyta do tymczasowego wyłączenia długich obliczeń (zostanie utworzone połączenie bazy i narzędzia, co jest szybką operacją).

-    **Ulepsz**: Określa, czy zastosować operację [ulepszania](Part_RefineShape/pl.md) wobec ostatecznego kształtu. Wartość domyślna jest określona przez pole wyboru \"Automatycznie udoskonal model po wykonaniu operacji logicznej\" w [Preferencjach środowiska Projekt Części](PartDesign_Preferences/pl.md). Gdy właściwość **Tryb** ma wartość **Obejdź**, Ulepszanie jest ignorowane *(nigdy nie jest stosowane)*.



## Przykład

1.  Utwórz rurę, stosując narzędzie [grubość](Part_Thickness/pl.md) do bryły [cylindra](Part_Cylinder/pl.md):

<img alt="" src=images/JoinFeatures_Example_step1.png  style="width:320px;">

1.  Utwórz kolejną rurę o mniejszej średnicy i [umieść](Placement/pl.md) ją tak, aby przebiła ścianę pierwszej rury:

![320px](images/JoinFeatures_Example_step2.png)

1.  Wybierz pierwszą rurę, a następnie drugą rurę (kolejność wyboru jest ważna) i kliknij opcję \"Osadź obiekt\" na rozwijanym pasku narzędzi Dołącz.

![320px](images/JoinFeatures_Example_step3_Embed.png)

1.  Zastosuj narzędzie przekroju *([Przełącz płaszczyznę tnącą](Std_ToggleClipPlane/pl.md), [Płaszczyzna przekroju](Arch_SectionPlane/pl.md) środowiska Architektura, [Płaszczyzna cięcia](Arch_CutPlane/pl.md) środowiska Architektura)*, aby odsłonić elementy wewnętrzne. Na poniższym obrazku użyto narzędzia Płaszczyzna przekroju środowiska Architektura.

![320px](images/JoinFeatures_Example_step4_Embed.png)



## Sposób działania 

Algorytmy stojące za narzędziami Połącz są dość proste, a ich zrozumienie jest ważne dla prawidłowego korzystania z narzędzi.

1\. Obiekt bazowy jest [wycięty logicznie](Part_Cut/pl.md) za pomocą obiektu narzędzia. Wynikowy kształt jest zestawem *([złożeń](Part_Compound/pl.md))* nieprzecinających się brył *(zazwyczaj dwóch)*.

2\. Uzyskane złożenie jest kolejnie filtrowane, przy czym zachowywana jest tylko największa bryła.

3\. Ta największa bryła jest [logicznym połączeniem](Part_Fuse/pl.md) z obiektem narzędzia.

4\. Jeśli właściwość Ulepsz ma wartość {{true/pl}}, wynikowy kształt to obiekt funkcji [Ulepsz](Part_RefineShape.md).
![800px](images/JoinFeatures-Algo-Embed.png)



### Uwagi

-   Jeśli po kroku 1 obiekt pozostaje w jednym kawałku, wynik operacji Osadź będzie równoważny [połączeniu](Part_Fuse/pl.md) bazy i narzędzia, ale jego obliczenie zajmie więcej czasu.
-   Obecnie narzędzie wygeneruje nieoczekiwany wynik, jeśli jako baza zostanie użyte złożenie. *(Może to zostać zmienione w przyszłości.)*
-   Ponieważ największy element jest określany przez porównanie objętości elementów, narzędzie może działać tylko z bryłami. *(Może to zostać zmienione w przyszłości.)*



## Tworzenie skryptów 

Narzędzie Osadź może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```pythonJoinFeatures.makePartJoinFeature(name = 'Embed', mode = 'Embed')```

-   Tworzy pusty element osadzania *(lub inny element dołączania, w zależności od przekazanego trybu)*. Następnie należy jawnie przypisać właściwości Baza i Narzędzie.
-   Zwraca nowo utworzony obiekt.

Przykład:


{{code|code=
import JoinFeatures
j = JoinFeatures.makePartJoinFeature(name = 'Embed', mode = 'Embed' )
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tool = FreeCADGui.Selection.getSelection()[1]
}}

Samo narzędzie jest zaimplementowane w środowisku Python, patrz **/Mod/Part/JoinFeatures.py** ([Link do Github](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/JoinFeatures.py)) w miejscu, w którym zainstalowany jest FreeCAD.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinEmbed/pl
