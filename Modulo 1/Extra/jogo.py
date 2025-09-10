import pygame

pygame.init()
tela = pygame.display.set_mode((400, 300))
fonte = pygame.font.SysFont(None, 36)

def desenhar_botao(texto, posicao, cor):
    texto_render = fonte.render(texto, True, (0, 0, 0))
    retangulo = texto_render.get_rect(center=posicao)
    pygame.draw.rect(tela, cor, retangulo.inflate(20, 20))
    tela.blit(texto_render, retangulo)
    return retangulo

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao.collidepoint(evento.pos):
                print("Botão clicado")
            
    tela.fill((200, 200, 220))
    botao = desenhar_botao("Clique Aqui", (200, 150), (100, 200, 100))
    pygame.display.update()

pygame.quit()