---
- GuiCommand:/pl
   Name:Sketcher ConstrainLock
   Name/pl:Sketcher: Blokada wiązania
   MenuLocation:Sketch → Wiązania szkicownika → Blokada wiązania
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   SeeAlso:[Utwórz wiązanie blokady](Sketcher_ConstrainBlock/pl.md)
---

# Sketcher ConstrainLock/pl

## Opis

**Wiązanie blokady** ma zastosowanie dla wiązań **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> <img src=images/Sketcher_ConstrainDistanceY.svg style="width:Zwiąż odległość poziomą](Sketcher_ConstrainDistanceX/pl.md)** i **[16px"> [Zwiąż odległość pionową](Sketcher_ConstrainDistanceY/pl.md)** związania wybranych wierzchołków *(punktów)* na szkicu. Jeśli wybrany zostanie pojedynczy wierzchołek, wówczas poziome i pionowe wiązania odległości będą odnosić się do punktu początkowego szkicu. Jeśli wybrane zostaną dwa lub więcej punktów, dla każdej pary punktów zostaną dodane wiązania odległości poziomej i pionowej. Nie pojawi się automatyczny monit o edycję wartości wiązań, należy je edytować ręcznie.

## Użycie

1.  Wybierz jeden lub więcej wierzchołków *(punktów)* na szkicu.
2.  Naciśnij przycisk **<img src=images/Sketcher_ConstrainLock.svg style="width:16px"> [Utwórz blokadę wiązania](Sketcher_ConstrainLock/pl.md)**.
3.  Aby edytować wartości wiązania, kliknij dwukrotnie na wartość wiązania w oknie widoku 3D, lub kliknij dwukrotnie na wiązanie, lub kliknij prawym przyciskiem myszy i wybierz z listy Wiązanie w zakładce Zadania **Edytuj wartość**.

**Uwaga:** Narzędzie wiązania może być również uruchomione bez wcześniejszego zaznaczenia obiektów. Będzie wtedy działało tylko na jednym wierzchołku i stosowało wiązania do punktu początku szkicu. Domyślnie polecenie jest aktywne w trybie kontynuacji, by utworzyć nowe wiązanie. Wciśnij raz prawy przycisk myszki lub klawisz **ESC**, by zakończyć działanie polecenia.

## Tworzenie skryptów 

Wiązanie <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Blokada wiązania](Sketcher_ConstrainLock/pl.md) jest poleceniem GUI, które tworzy wiązanie <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [odległości poziomej](Sketcher_ConstrainDistanceX/pl.md) oraz <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [odległości pionowej](Sketcher_ConstrainDistanceY/pl.md), i nie stanowi samodzielnego wiązania. Zobacz stronę [Skrypty Szkicownika](Sketcher_scripting/pl.md), aby uzyskać szczegóły i przykłady, jak tworzyć te wiązania za pomocą skryptów języka Python.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainLock/pl
