import pygame
import math

pygame.init()

LARGURA = 900
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("AI Challenge")
relogio = pygame.time.Clock()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
ROXO = (70, 23, 143)
ROXO_ESCURO = (35, 8, 80)
VERMELHO = (226, 27, 60)
AZUL = (19, 104, 206)
AMARELO = (216, 158, 0)
VERDE = (38, 137, 12)
CINZA = (90, 90, 90)
DOURADO = (255, 200, 0)

cores_respostas = [VERMELHO, AZUL, AMARELO, VERDE]

fonte_titulo = pygame.font.Font(None, 72)
fonte_grande = pygame.font.Font(None, 40)
fonte_media = pygame.font.Font(None, 30)
fonte_pequena = pygame.font.Font(None, 28)

TEMPO_NORMAL = 30
TEMPO_BONUS = 15
PONTOS_NORMAL = 100
PONTOS_BONUS = 200

perguntas = [
    {
        "pergunta": "Você usou IA pra ajudar num trabalho da faculdade. O que é mais correto?",
        "opcoes": ["Entregar do jeito que a IA fez, sem ler",
                   "Revisar, entender e avisar que usou IA",
                   "Dizer pro professor que fez tudo sozinho",
                   "Pedir pra IA disfarçar o texto"],
        "certa": 1,
        "explicacao": "A IA pode ajudar, mas você precisa entender o que entrega e ser honesto sobre o uso."
    },
    {
        "pergunta": "A IA te deu uma informação bem estranha. O que você faz?",
        "opcoes": ["Acredito, IA nunca erra",
                   "Mando no grupo da turma na hora",
                   "Confiro em outras fontes confiáveis",
                   "Copio e colo no trabalho"],
        "certa": 2,
        "explicacao": "IA pode errar e até inventar coisas. Sempre confira em fontes confiáveis."
    },
    {
        "pergunta": "Qual dessas coisas você NÃO deve colocar num chat de IA?",
        "opcoes": ["Sua senha do banco",
                   "Uma dúvida de matemática",
                   "Uma receita de bolo",
                   "Ideias de nome pro seu cachorro"],
        "certa": 0,
        "explicacao": "Nunca compartilhe senhas, documentos ou dados pessoais com uma IA."
    },
    {
        "pergunta": "O que é a \"alucinação\" de uma IA?",
        "opcoes": ["Quando ela trava e para de responder",
                   "Quando ela fica muito lenta",
                   "Quando ela desliga sozinha",
                   "Quando ela inventa algo que parece verdade"],
        "certa": 3,
        "explicacao": "A IA pode responder com muita confiança uma coisa que é totalmente falsa."
    },
    {
        "pergunta": "Fazer um vídeo falso (deepfake) de um colega usando IA é...",
        "opcoes": ["Só uma brincadeira, sem problema",
                   "Errado, pode prejudicar e expor a pessoa",
                   "Permitido se ficar engraçado",
                   "Normal, todo mundo faz"],
        "certa": 1,
        "explicacao": "Deepfakes podem humilhar pessoas e espalhar mentiras. Respeite os outros."
    },
    {
        "pergunta": "Por que uma IA pode ter preconceito (viés)?",
        "opcoes": ["Porque ela tem opinião própria",
                   "Porque ela fica com raiva",
                   "Porque aprendeu com dados que já tinham preconceito",
                   "Isso é impossível, IA é sempre neutra"],
        "certa": 2,
        "explicacao": "A IA aprende com dados feitos por pessoas, e esses dados podem ter preconceitos."
    },
    {
        "pergunta": "Qual é o melhor jeito de usar IA pra estudar pra prova?",
        "opcoes": ["Pedir explicações e fazer os exercícios você mesmo",
                   "Pedir todas as respostas e decorar",
                   "Nem estudar e confiar que ela resolve",
                   "Usar só pra colar na hora da prova"],
        "certa": 0,
        "explicacao": "Use a IA como professora, não como cola. Quem precisa aprender é você!"
    },
    {
        "pergunta": "No fim das contas, quem é responsável pelo que você faz usando IA?",
        "opcoes": ["A própria IA",
                   "A empresa que criou a IA",
                   "Ninguém, foi a máquina",
                   "Você"],
        "certa": 3,
        "explicacao": "A IA é só uma ferramenta. A responsabilidade é sempre de quem usa."
    }
]

estado = "menu"
pergunta_atual = 0
pontos = 0
acertos = 0
pontos_ganhos = 0
tempo_inicio = 0
resultado = ""

quadrados = [
    pygame.Rect(30, 320, 410, 120),
    pygame.Rect(460, 320, 410, 120),
    pygame.Rect(30, 455, 410, 120),
    pygame.Rect(460, 455, 410, 120)
]


def desenhar_texto(texto, fonte, cor, x, y):
    imagem = fonte.render(texto, True, cor)
    retangulo = imagem.get_rect(center=(x, y))
    tela.blit(imagem, retangulo)


def quebrar_texto(texto, fonte, largura_maxima):
    palavras = texto.split(" ")
    linhas = []
    linha = ""
    for palavra in palavras:
        teste = linha + palavra + " "
        if fonte.size(teste)[0] > largura_maxima and linha != "":
            linhas.append(linha)
            linha = palavra + " "
        else:
            linha = teste
    linhas.append(linha)
    return linhas


def desenhar_varias_linhas(texto, fonte, cor, x, y, largura_maxima):
    linhas = quebrar_texto(texto, fonte, largura_maxima)
    altura_linha = fonte.get_height() + 4
    y_inicial = y - (len(linhas) - 1) * altura_linha // 2
    for i in range(len(linhas)):
        desenhar_texto(linhas[i].strip(), fonte, cor, x, y_inicial + i * altura_linha)


def eh_bonus(numero):
    if (numero + 1) % 4 == 0:
        return True
    return False


def tempo_limite():
    if eh_bonus(pergunta_atual):
        return TEMPO_BONUS
    return TEMPO_NORMAL


def tempo_restante():
    passou = (pygame.time.get_ticks() - tempo_inicio) / 1000
    restante = tempo_limite() - passou
    if restante < 0:
        restante = 0
    return restante


def comecar_pergunta():
    global tempo_inicio
    tempo_inicio = pygame.time.get_ticks()


def voltar_ao_menu():
    global estado
    estado = "menu"


def reiniciar_jogo():
    global estado, pergunta_atual, pontos, acertos
    pergunta_atual = 0
    pontos = 0
    acertos = 0
    estado = "jogando"
    comecar_pergunta()


def responder(opcao):
    global estado, pontos, acertos, resultado, pontos_ganhos
    certa = perguntas[pergunta_atual]["certa"]
    if opcao == certa:
        resultado = "acertou"
        acertos = acertos + 1
        if eh_bonus(pergunta_atual):
            pontos_ganhos = PONTOS_BONUS
        else:
            pontos_ganhos = PONTOS_NORMAL
        pontos = pontos + pontos_ganhos
    else:
        resultado = "errou"
        pontos_ganhos = 0
    estado = "resposta"


def acabou_o_tempo():
    global estado, resultado, pontos_ganhos
    resultado = "tempo"
    pontos_ganhos = 0
    estado = "resposta"


def proxima_pergunta():
    global estado, pergunta_atual
    pergunta_atual = pergunta_atual + 1
    if pergunta_atual >= len(perguntas):
        estado = "fim"
    else:
        estado = "jogando"
        comecar_pergunta()


def opcao_clicada(posicao):
    for i in range(4):
        if quadrados[i].collidepoint(posicao):
            return i
    return -1


def desenhar_menu():
    tela.fill(ROXO)
    desenhar_texto("AI CHALLENGE", fonte_titulo, BRANCO, LARGURA // 2, 130)
    desenhar_texto("Você sabe usar inteligência artificial do jeito certo?", fonte_media, BRANCO, LARGURA // 2, 210)
    desenhar_texto(f"Cada pergunta tem {TEMPO_NORMAL} segundos e vale {PONTOS_NORMAL} pontos.", fonte_pequena, BRANCO, LARGURA // 2, 290)
    desenhar_texto(f"A cada 3 perguntas vem uma BÔNUS: vale {PONTOS_BONUS}, mas só tem {TEMPO_BONUS} segundos!", fonte_pequena, DOURADO, LARGURA // 2, 325)
    desenhar_texto("Clique na resposta ou use as teclas 1, 2, 3 e 4.", fonte_pequena, BRANCO, LARGURA // 2, 360)
    desenhar_texto("Aperte ENTER para começar", fonte_grande, BRANCO, LARGURA // 2, 470)


def desenhar_pergunta():
    bonus = eh_bonus(pergunta_atual)
    if bonus:
        tela.fill(ROXO_ESCURO)
    else:
        tela.fill(ROXO)

    desenhar_texto(f"Pergunta {pergunta_atual + 1}/{len(perguntas)}", fonte_pequena, BRANCO, 100, 30)
    desenhar_texto(f"Pontos: {pontos}", fonte_pequena, BRANCO, LARGURA - 100, 30)
    if bonus:
        desenhar_texto("RODADA BÔNUS! Pontos em dobro, tempo pela metade!", fonte_media, DOURADO, LARGURA // 2, 70)

    texto = perguntas[pergunta_atual]["pergunta"]
    desenhar_varias_linhas(texto, fonte_grande, BRANCO, LARGURA // 2, 160, LARGURA - 80)

    restante = tempo_restante()
    largura_barra = int(restante / tempo_limite() * (LARGURA - 60))
    cor_barra = VERDE
    if restante <= 5:
        cor_barra = VERMELHO
    pygame.draw.rect(tela, CINZA, (30, 250, LARGURA - 60, 35), border_radius=8)
    pygame.draw.rect(tela, cor_barra, (30, 250, largura_barra, 35), border_radius=8)
    desenhar_texto(f"{math.ceil(restante)} s", fonte_media, BRANCO, LARGURA // 2, 268)

    opcoes = perguntas[pergunta_atual]["opcoes"]
    for i in range(4):
        pygame.draw.rect(tela, cores_respostas[i], quadrados[i], border_radius=10)
        desenhar_texto(str(i + 1), fonte_pequena, BRANCO, quadrados[i].x + 18, quadrados[i].y + 18)
        desenhar_varias_linhas(opcoes[i], fonte_media, BRANCO, quadrados[i].centerx, quadrados[i].centery, quadrados[i].width - 60)


def desenhar_resposta():
    if resultado == "acertou":
        tela.fill(VERDE)
        desenhar_texto("ACERTOU!", fonte_titulo, BRANCO, LARGURA // 2, 90)
        desenhar_texto(f"+{pontos_ganhos} pontos", fonte_grande, BRANCO, LARGURA // 2, 150)
    elif resultado == "errou":
        tela.fill(VERMELHO)
        desenhar_texto("ERROU!", fonte_titulo, BRANCO, LARGURA // 2, 90)
        desenhar_texto("+0 pontos", fonte_grande, BRANCO, LARGURA // 2, 150)
    else:
        tela.fill(CINZA)
        desenhar_texto("ACABOU O TEMPO!", fonte_titulo, BRANCO, LARGURA // 2, 90)
        desenhar_texto("+0 pontos", fonte_grande, BRANCO, LARGURA // 2, 150)

    certa = perguntas[pergunta_atual]["certa"]
    desenhar_texto("Resposta certa:", fonte_pequena, BRANCO, LARGURA // 2, 215)
    desenhar_varias_linhas(perguntas[pergunta_atual]["opcoes"][certa], fonte_grande, BRANCO, LARGURA // 2, 255, LARGURA - 80)
    desenhar_varias_linhas(perguntas[pergunta_atual]["explicacao"], fonte_media, BRANCO, LARGURA // 2, 330, LARGURA - 120)
    desenhar_texto(f"Total: {pontos} pontos", fonte_grande, BRANCO, LARGURA // 2, 400)

    proxima = pergunta_atual + 1
    if proxima < len(perguntas) and eh_bonus(proxima):
        pygame.draw.rect(tela, PRETO, (60, 445, LARGURA - 120, 45), border_radius=8)
        desenhar_texto(f"Atenção: a próxima é BÔNUS! Vale o dobro, mas só tem {TEMPO_BONUS} segundos",
                       fonte_pequena, DOURADO, LARGURA // 2, 468)

    desenhar_texto("Aperte ENTER para continuar", fonte_pequena, BRANCO, LARGURA // 2, 550)


def desenhar_fim():
    tela.fill(ROXO)
    desenhar_texto("FIM DE JOGO!", fonte_titulo, BRANCO, LARGURA // 2, 130)
    desenhar_texto(f"Você fez {pontos} pontos", fonte_grande, DOURADO, LARGURA // 2, 230)
    desenhar_texto(f"Acertou {acertos} de {len(perguntas)} perguntas", fonte_grande, BRANCO, LARGURA // 2, 290)

    if acertos == len(perguntas):
        mensagem = "Perfeito! Você sabe usar IA com responsabilidade!"
    elif acertos >= len(perguntas) / 2:
        mensagem = "Mandou bem! Mas ainda dá pra melhorar."
    else:
        mensagem = "Hora de aprender mais sobre o uso responsável de IA!"
    desenhar_texto(mensagem, fonte_media, BRANCO, LARGURA // 2, 370)

    desenhar_texto("ENTER para voltar ao menu   |   ESC para sair", fonte_pequena, BRANCO, LARGURA // 2, 480)


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
            elif estado == "menu" and evento.key == pygame.K_RETURN:
                reiniciar_jogo()
            elif estado == "jogando":
                if evento.key == pygame.K_1:
                    responder(0)
                elif evento.key == pygame.K_2:
                    responder(1)
                elif evento.key == pygame.K_3:
                    responder(2)
                elif evento.key == pygame.K_4:
                    responder(3)
            elif estado == "resposta" and evento.key == pygame.K_RETURN:
                proxima_pergunta()
            elif estado == "fim" and evento.key == pygame.K_RETURN:
                voltar_ao_menu()

        if evento.type == pygame.MOUSEBUTTONDOWN and estado == "jogando":
            opcao = opcao_clicada(evento.pos)
            if opcao != -1:
                responder(opcao)

    if estado == "jogando" and tempo_restante() <= 0:
        acabou_o_tempo()

    if estado == "menu":
        desenhar_menu()
    elif estado == "jogando":
        desenhar_pergunta()
    elif estado == "resposta":
        desenhar_resposta()
    elif estado == "fim":
        desenhar_fim()

    pygame.display.flip()
    relogio.tick(30)

pygame.quit()
