---
 GuiCommand:
   Name: Draft SubelementHighlight
   Name/pl: Rysunek Roboczy: Podświetl element podrzędny
   MenuLocation: Rysunek Roboczy , Podświetl element podrzędny
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **S** **S**
   Version: 0.19
   SeeAlso: Draft_Move/pl, Draft_Rotate/pl, Draft_Scale/pl
---

# Draft SubelementHighlight/pl



## Opis

Polecenie <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:24px;"> **Podświetl element podrzędny** tymczasowo podświetla wybrane obiekty lub obiekty bazowe wybranych obiektów. Jest ono przeznaczone do użycia w połączeniu z trybem elementów podrzędnych polecenia [Przesuń](Draft_Move/pl.md), [Obróć](Draft_Rotate/pl.md) lub [Skaluj](Draft_Scale/pl.md). Obecnie tryb elementu podrzędnego działa poprawnie tylko dla [linii](Draft_Line/pl.md) i [polilinii](Draft_Wire/pl.md).

![](images/Draft_SubelementHighlight_example.png ) 
*Ściana środowiska Architektura, której podstawa, pililinia, została podświetlona.*



## Użycie

1.  Opcjonalnie wybierz jedną lub więcej [linii](Draft_Line/pl.md) lub [polilinii](Draft_Wire/pl.md) lub obiekty, których **Bazą** są [liniie](Draft_Line/pl.md) lub [polilinie](Draft_Wire/pl.md).
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_SubelementHighlight.svg" width=16px> '''Podświetl element podrzędny'''**.
    -   Wybierz opcję z menu **Modyfikacja → <img src="images/Draft_SubelementHighlight.svg" width=16px> Podświetl element podrzędny**.
    -   Użyj skrótu klawiaturowego: **H**, a następnie **S**.
3.  Jeśli obiekt nie został jeszcze wybrany: wybierz obiekt w oknie [widoku 3D](3D_view.md).
4.  Wybrane obiekty staną się widoczne *(jeśli jest to wymagane)*, ich **Kolor linii** i **Kolor punktu** zostaną zmienione na czerwone, a ich **Rozmiar punktu** zostanie zmieniony na {{Value|10}}.
5.  Zaleca się teraz odznaczenie istniejącego wyboru, na przykład poprzez kliknięcie losowego punktu w oknie [widoku 3D](3D_view/pl.md).
6.  Wybierz jeden lub więcej elementów podrzędnych, krawędzi lub punktów obiektów, które zostały zaznaczone na czerwono.
7.  Wywołaj polecenie [Przesuń](Draft_Move/pl.md), [Obróć](Draft_Rotate/pl.md) lub [Skaluj](Draft_Scale/pl.md).
8.  Przełącz tryb elementów podrzędnych w panelu zadań tego polecenia, zaznaczając pole wyboru **Modyfikuj elementy podrzędne**.
9.  Zmodyfikuj wybrane elementy podrzędne i zakończ polecenie modyfikacji.
10. Naciśnij **Esc**, aby przywrócić tymczasowe zmiany wizualne obiektów.



## Uwagi

-   Jeśli obiekty zostały podświetlone za pomocą tego polecenia, tymczasowe zmiany wizualne powinny zostać cofnięte przed zapisaniem i ponownym otwarciem pliku.
-   Podświetlone obiekty nie powinny być kopiowane, jeśli tryb elementów podrzędnych jest wyłączony. Tymczasowych zmian wizualnych nie można przywrócić dla kopii utworzonych w ten sposób.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SubelementHighlight/pl
