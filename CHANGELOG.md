# Changelog
Todas as mudanças notáveis ​​neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e este projeto adota o [Versionamento Semântico](https://semver.org/spec/v2.0.0.html).


##### Tags:
* `Added` para novos recursos.
* `Changed` para alterações na funcionalidade existente.
* `Deprecated` para recursos que serão removidos em breve.
* `Removed` por agora removido recursos.
* `Fixed` para qualquer correção de bugs.
* `Security` em caso de vulnerabilidades.


## [0.1.2] - 2019-08-16
### FIxed
* Erro no arquivo .whl (arquivo faltando por ter extensão .pyw).
* Erro ao invocar módulo como script (sintaxe error).


## [0.1.1] - 2019-08-14
### Added
* Script __ main__.py para módulo se comportar como script.
* CHANGELOG.md .
* _ version.py contendo versão do pacote e metadados sobre o pacote
* Docstrings aos scripts próprios deste pacote.


### Changed
* KLplus.py renomeado para klplus.py, para diferenciar pacote do módulo.
* Extensão de klplus para .pyw para executá-lo sem CLI visível.
* Versão dos pacotes em requirements.txt e requirements_dev.txt definidos (congelados).
* Configuração e designer do setup.py .
* README.md documentado do zero.
* Adicionado suporte apenas à Python >= 3.6 .

### Fixed
* Erro ao importar pyxhook em klplus.py (foi necessário importar do diretório pai).
* Erro do setup.py ao ler README em formato .md

## [0.1.0] - 2019-08-11
### Added
* Script KLplus.py (core).
* Script [pyxhook.py](https://github.com/JeffHoogland/pyxhook) como módulo interno.
* Licença GPLv2.
* Arquivo setup.py para instalação via `pip install setup.py`.
* Pacote em https://pypi.org/project/KLplus/ .
* README.md.
* Arquivo .gitignore.
* Arquivo requirements.txt e requirements_dev.txt .

[0.1.2]: https://github.com/danbros/KLplus/releases/tag/v0.1.2
[0.1.1]: https://github.com/danbros/KLplus/releases/tag/v0.1.1
[0.1.0]: https://github.com/danbros/KLplus/releases/tag/v0.1.0
