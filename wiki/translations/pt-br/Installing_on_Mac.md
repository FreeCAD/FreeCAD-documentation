# Installing on Mac/pt-br





FreeCAD pode ser instalado no MacOS a partir de um pacote .dmg que você pode arrastar e soltar em sua pasta de Aplicações:


{{DownloadMacStable}}

e a construção semanal pode ser baixada de

<img alt="" src=images/Nightly.png  style="width:30px;">[Semanalmente](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)

Você também pode usar um gerenciador de pacotes como o HomeBrew para manter seu software atualizado. Instruções para instalar o HomeBrew podem ser vistas [aqui](https://brew.sh/). Quando o HomeBrew for instalado, você pode simplesmente instalar o FreeCAD 0.18.4 através de seu terminal bash com


```python
brew install --cask freecad
```

e para usar a última versão disponível (0.19pre) no HomeBrew você pode rodar


```python
brew install freecad
```

Se houver algum problema com o HomeBrew Cask ou Fórmula, você pode relatá-lo [aqui](https://github.com/FreeCAD/homebrew-freecad).

Esta página descreve o uso e as características do instalador do FreeCAD. Ela também inclui instruções de desinstalação. Uma vez instalado, você pode [começar a usar!](Getting_started/pt-br.md)

## Instalação simples 

O instalador FreeCAD é fornecido como um pacote de aplicativos (.app) incluído em um arquivo de imagem de disco.

Você pode baixar o instalador mais recente da página [Download](Download.md). Depois de baixar o arquivo, basta montar a imagem do disco, depois arrastá-la para a pasta Aplicações ou para uma pasta de sua escolha.

![](images/mac_installer_1.png )

Basta clicar sobre o aplicativo para iniciar o FreeCAD. Se você tiver esta mensagem \"FreeCAD can\'t be open as it is from unidentified developer.\" Abra a pasta (Aplicações) e clique com o botão direito do mouse sobre a aplicação, depois clique em abrir e aceite para abrir a aplicação.

## Desinstalação

Atualmente não há um desinstalador para FreeCAD instalado com o pacote dmg. Para remover completamente o FreeCAD e todos os componentes instalados, arraste os seguintes arquivos e pastas para o Lixo:

-   Em /Aplicações:
    -   FreeCAD

Se você instalou o FreeCAD com homebrew simplesmente use o comando `brew uninstall freecad`. É isso aí.






