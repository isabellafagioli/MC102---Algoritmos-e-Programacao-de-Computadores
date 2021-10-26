Instruções elementares permitidas e utilizadas no algoritmo: operações matemáticas(soma, subtração)
e desvios condicionais

(1) Pergunte a data de início em formato dia/mês/ano;
(2) Pergunte a quantidade de dias a ser somado e acrescente no "dia";
(3) Se mês for igual a 1, 3, 5, 7, 8, 10, 12:
  (3.1) Se dia for maior que 31:
    (3.1.1) Execute dia - 31;
    (3.1.2) Some 1 mês;
(4) Se mês for igual a 4, 6, 9, 11:
  (4.1) Se dia for maior que 30:
    (4.1.1) Execute dia - 30;
    (4.1.2) Some 1 mês; 
(5) Se mês for igual a 2:
  (5.1)Se ano for divisível por 400 ou for divisível por 4 e não por 100:
  (5.1.1) Se dia for maior que 29:
    (5.1.1.1) Execute dia - 29;
    (5.1.1.2) Some 1 mês;
  (5.2) Se não:
    (5.2.1) Execute dia - 28;
    (5.2.2) Some 1 mês;
(6) Se mês for maior que 12:
  (6.1) Execute mês - 12;
  (6.2) Some 1 ano








