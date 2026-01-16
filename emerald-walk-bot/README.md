
# Emerald Walk Bot

O script `emerald-walk-bot/leftright-walker.py` é um exemplo de automação projetado para simular o movimento de caminhada (esquerda e direita) em um emulador, como o **mGBA**.

---

### Funcionalidade

O bot executa um ciclo contínuo de comandos:
1.  Pressiona as teclas **'left'** e **'z'** simultaneamente por um período de tempo (1.7 segundos).
2.  Libera as teclas.
3.  Pressiona as teclas **'right'** e **'z'** simultaneamente pelo mesmo período.
4.  Libera as teclas.

Este padrão é útil para automatizar a caminhada em jogos que requerem a manutenção de uma direção e uma ação (como correr). A tecla 'z' pode ser alterada pela tecla similar ao botão B.

---

### Uso do Emerald Walk Bot

1. **Execute o Vs Code como Administrador**

2.  **Navegue até o diretório do bot:**

    ```bash
    cd emerald-walk-bot
    ```

3.  **Execute o script:**

    ```bash
    python leftright-walker.py
    ```

4.  **Atenção:** O script iniciará uma contagem regressiva de 5 segundos. **Neste período, você deve clicar na janela do emulador (mGBA ou outro) para garantir que o `pydirectinput` envie os comandos para a aplicação correta.**

5.  Para **encerrar** o bot, pressione `Ctrl + C` no terminal.
