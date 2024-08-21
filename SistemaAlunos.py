class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = {}

    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Notas: {self.notas}"

alunos = []

def registrar_aluno(nome, matricula):
    aluno = Aluno(nome, matricula)
    alunos.append(aluno)
    print(f"Aluno {nome} registrado com sucesso")

def listar_alunos():
    for aluno in alunos:
        print(aluno)

def atribuir_notas(matricula, materia, nota):
    aluno = next((a for a in alunos if a.matricula == matricula), None)
    if aluno:
        if materia not in aluno.notas:
            aluno.notas[materia] = []
        aluno.notas[materia].append(nota)
        print(f"A nota {nota} foi adicionada para {aluno.nome} em {materia}")
    else:
        print("Aluno não encontrado")

def calcular_media(matricula, materia):
    aluno = next((a for a in alunos if a.matricula == matricula), None)
    if aluno:
        if materia in aluno.notas:
            media = sum(aluno.notas[materia]) / len(aluno.notas[materia])
            print(f"A média do aluno {aluno.nome} em {materia}: {media:.2f}")
        else:
            print(f"{aluno.nome} não possui notas registradas na matéria {materia}.")
    else:
        print("Aluno não encontrado")

# Testando o código
registrar_aluno("Ana Lara Carvalho", "A001")
registrar_aluno("Rodrigo Carvalho", "A002")
atribuir_notas("A001", "Matemática", 10.0)
atribuir_notas("A002", "Português", 8.5)
calcular_media("A001", "Matemática")
calcular_media("A002", "Português")
listar_alunos()

