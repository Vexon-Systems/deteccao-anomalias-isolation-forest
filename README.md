# Detecção de Anomalias em Logs de Sistema utilizando Isolation Forest

## Objetivo

Aplicar técnicas de Inteligência Artificial para detectar acessos anômalos em logs de sistemas computacionais utilizando o algoritmo Isolation Forest.

## Dataset

O conjunto de dados possui as seguintes variáveis:

- hora_acesso
- duracao_sessao_min
- numero_tentativas_login
- ip_diferente_habitual
- quantidade_paginas_acessadas

## Metodologia

1. Carregamento dos dados;
2. Análise exploratória;
3. Pré-processamento;
4. Aplicação do Isolation Forest;
5. Identificação das anomalias;
6. Geração de gráficos;
7. Interpretação dos resultados.

## Tecnologias

- Python
- Pandas
- Scikit-Learn
- Matplotlib

## Resultados

O modelo identificou aproximadamente 10% dos registros como anômalos.

As principais características foram:

- IP diferente do habitual;
- Sessões longas;
- Horários incomuns;
- Grande quantidade de páginas acessadas;
- Muitas tentativas de login.

## Autor

Felipe Lucas J. Cardoso
