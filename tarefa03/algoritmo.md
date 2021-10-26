Operações elementares: Divisão, laços.
[1] Guarde 0 (variável D);
[2] Receba N números;
[3] Para cada número execute:
[3.1] Equanto o resto da divisão por 2 for 0:
     [3.1.1] Divida por 2;
     [3.1.2] Some 1 na variável D;
[4.1] Equanto o resto da divisão por 3 for 0:
     [4.1.1] Divida por 3;
     [4.1.2] Some 1 na variável D;
[5.1] Equanto o resto da divisão por 5 for 0:
     [5.1.1] Divida por 5;
     [5.1.2] Some 1 na variável D;
[6.1] Equanto o resto da divisão por 7 for 0:
     [6.1.1] Divida por 7;
     [6.1.2] Some 1 na variável D;
[7] Repita o mesmo procedinto com todos os números até que reste apenas 1, tendo assim decomposto o número em divisores primos;
[8] Some a quantidade de números primos usados (caso algum seja usado mais de uma vez, ainda assim some apenas mais 1) e adicione na variável D;
[9] Se D do número atual for maior ou igual ao D do número anterior, guarde-o. Caso contrário, discarte-o e guarde o D anterior;
[10] Mostre o número cujo D ficou guardado ao final;

