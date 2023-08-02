---
- GuiCommand:
   Name: Std DuplicateSelection
   Name/pl: Std: Powiel zaznaczone
   MenuLocation: Edycja -> Powiel zaznaczone
   Workbenches: All
   SeeAlso: Std_Cut/pl, Std_Copy/pl, Std_Paste/pl
---

# Std DuplicateSelection/pl

## Opis

Polecenie **Powiel zaznaczone** powoduje powielanie wybranych obiektów w aktywnym dokumencie.

## Użycie

1.  Zaznacz jeden lub więcej obiektów.
2.  Wybierz z menu opcję **Edycja → Powiel zaznaczone**.
3.  Jeśli obiekty mają zależności, które nie zostały wybrane, zostanie wyświetlone okno dialogowe z prośbą o określenie, które z nich powinny zostać uwzględnione.

## Uwagi

-   FreeCAD automatycznie zmieni wewnętrzne nazwy oraz, w zależności od preferencji, etykiety obiektów, aby uniknąć konfliktów nazw.

## Ustawienia

-   Duplikaty etykiet są dozwolone, gdy opcja **Przybory → Edycja parametrów ... → BaseApp → Preferencje → Dokument → DuplicateLabels** jest ustawione na wartość {{TRUE/pl}}. To ustawienie można również zmienić w [Edytorze ustawień](Preferences_Editor/pl#Dokument.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std DuplicateSelection/pl
