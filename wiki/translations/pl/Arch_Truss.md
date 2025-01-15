---
 GuiCommand:
   Name: Arch Truss
   Name/pl: BIM: Wiązar
   MenuLocation: 3D / BIM , Wiązar
   Workbenches: BIM_Workbench/pl
   Version: 0.19
---

# Arch Truss/pl



## Opis

Narzędzie **Wiązar** tworzy obiekt [wiązara](https://pl.wikipedia.org/wiki/Wi%C4%85zar_(budownictwo)) z wybranego obiektu liniowego *(takiego jak [linia](Draft_Line/pl.md) lub [szkic](Sketcher_NewSketch/pl.md))* lub od podstaw, jeśli żaden obiekt nie został wybrany podczas uruchamiania polecenia.

<img alt="" src=images/Arch_Truss_example.png  style="width:600px;">



## Użycie



### Tworzenie z wybranego obiektu 

1.  Użyj wybranego środowiska pracy, aby utworzyć pojedynczą linię
2.  Wybierz tę linię.
3.  Naciśnij przycisk **<img src="images/Arch_Truss.svg" width=16px> '''Wiązar'''**.
4.  Dostosuj właściwości kratownicy do swoich potrzeb.



### Tworzenie od podstaw 

1.  Upewnij się, że nic nie jest zaznaczone
2.  Naciśnij przycisk **<img src="images/Arch_Truss.svg" width=16px> '''Wiązar'''**.
3.  Kliknij w widoku 3D, aby zdefiniować pierwszy punkt lub ręcznie wprowadź współrzędne X, Y i Z.
4.  Kliknij w widoku 3D, aby zdefiniować drugi punkt lub ręcznie wprowadź współrzędne X, Y i Z.
5.  Dostosuj właściwości kratownicy do własnych potrzeb.



## Właściwości



### Dane

-    **TrussAngle**: Kąt kratownicy.

-    **SlantType**: Typ skosu kratownicy.

-    **Normal**: Kierunek normalny kratownicy.

-    **HeightStart**: Wysokość kratownicy w pozycji początkowej.

-    **HeightEnd**: Wysokość kratownicy w pozycji końcowej.

-    **StrutStartOffset**: Opcjonalne przesunięcie początkowe dla górnej rozpórki.

-    **StrutEndOffset**: Opcjonalne przesunięcie końcowe dla górnej rozpórki.

-    **StrutHeight**: Wysokość głównych górnych i dolnych elementów kratownicy.

-    **StrutWidth**: szerokość głównego górnego i dolnego elementu kratownicy.

-    **RodType**: Typ środkowego elementu kratownicy.

-    **RodDirection**: Kierunek prętów.

-    **RodSize**: Średnica lub bok prętów.

-    **RodSections**: Liczba sekcji prętów.

-    **RodEnd**: Czy kratownica ma pręt w punkcie końcowym, czy nie.

-    **RodMode**: Sposób rysowania prętów.



## Tworzenie skryptów 

Narzędzie **Wiązar** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Truss = makeFence([baseobj])
```

Przykład:


```python
import FreeCAD
import Draft
import Arch

p1 = FreeCAD.Vector(0,0,0)
p2 = FreeCAD.Vector(2000,0,0)
baseline = Draft.makeLine(p1,p2)
truss = Arch.makeTruss(baseline)
truss.HeightStart = 200
truss.HeightEnd = 400
# adjust other needed properties
```



---
⏵ [documentation index](../README.md) > Arch Truss/pl
