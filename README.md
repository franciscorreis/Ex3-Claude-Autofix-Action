# Exercício 3 — Claude-Autofix-Action

## Introdução

Este exercício tem o objetivo de testar o projeto Claude Autofix Action, disponível em [https://github.com/enriconunes/claude-autofix-action](https://github.com/enriconunes/claude-autofix-action). É importante manter a estrutura de ficheiros original e descrita no README do projeto; assim como proceder às configurações necessárias dentro repositório que forem utilizar. São as seguintes:

---

- **Criar um repositório publico** (com este código)

- **Configurar algumas definições:**  
  `Settings → Actions → General → Workflow permissions`
  - Selecionar **"Read and write permissions"**
  - Marcar **"Allow GitHub Actions to create and approve pull requests"**
  - Clicar **Save**

- **Adicionar chave de API Anthropic:**  
  `Settings → Secrets and variables → Actions → New repository secret`

  | Name | Value |
  |------|-------|
  | `ANTHROPIC_API_KEY` | A tua chave de console.anthropic.com |

---

## Exercício 3 — Caso real

Este exercício já pretende simular um caso mais real do uso desta ferramenta. Enquanto nos anteriores testámos e vimos exemplos simples, aqui a ideia é simular uma implementação de um sistema de autênticação, analisando a utilidade da resposta do agente mas sempre tendo em conta o ficheiro `REQUISITOS.md` (que simula o que nos foi pedido).
