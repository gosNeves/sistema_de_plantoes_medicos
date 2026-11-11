class Medico:
    def __init__(self, id_med, nome, espec, disp_m, disp_t, disp_n):
        self.id = id_med
        self.nome = nome
        self.espec = espec
        self.disp_m = disp_m
        self.disp_t = disp_t
        self.disp_n = disp_n
        self.qtd_t = [0] * 7
def menu():
    medicos = [None] * 140
    semana = []
    for i in range(7):
        semana.append([[],[],[]])
    while True: 
        print("=== Menu Principal ===")
        print("=== Escolha uma opção ===")
        try:
            opcao = int(input("(1) => Cadastro, (2) => Consulta, (3) => Construção de Escalas, (4) => Menu de Validações, (5) => Encerrar Programa"))
        except ValueError:
            print("Valor Inválido")
            continue
        if opcao == 1:
            cadastro(medicos)
        elif opcao == 2:
            consulta(medicos)
        elif opcao == 3:
            construção(medicos,semana)
        elif opcao == 4:
            validacao(medicos,semana)
        elif opcao == 5:
            print("Encerrando Programa")
            break
        else: 
            print("Opção Inválida")
def cadastro(lista):
    print("=== Menu de Cadastros ===")
    while True:
        opcao = input("(1) => Cadastrar médicos, (2) => Excluir cadastros, (3) => Sair")
        continuar = True
        if opcao == "1": 
            print("=== Cadastramento ===")
            while continuar:
                for i in range(len(lista)):
                    if lista[i] is None:
                        nome_med = input("Digite o nome do médico:")
                        print("Qual a especialidade do médico?")
                        while True:
                            espec_med = input("(1) => Clínico Geral, (2) => Pediatra, (3) => Cirurgião")
                            if espec_med in ("1", "2", "3"):
                                break
                            else:
                                print("Valor inválido")
                                continue
                        print("Ele tem disponibilidade para escalas no período da MANHÃ?")
                        while True:
                            disp_m = input("(1) => Sim, (2) => Não")
                            if disp_m in ("1", "2"):
                                break
                            else:
                                print("Valor inválido")
                                continue
                        print("Ele tem disponibilidade para escalas no período da TARDE?")
                        while True:
                            disp_t = input("(1) => Sim, (2) => Não")
                            if disp_t in ("1", "2"):
                                break
                            else:
                                print("Valor inválido")
                                continue
                        print("Ele tem disponibilidade para escalas no período da NOITE?")
                        while True:
                            disp_n = input("(1) => Sim, (2) => Não")
                            if disp_n in ("1", "2"):
                                break
                            else:
                                print("Valor inválido")
                                continue
                        ident = i + 1
                        medico = Medico(ident, nome_med, espec_med, disp_m, disp_t, disp_n)
                        lista[i] = medico
                        break
                else:
                    print("Não há espaços livres para novos cadastros")
                    break
                print("Deseja cadastrar outro Médico?")
                while True:
                    opcao = input("Digite '1' para SIM e '2' para NÃO:").capitalize()
                    if opcao == "1":
                        break
                    elif opcao == "2":
                        continuar = False
                        break
                    else:
                        print("Opção inválida, digite apenas '1' para SIM ou '2' para NÃO!")
                        continue
        elif opcao == "2":
            print("Exclusão de cadastros")
            while continuar: 
                try:
                    opcao = int(input("Digite o ID do cadastro que você quer excluir:"))
                    i = opcao - 1
                except ValueError:
                    print("Valor inválido!")
                    continue
                if i in range(len(lista)):
                    if lista[i] is None:
                        print("Não existe um cadastro nesta posição")
                    elif lista [i] is not None:
                        lista[i] = None
                        print("Cadastro excluído com sucesso")
                else:
                    print("Valor inválido")
                print("Deseja excluir outro cadastro?")
                while True:
                    opcao = input("Digite '1' para SIM e '2' para NÃO:").capitalize()
                    if opcao == "1":
                        break
                    elif opcao == "2":
                        continuar = False
                        break
                    else:
                        print("Opção inválida, digite apenas '1' para SIM ou '2' para NÃO!")
                        continue
        elif opcao == "3":
            print("Retornando ao menu principal")
            break
        else:
            print("Opção inválida!")
    return lista
def consulta(lista):
    especialidades = {"1":"Clínico Geral", "2":"Pediatra", "3":"Cirurgião"}
    disponibilidade = {"1":"Sim", "2":"Não"}
    while True:
        try:
            opcao = int(input("Digite o ID que você quer consultar:"))
            break
        except ValueError:
            print("Valor Inválido")
            continue
    i = opcao - 1
    if i in range(len(lista)):
        if lista[i] is None:
            print("Não há cadastros nesta posição")
        else:
            print(f"ID => {lista[i].id}")
            print(f"Nome => {lista[i].nome}")
            print(f"Especialidade => {especialidades[lista[i].espec]}")
            print(f"Disponível de MANHÃ? => {disponibilidade[lista[i].disp_m]}")
            print(f"Disponível de TARDE? => {disponibilidade[lista[i].disp_t]}")
            print(f"Disponível de NOITE? => {disponibilidade[lista[i].disp_n]}")
    else:
        print("Valor Inválido")
def construção(lista, matriz):
    print("=== Menu de Construção de Turnos ===")
    while True:
        try:
            opcao = int(input("(1) => Construir Escalas, (2) => Sair"))
        except ValueError:
            print("Valor inválido")
            continue
        if opcao == 1:
            if any(medico is not None in lista for medico in lista):
                while True:
                    print("Escolha um dia da semana:")
                    try:
                        opcao_d = int(input("(1) => Domingo, (2) => Segunda, (3) => Terça, (4) => Quarta, (5) => Quinta, (6) => Sexta, (7) => Sábado"))
                    except ValueError:
                        print("Opção inválida")
                        continue
                    print("Escolha um turno:")
                    try:
                        opcao_t = int(input("(1) => Manhã, (2) => Tarde, (3) => Noite"))
                    except ValueError:
                        print("Opção inválida")
                        continue
                    x = opcao_d - 1
                    y = opcao_t - 1
                    atualizacao(x,y,lista,matriz,operacao=-1)
                    cadastro_escala(x,y,lista,matriz)
                    break
            else:
                print("Não há cadastros no sistema. Cadastre pelo menos um médico para prosseguir!")
        elif opcao == 2:
            print("=== Retornando ao menu principal ===")
            break
        else: 
            print("Opção inválida")
            continue
def cadastro_escala(x,y,lista,matriz):
    dias = {0:"Domingo", 1:"Segunda", 2:"Terça", 3:"Quarta", 4:"Quinta", 5:"Sexta", 6:"Sábado"}
    turnos = {0:"Manhã", 1:"Tarde", 2:"Noite"}
    erros_dict = {1:"Erro! Limite diário de escalas excedido.", 2:"Erro! O profissional já está escalado no turno noturno anterior",
             3:"Erro! O profissional já está escalado no turno matutino posterior.", 4:"Erro! Limite semanal de escalas excedido"}
    print(f"Você está no turno de {dias[x]} no período da {turnos[y]}")
    continuar = True
    while continuar:
        if any(medico.espec == "1" and medico.disp_m == "1" for medico in lista if medico is not None):
            print("Você tem a disposição os seguintes CLÍNICOS GERAIS:")
            cont = 0
            for i in range(len(lista)):  
                if lista[i] is None:
                    continue
                elif lista[i].disp_m == "1" and lista[i].espec == "1":
                    ident = i + 1
                    cont = cont + 1
                    print(f"Profissional nº{cont}:\nID => {ident}\nNome => {lista[i].nome}")
            while True:
                try:
                    id_med = int(input("Digite um ID"))
                except ValueError:
                    print("Valor inválido!")
                    continue
                if id_med > 0 and id_med < 141:
                    erros = checagens(lista,matriz,x,y,id_med)
                    if not erros:
                        matriz[x][y].append(id_med)
                        atualizacao(x,y,lista,matriz,operacao=1)
                        break
                    else:
                        for i in erros:
                            print(erros_dict[i])
                else: 
                    print("Valor Inválido")
            print("Deseja cadastrar outro CLÍNICO GERAL?")
            while True:
                opcao = input("Digite '1' para SIM e '2' para NÃO:")
                if opcao == "1":
                    break
                elif opcao == "2":
                    continuar = False
                    break
                else:
                    print("Opção inválida, digite apenas '1' para SIM ou '2' para NÃO!")
                    continue
        else:
            print(f"Você não possui Clínicos Gerais disponíveis no período da {turnos[y]}")
            break
    continuar = True
    while continuar:
        if any(medico.espec == "2" and medico.disp_m == "1" for medico in lista if medico is not None):
            print("Você tem a disposição os seguintes PEDIATRAS:")
            cont = 0
            for i in range(len(lista)):  
                if lista[i] is None:
                    continue
                elif lista[i].disp_m == "1" and lista[i].espec == "2":
                    ident = i + 1
                    print(f"Profissional nº{cont}:\nID => {ident}\nNome => {lista[i].nome}")
            while True:
                try:
                    id_med = int(input("Digite um ID"))
                except ValueError:
                    print("Valor inválido!")
                    continue
                if id_med > 0 and id_med < 141:
                    erros = checagens(lista,matriz,x,y,id_med)
                    if not erros:
                        matriz[x][y].append(id_med)
                        atualizacao(x,y,lista,matriz,operacao=1)
                        break
                    else:
                        for i in erros:
                            print(erros_dict[i])
                else: 
                    print("Valor Inválido")
            print("Deseja cadastrar outro PEDIATRA?")
            while True:
                opcao = input("Digite '1' para SIM e '2' para NÃO:")
                if opcao == "1":
                    break
                elif opcao == "2":
                    continuar = False
                    break
                else:
                    print("Opção inválida, digite apenas '1' para SIM ou '2' para NÃO!")
                    continue
        else:
            print(f"Você não possui Pediatras disponíveis no período da {turnos[y]}")
            break
    continuar = True
    while continuar:
        if any(medico.espec == "3" and medico.disp_m == "1" for medico in lista if medico is not None):
            print("Você tem a disposição os seguintes CIRURGIÕES:")
            cont = 0
            for i in range(len(lista)):  
                if lista[i] is None:
                    continue
                elif lista[i].disp_m == "1" and lista[i].espec == "3":
                    ident = i + 1
                    cont = cont + 1
                    print(f"Profissional nº{cont}:\nID => {ident}\nNome => {lista[i].nome}")
            while True:
                try:
                    id_med = int(input("Digite um ID"))
                except ValueError:
                    print("Valor inválido!")
                    continue
                if id_med > 0 and id_med < 141:
                    erros = checagens(lista,matriz,x,y,id_med)
                    if not erros:
                        matriz[x][y].append(id_med)
                        atualizacao(x,y,lista,matriz,operacao=1)
                        break
                    else:
                        for i in erros:
                            print(erros_dict[i])
                else: 
                    print("Valor Inválido")
            print("Deseja cadastrar outro CIRURGIÃO?")
            while True:
                opcao = input("Digite '1' para SIM e '2' para NÃO:")
                if opcao == "1":
                    break
                elif opcao == "2":
                    continuar = False
                    break
                else:
                    print("Opção inválida, digite apenas '1' para SIM ou '2' para NÃO!")
                    continue
        else:
            print(f"Você não possui Cirurgiões disponíveis no período da {turnos[y]}")
            break
    print("Escala Salva! Retornando ao menu de Construção de Escalas")
    return matriz
def checagens(lista,matriz,x,y,id_med):
    erros = [] 
    prox_dia = (x+1)%7
    dia_ant = (6+x)%7
    total_semana = sum(lista[id_med-1].qtd_t)
    #1 No máximo 2 turnos no mesmo dia
    if lista[id_med-1].qtd_t[x] >= 2:
        erros.append(1)        
    #2 Turno noturno não pode ser seguido de matutino e vice-versa
    if y == 0: 
        if id_med in matriz[dia_ant][2] and id_med in matriz[x][0]:
            erros.append(2)
    elif y == 2:
        if id_med in matriz[x][2] and id_med in matriz[prox_dia][0]:
            erros.append(3)
    #3 Máximo de 8 turnos na semana
    if total_semana >= 8:
        erros.append(4)
    return erros
def atualizacao(x,y,lista,matriz,operacao):
    for id in matriz[x][y]:
        lista[id-1].qtd_t[x] += operacao
def validacao(lista,matriz):
    while True: 
        print("=== Menu de Validações ===")
        print("=== Escolha uma opção ===")
        try:
            opcao = int(input("(1) => Validação Diária, (2) => Validação Semanal, (3) => Sair"))
        except ValueError:
            print("Valor Inválido")
            continue
        if opcao == 1:
            validacao_diaria(lista,matriz)
        elif opcao == 2:
            validacao_semanal(lista,matriz)
        elif opcao == 3:
            print("Retornando ao Menu Principal")
            break
        else: 
            print("Opção Inválida") 
def validacao_diaria(lista,matriz):
    dias = {0:"Domingo", 1:"Segunda", 2:"Terça", 3:"Quarta", 4:"Quinta", 5:"Sexta", 6:"Sábado"}
    turnos = {0:"Manhã", 1:"Tarde", 2:"Noite"}
    erros_dict = {0:"Turno Aprovado", 1:"Erro! Faltam Clinicos Gerais", 2:"Erro! Faltam Pediatras", 3:"Erro! Faltam Cirurgiões", 4:"Plantão 24 Hrs Aprovado!"}
    espec_dict = {0:"Clínicos Gerais", 1:"Pediatras", 2:"Cirurgiões"}
    erros =[]
    while True: 
        print("=== Validações de Escalas ===")
        print("=== Escolha um dia ===")
        try:
            x = int(input("(1) => Domingo, (2) => Segunda, (3) => Terça, (4) => Quarta, (5) => Quinta, (6) => Sexta, (7) => Sábado"))
        except ValueError:
            print("Valor Inválido")
            continue
        print("=== Qual turno você deseja validar? ===")
        try:
            y = int(input("(1) => Manhã, (2) => Tarde, (3) => Noite, (4) => Plantão 24 Hrs (3 Turnos Juntos)"))
        except ValueError:
            print("Valor Inválido")
            continue
        x = x-1
        y = y-1
        if y == 3:
            #Validação do Plantão 24 Hrs
            turno_M = contagem_espec(x,0,lista,matriz)
            turno_T = contagem_espec(x,1,lista,matriz)
            turno_N = contagem_espec(x,2,lista,matriz)
            turnos_dia = [turno_M,turno_T,turno_N]
            cl =[]
            p =[]
            c=[]
            for i in range(len(turnos_dia)):
                print(f"\nTurno da {turnos[i]}")
                if all(j == 0 for j in turnos_dia[i]):
                    print("O turno não possui profissionais cadastrados")
                else:
                    for espec in range(len(turnos_dia[i])):
                        print(f"Você possui {turnos_dia[i][espec]} {espec_dict[espec]} cadastrados")
            for turno in turnos_dia:
                cl.append(max(0, 2-turno[0]))
                p.append(max(0, 1-turno[1]))
                c.append(max(0, 1-turno[2]))
            if any(cl) or any(p) or any(c): 
                for n in range(3):
                    if cl[n] > 0:
                        print(f"Erro! Faltam {cl[n]} Clínicos Gerais no turno da {turnos[n]}")
                    if p[n] > 0:
                        print(f"Erro! Faltam {p[n]} Pediatras no turno da {turnos[n]}")
                    if c[n] > 0:
                        print(f"Erro! Faltam {c[n]} Cirurgiões no turno da {turnos[n]}")
            else:
                print(erros_dict[4])          
            break
        elif y in turnos:
            #Validação do turno específico e impressão de relatórios
            print(f"Você selecionou o turno de {dias[x]} de {turnos[y]}")
            espec_quant = contagem_espec(x,y,lista,matriz)
            if espec_quant[0] < 2:
                erros.append(1)
            if espec_quant[1] < 1:
                erros.append(2)
            if espec_quant[2] < 1:
                erros.append(3)
            if not erros:
                erros.append(0)
            print(f"Você possui {espec_quant[0]} Clínicos Gerais cadastrados")
            print(f"Você possui {espec_quant[1]} Pediatras cadastrados")
            print(f"Você possui {espec_quant[2]} Cirurgiões cadastrados")
            for i in erros:
                print(erros_dict[i])
            print("=== Lista de Profissionais Escalados ===")
            for i in range(len(espec_quant)):
                if espec_quant[i] == 0:
                    print(f"Não há {espec_dict[i]} cadastrados neste turno")
                else:
                    print(espec_dict[i])
                    for id in matriz[x][y]:    
                        if lista[id-1].espec == str(i+1):                     
                            print(f"ID => {lista[id-1].id}")
                            print(f"Nome => {lista[id-1].nome}")
                            print(f"Especialidade => {espec_dict[i]}\n")
            break
        else: 
            print("Opção Inválida") 
def contagem_espec(x,y,lista,matriz):
    espec = []
    for id in matriz[x][y]:
        espec.append(lista[id-1].espec)
    cl = espec.count("1")
    p = espec.count("2")
    c = espec.count("3")
    espec_quant = [cl,p,c]
    return espec_quant

#def validacao_semanal(lista,matriz):
#def media_escalas():
#def cobertura_turnos():
#def validação_semana():
menu()