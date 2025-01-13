---
 GuiCommand:
   Name: Assembly CreateJointScrew
   Name/pl: Złożenie Utwórz połączenie śrubowe
   MenuLocation: Złożenie , Utwórz połączenie śrubowe
   Workbenches: Assembly_Workbench/pl
   Shortcut: **W**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateJointScrew/pl



## Opis

Narzędzie <img alt="" src=images/Assembly_CreateJointScrew.svg  style="width:24px;"> [Utwórz połączenie śrubowe](Assembly_CreateJointScrew/pl.md) tworzy połączenie śrubowe **(złącze spiralne)**, które wiąże przesunięcie części z połączeniem typu Przesuwne i obrót części z połączeniem typu Obrotowe. W połączeniu z istniejącymi już połączeniami, może być stosowane do symulowania np. śrub pociągowych.



## Użycie

1.  Opcjonalnie wybierz dwa obiekty geometryczne należące do dwóch różnych kształtów, które zostały wcześniej użyte do zdefiniowania połączeń typu Przesuwne i Obrotowe.
2.  Jest kilka sposobów na wywołanie tej komendy:
    -   Wciśnij przycisk **<img src="images/Assembly_CreateJointScrew.svg" width=16px> [Utwórz połączenie śrubowe](Assembly_CreateJointScrew/pl.md)**.
    -   Wybierz opcję **Złożenie → <img src="images/Assembly_CreateJointScrew.svg" width=16px> Utwórz połączenie śrubowe** z menu.
    -   Użyj skrótu: **W**.
3.  Okno dialogowe **Utwórz połączenie** zostanie otwarte w [panelu zadań](Task_panel/pl.md), wymieniając wcześniej wskazane obiekty.
4.  Dla dalszych kroków zobacz [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl#Użycie.md).



## Uwagi

-   Promień skoku odnosi się do skoku śruby napędowej. Jest przechowywany we właściwości **Distance** i definiuje przesunięcie na jeden obrót śruby.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt **Screw** wywodzi się z obiektu [App: Właściwości Python](App_FeaturePython/pl.md) i dziedziczy wszystkie jego właściwości. Zobacz [Utwórz połączenie stałe](Assembly_CreateJointFixed/pl#Właściwości.md) aby znaleźć dodatkowe właściwości.





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateJointScrew/pl
