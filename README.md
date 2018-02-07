# xmltocsv

Converte arquivos XML no padrão "http://rddl.xmlinside.net/PowerMeasurement/data" para csv. Passo a passo:

1. Baixe ou clone este projeto
1. Instale a versão mais nova do Python 3.x. 
1. Execute o comando `python3 main.py [NOME DO ARQUIVO XML 1] [NOME DO ARQUIVO XML 2] ...`
1. Accese os arquivos CSV (com o mesmo nome do correspondente XML na raiz do projeto

## Observações

1. O arquivo XML deve estar dentro da pasta do projeto, ou ser passado com o caminho relativo. Nesse caso o CSV será criado na mesma pasta onde o XML se encontra
1. O Header é montado através das Labels de cada canal.
1. Canais ausentes são substituídos pelo campo vazio. 
