def inserir_conceitos_e_frequencia():
   """entrada dos dados utilizados"""
   tarefas = input().split()
   lista_frequencia = []
   while True:
        try:
          estava_presente = input()  
          lista_frequencia.append(estava_presente)
        except EOFError:
            break 
   conceitos_e_frequencia = (tarefas, lista_frequencia)
   return conceitos_e_frequencia

def tarefa_aprovada(lista):
    """define se todas as tarefas obtiveram ao menos um C"""
    k = 0
    quantidade_tarefas = len(lista)/2
    while k < quantidade_tarefas:
        indice_impar = 2*k + 1
        if lista[indice_impar] == "D":    
             return 0
        k+=1     
    return 1     
    """como os conceitos da tarefa estão nos índices ímpares da lista, analisam-se estes"""     
def presenca_aprovada(lista):
    """define se a frequência obtida foi maior ou igual a 75%"""
    presente = 0
    i = 0
    while i < len(lista):
        if lista[i] == "presente":
            presente+=1
        i+=1    
    frequencia = float(presente/len(lista)) 
    if frequencia >= 0.75:
        return 1   
    return 0 
def aprovacao():
    """define se o aluno foi aprovado nos dois conceitos"""
    definicoes = inserir_conceitos_e_frequencia()
    tarefas = definicoes[0]
    lista_frequencia = definicoes[1]
    avaliar_tarefas = tarefa_aprovada(tarefas)
    avaliar_frequencia = presenca_aprovada(lista_frequencia)
    if avaliar_tarefas == 1 and avaliar_frequencia == 1 :
         return 1
    return 0    
def main():
    foi_aprovado = aprovacao()
    if foi_aprovado == 1:
       print("Aprovadx")
    elif foi_aprovado == 0:
       print("Reprovadx")   
main()