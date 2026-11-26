# Banco de dados das 15 questões e funções de persistência (recorde)

PERGUNTAS_QUIZ = [
    {
        "pergunta": "1. Uma IA gerou um texto com dados históricos para seu trabalho. O que fazer?",
        "opcoes": [
            "Copiar direto, pois a IA nunca erra fatos",
            "Conferir as informações em fontes confiáveis antes de usar",
            "Usar apenas se o texto parecer bem escrito",
            "Apagar as referências para parecer autoral"
        ],
        "correta": 1,
        "explicacao": "IAs podem gerar informações falsas ('alucinações'). Sempre cheque os fatos em fontes seguras."
    },
    {
        "pergunta": "2. Qual informação NUNCA deve ser digitada em um chat de IA público?",
        "opcoes": [
            "Dúvidas sobre regras de gramática",
            "Pedidos de ideias para uma apresentação",
            "Senhas, CPF, dados bancários ou sigilosos",
            "Exemplos de exercícios de programação"
        ],
        "correta": 2,
        "explicacao": "Dados pessoais ou confidenciais podem ser armazenados ou vazados. Proteja sua privacidade."
    },
    {
        "pergunta": "3. Ao usar IA para ajudar em um trabalho acadêmico, qual é a atitude ética?",
        "opcoes": [
            "Entregar o texto gerado como se fosse 100% seu",
            "Declarar o uso da ferramenta e revisar o conteúdo",
            "Trocar apenas três palavras para evitar detecção",
            "Esconder do professor que utilizou tecnologia"
        ],
        "correta": 1,
        "explicacao": "Transparência e revisão crítica garantem aprendizado real e evitam plágio acadêmico."
    },
    {
        "pergunta": "4. Você recebe um vídeo de um familiar pedindo Pix urgente, mas a voz parece estranha.",
        "opcoes": [
            "Fazer a transferência imediatamente pela urgência",
            "Compartilhar o vídeo em todos os grupos",
            "Ligar por outro canal para confirmar se é um deepfake",
            "Responder pedindo a senha do banco dele"
        ],
        "correta": 2,
        "explicacao": "Golpistas usam IA (deepfake) para clonar voz e rosto. Sempre confirme por outro meio."
    },
    {
        "pergunta": "5. Um sistema de IA de RH descarta currículos de um grupo específico. O que houve?",
        "opcoes": [
            "Viés algorítmico herdado de dados históricos",
            "Falha na placa de vídeo do computador",
            "Excesso de memória RAM no servidor",
            "Garantia de neutralidade total da máquina"
        ],
        "correta": 0,
        "explicacao": "Se os dados de treino têm preconceitos históricos, a IA repete decisões injustas."
    },
    {
        "pergunta": "6. Qual o risco de pedir diagnóstico médico definitivo apenas para um chatbot?",
        "opcoes": [
            "Nenhum, pois chatbots substituem hospitais",
            "O chat pode errar e atrasar um tratamento real",
            "O computador pode pegar vírus biológico",
            "A IA sempre receita remédios gratuitos"
        ],
        "correta": 1,
        "explicacao": "IA apoia buscas gerais, mas não substitui avaliação clínica de profissionais de saúde."
    },
    {
        "pergunta": "7. Como identificar uma imagem possivelmente criada por IA nas redes sociais?",
        "opcoes": [
            "Verificar detalhes como mãos, textos borrados e fonte",
            "Acreditar se a imagem tiver muitas curtidas",
            "Confiar apenas porque a foto é colorida",
            "Assumir que toda foto na internet é real"
        ],
        "correta": 0,
        "explicacao": "Anomalias visuais e checagem da origem da publicação ajudam a detectar imagens sintéticas."
    },
    {
        "pergunta": "8. Por que algoritmos de recomendação podem criar 'bolhas de informação'?",
        "opcoes": [
            "Porque bloqueiam o acesso à internet",
            "Porque mostram só conteúdos parecidos com seus cliques",
            "Porque apagam vídeos antigos automaticamente",
            "Porque funcionam apenas sem conexão"
        ],
        "correta": 1,
        "explicacao": "Sistemas de recomendação priorizam engajamento, reduzindo a diversidade de pontos de vista."
    },
    {
        "pergunta": "9. Um assistente virtual redigiu um e-mail importante para um cliente. Qual o próximo passo?",
        "opcoes": [
            "Enviar sem ler para economizar tempo",
            "Revisar tom, clareza e dados antes de enviar",
            "Enviar dez vezes seguidas por segurança",
            "Apagar o assunto do e-mail"
        ],
        "correta": 1,
        "explicacao": "A supervisão humana evita erros de contexto, promessas indevidas ou falhas de comunicação."
    },
    {
        "pergunta": "10. Usar IA para gerar código de programação sem entender o que ele faz gera qual risco?",
        "opcoes": [
            "Introduzir falhas de segurança e bugs ocultos",
            "Deixar o teclado mais lento",
            "Impedir o computador de desligar",
            "Aumentar o brilho do monitor"
        ],
        "correta": 0,
        "explicacao": "Código gerado por IA precisa ser testado e compreendido para evitar brechas de segurança."
    },
    {
        "pergunta": "11. O que significa 'uso responsável da Inteligência Artificial'?",
        "opcoes": [
            "Usar IA para automatizar qualquer decisão sem revisão",
            "Aplicar IA com ética, segurança, transparência e crítica",
            "Proibir qualquer tecnologia nas escolas",
            "Confiar cegamente em respostas rápidas"
        ],
        "correta": 1,
        "explicacao": "Uso responsável une benefícios da tecnologia com supervisão humana e respeito às pessoas."
    },
    {
        "pergunta": "12. Ao criar imagens ou músicas com IA para uso comercial, com o que devemos ter cuidado?",
        "opcoes": [
            "Com direitos autorais e regras de licença da plataforma",
            "Com a cor do cabo de rede",
            "Com o tamanho do mouse utilizado",
            "Não existe nenhuma regra sobre uso comercial"
        ],
        "correta": 0,
        "explicacao": "Obras geradas por IA podem envolver restrições de licença e debates sobre direitos autorais."
    },
    {
        "pergunta": "13. E-mails de golpe (phishing) feitos com IA estão mais difíceis de notar porque:",
        "opcoes": [
            "Possuem textos bem escritos e personalizados",
            "Sempre vêm em letras maiúsculas",
            "Nunca contêm links ou anexos",
            "São enviados apenas por carta"
        ],
        "correta": 0,
        "explicacao": "A IA melhora a escrita dos golpes. Desconfie de pedidos urgentes e verifique o remetente."
    },
    {
        "pergunta": "14. Em uma casa inteligente, qual prática melhora a segurança dos dispositivos conectados?",
        "opcoes": [
            "Manter a senha padrão de fábrica",
            "Trocar senhas padrão e atualizar o sistema",
            "Compartilhar o Wi-Fi aberto com a rua",
            "Desativar todas as notificações de alerta"
        ],
        "correta": 1,
        "explicacao": "Dispositivos inteligentes conectados à rede precisam de senhas fortes e atualizações."
    },
    {
        "pergunta": "15. Qual papel deve ter o ser humano diante de sistemas automatizados?",
        "opcoes": [
            "Apenas apertar botões sem questionar",
            "Manter o pensamento crítico e a decisão final",
            "Transferir toda responsabilidade legal à máquina",
            "Ignorar erros quando o sistema for rápido"
        ],
        "correta": 1,
        "explicacao": "A IA é uma ferramenta de apoio; a responsabilidade pelas decisões continua sendo humana."
    },
]


def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0