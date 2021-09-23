# Installing Helpfile/pt-br
## FreeCAD arquivo de ajuda 


<div class="mw-translate-fuzzy">

A documentação offline do FreeCAD é construída a partir do wiki FreeCAD, utilizando scripts. Ele cresceu para um tamanho de arquivo superior a 180 MB. Estes grandes arquivos não fazem parte dos instaladores e executáveis do FreeCAD, mas podem ser instalados separadamente, conforme documentado aqui.


</div>

As traduções da comunidade são encorajadas, portanto, a documentação off-line agora também está disponível em francês e italiano. Outros idiomas podem estar em diferentes estágios de completude.

## Download arquivo de ajuda 

Uma documentação off-line de trabalho consiste de pelo menos dois arquivos: {{FileName|freecad.qhc}} o Qt-helpfile-configuration e {{FileName|freecad.qch}} o Qt-helpfile comprimido. Eles são colocados juntos em um arquivo ZIP.


<div class="mw-translate-fuzzy">

Os arquivos de ajuda podem ser baixados aqui: <https://github.com/FreeCAD/FreeCAD/releases/download/0.18.1/FreeCAD.0_18.Offline.Doc.7z>


</div>

Como opção futura, eles podem ser instalados de dentro do FreeCAD com o [Gerenciador de Extensões](Addon_Manager/pt-br.md).

Os arquivos de ajuda têm sempre os mesmos nomes: {{FileName|freecad.qhc}} e {{FileName|freecad.qch}}. Para ter versões diferentes dos arquivos de ajuda, estes precisam ser instalados em diretórios diferentes. No caso de um download manual, basta armazenar o arquivo zip localmente e extrair o arquivo para o diretório desejado.

## Registro da Documentação 

O sistema de documentação do FreeCAD utiliza o Qt Assistant. Você deve instalar este programa primeiro, se você não o tiver.

A organização real da ajuda offline permite que apenas um arquivo de ajuda esteja ativo. Não é possível, portanto, ter arquivos de ajuda em diferentes idiomas acessíveis a partir do FreeCAD ao mesmo tempo.

A fim de tornar ativa outra documentação do FreeCAD, os seguintes passos devem ser aplicados:

-   Clique dentro do FreeCAD no menu **Ajuda → Ajuda**. O programa Qt-assistant deve abrir.
-   Em Qt-assistant clique no menu **Editar → preferências**.
-   Na janela Preferências Geral clique na aba **Documento**.
-   Na lista de documentação registrada selecione `org.freecad.usermanual` e clique no botão **Remover**.
-   Feche o diálogo com **OK**, mas não feche o Qt-assistant. Isto é importante, pois caso contrário, outro arquivo de ajuda não será registrado.
-   Abra novamente o diálogo de preferências através do menu **Editar → preferências**.
-   Selecione a documentação da aba e clique no botão **Add...**
-   No diálogo, navegue até seu novo arquivo de ajuda e selecione {{FileName|freecad.qch}} feche o diálogo, confirmando sua seleção. Na aba **Documento** nas preferências deve haver agora uma linha com `org.freecad.usermanual`.
-   Feche a aba **Preferências** com **OK**.
-   Agora você deve ter a nova documentação disponível no Qt-assistant, acessível de dentro do FreeCAD.


<div class="mw-translate-fuzzy">

## Uma nota sobre o Ubuntu 

Podem surgir dificuldades ao tentar instalar os pacotes de documentação no Ubuntu (por exemplo, `freecad-doc` ou `freecad-daily-doc`). Se este for o caso, então a execução dos seguintes passos permitirá que você tenha a documentação offline.

-   Baixe os arquivos de ajuda {{FileName|freecad.qhc}} e {{FileName|freecad.qch}} em <https://github.com/FreeCAD/FreeCAD/releases/download/0.18.1/FreeCAD.0_18.Offline.Doc.7z> e extraia-os usando o 7zip.
-   Alternativamente, você pode obter as versões de desenvolvimento dos arquivos de ajuda {{FileName|freecad.qhc}} e {{FileName|freecad.qch}} de [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Doc). Você precisará [concatenar](http://man7.org/linux/man-pages/man1/cat.1.html) os arquivos .part juntos: `cat freecad.qch.part00 freecad.qch.part01 freecad.qch.part02 freecad.qch.part03 > freecad.qch`.
-   Com privilégios administrativos (por exemplo, `sudo`), copiar ou mover {{FileName|freecad.qhc}} e {{FileName|freecad.qch}} para {{FileName|/usr/share/doc/freecad-doc/}}. Se você estiver usando `freecad-daily`, isto será {{FileName|/usr/share/doc/freecad-daily-doc/}}.


</div>

---
[documentation index](../README.md) > Installing Helpfile/pt-br
