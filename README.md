# Simulador do Algoritmo Raft

## Descrição do Projeto
Este projeto implementa uma simulação do algoritmo Raft, um dos principais algoritmos de consenso utilizados em sistemas distribuídos. O Raft é conhecido por sua simplicidade e eficácia, sendo amplamente adotado em ambientes onde vários nós precisam tomar decisões de forma consistente, mesmo diante de falhas.

O simulador simula um ambiente distribuído com múltiplos nós que podem alternar entre três estados: Follower, Candidate, e Leader. Durante a execução, o sistema realiza eleições para escolher um líder, replica logs entre os nós e demonstra como o algoritmo lida com falhas de nós.

## Configuração do Ambiente

### Requisitos do Sistema
Python 3.10 ou superior
Sistemas operacionais suportados: Linux, Windows, MacOS

## Instalação
Clone o repositório:
```bash
git clone https://github.com/seu-usuario/simulador-raft.git
cd simulador-raft
```bash

Execute o programa:
```bash
python main.py
```

## Execução do Algoritmo
Ao executar o simulador, os seguintes eventos ocorrem:

### Inicialização dos Nós
O programa cria 5 nós em um sistema distribuído.
Todos os nós iniciam no estado Follower.

### Eleições de Líder:
Quando um nó não recebe instruções do líder dentro de um intervalo de tempo aleatório (timeout), ele se torna um Candidate e inicia uma eleição.
Cada nó pode votar apenas uma vez por termo.
Se um nó recebe votos da maioria, ele se torna o Leader.

### Replicação de Logs:
O líder replica comandos para todos os outros nós, garantindo consistência entre eles.
Cada entrada replicada é registrada nos logs locais de cada nó.

### Manutenção de Estados:

Nós alternam entre os estados Follower, Candidate e Leader, dependendo das mensagens recebidas e do andamento das eleições.

## Fases do Algoritmo na Implementação
1. Proposição
Um nó candidato solicita votos dos demais, incrementando seu termo atual e votando em si mesmo.
Os nós verificam critérios para conceder votos, como logs atualizados e termos.

2. Votação
Cada nó vota em apenas um candidato por termo.
Se o candidato receber votos da maioria, ele se torna o líder.

3. Replicação
O líder envia comandos para replicar entradas de log nos seguidores.
Os seguidores confirmam as entradas, garantindo consistência.

## Falhas Simuladas

### Falha de Nó
Um nó é removido da rede temporariamente para simular falhas.
O sistema continua funcionando com os nós restantes e realiza novas eleições, caso necessário.
Após um período, o nó recuperado sincroniza seus logs com o líder.

### Timeout (Líder Inativo)
Quando o líder não envia mensagens para os seguidores dentro de um tempo limite, os seguidores iniciam uma nova eleição.
Este mecanismo garante a continuidade do consenso, mesmo que o líder original falhe.

### Latência Artificial
A comunicação entre os nós é atrasada artificialmente para testar o desempenho do sistema.
Mesmo com latência elevada, o algoritmo alcança consenso eventualmente.

## Como Personalizar

### Alterar Número de Nós
Modifique o parâmetro total_nodes em main.py para aumentar ou reduzir o número de nós na rede.

### Simular Mais Falhas
Utilize o método simulate_failure() em election.py para forçar falhas adicionais.

### Adicionar Novos Testes
Crie novos casos de teste na pasta tests/ para validar diferentes cenários.