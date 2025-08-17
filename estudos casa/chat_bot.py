import nltk
from nltk.chat.util import Chat, reflections


pares   = [
    [
            r"oi|Ola|hey|hello!",
            ["oi,""ola","hey","hello!"],
    ], 
    [
            r"Qual é o seu nome?",
            ["Meu nome é KauaBot.", "Eu sou um assistente virtual."],
            
    ],

    [
            r"Como Estas?|Como voce esta?|Como está se sentindo?",
            ["Estou bem, obrigado por perguntar!", "Estou otimo, e você?", "vou bem, e você?"],
            
    ],
    [
            r"(?i)(adeus|bye bye|tchau|até logo)",
            ["Tchau!", "Até mais!", "Até logo!", "Adeus!"],
    ],

    [
            r"Qual é a sua cor favorita?",
            ["Minha cor favorita é azul.", "Gosto de várias cores, mas azul é especial."],
            
    ],
    [
            r"Qual é o seu animal favorito?",
            ["Gosto de cães e gatos, mas não tenho um favorito específico."],
            
    ],
    [
            r"Qual é o seu hobby?",
            ["Meu hobby é ajudar as pessoas com informações e responder perguntas."],
            
    ],
    [
            r"Você gosta de música?",
            ["Sim, gosto de música!"],
            
    ],
    [
            r"Você pode me ajudar com alguma coisa?",
            ["Claro! Estou aqui para ajudar. O que você precisa?"],
            
    ],
    [
            r"Você pode me contar uma piada?",
            ["Claro! Por que o computador foi ao médico? Porque ele tinha um vírus!", "Por que o livro de matemática se suicidou? Porque tinha muitos problemas!"],
            
    ],
    [
            r"Você gosta de esportes?",
            ["Sim, gosto de esportes!"],
            
    ],
    [
            r"Você pode me dar uma dica de estudo?",
            ["Claro! Tente estudar em um ambiente tranquilo e sem distrações."],
            
    ],
    [
            r"Você tem alguma recomendação de filme?",
            ["Sim, recomendo assistir a um bom filme de comédia ou aventura."],
            
    ],
    [
            r"Você pode me ajudar com programação?",
            ["Claro! Posso ajudar com perguntas sobre programação e linguagens de programação."],
            
    ],
    [
            r"Você gosta de viajar?",
            ["Sim, viajar é uma ótima maneira de aprender sobre novas culturas e lugares."],
            
    ],
    [
            r"Você pode me dar uma dica de saúde?",
            ["Claro! Tente manter uma dieta equilibrada e fazer exercícios regularmente."],
            
    ],
    [
            r"Você gosta de ler?",
            ["Sim, gosto de ler livros e artigos interessantes."],
            
    ],
    [
            r"Você pode me ajudar com matemática?",
            ["Claro! Posso ajudar com perguntas de matemática e resolver problemas simples."],
            
    ],
    [
            r"Você gosta de cozinhar?",
            ["Sim, cozinhar é uma atividade divertida e criativa!"],
            
    ],
    [
            r"Você pode me dar uma dica de produtividade?",
            ["Claro! Tente fazer listas de tarefas e priorizar o que é mais importante."],
            
    ],
    [
            r"Você gosta de arte?",
            ["Sim, arte é uma forma incrível de expressão!"],
            
    ],
    [
            r"Você pode me ajudar com ciências?",
            ["Claro! Posso ajudar com perguntas sobre ciências e explicar conceitos básicos."],
            
    ],
    [
            r"Você gosta de história?",
            ["Sim, história é fascinante!"],
            
    ],
    [
            r"Você pode me ajudar com geografia?",
            ["Claro! Posso ajudar com perguntas sobre geografia e mapas."],
            
    ],
    [
            r"Você gosta de tecnologia?",
            ["Sim, tecnologia é incrível e está sempre evoluindo!"],
            
    ],
    [
            r"Você pode me ajudar com inglês?",
            ["Claro! Posso ajudar com perguntas sobre inglês e vocabulário."],
            
    ],
    [
            r"Você gosta de ciência da computação?",
            ["Sim, ciência da computação é uma área fascinante!"],
            
    ],
    [
            r"Você pode me ajudar com história da arte?",
            ["Claro! Posso ajudar com perguntas sobre história da arte e artistas famosos."],
            
    ],
    [
            r"Você gosta de filosofia?",
            ["Sim, filosofia é uma área interessante que faz você pensar sobre a vida."],
            
    ],
    [
            r"Você pode me ajudar com psicologia?",
            ["Claro! Posso ajudar com perguntas sobre psicologia e comportamento humano."],
            
    ],
    [
            r"Você gosta de sociologia?",
            ["Sim, sociologia é uma área interessante que estuda a sociedade e as interações humanas."],
            
    ],
    [
            r"Você pode me ajudar com economia?",
            ["Claro! Posso ajudar com perguntas sobre economia e conceitos básicos."],
            
    ],
    [
            r"Você gosta de política?",
            ["Sim, política é importante para entender como o mundo funciona."],
            
    ],
    [
            r"Você pode me ajudar com direito?",
            ["Claro! Posso ajudar com perguntas sobre direito e conceitos legais."],
            
    ],
    [
            r"Você gosta de música clássica?",
            ["Sim, música clássica é linda e cheia de emoção."],
            
    ],
    [
            r"Você pode me ajudar com literatura?",
            ["Claro! Posso ajudar com perguntas sobre literatura e autores famosos."],
            
    ],
    [
            r"Você gosta de cinema?",
            ["Sim, cinema é uma forma incrível de contar histórias."],
            
    ],
    [
            r"Você pode me ajudar com design gráfico?",
            ["Claro! Posso ajudar com perguntas sobre design gráfico e ferramentas de design."],
            
    ],
    [
            r"Você gosta de fotografia?",
            ["Sim, fotografia é uma forma maravilhosa de capturar momentos."],
            
    ],
    [
            r"Você pode me ajudar com marketing digital?",
            ["Claro! Posso ajudar com perguntas sobre marketing digital e estratégias online."],
            
    ],
    [
            r"Você gosta de programação web?",
            ["Sim, programação web é uma área interessante e em constante evolução."],
            
    ],
    [
            r"Você pode me ajudar com desenvolvimento de aplicativos?",
            ["Claro! Posso ajudar com perguntas sobre desenvolvimento de aplicativos móveis."],
            
    ],
    [
            r"Você gosta de jogos?",
            ["Sim, jogos são uma forma divertida de entretenimento."],
            
    ],
    [
            r"Você pode me ajudar com redes sociais?",
            ["Claro! Posso ajudar com perguntas sobre redes sociais e como usá-las efetivamente."],
            
    ],
    [
            r"Você gosta de ciência dos dados?",
            ["Sim, ciência dos dados é uma área fascinante que analisa informações para obter insights."],
            
    ],
    [
            r"Você pode me ajudar com inteligência artificial?",
            ["Claro! Posso ajudar com perguntas sobre inteligência artificial e suas aplicações."],
            
    ],
    [
            r"Você gosta de machine learning?",
            ["Sim, machine learning é uma área interessante que permite que os computadores aprendam com os dados."],
            
    ],
    [
            r"Você pode me ajudar com blockchain?",
            ["Claro! Posso ajudar com perguntas sobre blockchain e criptomoedas."],
            
    ],
    [
            r"Você gosta de segurança cibernética?",
            ["Sim, segurança cibernética é importante para proteger informações online."],
            
    ],
    [
            r"Você pode me ajudar com computação em nuvem?",
            ["Claro! Posso ajudar com perguntas sobre computação em nuvem e serviços relacionados."],
            
    ],
    [
            r"Você gosta de realidade virtual?",
            ["Sim, realidade virtual é uma tecnologia incrível que cria experiências imersivas."],
            
    ],
    [
            r"Você pode me ajudar com realidade aumentada?",
            ["Claro! Posso ajudar com perguntas sobre realidade aumentada e suas aplicações."],
            
    ],
    [
            r"Você gosta de robótica?",
            ["Sim, robótica é uma área fascinante que combina engenharia e programação."],
            
    ],
    [
            r"Você pode me ajudar com automação?",
            ["Claro! Posso ajudar com perguntas sobre automação e como implementá-la."],
            
    ],
    [
            r"Você gosta de ciência espacial?",
            ["Sim, ciência espacial é fascinante e nos ajuda a entender o universo."],
            
    ],
    [
            r"Você pode me ajudar com astronomia?",
            ["Claro! Posso ajudar com perguntas sobre astronomia e corpos celestes."],
            
    ],
    [
            r"Você gosta de biologia?",
            ["Sim, biologia é uma área interessante que estuda a vida e os organismos."],
            
    ],
    [
            r"Você pode me ajudar com química?",
            ["Claro! Posso ajudar com perguntas sobre química e reações químicas."],
    ],
    [
            r"Você gosta de física?",
            ["Sim, física é uma área fascinante que estuda as leis do universo."],
            
    ],
    [
            r"(?i)Você pode me ajudar com matemática avançada?",
            ["Claro! Posso ajudar com perguntas sobre matemática avançada e conceitos complexos."],
            
    ],
    [
            r"Você gosta de estatística?",
            ["Sim, estatística é uma ferramenta importante para analisar dados."],
            
    ],
    [
            r"Você pode me ajudar com probabilidade?",
            ["Claro! Posso ajudar com perguntas sobre probabilidade e como calculá-la."],
            
    ],
    [
            r"Você gosta de lógica?|Logica é importante?|Lógica é importante?",
            ["Sim, lógica é uma parte fundamental do raciocínio e da resolução de problemas."],
            
    ],
    [
            r"Você pode me ajudar com algoritmos?",
            ["Claro! Posso ajudar com perguntas sobre algoritmos e como eles funcionam."],
            
    ],
    [
            r"Você gosta de estruturas de dados?",
            ["Sim, estruturas de dados são essenciais para organizar e manipular informações."],
            
    ],
    [
            r"Você pode me ajudar com programação orientada a objetos?",
            ["Claro! Posso ajudar com perguntas sobre programação orientada a objetos e seus conceitos."],
            
    ],
    [
            r"Você gosta de desenvolvimento ágil?",
            ["Sim, desenvolvimento ágil é uma abordagem eficaz para gerenciar projetos de software."],
            
    ],

    ] 
def chat_bot():
    print("Olá! Eu sou o KauaBot. Como posso ajudar você hoje? (Digite Ctrl+C para sair)")
    chat = Chat(pares, reflections)
    while True:
        try:
            entrada = input("Você: ")
            resposta = chat.respond(entrada)
            if resposta:
                print("KauaBot:", resposta)
            else:
                print("KauaBot: Desculpe, não entendi. Pode reformular?")
        except (KeyboardInterrupt, EOFError):
            print("\nKauaBot: Até logo!")
            break

chat_bot()
    
    
        

