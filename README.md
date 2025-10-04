# JustPost website

Um site simples que permite postagem por usuários sobre diversos temas, em geral jogos ou relacionados.

---

### Índice

* [1. Sobre o Projeto](#1-sobre-o-projeto)
* [2. Manual do Usuário](#2-manual-do-usuário)
* [3. Como Executar o Projeto Localmente](#3-como-executar-o-projeto-localmente)
* [4. Relatório de Funcionalidades](#4-relatório-de-funcionalidades)

---

## 1. Sobre o Projeto

O **JustPost** é uma aplicação web construída com Python e Django que serve como uma plataforma de blog simplificada. O projeto foi desenvolvido para aplicar conceitos de desenvolvimento web backend, incluindo operações de banco de dados, autenticação de usuários e renderização de templates no lado do servidor, sem o uso de JavaScript.

**Autores:** Gabriel Moreira, Luiz Augusto Papa

### Funcionalidades Principais

* **Autenticação Completa:** Sistema de registro, login, logout, troca de senha e recuperação de senha por e-mail.
* **Gerenciamento de Posts (CRUD):**
    * **Create:** Usuários autenticados podem criar novos posts.
    * **Read:** Todos os visitantes podem visualizar a lista de posts e ler seu conteúdo completo.
    * **Update:** O autor de um post pode editá-lo após a publicação.
    * **Delete:** O autor de um post pode excluí-lo permanentemente.
* **Formatação de posts:** O conteúdo de cada post é interpretado como Markdown ao ser exibido, permitindo diretivas de formatação como negrito e itálico.
* **Controle de Permissões:** O sistema diferencia as ações disponíveis para visitantes, usuários logados e os autores dos posts, garantindo que apenas o autor possa modificar seu próprio conteúdo.

---

## 2. Manual do Usuário

Este manual explica como utilizar as principais funcionalidades do JustPost.

### Criando uma Conta

1.  Na barra de navegação superior, clique em **"Registrar"**.
2.  Preencha o formulário com um nome de usuário, endereço de e-mail (opcional, mas necessário para recuperação de senha) e uma senha.
3.  Clique em **"Criar conta"**. Você será redirecionado para a página inicial, já logado.

### Fazendo Login e Logout

* **Login:** Clique em **"Login"** na barra de navegação, insira seu nome de usuário e senha.
* **Logout:** Se estiver logado, clique no seu nome de usuário na barra de navegação no topo e clique no botão **"Logout"** no menu que aparece.

### Criando e Gerenciando Posts (CRUD)

1.  **Create:** Estando logado, clique em **"Criar Post"**. Preencha o título e o conteúdo e clique em "Salvar". Você será redirecionado para a página do seu novo post.
  - **Formatação:** Aqui, é possível o uso de formatação no conteúdo do post via **Markdown** (com a sintaxe de \*\*negrito\*\*, \_itálico\_ etc.).
2.  **Read:** A página inicial exibe a lista de todos os posts. Clique no título de qualquer post para ler seu conteúdo completo.
3.  **Update:** Na página de um post que você criou, um link **"Editar Post"** estará visível. Clique nele para modificar o título ou o conteúdo.
4.  **Delete:** Na página de um post que você criou, clique no link **"Deletar Post"**. Uma página de confirmação será exibida. Clique em "Sim, deletar" para remover o post permanentemente.

### Alterando e Recuperando a Senha

* **Alterar Senha (Logado):** Se você estiver logado, clique em **"Trocar Senha"** no menu. Você precisará informar sua senha antiga e a nova senha duas vezes.
* **Recuperar Senha (Esqueci a Senha):**
    1.  Na página de Login, clique no link **"Esqueceu sua senha?"**.
    2.  Digite o endereço de e-mail associado à sua conta.
    3.  Um e-mail com um link para redefinição de senha será enviado (no ambiente de desenvolvimento, este e-mail é impresso no console).
    4.  Clique no link e defina sua nova senha.

---

## 3. Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente de desenvolvimento.

### Pré-requisitos

* **Python 3.11+**
* **Git** para clonar o repositório.
* **uv**, um instalador e gerenciador de pacotes Python.
  - Usado para instalação de dependências em `pyproject.toml` (`django`, `django-stubs` e `markdown-it-py`)

Se você não tiver o `uv` instalado, instale-o com:
```bash
# No macOS e Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# No Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/PgBiel/web-prog-site.git
    cd web-prog-site
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    uv sync

    # Para Linux/macOS
    source .venv/bin/activate

    # Para Windows
    .\.venv\Scripts\activate
    ```

3.  **Aplique as migrações do banco de dados:**
    ```bash
    cd justpost
    python manage.py migrate
    ```

4.  **Rode o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

---

## 4. Relatório de Funcionalidades

Esta seção detalha o status de cada funcionalidade implementada no projeto.

### ✅ O que Funcionou

* **Registro, Login e Logout de Usuários:** O ciclo completo de autenticação foi testado e está 100% funcional. Usuários podem se registrar, entrar e sair da plataforma sem problemas.
* **Criação de Posts:** Usuários autenticados conseguem criar novos posts através do formulário, e os posts são corretamente associados ao autor.
* **Formatação de Posts:** O conteúdo de cada post está no formato Markdown, que é interpretado no backend na visualização para produzir texto em negrito, itálico, subtítulos etc.
* **Estilos e customização:** O site foi devidamente customizado com a ajuda do framework "pico.css".
  * Customizações incluem:
    - **Página 404 (Not Found)** própria ao acessar um link inválido;
    - **Formulários customizados**, alterando o template do Django;
    - Barra de navegação própria.
* **Visualização de Posts:** A lista de posts na página inicial e a página de detalhes de cada post estão funcionando como esperado para todos os tipos de usuário (visitantes e logados).
* **Edição e Deleção de Posts:** Apenas o autor original de um post consegue ver os botões de "Editar" e "Deletar" e acessar as respectivas páginas. A atualização e a exclusão no banco de dados funcionam corretamente.
* **Troca de Senha (Logado):** O formulário de troca de senha funciona, exigindo a senha antiga e validando a nova senha.

### ❌ O que Não Funcionou (ou Problemas Conhecidos)

* **Recuperação de Senha por E-mail:** O fluxo de recuperação de senha funciona no ambiente de desenvolvimento (com o e-mail sendo impresso no console), mas **não foi configurado um servidor de e-mail SMTP para produção**. Portanto, no site publicado, a funcionalidade não enviará e-mails reais.
  - Enfatize-se que a recuperação de senha **funciona** ao seguir o link impresso no console. Porém, o email com o link não será enviado de fato.
