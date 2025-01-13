# Body/pt-br
## Introdução

No FreeCAD, o termo \"[Corpo](Body.md)\" normalmente se refere a um objeto [Corpo do PartDesign](PartDesign_Body/pt-br.md) (classe `PartDesign::Body`) definido pela [Bancada PartDesign](PartDesign_Workbench/pt-br.md). Este é um objeto contêiner que pode conter [esboços 2D](Sketch/pt-br.md) e [recursos geométricos 3D](PartDesign_Feature/pt-br.md) para construir uma forma sólida.

Consulte [Corpo do PartDesign](PartDesign_Body/pt-br.md) para mais informações sobre esse tipo de objeto.



## Utilização

1.  Mude para a [Bancada PartDesign](PartDesign_Workbench/pt-br.md).
2.  Pressione **[<img src=images/PartDesign_Body.svg style="width:16px"> [Corpo do PartDesign](PartDesign_Body/pt-br.md)**.
3.  Pressione **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [Novo Esboço do PartDesign](PartDesign_NewSketch/pt-br.md)** para criar um novo [esboço](Sketch/pt-br.md).
4.  Crie um contorno fechado e, em seguida, use **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad/pt-br.md)** para extrudir o esboço e criar um sólido inicial.
5.  Adicione mais esboços e extrusões, e utilize outras ferramentas da [Bancada PartDesign](PartDesign_Workbench/pt-br.md) para modificar e transformar o sólido inicial.

Alternativamente, em vez de usar [esboços](Sketch/pt-br.md), você pode adicionar primitivas de [Recursos do PartDesign](PartDesign_Feature/pt-br.md), como, por exemplo, um **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [Caixa Aditiva do PartDesign](PartDesign_AdditiveBox/pt-br.md)**. É possível usar qualquer quantidade de recursos aditivos e subtrativos para criar um volume final.



## Notas

Um Corpo é necessário ao utilizar a [Bancada PartDesign](PartDesign_Workbench/pt-br.md) em uma metodologia de [edição de recursos](Feature_editing/pt-br.md).

Um Corpo não é necessário ao utilizar a [Bancada Part](Part_Workbench/pt-br.md), pois essa bancada utiliza um fluxo de trabalho baseado em [geometria sólida construtiva](Constructive_solid_geometry/pt-br.md), que se fundamenta em [formas primitivas](Part_Primitives/pt-br.md) e operações booleanas.


{{PartDesign Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > Body/pt-br
