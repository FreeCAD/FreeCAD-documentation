---
- GuiCommand:
   Name: Part Offset
   Name/pl: Część: Odsunięcie 3D
   MenuLocation: Część -> Odsunięcie 3D
   Workbenches: Part_Workbench/pl
   SeeAlso: Part_Thickness/pl, Part_Offset2D/pl
---

# Part Offset/pl



## Opis

Narzędzie <img alt="" src=images/Part_Offset.svg  style="width:24px;"> **Odsunięcie 3D** tworzy równoległe kopie wybranego kształtu w pewnej odległości od kształtu bazowego, równocześnie tworząc nowy obiekt.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">



## Użycie

1.  Wybierz obiekt, z którym chcesz utworzyć odsunięcie.
2.  Naciśnij przycisk **<img src="images/Part_Offset.svg" width=16px> '''Odsunięcie 3D'''
**
3.  Dostosuj odległość i parametry w zależności od wymaganych rezultatów.



## Uwagi

-   Obiekty typu [App: Łącze](App_Link/pl.md) powiązane z odpowiednimi typami obiektów oraz kontenery typu [App: Część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również używane jako obiekty źródłowe. {{Version/pl|0.20}}



## Przykłady

Obiekt z niewielkim odsunięciem i zaokrąglonymi rogami *(łuk)*.

<img alt="" src=images/PartOffset0.png  style="width:400" height="200px;"> → <img alt="" src=images/PartOffset1.png  style="width:400" height="200px;">

Ten sam obiekt z ostrymi *(przecinającymi się)* narożnikami.

<img alt="" src=images/PartOffset3.png  style="width:400" height="200px;">

Ten sam obiekt z dużym odstępem wypełnia przednią lewą lukę i umożliwia przecięcie linii.

<img alt="" src=images/PartOffset2.png  style="width:400" height="200px;">

Arbitralny kształt *(projekt poli jak polilinia)* z odsunięciem 3D *(ignoruje parametr MODE)*.

<img alt="" src=images/PartOffset4.png  style="width:400" height="200px;">

ten sam kształt z odsunięciem 3D jako POWŁOKA i *wypełnionym* odsunięciem

<img alt="" src=images/PartOffset5.png  style="width:400" height="200px;">

Odsunięcie **wypełnione** z 2 cylindrami tworzącymi cięcia funkcją logiczną. Cylinder A przechodzi przez WYPEŁNIENIE, podczas gdy Cylinder B przechodzi tylko przez WYPEŁNIENIE, a NIE przez źródłowy kształt 2D.

<img alt="" src=images/PartOffset6.png  style="width:400" height="200px;">



## Właściwości

-    {{PropertyData/pl|Offset}}: Odległość, o którą mają być przesunięte wierzchołki kształtu

-    {{PropertyData/pl|Mode}}: Tryb tworzenia. Powłoka tworzy nowy kształt wokół kształtu źródłowego. Rura *(do zrobienia)*. RectoVerso *(do zrobienia)*.

-    {{PropertyData/pl|Join type}}: W jaki sposób budowane są nowe narożniki. Przecięcie daje ostre narożniki przez liniowe przedłużenie krawędzi. Łuk i styczna dają zaokrąglone narożniki.

1.  Opcjaː Przecięcieː Pozwala na podsunięcia skierowane do wewnątrz w celu \"zalania\" luki przez przecięcie wynikowego kształtu, aż do osiągnięcia przeciwległych powierzchni.
2.  Opcjaː Samodzielne przecięcieː *(do zrobienia)*
3.  Opcjaː Wypełnianie odsunięciaː Jeśli kształt był dwuwymiarowy, luka pomiędzy dwoma kształtami zostanie wypełniona. Wypełnienie jest teraz bryłą, stąd kształt źródłowy nie jest bryłą. Tak więc operacje logiczne mogą prowadzić do dziwnych rezultatów *(patrz przykład poniżej)*.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset/pl
