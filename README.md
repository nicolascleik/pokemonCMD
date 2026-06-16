# 🎮 PokémonCMD

> Um RPG de texto no terminal inspirado em Stardew Valley e Pokémon — com sistema de tempo, dívidas, fome, cassino e batalhas.

---

## 🚀 Como Rodar

**Requisitos:** Python 3.10 ou superior. Sem dependências externas.

```bash
python main.py
```

O jogo roda inteiramente no terminal, sem instalação de pacotes.

---

## 🗂️ Estrutura do Projeto

```
RAIZ/
│
├── main.py                        # Ponto de entrada e loop principal do jogo
│
├── models/                        # Classes base (contratos abstratos)
│   ├── pokemon.py                 # Superclasse abstrata de todos os Pokémons
│   ├── item.py                    # Superclasse abstrata de todos os itens
│   ├── estabelecimento.py         # Superclasse abstrata de todos os locais
│   ├── player.py                  # Estado e recursos do jogador
│   ├── relogio.py                 # Controle de horas e dias
│   ├── batalha.py                 # Lógica de combate turno a turno
│   ├── agiota.py                  # Sistema de dívidas, juros e cobradores
│   └── gameManager.py             # Verificação de vitória, derrota e penalidades
│
├── estabelecimentos/              # Locais visitáveis do mapa
│   ├── casa.py                    # Dormir e recuperar energia
│   ├── mercadinho.py              # Comprar, vender itens e trabalhar
│   ├── centro_pokemon.py          # Curar a equipe (mediante pagamento)
│   ├── floresta.py                # Encontrar e capturar Pokémons comuns/lendários
│   ├── caverna_cerulean.py        # Zona difícil com maior chance de lendários
│   ├── lago_de_pesca.py           # Pescar Pokémons aquáticos ou peixes para venda
│   ├── cassino.py                 # Caça-níquel, adivinhação e Blackjack
│   ├── arena_de_batalha.py        # Batalhas com fuga bloqueada por prêmio em dinheiro
│   └── beco_escuro.py             # Interagir com o Agiota (pegar/pagar empréstimos)
│
├── itens/                         # Itens usáveis e consumíveis
│   ├── pocao_pequena.py           # Cura 20 HP de um Pokémon
│   ├── pocao_grande.py            # Cura 50 HP de um Pokémon
│   ├── pokebola.py                # Usada em batalha para capturar Pokémons
│   ├── maca.py                    # Comida: recupera 10 de energia
│   ├── salgadinho.py              # Comida: recupera 20 de energia
│   ├── marmita.py                 # Comida: recupera 40 de energia
│   └── peixe.py                   # Item de venda (pescado no lago, vale $25)
│
├── pokemons_comuns/               # 18 Pokémons comuns jogáveis
│   ├── arts.py                    # Arte ASCII compartilhada
│   ├── pikachu.py, charmander.py, bulbasaur.py, squirtle.py
│   ├── eevee.py, meowth.py, venonat.py, butterfree.py
│   ├── gengar.py, haunter.py, mimikyu.py, jigglypuff.py
│   ├── mew.py, snorlax.py, slowpoke.py, charizard.py
│   ├── blastoise.py e chikoritta.py
│
└── pokemons_lendarios/            # 7 Pokémons lendários capturáveis
    ├── arts.py                    # Arte ASCII compartilhada
    ├── mewtwo.py, articuno.py, dialga.py
    ├── kyogre.py, lugia.py, mesprit.py e rayquaza.py
```

---

## 🎯 Objetivo do Jogo

O jogo tem **duas condições de vitória** e pode ser encerrado por **derrota total**:

### Vitórias
| Condição | Descrição |
|---|---|
| 💰 Vitória Capitalista | Acumule **$10.000** em saldo |
| 🏆 Vitória de Mestre | Capture **5 Pokémons Lendários** |

### Derrota
| Condição | Descrição |
|---|---|
| 💀 Falência Absoluta | Sem dinheiro + com dívida + sem itens para sobreviver |

---

## ⚙️ Sistemas do Jogo

### ⏰ Sistema de Tempo
Cada dia começa às **06:00** e o limite é **meia-noite (24:00)**. Toda viagem até um local consome horas e energia simultaneamente. Se o jogador chegar à meia-noite fora de casa, **desmaia na rua** e sofre penalidades.

| Local | Custo de Tempo | Custo de Energia |
|---|---|---|
| Casa | 1h | 10 |
| Mercadinho | 1h | 10 |
| Centro Pokémon | 1h | 10 |
| Beco Escuro | 1h | 10 |
| Floresta | 2h | 20 |
| Lago de Pesca | 2h | 20 |
| Cassino | 2h | 20 |
| Caverna Cerulean | 4h | 40 |
| Arena de Batalha | 4h | 40 |

### 🍎 Sistema de Energia (Fome)
O jogador possui **100 de energia máxima**. Energia é consumida em viagens e durante atividades nos locais (pescar, explorar caverna, trabalhar). Ao atingir 0, o jogador desmaia. Para recuperar energia é necessário comer itens de comida comprados no mercadinho.

| Item | Preço | Energia Recuperada |
|---|---|---|
| Maçã | $5 | +10 |
| Salgadinho | $15 | +20 |
| Marmita | $25 | +40 |

Além disso, existe um **custo diário fixo de $20** de alimentação que é descontado automaticamente a cada virada de dia. Sem pagar, a energia máxima é prejudicada.

### 💸 Sistema de Dívidas (Agiota)
No **Beco Escuro**, o jogador pode pegar dinheiro emprestado com o Agiota. O empréstimo tem um **prazo em dias** e acumula **10% de juros ao dia**.

- Se o prazo vencer sem pagamento, os **Pokémons cobradores** (Gengar, Haunter, Meowth) passam a aparecer no início de cada turno, forçando uma batalha.
- O jogador pode tentar **fugir** dos cobradores ou lutar.
- A dívida só para de crescer quando for **totalmente quitada**.

### ⚔️ Sistema de Batalha
As batalhas são **turno a turno**. O jogador sempre ataca primeiro:

**Opções por turno:**
1. **Atacar** — causa dano baseado no `poder_ataque` do Pokémon ativo
2. **Usar Pokébola** — tenta capturar o Pokémon selvagem (consome uma Pokébola do inventário)
3. **Fugir** — 50% de chance de sucesso; se falhar, o inimigo ataca

**Chance de captura** varia de acordo com a raridade e o HP atual do inimigo:
- Quanto menor o HP do inimigo, maior a chance
- Lendários têm chance base de **10%** (máximo ~40%)
- Comuns têm chance base de **50%** (máximo ~80%)

Ao capturar, o jogo instancia um Pokémon novo com HP cheio — não o danificado da batalha.

Na **Arena de Batalha**, a fuga é **bloqueada** — o jogador precisa vencer ou ser derrotado.

### 😴 Desmaio e Penalidades
Quando o jogador desmaia (por horário, energia ou derrota em batalha):
- **30% de chance** de ser **roubado** (perde 20% do dinheiro)
- **70% de chance** de pagar taxa de resgate ($50)
- O dia avança automaticamente para o próximo
- A equipe recebe cura parcial de 50% do HP máximo

---

## 🗺️ Locais Detalhados

### 🏠 Casa
Dormir restaura energia ao máximo e cura 20 HP em cada Pokémon da equipe. É o único local seguro para encerrar o dia sem penalidades.

### 🛒 Mercadinho
Três funções disponíveis:
- **Comprar** — poções, pokébolas e comida
- **Vender** — peixes pescados no lago valem $25 cada; outros itens valem 50% do preço original
- **Trabalhar no estoque** — gasta 4h e 40 de energia, mas rende **$60**

### 💊 Centro Pokémon
Cura Pokémons por $30 cada. É possível curar um por um ou toda a equipe de vez (desconto automático apenas pelos que precisam).

### 🌲 Floresta
A zona mais acessível para caça de Pokémons. A cada exploração (1h, 10 de energia):
- **20%** de chance de não encontrar nada
- **2%** de chance de encontrar um **Lendário**
- **78%** de chance de encontrar um **Pokémon Comum**

### 🪨 Caverna Cerulean
Zona de risco elevado (4h para chegar, 3h por exploração, 25 de energia). Melhor taxa de lendários:
- **20%** de nada
- **10%** de **Lendário**
- **70%** de **Comum**

### 🎣 Lago de Pesca
Atividade mais tranquila para gerar renda passiva:
- **30%** de nada
- **30%** de **Peixe** (vendável por $25)
- **5%** de **Kyogre** (Pokémon Lendário)
- **35%** de **Pokémon Comum de água**

### 🎰 Cassino
Três jogos disponíveis (cada rodada custa 1h e 5 de energia):
- **Caça-Níquel** ($10 fixo) — par paga $15, trinca paga $50, jackpot de estrelas paga $200
- **Adivinhe o Número** (aposta livre) — acerto exato paga 5x, número adjacente paga 1.5x
- **Blackjack/21** (aposta livre) — regras clássicas com Dealer seguindo a regra dos 17

### ⚔️ Arena de Batalha
Torneios contra oponentes fortes (Charizard, Blastoise, Snorlax, Gengar). Vencer paga **$150**. A **fuga é bloqueada** — é lutar ou perder.

### 🌑 Beco Escuro
Única forma de acessar o Agiota para pegar empréstimos ou quitar dívidas.

---

## 🐾 Pokédex do Jogo

### Pokémons Comuns (18)

| Pokémon | HP | Ataque | Pokémon | HP | Ataque |
|---|---|---|---|---|---|
| Pikachu | 40 | 15 | Bulbasaur | 45 | 12 |
| Charmander | 39 | 13 | Squirtle | 44 | 11 |
| Eevee | 55 | 10 | Meowth | 40 | 9 |
| Venonat | 60 | 8 | Butterfree | 60 | 12 |
| Gengar | 60 | 18 | Haunter | 45 | 15 |
| Mimikyu | 55 | 14 | Jigglypuff | 115 | 8 |
| Mew | 100 | 20 | Snorlax | 160 | 10 |
| Slowpoke | 90 | 5 | Charizard | 150 | 25 |
| Blastoise | 140 | 20 | Chikoritta | 45 | 10 |

### Pokémons Lendários (7)

| Pokémon | HP | Ataque | Onde Encontrar |
|---|---|---|---|
| Mewtwo | 500 | 80 | Floresta / Caverna |
| Articuno | 420 | 55 | Floresta / Caverna |
| Dialga | 460 | 70 | Floresta / Caverna |
| Kyogre | 450 | 70 | Lago de Pesca / Caverna |
| Lugia | 440 | 60 | Floresta / Caverna |
| Mesprit | 380 | 50 | Floresta / Caverna |
| Rayquaza | 480 | 65 | Floresta / Caverna |

---

## 🧱 Arquitetura e Conceitos de POO

O projeto foi desenvolvido aplicando os pilares de **Programação Orientada a Objetos**:

**Herança:** `Pokemon`, `Item` e `Estabelecimento` são classes abstratas base. Todas as subclasses (Pikachu, Pocao, Casa, etc.) herdam e especializam esse comportamento.

**Abstração:** Nenhuma das três classes base pode ser instanciada diretamente — elas apenas definem contratos com `@abstractmethod`.

**Encapsulamento:** Atributos sensíveis (dinheiro, vida, inventário) usam prefixo `_` e são acessados apenas por `@property` ou métodos específicos (`modificar_dinheiro`, `consumir_item`, etc.).

**Polimorfismo:** Todos os locais implementam `interagir(jogador, relogio)`. O game loop do `main.py` chama `local_escolhido.interagir(...)` sem precisar saber que local é — cada um responde à sua maneira.

**Injeção de Dependência:** A classe `Batalha` recebe `player` e `wild_pokemon` via construtor. O `BecoEscuro` recebe a instância do `Agiota`. Isso torna os componentes testáveis e desacoplados.

**Separação de Responsabilidades (SRP):** `Relogio` só controla tempo. `Agiota` só gerencia dívidas. `GameManager` só avalia vitória/derrota. Nenhum deles conhece os outros diretamente.

---

## 📦 Itens e Preços

| Item | Preço | Efeito |
|---|---|---|
| Poção Pequena | $20 | +20 HP em um Pokémon |
| Poção Grande | $50 | +50 HP em um Pokémon |
| Pokébola | $30 | Usada em batalha para captura |
| Maçã | $5 | +10 de energia ao jogador |
| Salgadinho | $15 | +20 de energia ao jogador |
| Marmita | $25 | +40 de energia ao jogador |
| Peixe | — | Vendável por $25 no Mercadinho (obtido no lago) |

---

## 💡 Dicas de Sobrevivência

- Sempre durma em casa antes da meia-noite. Desmaiar na rua custa mais do que vale.
- A Arena garante $150 por vitória — é a fonte de renda mais segura para quem tem uma equipe forte.
- Se pegar dinheiro emprestado com o Agiota, pague antes do prazo. Os juros de 10% ao dia dobram a dívida em menos de uma semana.
- Trabalhar no Mercadinho é arriscado quando o dia está avançado — 4 horas é muito tempo.
- O Lago de Pesca tem a melhor relação custo-benefício para acumular dinheiro sem batalhas.
- Compre Pokébolas antes de ir para a Floresta. Sem elas, você só pode lutar ou fugir.
- Lendários com HP baixo ficam com até ~40% de chance de captura. Desgaste antes de lançar a Pokébola.

---

## 👥 Cobradores do Agiota

Quando o prazo da dívida vence, estes três Pokémons passam a bloquear seu caminho no início de cada turno:

| Cobrador | HP | Ataque |
|---|---|---|
| Gengar | 60 | 18 |
| Haunter | 45 | 15 |
| Meowth | 40 | 9 |

A fuga não é bloqueada nestas batalhas — você pode tentar escapar (50% de chance). Se perder, sofre penalidade de desmaio normalmente.