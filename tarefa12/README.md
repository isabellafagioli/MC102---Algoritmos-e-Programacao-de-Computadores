Para que serve?

Agenda.py é um programa para armazenar um evento com base no seu nome, descrição e data.
Com ele é possível criar um arquivo contendo os eventos desejados, além de alterá-los, adicionar, remover e listar.

Como usar?

Cada função deve ser acessada a partir da linha de comando, assim a função “inicializar” cria um arquivo, enquanto que a função “criar” cria um evento a partir das informações também dadas na linha de comando. A função “alterar” seguida de qual evento deve ser mudado e qual a alteração a ser feita, ajusta o evento ao novo detalhe e a função “remover”, seguida do evento, remove toda a informação a respeito dele. Por último, a função “listar” seguida do dia, mostra na tela todos os eventos naquela data e seus respectivos detalhes.
Alguns exemplos do que pode ser escrito na linha de comando e quais ações serão realizadas por ela:

- Primeiramente qualquer que seja a ação desejada devemos inciar com:

	python3 agenda.py -a  XXXXXX.csv

-A partir desse comando, se digitarmos:

	- inicializar: automaticamente será criado um arquivo XXXXXX.csv

	- criar --nome "XX" --descricao "XX" --data "XX/XX/XXXX" --hora "XX:XX" : Deve ser seguido dos argumentos apresentados que são os detalhes do evento e a partir desse comando, será escrito esse evento no arquivo.

	- alterar --evento X –xxx “XXXX”: Deve ser seguido do número do evento sobre o qual será feita a alteração, assim como também da alteração desejada (seja o nome, a descrição, a data ou a hora) e assim a informação antiga será substituída pela escrita na linha de comando.

	- remover –evento X: Remove o evento desejado, sendo X seu respectivo número.

	- listar –data “XX/XX/XXXX”: Mostrará todos os eventos na data pedida. Caso não haja nenhum mostrará uma mensagem dizendo não ter nada naquele dia.
 
Detalhes do arquivo e do programa:

A estrutura do arquivo CSV é feita por cada coluna representando um detalhe do evento (identificador, nome, descrição, data e hora, nessa ordem). Os separadores utilizados são as vírgulas.

Ao ler o arquivo, o programa armazena os dados em um dicionário, no qual as chaves são os identificadors e os valores respectivos são uma lista com os detalhes do evento, conforme escritos por quem manipula o programa, e depois a partir dele reescreve (ou cria um novo) o evento com todas as alterações necessárias.
