# sistema_de_plantoes_medicos
Repositório de estudo onde desenvolvo uma aplicação baseada na atividade proposta como API para o 1º semestre do curso de Banco de Dados da Fatec de São José dos Campos.

Meu objetivo com este repositório é praticar e aprimorar meus conhecimentos e habilidades de desenvolvimento em Python e aprimorar técnicas e rotinas de Branching e Commits no Git. Uso este espaço como laboratório pessoal de desenvolvimento.

Sobre a atividade proposta:
A atividade se baseia na criação de um programa que auxilia na construção e validação de plantões médicos de um hospital fictício de médio porte.

Neste primeiro momento o objetivo é criar um programa que: 
  -Seja capaz de estipular um limite máximo de profissionais por plantão
  -Permita a entrada de dados numéricos de forma a contabilizar os profissionais disponíveis para o plantão
  -Seja capaz de analisar os dados inseridos e retornar um relatório geral da quantidade de profissionais disponíveis por turno e especialidade
  -Seja capaz de analisar os dados inseridos e retornar uma mensagem que invalida o plantão caso as necessidades mínimas de validação não sejam atendidas e especificar quais especialidades e turnos carecem de revisão
  -Seja capaz de analisar os dados inseridos e retornar uma mensagem que valida o plantão caso as necessidades mínimas de validação sejam atendidas
  -Seja capaz de tratar os erros de inserção de dados de forma consistente 

O hospital fictício em questão possui as seguintes regras para criação dos plantões:
  -O hospital trabalha com três turnos: MANHÃ, TARDE e NOITE. 
  -Cada plantão é composto por profissionais de três especialidades: Clínico Geral, Pediatra e Cirurgião. 
  -Cada turno tem a seguinte cobertura mínima obrigatória: 2 Clínicos Gerais, 1 Pediatra e 1 Cirurgião. 
  -Um plantão que não atenda à cobertura mínima não pode ser publicado. 
  -Quando um plantão não pode ser publicado, a coordenação precisa saber o motivo, e não apenas 
que houve um problema. 
  -Quantidades negativas de profissionais são impossíveis e não devem ser aceitas. 
  -Quantidades absurdamente altas também indicam erro de digitação. 
  -A coordenação opera o sistema pelo teclado e não tem acesso ao código. 
