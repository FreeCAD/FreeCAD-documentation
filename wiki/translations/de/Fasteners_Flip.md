---
- GuiCommand:
   Name: Fasteners Flip
   Name/de: Fasteners Umdrehen
   MenuLocation: Fasteners -> Invert fastener
   Workbenches: Fasteners_Workbench/de
---

# Fasteners Flip/de

## Beschreibung

Der Befehl <img alt="" src=images/Fasteners_Flip.svg  style="width:24px;"> **Invert Fastener** dreht die Ausrichtung von [befestigten Verbindungselementen](Fasteners_Workbench#Anwendung.md) um durch Änderung ihrer {{PropertyData/de|invert}}.

## Anwendung

1.  Ein oder mehrere befestigte Verbindungselemente auswählen. Die Auswahl kann nicht befestigte Verbindungselemente enthalten, aber diese werden nicht umgedreht. Siehe [Hinweise](#Hinweise.md)
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Fasteners_Flip.svg" width=16px> [Fasteners Umdrehen](Fasteners_Flip/de.md)** drücken.
    -   Dem Menüeintrag **Fasteners → <img src="images/Fasteners_Flip.svg" width=16px> Invert fastener** auswählen.
3.  Die Ausrichtung der ausgewählten befestigten Verbindungselemente ist umgedreht.

## Hinweise

-   Die {{PropertyData/de|invert}} wird für nicht befestigte Verbindungselemente ignoriert und sie können mit diesem Befehl nicht umgedreht werden. Um sie umzudrehen, sollte ihre {{PropertyData/de|Placement}} geändert werden, z.B. mit dem Befehl <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std Bewegen](Std_TransformManip/de.md).





{{Fasteners Tools navi

}}



---
⏵ [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Fasteners](Category_Fasteners.md) > Fasteners Flip/de
