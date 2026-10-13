# Sistema de Plantões Médicos

Repositório de estudos em que desenvolvo uma aplicação baseada na atividade proposta como **API (Aprendizado por Projeto Integrado)** para o 1º semestre do curso de Banco de Dados da FATEC São José dos Campos.

## Objetivo do repositório

Meu objetivo é praticar e aprimorar meus conhecimentos em **Python**, além de desenvolver boas práticas de versionamento com **Git**, especialmente no uso de *branches* e *commits*.

Utilizo este repositório como um laboratório pessoal de desenvolvimento, experimentação e aprendizado.

## Sobre a atividade proposta

A atividade consiste na criação de um programa que auxilia na construção e validação das escalas de plantões médicos de um hospital fictício de médio porte.

Neste primeiro momento, o objetivo é desenvolver um programa capaz de:

- Estabelecer um limite máximo de profissionais por plantão.
- Receber dados numéricos para contabilizar os profissionais disponíveis.
- Gerar um relatório geral com a quantidade de profissionais disponíveis por turno e especialidade.
- Analisar os dados inseridos e identificar plantões que não atendam aos requisitos mínimos de cobertura.
- Informar os motivos da invalidação, especificando os turnos e as especialidades que precisam de revisão.
- Validar os plantões que atendam a todos os requisitos mínimos estabelecidos.
- Tratar erros de entrada de dados de maneira consistente.

## Regras de negócio

O hospital fictício considerado na atividade possui as seguintes regras para a construção dos plantões:

### Turnos e especialidades

O hospital opera em três turnos:

- **Manhã**
- **Tarde**
- **Noite**

Cada turno deve contar com profissionais de três especialidades:

- Clínico Geral
- Pediatra
- Cirurgião

### Cobertura mínima obrigatória

A quantidade mínima de profissionais exigida para cada turno é:

| Especialidade | Quantidade mínima por turno |
|---|---:|
| Clínico Geral | 2 |
| Pediatra | 1 |
| Cirurgião | 1 |

Um plantão que não atenda à cobertura mínima obrigatória **não pode ser publicado**.

### Validação e tratamento de entradas

- Quando um plantão não puder ser publicado, o sistema deve informar os motivos da invalidação, e não apenas indicar que houve um problema.
- Quantidades negativas de profissionais não devem ser aceitas.
- Quantidades excessivamente altas também devem ser identificadas como possíveis erros de digitação.
- A entrada de dados deve ocorrer pelo teclado, considerando que a coordenação do hospital não tem acesso ao código-fonte do programa.

## Propósito do projeto

Este projeto faz parte do meu processo de aprendizado em programação e desenvolvimento de sistemas. Por meio dele, busco consolidar fundamentos de Python, praticar a validação de dados e aprimorar minhas habilidades com Git e GitHub.
