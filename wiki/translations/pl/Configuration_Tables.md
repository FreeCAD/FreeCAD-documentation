---
 TutorialInfo:l
   Topic: Korzystanie z tabel konfiguracji
   Level: Początkującyy
   Time: 30 minut
   Author: Gbroques
   FCVersion: 0.20
   Files: https://forum.freecad.org/download/file.php?id=270593 ConfigurationTableExample.FCStd
---

# Configuration Tables/pl







## Wprowadzenie

Wraz z wydaniem [FreeCAD V0.20](Release_notes_0.20/pl#Środowisko_pracy_Arkusz_Kalkulacyjny.md) pojawiły się dwa nowe potężne narzędzia: *[Łącza](Std_LinkMake/pl.md) wariantowe* i *[Tabele konfiguracji](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183)*. Tabele konfiguracji to specjalny typ łączy wariantowych. Pozwalają na zmianę zestawów predefiniowanych parametrów dla danego obiektu.

Wcześniej można było parametryzować obiekty za pomocą technik takich jak arkusze kalkulacyjne, ale jednoczesne istnienie wielu zróżnicowanych instancji tego samego obiektu było niemożliwe, chyba że użyto technik takich jak kopiowanie plików lub obiektów, co powodowało problemy z utrzymaniem. Tabele konfiguracyjne ułatwiają zarządzanie takimi wariantami oraz możliwość łatwego przełączania się między nimi.

Ten poradnik zakłada, że jesteś już częściowo zaznajomiony ze środowiskami [Projekt Części](PartDesign_Workbench/pl.md) i [Szkicownik](Sketcher_Workbench/pl.md). Powinieneś też umieć korzystać z [widoku drzewa](Tree_view/pl.md) i [Edytora właściwości](Property_editor/pl.md).

Jest tez dostępna [wersja wideo tego poradnika](https://www.youtube.com/watch?v=m9C_ahIVKOI).



## Przykład

Aby lepiej zrozumieć tabele konfiguracji, rozważmy następujący przykład.

Wyobraź sobie prostą sześciokątną nakrętkę ze średnicą gwintu 10mm (M10).

Możemy ponownie wykorzystać ten sam projekt, utworzyć łącze i zmienić pewne parametry aby uzyskać nakrętkę M12.

Dla naszego przykładu opiszemy różnice między tymi dwoma wariantami przy pomocy 3 parametrów:

1.  średnica otworu,
2.  szerokość między narożnikami,
3.  grubość.

Konkretne wartości parametrów dla naszych wariantów są opisane w tej tabeli:

  Wariant   Średnica (Diameter)   Szerokość między narożnikami (WidthAcrossCorners)   Grubość (Thickness)
     
  M10       10                    18.48                                               8.4
  M12       12                    20.78                                               10.8



### Wytyczne

1.  Utwórz nowy [arkusz kalkulacyjny](Spreadsheet_CreateSheet/pl.md) z nagłówkiem w pierwszym wierszu. Zostaw drugi wiersz pusty. Ten wiersz będzie przechowywał bieżącą konfigurację i zostanie automatycznie wypełniony później. Dodaj parametry dla M10 i M12 w wierszach 3 i 4:
    ![](images/Variant-link-spreadsheet-table-example-before-configuration-table.png )
2.  Użyj [środowiska pracy Projekt Części](PartDesign_Workbench/pl.md) do stworzenia [Zawartości](PartDesign_Body.md) i [szkicu](PartDesign_NewSketch.md) dla nakrętki sześciokątnej. Wiązanie wymiarowe zostanie dodane w dalszym kroku.
    ![](images/Variant-link-example-hex-nut-sketch-unconstrained.png )
3.  [Wyciągnij](PartDesign_Pad/pl.md) szkic. Zaakceptuj domyślną wartość Długości.
4.  Kliknij prawym przyciskiem myszy na komórkę A2 w arkuszu kalkulacyjnym i wybierz **Tabela konfiguracji...** z menu kontekstowego.
5.  Otworzy się okno dialogowe **Konfiguracja Tabeli**.
6.  Wprowadź następujące dane:
    ![](images/Variant-link-example-setup-configuration-table.png )

    To wypełnia drugi wiersz w tabeli, dodaje nową właściwość **Configuration** do Zawartości i wiąże tabelę konfiguracji z nią.
7.  Naciśnij przycisk **OK**.
8.  Jeśli komórka A2 pokazuje {{Value|#PENDING}}, możesz kliknąć arkusz prawym przyciskiem myszy w [widoku drzewa](Tree_view/pl.md) i wybrać **Przelicz obiekt** aby pokazać poprawną wartość.
9.  Nadaj alias dla 3 komórek w wierszu 2 pod nagłówkami Diameter, WidthAcrossCorners i Thickness. Każdy alias powinien odpowiadać nagłówkowi kolumny komórki.
    ![](images/Variant-link-spreadsheet-table-example.png )
10. Zwiąż szkic dwoma wiązaniami i przypisz do nich [wyrażenia](Expressions/pl.md) {{Value|Spreadsheet.Diameter}} i {{Value|Spreadsheet.WidthAcrossCorners}}:
    ![](images/Variant-link-example-hex-nut-sketch.png )
11. Przypisz {{Value|Spreadsheet.Thickness}} do właściwości **Length** wyciągnięcia.
12. Utwórz [łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md).
13. W [widoku drzewa](Tree_view/pl.md) przeciągnij łącznik kształtów podrzędnych z Zawartości i upuść go na węźle Dokumentu.
14. Upuść Zawartość na łącznik, aby ustawić jego właściwość **Support** na Zawartość. Upuszczenie jest wymagane, ponieważ ta właściwość jest domyślnie tylko do odczytu.
15. Ustaw właściwość **Bind Copy on Change** łącznika na {{Value|Enabled}}.
16. Wybierz {{Value|M12}} dla właściwości **Configuration** łącznika.
17. Ustaw właściwość **Use Binder Style** na `False` dla łącznika.
18. Zmień właściwość **Placement** łącznika, aby był oddalony od Zawartości.
19. Po zakończeniu powinieneś mieć coś takiego:
    <img alt="" src=images/Variant-link-finished-example-document.png  style="width:500px;">



### Użyj Łącza zamiast Łącznika kształtów podrzędnych 

Dla łącza wariantowego możesz również użyć [Łącza](Std_LinkMake/pl.md) zamiast [Łącznika kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md): 1. Wstępne kroki 1-10 opisane powyżej są takie same. 2. Utwórz Łącze do Zawartości. 3. Ustaw właściwość Łącza **Link Copy On Change** na {{Value|Enabled}}. 4. Postępuj zgodnie z krokami 16, 18 i 19 opisanymi powyżej.



## Kluczowe kwestie 

-   Jak wspomniano, łącze wariantowe można utworzyć za pomocą [Łącza](Std_LinkMake/pl.md) lub [Łącznika kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md). Realthunder wyjaśnia różnicę [tutaj](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183):{{quote|text=Zamiast duplikować połączony obiekt z całą jego hierarchią, [Łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md) utworzy spłaszczoną kopię zmienionego obiektu. Inną różnicą w stosunku do Łącza jest to, że [Łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md) synchronizuje wszelkie zmiany oryginalnego obiektu z kopią, nawet jeśli konfiguracje są różne, podczas gdy w przypadku Łącza, po skopiowaniu, dwa obiekty stają się niezależne.}}
    
-   Chociaż oparte na łączach, łącza wariantowe nie są tak \"tanie\" jak zwykłe łącza, ponieważ tworzą kopie oryginalnego obiektu. Realthunder udziela wskazówek [tutaj](https://forum.freecadweb.org/viewtopic.php?p=532130#p532130) i [tutaj](https://forum.freecadweb.org/viewtopic.php?p=358582#p358582):{{quote|text=[Podczas] korzystania z łącza dla alternatywnych konfiguracji, musisz zdawać sobie sprawę, że tworzy to kopię oryginalnego obiektu... lepiej jest stworzyć pojedyncze łącze 'wariantowe' dla każdego [wariantu], aby uniknąć niepotrzebnych duplikatów. A jeszcze lepiej, użyj Łącznika kształtów podrzędnych... I znów, stwórz jeden [Łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md) dla każdej konfiguracji.}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Spreadsheet](Category_Spreadsheet.md) > Configuration Tables/pl
