import argparse
import csv      

def achar_identificador(arquivo):
    with open(arquivo,'r') as agenda:
        identificador = 0
        for linha in agenda:
            identificador+=1
    return(identificador)        

def transcrever(eventos_agenda, arquivo):
    """Transforma o dicionário com os eventos em um arquivo"""
    with open(arquivo, 'w') as agenda: 
         escrever = csv.writer(agenda)  
         for item in eventos_agenda:
             print(eventos_agenda[item])
             if len(eventos_agenda[item])>1:
                 escrever.writerow([item,eventos_agenda[item][1],eventos_agenda[item][2],eventos_agenda[item][3],eventos_agenda[item][4]])
         # Escreve identificador, nome, descrição, data e hora, nessa ordem no arquivo
             
def descobrir_alteracao(nome,descricao,data,hora, evento):
    """Descobre qual foi a alteração solicitada na linha de comando"""
    alteracoes = {}
    if nome is not None:      # Como não sabemos qual foi o argumento opicional utilizado, 
        alteracoes[1] = nome  # descobrimos qual deles possui alguma informação      
    if data is not None:      # Criamos então um dicionário no qual a chave é o índice da lista
        alteracoes[3] = data  # [identificador, nome, descricao, data, hora] em que a alteração será feita
    if descricao is not None:
       alteracoes[2]  = descricao
    if hora is not None:
        alteracoes[4] = hora
    return alteracoes                    

def mostrar_eventos(item):
    """Imprime na tela de forma organizada"""
    evento = "Evento " + str(item[0])
    print(f'{evento} - {item[1]}')
    print(f'Descrição: {item[2]}')
    print(f'Data: {item[3]}')
    print(f'Hora: {item[4]}')

def ler_arquivo(arquivo):
    """Armazena as informações de cada evento em uma lista e todos os eventos(listas) em um dicionário"""
    with open(arquivo, 'r') as agenda:
        leitor = csv.reader(agenda)
        eventos_agenda = {}
        for i,linha in enumerate(leitor):
            eventos_agenda[i+1] = linha                        
    return(eventos_agenda)      

def inicializar(arquivo):
    """Cria um arquivo para a agenda"""
    with open(arquivo, 'w') as agenda:   
        print(f'Uma agenda vazia {arquivo} foi criada!')    
    pass   

def criar(arquivo, nome, descricao,data,hora):
    """ Escreve as informações do evento no arquivo csv"""
    eventos_agenda = ler_arquivo(arquivo)
    identificador = achar_identificador(arquivo)
    identificador = str(identificador + 1)
    eventos_agenda[identificador] = [identificador, nome, descricao, data, hora]   
    transcrever(eventos_agenda, arquivo)
    print(f'Foi adicionado evento {identificador}')    
    
def alterar(arquivo,nome,descricao,data,hora,evento):
    """Altera um evento específico"""
    eventos_agenda = ler_arquivo(arquivo)
    alteracoes = descobrir_alteracao(nome,descricao,data,hora,evento)
    ser_alterado = eventos_agenda[evento] 
    for item in alteracoes:
        i = int(item)
        ser_alterado[i] = alteracoes[item] 
    transcrever(eventos_agenda, arquivo)
    print("Evento alterado com sucesso")
    pass         

def remover(evento,arquivo):
    """Remove evento específico"""
    eventos_agenda = ler_arquivo(arquivo)
    eventos_agenda[evento] = []    
    transcrever(eventos_agenda,arquivo) 
    print("Evento removido com sucesso")
    pass

def listar(arquivo, data):
    """Lista os eventos do dia desejado"""
    agenda = ler_arquivo(arquivo)
    tem_evento = False
    eventos_dia = []
    for item in agenda:
        infos_evento = agenda[item]
        if data in infos_evento:
           tem_evento = True
           eventos_dia.append(infos_evento)
    if tem_evento:       
           print(f'Eventos do dia {data}')
           print('-----------------------------------------------')
           for item in eventos_dia:
               mostrar_eventos(item)
               print('-----------------------------------------------')    
    if not tem_evento:
            print(f'Não existem eventos para o dia {data}!')         

def main():
    parser = argparse.ArgumentParser()   # Aqui usamos o módulo argparse para reconhcer os arguemtos da linha de comando 
    parser.add_argument("-a","--arquivo", help="Nome do arquivo", type=str)
    parser.add_argument("acao", help="O que o programa deve realizar na agenda", type=str)
    parser.add_argument("-n","--nome", help="O nome do evento", type=str)
    parser.add_argument("-D","--descricao", help="Descrição do evento", type=str)
    parser.add_argument("-d","--data", help="Dia do evento", type=str)
    parser.add_argument("-H","--hora",help="Horário do evento", type=str)
    parser.add_argument("-e","--evento",help="Evento já existente", type=int)

    args = parser.parse_args()    # Devemos agora pegar os argumentos para serem usados no programa
    arquivo = args.arquivo
    nome = args.nome
    descricao = args.descricao
    data = args.data
    hora = args.hora
    evento = args.evento
    # Uma tarefa deverá ser executada de acordo com a ação que aparece na linha de comando:
    if args.acao == 'inicializar':
        inicializar(arquivo)
    if args.acao == 'criar':
        criar(arquivo, nome, descricao,data,hora)
    if args.acao == 'alterar':
        alterar(arquivo, nome,descricao,data,hora,evento)
    if args.acao == 'remover':
        remover(evento,arquivo)
    if args.acao == 'listar':
        listar(arquivo, data)                
if __name__ == "__main__":
    main()