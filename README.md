# Projeto Banese

Este é um projeto desenvolvido para o Banco do Estado Banese em conjunto com o Banese Labs, utilizando IA generativa para criar dados e enviá-los para filas de provisionamento e processamento. O projeto foi criado para seguir a normativa 4966 do Banco Central e auxiliar na padronização referente aos testes de provisionamento.

## Configuração do Ambiente

### Executando o Código Localmente (Sem Docker)

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/projeto-banese.git
    cd projeto-banese
    ```

2. **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Realize as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5. **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

### Executando o Código com Docker

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/projeto-banese.git
    cd projeto-banese
    ```

2. **Construa e inicie os containers Docker:**
    ```bash
    docker-compose up --build
    ```

3. **Acesse a aplicação em seu navegador:**
    ```
    http://localhost:8000
    ```

## Trabalho com Branches e Pull Requests

### Criando Branches

Trabalhar com branches permite que você mantenha seu código organizado e seguro. Aqui está como criar uma nova branch:

1. **Crie uma nova branch:**
    ```bash
    git checkout -b nome-da-sua-branch
    ```

2. **Faça as alterações desejadas no código.**

3. **Adicione e commit suas alterações:**
    ```bash
    git add .
    git commit -m "Descrição das suas alterações"
    ```

4. **Envie suas alterações para o repositório remoto:**
    ```bash
    git push origin nome-da-sua-branch
    ```

### Realizando Pull Requests

Realizar pull requests (PR) é uma prática importante para garantir a qualidade e a integridade do código. Aqui está como você pode fazer isso:

1. **Vá até o repositório no GitHub.**

2. **Clique no botão "New Pull Request".**

3. **Escolha a branch que você criou e clique em "Create Pull Request".**

4. **Adicione uma descrição detalhada do que foi alterado e clique em "Create Pull Request".**

### Benefícios de Trabalhar com Branches e Pull Requests

- **Isolamento de Funcionalidades:** Cada branch pode representar uma nova funcionalidade ou correção de bug, isolando as alterações e facilitando a gestão de versões.
- **Revisão de Código:** As pull requests permitem que outros desenvolvedores revisem o código antes de ser mesclado na branch principal, melhorando a qualidade do código.
- **Histórico de Alterações:** Mantém um histórico claro das alterações feitas, ajudando na documentação e rastreamento de mudanças.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto é licenciado sob a licença MIT.

