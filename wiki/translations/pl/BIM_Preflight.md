---
 GuiCommand:Addon/pl
   Name: BIM Preflight
   Name/pl: BIM: Kontrola wstępna
   Workbenches: Image:IFC.svg BIM_Workbench/pl
   Addon: BIM
   MenuLocation: Manage , Preflight check
---

# BIM Preflight/pl



## Opis

<img alt="" src=images/BIM_preflight_screenshot.png  style="width:1024px;">

Ponieważ FreeCAD jest bardzo swobodną platformą do modelowania, wymagania są bardzo niskie. Zasadniczo można modelować i organizować model BIM w dowolny sposób, korzystając ze wszystkich narzędzi oferowanych przez FreeCAD, zarówno ze środowiska pracy BIM, jak i innych środowisk pracy. Format IFC ma jednak pewne surowe wymagania, a inne aplikacje BIM, które mogą odczytywać pliki IFC, często wprowadzają dodatkowe ograniczenia, ponieważ często mają trudności z niektórymi jednostkami lub sposobem modelowania niektórych obiektów.

Narzędzie Kontrola wstępna umożliwia przeprowadzenie kilku testów modelu w celu zweryfikowania jego zgodności ze standardami IFC i najlepszymi praktykami, a także pomaga wykryć ewentualne problemy, które warto naprawić.

Wyniki większości testów dostarczanych przez to narzędzie są opcjonalne, co oznacza, że możesz wyeksportować swój model, nawet jeśli zakończą się one niepowodzeniem. To Ty musisz ocenić, czy potrzebujesz testu, aby go zdać, czy nie. Dołożyliśmy wszelkich starań, aby dostarczyć rzetelnych informacji, które pomogą Ci podjąć decyzję.



## Użycie

-   Mieć otwarty model w programie FreeCAD, z co najmniej kilkoma obiektami.
-   Możesz wybrać obiekty przed uruchomieniem testów, w którym to przypadku masz możliwość wykonania testu tylko na wybranych obiektach.
-   Naciśnij przycisk **Testuj wszystko**, aby wykonać wszystkie testy, lub tylko przyciski odpowiadające poszczególnym testom.
-   Po zakończeniu testów naciśnięcie przycisku **Niepowodzenie** spowoduje wyświetlenie dodatkowych informacji, które pomogą ci zdecydować, czy jest to dla ciebie istotne, czy nie.



## Testy wbudowane 

-   **Uruchom wszystkie testy**: uruchamia wszystkie testy jeden po drugim.



### Testy konfiguracji programu FreeCAD 

-   **Obsługa IFC4**: Sprawdza, czy system importu / eksportu IFC FreeCAD działa poprawnie i czy format IFC4 jest dostępny *(co wymaga aktualnej i włączonej w preferencjach wersji [IfcOpenShell](Arch_IFC/pl.md))*.



### Testy dotyczące organizacji projektu 

-   **Hierarchia projektu**: Format IFC wymaga co najmniej jednego obiektu [budynku](Arch_Building/pl.md), a powszechną praktyką jest również posiadanie jednego [terenu](Arch_Site/pl.md) i co najmniej jednego [poziomu (kondygnacji)](Arch_BuildingPart/pl.md). Ten test sprawdza, czy są one obecne w modelu
-   **Budynki**: Sprawdza, czy wszystkie budynki znalezione w modelu są częścią [terenu](Arch_Site/pl.md).
-   **Poziomy**: Sprawdza, czy wszystkie [poziomy](Arch_BuildingPart/pl.md) *(kondygnacje budynku)* znalezione w modelu są częścią budynku.
-   **Struktura obiektów**: Sprawdza, czy wszystkie obiekty znalezione w modelu są częścią poziomu.



### Test obiektów i właściwościs 

-   **Niezdefiniowane obiekty**: Sprawdza, czy w modelu znajdują się obiekty, które nie są obiektami BIM i dlatego zostaną wyeksportowane bez pełnych właściwości BIM.
-   **Bryły**: Sprawdza, czy wszystkie obiekty w modelu mają prawidłową geometrię bryłową.
-   **Ilości jawne**: Sprawdza, czy wszystkie obiekty z właściwościami długości, szerokości lub wysokości są [oznaczone do wyraźnego eksportu](BIM_IfcQuantities.md) tych wielkości.
-   **Zestawy wspólnych właściwości**: Sprawdza, czy wszystkie obiekty BIM wspólnych typów *(ściana, drzwi itp.)* mają zastosowany odpowiedni \"wspólny\" zestaw właściwości *(Pset_WallCommon, Pset_DoorCommon itp.)*.
-   **Integralność zestawów właściwości**: Sprawdza, czy wszystkie wspólne zestawy właściwości *(Pset_WallCommon, Pset_DoorCommon itp.)* znalezione w modelu zawierają wszystkie i tylko właściwości zdefiniowane przez standardy IFC.
-   **Materiały**: Sprawdza, czy wszystkie obiekty BIM mają materiał.
-   **Standardy**: Sprawdza, czy wszystkie obiekty BIM mają [kod standardu](BIM_Classification/pl.md).



### Testy kompatybilności 

-   **Wyciągnięcia**: Sprawdza, czy wszystkie obiekty BIM są wyciągnięciami liniowymi.
-   **Przypadki standardowe**: Sprawdza, czy wszystkie elementy [ściany](Arch_Wall/pl.md) i [elementy konstrukcyjne](Arch_Structure/pl.md) są przypadkami standardowymi, zgodnie ze schematem IFC.
-   **Drobne linie**: Sprawdza, czy żaden segment linii w modelu nie jest mniejszy niż 1/32\", minimalna długość, z którą Revit jest w stanie sobie poradzić\...
-   **IfcRectangleProfileDef**: Sprawdza, czy opcja eksportu profili prostokątnych jako IfcRectangleProfileDef jest wyłączona, ponieważ Revit *(tak, znowu oni)* nie jest w stanie zaimportować tego elementu.



## Testy niestandardowe 

Narzędzie **Kontrola wstępna** umożliwia również pisanie niestandardowych testów, które będą dołączane po wbudowanych narzędziach w oknie dialogowym Kontrola wstępna i uruchamiane po użyciu przycisku *Uruchom wszystkie testy*. Testy te są napisane w języku Python. Składają się one z prostych funkcji wewnątrz jednego lub więcej plików Python. Możesz wykonać dowolną operację wewnątrz tych funkcji, muszą one po prostu przejść lub zakończyć się niepowodzeniem, a w przypadku niepowodzenia wyświetlić komunikat informujący użytkownika o niepowodzeniu.

Możesz napisać kilka testów w jednym pliku Python lub podzielić je na kilka plików, jak wolisz. Pliki te muszą być umieszczone w \$USERAPPDATA/BIM/Preflight i mogą mieć dowolną nazwę *(Upewnij się, że używasz bardzo unikalnych nazw, aby nie kolidować z żadnym wbudowanym modułem Pythona)*. Folder \$USERAPPDATA zależy od platformy/systemu operacyjnego *(zazwyczaj \$HOME/.FreeCAD na linux/mac, /users/YOUR USER/Application Data/roaming/FreeCAD na windows)* i można go również znaleźć wpisując go w konsoli FreeCAD Python:

FreeCAD.getUserAppDataDir()

Wewnątrz każdego pliku Python testy są prostymi funkcjami, które nie przyjmują żadnych argumentów i zwracają albo wartość {{True/pl}}, jeśli test się powiódł, albo ciąg tekstu, który zostanie wyświetlony użytkownikowi, jeśli test się nie powiódł.

Typowy plik testowy powinien mieć nazwę \"myCustomTest.py\" i być umieszczony w \$USERAPPDATA/BIM/Preflight:

import FreeCAD
# The name of your test. You can give the functions any name
# you want, the important is the description text below
def myCustomTest():
   # This describes what your test does. For example,
   # here, it checks that there is at least one object in the document.
   # This text will appear next to the button in the Preflight tool
   """Checks that the document contains at least one object"""
   doc = FreeCAD.ActiveDocument
   objects = doc.Objects
   if len(objects) >= 1:
       result = True
   else:
       result = "This document contains no object"
   # The function must return either True or a string of
   # text if the test failed. The string or text will be displayed
   # to the user when they press the "Failed" button.
   return result



---
⏵ [documentation index](../README.md) > BIM Preflight/pl
