---
 GuiCommand:
   Name: Sketcher SelectElementsWithDoFs
   Name/pl: Szkicownik: Wybierz elementy bez wiązań
   MenuLocation: Szkic , Widok szkicu , Wybierz elementy bez wiązań
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **F**
   Version: 0.18
---

# Sketcher SelectElementsWithDoFs/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:24px;"> **Wybierz elementy bez wiązań** wybiera nie w pełni związane elementy w szkicu.

Jeśli takie elementy istnieją w szkicu, [sekcja komunikatów Solvera w oknie dialogowym Szkcownika](Sketcher_Dialog/pl#Komunikaty_solvera.md) wyświetla następujący komunikat:

-   Niezwiązany: n DoF

Gdzie „n" to pozostała liczba stopni swobody. Kliknięcie podkreślonego tekstu spowoduje zaznaczenie niedostatecznie związanych elementów.

Należy pamiętać, że szkic może również zawierać nadmiarowe więzy, jeśli zostanie wyświetlony jeden z innych [komunikatów solvera](Sketcher_Dialog/pl#Komunikaty_solvera.md).



## Użycie

1.  Narzędzie można wywołać na kilka sposobów:
    -   Kliknij podkreślony tekst w oknie dialogowym szkicownika, jak opisano powyżej.
    -   Wybierz z menu opcję **Szkic → Widok szkicu → <img src="images/Sketcher_SelectElementsWithDoFs.svg" width=16px> Wybierz elementy bez wiązań**.
    -   Użyj skrótu klawiaturowego: **Z**, następnie **F**.
2.  Wybierane są elementy szkicu zawierające niewystarczające wiązania.
3.  Opcjonalnie kliknij w pustym obszarze w [widoku 3D](3D_view/pl.md), aby usunąć zaznaczenie.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SelectElementsWithDoFs/pl
