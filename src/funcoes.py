import random


def sortear_perguntas(lista_perguntas, quantidade):
    """Sorteia perguntas aleatórias sem repetição conforme o modo escolhido."""
    qtd_segura = min(quantidade, len(lista_perguntas))
    return random.sample(lista_perguntas, qtd_segura)


def verificar_resposta(pergunta, indice_escolhido):
    """Retorna True se o índice escolhido for igual à resposta correta."""
    return indice_escolhido == pergunta["correta"]


def calcular_pontos_quiz(pontos_atual, acertou, tempo_restante, pontos_base, bonus_segundo):
    """Calcula a nova pontuação considerando acerto e bônus de rapidez."""
    if not acertou:
        return pontos_atual

    bonus = int(tempo_restante) * bonus_segundo
    return pontos_atual + pontos_base + bonus


def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano=1):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0