---
- GuiCommand:
   Name: Part Offset2D
   Name/pl: Część: Odsunięcie 2D
   MenuLocation: Część -> Odsunięcie 2D
   Workbenches: Part_Workbench/pl
   Version: 0.17
   SeeAlso: Part_Offset/pl, Part_Thickness/pl, Draft_Offset/pl
---

# Part Offset2D/pl



## Opis

Narzędzie <img alt="" src=images/Part_Offset2D.svg  style="width:24px;"> **Offset 2D** tworzy polilinię równoległą do oryginalnej polilinii w pewnej odległości od niej. Lub powiększa/zmniejsza płaską ścianę, w podobny sposób.

Polilinia / ściana musi być płaska. W jednym obiekcie może znajdować się wiele przewodów, niekoniecznie współpłaszczyznowych.

![600px](images/Part_Offset2D_Demo.png)



## Użycie

1.  Wybierz obiekt do przesunięcia.
2.  Naciśnij przycisk **<img src="images/Part_Offset2D.svg" width=16px> [Odsunięcie 2D](Part_Offset2D/pl.md)**.
3.  Ustaw przesunięcie w oknie [Panelu zadań](Task_panel/pl.md).
4.  Naciśnij **OK**.



## Uwagi

-   Obiekty typu [App: Łącze](App_Link/pl.md) powiązane z odpowiednimi typami obiektów oraz kontenery typu [App: Część](App_Part/pl.md) z odpowiednimi widocznymi obiektami wewnątrz mogą być również używane jako obiekty źródłowe. {{Version/pl|0.20}}



## Znane problemy 

-   Większość trybów innych niż domyślne będzie działać tylko z OCC 7.0.0 lub nowszym.

-   Korzystanie z narzędzia może spowodować awarię FreeCAD *(patrz następny punkt)*. W systemie Windows awarie te są konwertowane na wyjątki i generalnie nie powodują zamknięcia FreeCAD. W innych systemach operacyjnych tak nie jest, dlatego zaleca się zapisanie projektu przed próbą użycia narzędzia. Nie są również obsługiwane elipsy.

-   Powiększanie ścian z okrągłymi otworami o ilość wystarczającą do zamknięcia otworów powoduje awarię *(OCC 7.0.0)*. Problem wydaje się być specyficzny dla okręgów; inne kształty wydają się zamykać prawidłowo.

-   Podczas kompensowania okręgów, które mają niezerowe Umiejscowienie, wynik jest umieszczany nieprawidłowo. *(OCC 7.0.0)*

-   Podczas przesuwania okręgów czasami są one przesuwane w nieoczekiwanym kierunku *(np. do wewnątrz zamiast na zewnątrz). (OCC 7.0.0)*

-   Wypełnienie - wartość {{true/pl}} nie działa podczas zbiorczego odsunięcia otwartych polilinii w trybie \"Powłoka\".

-   Tryb łączenia \"styczny\" nie działa *(OCC 7.0.0)*.

-   Odsunięcie polilinii wykonanej z pojedynczego segmentu linii nie jest obsługiwane *(ponieważ segment linii nie definiuje płaszczyzny)*. Pojedyncze segmenty linii również nie mogą uczestniczyć w przesunięciu zbiorowym.



## Właściwości

-    **Źródło**: Łącze do oryginalnego kształtu

-    **Wartość**: Odległość, o którą ma zostać powiększona polilinia / ściana. Jeśli wartość jest ujemna, przewód / powierzchnia zostanie zmniejszona.

-    **Tryb***(\"Rura\" lub \"Powłoka\")*: ustawia sposób przetwarzania niezamkniętych przewodów. Jeśli wybrano \"Rura\", to polilinia jest obrysowywana tak, jakby była bardzo cienkim zamkniętym konturem. Jeśli \"Powłoka\", tworzony jest rozwarta linia.

:   ![600px](images/Part_Offset2D_Mode.png)

-    **Połącz***(\"Łuk\", \"Stycznie\", \"Przecięcie\")*: ustawia zachowanie wokół załamań. Jeśli wybrano \"Łuk\", przesunięte segmenty są połączone łukiem okręgu, wyśrodkowanym w wierzchołku. \"Stycznie\" nie jest obsługiwane w OCC7.0.0. \"Przecięcie\": przesunięte segmenty są przedłużane do momentu ich przecięcia.

:   ![600px](images/Part_Offset2D_Join.png)

-    **Przecięcie**przyjmuje wartości *({{false/pl}} i {{true/pl}})*: ustawia, czy wiele linii ma być traktowanych łącznie, czy niezależnie. Jeśli wybrano {{false/pl}}, przewody są przesunięte niezależnie, przecięcia między wynikowymi liniami są ignorowane. Jeśli {{true/pl}}, linie są przesunięte grupowo.

:   ![600px](images/Part_Offset2D_Intersection.png)

Tylko linie wewnątrz struktury złożonej są połączone. Na przykład, jeśli struktura jest typu *compound(wire1, wire2, compound(wire3, wire4))*, linie wire1 i wire2 będą traktowane zbiorczo, ale niezależnie od linii wire3 i wire4. Podobnie, wire3 i wire4 są traktowane zbiorczo, ale niezależnie od wire1 + wire2.

Również w trybie zbiorczym kierunki linii są ważne i wpływają na kierunek przesunięcia. Jest to ściśle związane z tym, jak traktowane są otwory w ścianach.

Przewody traktowane zbiorczo muszą być współpłaszczyznowe. Przewody traktowane niezależnie nie muszą być współpłaszczyznowe.

-    **Wypełnienie**przyjmuje wartości *({{false/pl}}, {{true/pl}})*: jeśli wybrano {{true/pl}}, przestrzeń między oryginalną linią/ścianą a przesunięciem jest wypełniana ścianą.

:   ![600px](images/Part_Offset2D_Fill.png)



## Tworzenie skryptów 

Narzędzie **Odsunięcie 2D** może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji: {{code|code=
f = App.ActiveDocument.addObject("Part::Offset2D", "Offset2D")
f.Source =  #some object
f.Value = 10.0
}}

Odsunięcie 2D jest również dostępne jako metoda {{Incode|Part.Shape.}} Przykład: {{code|code=
import Part
circle = Part.Circle().toShape()
enlarged_circle = circle.makeOffset2D(10.0)
Part.show(circle)
Part.show(enlarged_circle)
# makeOffset2D(offset, join = 0, fill = False, openResult = false, intersection = false)
# 
# * offset: distance to expand the shape by. 
# 
# * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
# intersection
# 
# * fill: if true, the output is a face filling the space covered by offset. If
# false, the output is a wire/face.
# 
# * openResult: True for "Skin" mode; False for Pipe mode. 
# 
# * intersection: collective offset
# 
# Returns: result of offsetting (wire or face or compound of those). Compounding
# structure follows that of source shape.
}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset2D/pl
