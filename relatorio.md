Detecção de Anomalias em Logs de Sistema utilizando Isolation Forest
1. Introdução

A detecção de anomalias é uma técnica amplamente utilizada em sistemas computacionais para identificar comportamentos fora do padrão. Em ambientes de segurança, essa abordagem auxilia na identificação de acessos suspeitos, tentativas de invasão e outras atividades potencialmente maliciosas.

Neste trabalho foi utilizado o algoritmo Isolation Forest para identificar acessos anômalos em um conjunto de logs de sistema.

2. Descrição da Abordagem

Inicialmente foi realizado o carregamento do dataset contendo informações sobre os acessos ao sistema.

As variáveis analisadas foram:

hora de acesso;
duração da sessão;
número de tentativas de login;
utilização de IP diferente do habitual;
quantidade de páginas acessadas.

Após a exploração dos dados, realizou-se a padronização das variáveis utilizando StandardScaler.

Posteriormente foi treinado um modelo Isolation Forest, configurado com taxa de contaminação de 10%, responsável por identificar registros potencialmente anômalos.

Por fim, foram geradas visualizações para facilitar a interpretação dos resultados.

3. Interpretação dos Resultados

O modelo classificou aproximadamente 10% dos registros como anômalos.

As principais características observadas nesses acessos foram:

utilização de IP diferente do habitual;
horários incomuns;
sessões muito longas;
elevado número de páginas acessadas;
grande quantidade de tentativas de login.

Esses fatores indicam comportamentos significativamente diferentes da maioria dos acessos registrados.

Respostas às Questões
1. Quais padrões de acesso foram considerados normais pelo modelo?

O modelo considerou normais os acessos realizados em horários habituais, com duração moderada, poucas tentativas de login, utilização de IP conhecido e quantidade moderada de páginas acessadas.

2. Quais características aparecem com maior frequência nos acessos classificados como anômalos?

As características mais frequentes foram:

IP diferente do habitual;
horários noturnos;
sessões longas;
elevado número de páginas acessadas;
muitas tentativas de login.
3. Todas as anomalias identificadas representam um possível problema de segurança? Justifique.

Não.

Uma anomalia representa apenas um comportamento fora do padrão. Existem situações legítimas, como acesso em viagem, trabalho remoto, uso de um novo dispositivo ou esquecimento da senha, que podem gerar comportamentos considerados anômalos sem indicar um ataque.

Assim, as anomalias devem ser analisadas antes da tomada de decisão.

4. Que tipos de falso positivo podem ocorrer nesse cenário?

Os principais falsos positivos podem ocorrer em situações como:

acesso em viagens;
trabalho fora do horário habitual;
utilização de novos dispositivos;
sessões longas por necessidade profissional;
múltiplas tentativas de login devido ao esquecimento da senha.

Esses eventos podem ser classificados como anomalias sem representar ameaças reais.

5. Como esse tipo de modelo poderia ser usado em um sistema real de monitoramento?

O Isolation Forest pode ser integrado a sistemas de monitoramento em tempo real.

Cada novo acesso seria analisado automaticamente, recebendo um nível de risco. Eventos suspeitos poderiam gerar alertas para a equipe de segurança, reduzindo o tempo de resposta e auxiliando na prevenção de incidentes.

Conclusão

O algoritmo Isolation Forest mostrou-se eficiente na identificação de padrões incomuns de acesso em logs de sistema. Os resultados indicaram que fatores como IP diferente do habitual, sessões longas, horários incomuns e grande quantidade de páginas acessadas contribuem para a classificação de anomalias.

Entretanto, nem toda anomalia representa um ataque, sendo necessária a análise do contexto antes da tomada de decisões. Em sistemas reais, essa técnica pode atuar como uma importante ferramenta de apoio ao monitoramento e à segurança da informação.
