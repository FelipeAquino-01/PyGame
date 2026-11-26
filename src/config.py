# ==============================================================================
# CONFIGURAÇÕES GERAIS DO JOGO - AI CHALLENGE
# Dica para a apresentação: altere os valores abaixo para mudar o jogo ao vivo!
# ==============================================================================

# Janela e desempenho
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60
TITULO_JOGO = "AI Challenge - Uso Responsável de IA"

# Regras principais (modificáveis facilmente na apresentação)
VIDAS_INICIAIS = 3          # Quantidade de erros permitidos antes de perder
PONTOS_BASE = 100           # Pontos ganhos por cada resposta certa
BONUS_POR_SEGUNDO = 10      # Pontos extras por cada segundo restante no relógio

# Modos de jogo: define quantidade de perguntas sorteadas e tempo (em segundos)
MODOS_JOGO = {
    "arcade": {
        "nome": "Arcade",
        "qtd_perguntas": 5,
        "tempo": 15,
    },
    "normal": {
        "nome": "Normal",
        "qtd_perguntas": 10,
        "tempo": 25,
    },
    "grande": {
        "nome": "Grande",
        "qtd_perguntas": 15,
        "tempo": 35,
    },
}

# Cores (R, G, B)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (212, 212, 212)
AZUL_FUNDO = (25, 42, 75)
AZUL_BOTAO = (52, 101, 164)
VERDE = (39, 174, 96)
VERMELHO = (192, 57, 43)
AMARELO = (241, 196, 15)

# Caminhos de arquivos
CAMINHO_RECORDE = "data/recorde.txt"
CAMINHO_RANKING = "data/ranking.txt"
CAMINHO_SPRITES = "assets/imagens/spritesheet.bmp"