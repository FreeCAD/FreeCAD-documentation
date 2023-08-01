---
- GuiCommand:
   Name:Part JoinCutout
   Name/pl:Część: Wycięcie dla obiektu
   MenuLocation:Part → Join → Wycięcie dla obiektu
   Workbenches:[Część](Part_Workbench/pl.md)
   Version:0.16
   SeeAlso:[Połącz obiekty](Part_JoinConnect/pl.md), [Osadź obiekty](Part_JoinEmbed/pl.md), [Operacja logiczna](Part_Boolean/pl.md), [Grubość](Part_Thickness/pl.md)
---

# Part JoinCutout/pl



## Opis

Narzędzie <img alt="" src=images/Part_JoinCutout.svg  style="width:24px;"> **Wycięcie dla obiektu** tworzy wycięcie w obiekcie ze ściankami *(np. rurze)*, aby dopasować je do innego obiektu ze ściankami.

![600px](images/JoinFeatures_Cutout.png)



## Użycie

1.  Najpierw wybierz obiekt bazowy, a następnie obiekt do zdefiniowania wycięcia.

Kolejność wyboru jest ważna. Wystarczy wybrać jeden kształt podrzędny każdego obiektu *(np. ściany)*.

1.  Polecenie Wycięcie dla obiektu można wywołać na kilka sposobów:
    -   Naciśnij przycisk <img alt="" src=images/Part_JoinCutout.svg  style="width:24px;"> **Wycięcie dla obiektu** na pasku narzędzi.
    -   Użyj polecenia **Część → Połącz → Wycięcie dla obiektu** w menu głównym.

Tworzony jest obiekt środowiska Część Wycięcie dla obiektu z ustawionym trybem \"Wycięcie\". Oryginalne obiekty są ukryte, a wynik osadzenia jest wyświetlany w oknie widoku 3D.



## Właściwości


{{TitleProperty|Podstawa}}

-    **Baza**: Odniesienie do obiektu bazowego (tego, w którym ma zostać wykonane wycięcie). Obiekt powinien być pojedynczą bryłą.

-    **Narzędzie**: Odniesienie do obiektu narzędzia *(obiektu, który ma pasować do wycięcia)*. Obiekt może być pojedynczą bryłą lub [prawidłowym złożeniem](Part_Compound.md) brył.

-    **Tryb**: Tryb działania, równy *Wycięcie* *(Zmiana, która przekształci narzędzie w inne Part_JoinXXX)*. Wartość \"Obejdź\" może być użyta do tymczasowego wyłączenia długich obliczeń *(zostanie utworzone złożenie bazy i narzędzia, co jest szybką operacją)*.

-    **Ulepsz**: Określa, czy zastosować operację [ulepszenia](Part_RefineShape/pl.md) do ostatecznego kształtu. wobec ostatecznego kształtu. Wartość domyślna jest określona przez pole wyboru \"Automatycznie udoskonal model po wykonaniu operacji logicznej\" w [Preferencjach środowiska Projekt Części](PartDesign_Preferences/pl.md). Gdy właściwość **Tryb** ma wartość **Obejdź**, Ulepszanie jest ignorowane *(nigdy nie jest stosowane)*.



## Przykład

1.  Utwórz rurę, stosując narzędzie [grubość](Part_Thickness/pl.md) do [cylindra](Part_Cylinder/pl.md):

![320px](images/JoinFeatures_Example_step1.png)

1.  Utwórz kolejną rurę o mniejszej średnicy i [umieść](Placement/pl.md) ją tak, aby przebiła ścianę pierwszej rury:

![320px](images/JoinFeatures_Example_step2.png)

1.  Zaznacz pierwszą rurę, a następnie drugą rurę *(kolejność zaznaczania jest ważna)* i kliknij opcję \"Wycięcie dla obiektu\" na rozwijanym pasku narzędzi **Połącz obiekty**.

![320px](images/JoinFeatures_Example_step3_Cutout.png)



## Sposób działania 

Algorytmy stojące za narzędziami Połącz są dość proste, a ich zrozumienie jest ważne dla prawidłowego korzystania z narzędzi.

1\. Obiekt bazowy jest [wycięty logicznie](Part_Cut/pl.md) za pomocą obiektu narzędzia. Wynikowy kształt jest zestawem *([złożeń](Part_Compound/pl.md))* nieprzecinających się brył *(zazwyczaj dwóch)*.

2\. Uzyskane złożenie jest kolejnie filtrowane, przy czym zachowywana jest tylko największa bryła.

4\. Jeśli właściwość Ulepsz ma wartość {{true/pl}}, wynikowy kształt to obiekt funkcji [Ulepsz](Part_RefineShape.md).
![800px](images/JoinFeatures-Algo-Cutout.png)



### Uwagi

-   Jeśli po kroku 1 obiekt pozostaje w jednym kawałku, wynik operacji Wycięcie będzie równoważny logicznej operacji[Wytnij](Part_Fuse/pl.md) bazy i narzędzia.
-   Obecnie narzędzie wygeneruje nieoczekiwany wynik, jeśli jako baza zostanie użyte złożenie. *(Może to zostać zmienione w przyszłości.)*
-   Ponieważ największy element jest określany przez porównanie objętości elementów, narzędzie może działać tylko z bryłami. *(Może to zostać zmienione w przyszłości.)*



## Tworzenie skryptów 

Narzędzie Osadź może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```pythonJoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout')```

-   Tworzy pusty element Wycięcia *(lub inną cechę dołączania, w zależności od przekazanego trybu)*. Następnie należy jawnie przypisać właściwości Baza i Narzędzie.
-   Zwraca nowo utworzony obiekt.

Przykład: {{code|code=
import JoinFeatures
j = JoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout' )
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tool = FreeCADGui.Selection.getSelection()[1]
}}

Samo narzędzie jest zaimplementowane w środowisku Python, patrz **/Mod/Part/JoinFeatures.py** ([Link do Github](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/JoinFeatures.py)) w miejscu, w którym zainstalowany jest FreeCAD.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinCutout/pl
