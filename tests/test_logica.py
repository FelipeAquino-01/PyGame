import os
import sys

# Garante que o Python encontre a pasta 'src' na raiz do projeto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import MODOS_JOGO
from src.dados import PERGUNTAS_QUIZ
from src.funcoes import (
    calcular_pontos,
    calcular_pontos_quiz,
    jogador_perdeu,
    sortear_perguntas,
    tomar_dano,
    verificar_resposta,
)


def test_banco_possui_15_perguntas():
    """Garante que o banco de dados possui exatamente 15 questoes."""
    assert len(PERGUNTAS_QUIZ) == 15


def test_sortear_perguntas_por_modo():
    """Deve sortear a quantidade certa de perguntas sem repeticao para cada modo."""
    for modo in MODOS_JOGO.values():
        qtd = modo["qtd_perguntas"]
        sorteadas = sortear_perguntas(PERGUNTAS_QUIZ, qtd)

        assert len(sorteadas) == qtd
        enunciados = [p["pergunta"] for p in sorteadas]
        assert len(set(enunciados)) == qtd


def test_verificar_resposta():
    """Deve retornar True apenas quando o indice escolhido for o correto."""
    pergunta_exemplo = {
        "pergunta": "Teste?",
        "opcoes": ["A", "B", "C", "D"],
        "correta": 2,
        "explicacao": "Explicacao teste.",
    }
    assert verificar_resposta(pergunta_exemplo, 2) is True
    assert verificar_resposta(pergunta_exemplo, 0) is False


def test_calcular_pontos_quiz_acerto_e_erro():
    """Deve somar pontos base + bonus de tempo ao acertar, e manter ao errar."""
    assert calcular_pontos_quiz(0, True, 10.5, 100, 10) == 200
    assert calcular_pontos_quiz(200, False, 10.5, 100, 10) == 200


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_tomar_dano_e_jogador_perdeu():
    """Deve descontar vidas e indicar derrota quando chegar a zero."""
    vidas = tomar_dano(2, 1)
    assert vidas == 1
    assert jogador_perdeu(vidas) is False

    vidas = tomar_dano(vidas, 1)
    assert vidas == 0
    assert jogador_perdeu(vidas) is True