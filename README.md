# 📚 Lista II - Programação Orientada a Objetos (POO)

Bem-vindo ao repositório de soluções da **Lista II de exercícios de Programação Orientada a Objetos**. Este projeto contém implementações práticas e modulares que demonstram os pilares fundamentais da POO, como Abstração, Encapsulamento, Herança e Polimorfismo.

---

## 🏛️ Informações Acadêmicas

> **Instituição:** Universidade Federal do Amazonas (UFAM)  
> **Curso:** Sistemas de Informação  
> **Período:** 5º Período  
> **Disciplina:** Programação Orientada a Objetos  
> **Professor:** Alternei de Souza Brito  
> **Aluno:** Pedro Jhevison Menezes de Souza  

---

## 💻 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

---

## 🧠 Lógica e Arquitetura dos Sistemas

Os exercícios foram divididos em 5 sistemas modulares. Abaixo, explico a lógica e os conceitos de POO aplicados na construção de cada um deles:

### 1. Sistema de Funcionários (`sistema_funcionarios`)
* **Conceito principal:** Herança, Polimorfismo e Composição.
* **Como foi criado:** Foi desenvolvida uma classe abstrata base `Funcionario` que dita um "contrato" com o método abstrato `calcular_pagamento()`. Três subclasses (`FuncionarioAssalariado`, `FuncionarioHorista`, e `FuncionarioComissionado`) herdam dessa classe base e sobrescrevem o método de pagamento com suas regras matemáticas específicas. A classe `Empresa` atua por composição: ela armazena uma lista de objetos do tipo `Funcionario` e, aproveitando o polimorfismo, percorre a lista chamando o mesmo método `calcular_pagamento()` de forma padronizada, independentemente do tipo de funcionário.

### 2. Sistema de Mídias (`sistema_midias`)
* **Conceito principal:** Abstração e Polimorfismo.
* **Como foi criado:** Criamos uma superclasse abstrata `Midia` contendo atributos comuns (título e duração) e um método concreto `mostrar_info()`, além de um método abstrato `reproduzir()`. As classes derivadas (`Video`, `Podcast` e `TextoNarrado`) adicionam atributos próprios (como resolução, apresentador ou idioma) e implementam o comportamento de reprodução específico. A classe `Plataforma` gerencia as mídias, permitindo adicionar qualquer tipo e acionar todas em sequência.

### 3. Sistema de Notificações (`sistema_notificacoes`)
* **Conceito principal:** Padrão *Strategy* (Estratégia) e Injeção de Dependência.
* **Como foi criado:** Ao invés de uma classe gigante cheia de `if/else` para saber qual notificação enviar, criou-se a classe abstrata `Notificador`. A partir dela, surgiram `NotificadorEmail`, `NotificadorSMS` e `NotificadorApp`. A classe `CentralNotificacoes` simplesmente recebe esses notificadores (injeção de dependência) em sua lista interna. Quando o método `enviar_para_todos()` é acionado, a central dispara a notificação para cada serviço cadastrado, demonstrando baixo acoplamento.

### 4. Sistema de Armazenamento (`sistema_armazenamento`)
* **Conceito principal:** Interfaces Formais (`ABC`) *vs* Interfaces Flexíveis (*Duck Typing* com `Protocol`).
* **Como foi criado:** Este módulo é um estudo profundo da tipagem no Python. Foi criada uma interface rígida `Armazenador` utilizando herança com `ABC` (implementada por `ArmazenadorArquivo` e `ArmazenadorBanco`). Em paralelo, foi criada a interface flexível `Salvavel` usando a classe `Protocol` nativa do Python. Isso permitiu criar a classe independente `ArmazenadorNuvem` que não herda de ninguém, mas, por possuir a mesma assinatura de método (`salvar`), é aceita pelo sistema puramente por seu comportamento (*Duck Typing*).

### 5. Sistema de Impressão (`sistema_impressao`)
* **Conceito principal:** Polimorfismo através de Protocolos (*Duck Typing* estrutural).
* **Como foi criado:** Focado em extrema flexibilidade, o sistema define um contrato estrutural `Imprimivel` via `Protocol`. Criamos classes isoladas (`Boleto`, `Etiqueta`, `RelatorioSimples`) que não possuem hierarquia (não herdam de uma mesma classe pai), mas todas possuem o método `imprimir()`. A função solta `processar_impressao()` aceita processar qualquer uma delas, provando que em Python, se um objeto "anda como um pato e grasna como um pato", ele é aceito pela interface.

---

## 📂 Estrutura do Repositório

```text
├── sistema_armazenamento/
│   ├── armazenamento.py
│   └── main.py
├── sistema_funcionarios/
│   ├── sistema_funcionarios.py
│   └── main.py
├── sistema_impressao/
│   ├── impressao.py
│   └── main.py
├── sistema_midias/
│   ├── sistema_midias.py
│   └── main.py
├── sistema_notificacoes/
│   ├── notificacoes.py
│   └── main.py
└── README.md
