# Sistema de Apoio às Escalas Médicas

## Introdução

O **Sistema de Apoio às Escalas Médicas** é uma aplicação desenvolvida
em Python com o objetivo de auxiliar no cadastro de profissionais da
saúde, na organização de equipes e na construção e validação de escalas
médicas.

O projeto foi concebido baseando-se no contexto de uma atividade de **API
(Aprendizado por Projeto Integrado)**, proposta acadêmica da Fatec São José 
dos Campos que busca aproximar os conhecimentos desenvolvidos durante o curso 
da resolução de problemas reais por meio de um projeto prático. O desafio que 
contextualiza este projeto é baseado na atividade proposta ao 1º semestre do 
curso de Banco de Dados iniciado no segundo semestre de 2026.

Este repositório representa um **desenvolvimento independente**, realizado 
com o propósito de aprofundar meus estudos em programação, praticar conceitos 
de desenvolvimento de software e construir meu portfólio pessoal na área de
Tecnologia da Informação.

A versão atual foi desenvolvida em Python, com foco na organização dos
dados, aplicação de regras de negócio e validação das escalas. O projeto
também foi estruturado considerando uma futura integração com um banco
de dados relacional.

## Funcionalidades do programa

### 1. Cadastro de profissionais

A funcionalidade de cadastro permite registrar médicos no sistema,
armazenando informações como nome, especialidade e disponibilidade para
os turnos da manhã, tarde e noite.

O desenvolvimento utiliza **Programação Orientada a Objetos (POO)**, por
meio de uma classe responsável por representar cada profissional e
organizar seus atributos.

Nesta etapa, os objetos são armazenados em uma **lista de tamanho fixo,
com capacidade para até 140 profissionais cadastrados simultaneamente**.
Cada posição da lista corresponde a um identificador, permitindo
localizar os registros diretamente. Quando um profissional é excluído,
sua posição fica disponível para um novo cadastro.

### 2. Consulta de profissionais

A consulta permite visualizar os profissionais cadastrados e suas
respectivas informações, facilitando a identificação por número
identificador, nome, especialidade e disponibilidade.

A funcionalidade também auxilia na conferência da quantidade de turnos
atribuídos aos profissionais, oferecendo uma visão organizada dos dados
utilizados na construção das escalas.

### 3. Construção de escalas

A construção de escalas permite selecionar os profissionais que serão
alocados em cada turno, considerando suas especialidades,
disponibilidades e as regras estabelecidas pelo sistema.

A montagem pode ser realizada de maneira direcionada: é possível
escolher um **dia específico da semana e um turno específico** para
construir ou complementar a escala, sem precisar trabalhar
necessariamente com todos os períodos de uma só vez.

O sistema utiliza uma estrutura matricial para organizar os dias da
semana e os turnos, mantendo os identificadores dos profissionais
alocados em cada período.

### 4. Validação diária

A validação diária verifica se a composição de cada turno atende aos
requisitos mínimos definidos para a equipe médica.

Os parâmetros de cobertura adotados são:

-   **2 médicos clínicos gerais** por turno;
-   **1 pediatra** por turno;
-   **1 cirurgião** por turno.

A partir desses critérios, o sistema identifica quais especialidades
estão abaixo da quantidade mínima exigida e informa as pendências
encontradas. Dessa forma, é possível avaliar a cobertura de um turno
antes de considerá-lo adequado.

### 5. Validações semanais

As validações semanais analisam a distribuição das escalas ao longo dos
sete dias da semana. O objetivo é verificar não apenas a cobertura dos
turnos, mas também se a distribuição respeita as regras de escalação
definidas para cada profissional.

As principais verificações são:

-   **Limite diário de escalas:** um profissional não pode receber mais
    de dois turnos no mesmo dia.
-   **Limite semanal de escalas:** um profissional não pode ultrapassar
    oito turnos ao longo da semana.
-   **Intervalo entre turnos noturnos e matutinos:** o sistema verifica
    a sequência entre dias consecutivos para impedir a combinação de um
    turno noturno com um turno matutino no dia imediatamente adjacente,
    conforme a regra estabelecida para a escala.
-   **Disponibilidade declarada:** o profissional só pode ser escalado
    em turnos para os quais informou disponibilidade no cadastro.
-   **Existência do profissional:** a escala deve referenciar um
    profissional efetivamente cadastrado.
-   **Cobertura por especialidade:** cada turno deve atender aos
    quantitativos mínimos de clínicos gerais, pediatras e cirurgiões.

Ao final, o sistema apresenta as pendências identificadas, permitindo
revisar a escala e realizar os ajustes necessários. A análise semanal
também permite acompanhar a quantidade de turnos cobertos e aqueles que
ainda não atendem aos requisitos de cobertura.

## Uso de Inteligência Artificial

Durante o desenvolvimento, utilizei o ChatGPT como ferramenta de apoio
ao aprendizado e à resolução de dúvidas relacionadas à programação em
Python.

A colaboração foi orientada por um combinado que guiou nossas
interações: **"Direcionamento sem entregar a resposta pronta".**

Na prática, isso significa que a IA foi utilizada principalmente para
explicar conceitos, apontar possíveis problemas na lógica, questionar
decisões de implementação e sugerir caminhos para investigação. Em vez
de simplesmente receber soluções completas, procurei desenvolver o
raciocínio necessário para implementar e corrigir cada funcionalidade
por conta própria.

Essa abordagem contribuiu para exercitar a autonomia, a interpretação de
erros e a capacidade de estruturar soluções, mantendo o aprendizado como
parte central do processo de desenvolvimento.

## Próximos passos

O projeto continuará evoluindo com as seguintes etapas:

1.  **Criação de um banco de dados relacional:** modelar e implementar
    uma estrutura de banco de dados para armazenar os profissionais,
    suas disponibilidades e as informações relacionadas às escalas.
2.  **Integração do banco de dados com a aplicação atual:** adaptar o
    sistema para realizar operações de cadastro, consulta, atualização e
    exclusão utilizando o banco de dados.
3.  **Correções e adaptações do código atual:** revisar a implementação
    existente, aprimorar a organização do código e adequar as
    funcionalidades à nova estrutura de persistência de dados.

Essas etapas permitirão evoluir a aplicação de uma versão baseada em
estruturas de dados mantidas em memória para uma solução com
armazenamento persistente e maior possibilidade de expansão.

## Considerações finais

O desenvolvimento do Sistema de Apoio às Escalas Médicas representa uma
oportunidade de aplicar, de forma prática, os conhecimentos adquiridos
em programação e organização de dados. Ao longo do projeto, foram
trabalhados conceitos como Programação Orientada a Objetos, estruturas
de dados, listas, matrizes, funções, validações e regras de negócio.

Mais do que concluir uma aplicação funcional, o objetivo é construir uma
base sólida de aprendizado, compreender as decisões envolvidas no
desenvolvimento de software e evoluir gradualmente a solução.

A próxima fase, com a criação e integração de um banco de dados
relacional, será um passo importante nessa evolução. Este repositório
documenta esse processo e continuará sendo atualizado conforme novas
funcionalidades, melhorias e conhecimentos forem incorporados.