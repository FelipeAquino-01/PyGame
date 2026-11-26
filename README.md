# AI Challenge

## Integrantes do grupo

- Daniel Ischaber Xavier
- Vinicius Daniel Santos
- Felipe Gabriel Nogueira Aquino
- Gabriel Luiz Drumond Oliveira

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (`config.py`, `dados.py`, `funcoes.py`, `jogo.py`, `sprites.py`).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (`recorde.txt` e `ranking.txt`).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo a proposta inicial (`proposta.MD`).

## Descrição do jogo

O **AI Challenge** é um jogo de perguntas e respostas (quiz) sobre o uso responsável da Inteligência Artificial no cotidiano. As situações abordam checagem de informações geradas por IA, proteção de dados pessoais, combate ao plágio, reconhecimento de vieses e *deepfakes*, além da transparência no uso de ferramentas inteligentes.

A cada rodada, as perguntas são sorteadas aleatoriamente a partir de um banco de 15 questões. Quem responde mais rápido acumula mais pontos e, após cada resposta, o jogo exibe uma explicação educativa sobre a alternativa correta.

## Objetivo do jogador

Responder corretamente às perguntas sorteadas dentro do tempo limite, mantendo vidas restantes e alcançando a maior pontuação possível para superar o recorde salvo.

## Modos de jogo

- **Arcade:** partida rápida com menos perguntas e tempo reduzido por questão.
- **Normal:** partida equilibrada com quantidade intermediária de perguntas e tempo padrão.
- **Grande:** maratona completa com todas as 15 questões do banco de dados.

## Regras do jogo

- No início da partida, o jogador escolhe entre os modos **Arcade**, **Normal** ou **Grande**.
- Cada pergunta possui um cronômetro regressivo; responder antes de o tempo acabar garante pontos base mais bônus pelos segundos restantes.
- Errar uma pergunta ou deixar o tempo zerar desconta uma vida.
- Após cada escolha, o jogo exibe uma breve explicação sobre o uso responsável da IA relacionado à questão.
- A partida termina quando todas as perguntas do modo forem respondidas ou quando as vidas chegarem a zero.

## Controles

- **Botão esquerdo do mouse:** selecionar o modo de jogo, clicar na alternativa desejada e avançar para a próxima pergunta.

## Como executar o projeto

1. Certifique-se de ter o Python e o Pygame instalados (`pip install -r requirements.txt`).
2. Na raiz do projeto, execute:
   ```bash
   python main.py