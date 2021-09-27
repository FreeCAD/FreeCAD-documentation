# <img alt="Ícone da bancada de trabalho de imagem" src=images/Workbench_Image.svg  style="width:64px;"> Image Workbench/pt-br

## Introdução


{{TOCright}}

A <img alt="" src=images/Workbench_Image.svg  style="width:24px;"> [Bancada de trabalho Imagem](Image_Workbench/pt-br.md) controla diferentes tipos de imagens [bitmap](bitmap/pt-br.md) e permite que você as abra no FreeCAD.

## Ferramentas

-   <img alt="" src=images/Image-import.svg  style="width:32px;"> [Abrir](Image_Open/pt-br.md): abre uma imagem em uma nova janela de visualização.
-   <img alt="" src=images/Image-import-to-plane.svg  style="width:32px;"> [Importar para o plano](Image_CreateImagePlane/pt-br.md): importa uma imagem para um plano na vista 3D.
-   <img alt="" src=images/Image-scale.svg  style="width:32px;"> [Escalar](Image_Scaling/pt-br.md): Escala uma imagem importada para um plano.

## Recursos

-   Assim como a bancada [Sketch](Sketcher_Workbench/pt-br.md), uma imagem importada por ser anexada a um dos principais planos XY, XZ ou YZ, e dado um deslocamento positivo ou negativo.
-   A imagem é importada com uma relação de 1 pixel para 1 milímetro.
-   A recomendação é ter a imagem importada em uma resolução razoável.

## Fluxo de trabalho 

A maior utilização desta bancada de trabalho é fazer um traçado sobre a imagem, utilizando as ferramentas da bancada [Draft](Draft_Workbench/pt-br.md) ou [Sketcher](Sketcher_Workbench/pt-br.md), com o intuito de gerar um sólido baseado nos contornos traçados na imagem.

Traçar uma imagem funciona melhor se a imagem tem um deslocamento negativo pequeno como, por exemplo, de -0.1 mm, a partir do plano de trabalho. Isto significa que a imagem estará levemente atrás do plano onde você desenha sua geometria 2D. Sendo assim, não desenhe na própria imagem.

O deslocamento da imagem pode ser configurado durante a importação ou alterada posteriormente por meio de suas propriedades.





{{Image Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Image Workbench/pt-br
