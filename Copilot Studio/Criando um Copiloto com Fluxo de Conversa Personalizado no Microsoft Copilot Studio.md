# Criando um Copiloto com Fluxo de Conversa Personalizado no Microsoft Copilot Studio

## 1. Criar um copiloto do zero

Selecione **Criar** e, em seguida, clique em **Novo agente**. Nessa etapa, você pode descrever com o auxílio de IA como deseja que o agente se comporte ou configurar tudo manualmente.

Defina:

- **Nome do copiloto**
- **Descrição de sua utilidade**
- **Instruções** (prompt que orientará o funcionamento do copiloto)
- **Base de conhecimento** (opcional)
- **Permissão para pesquisa na web** (opcional)

## 2. Personalizar um tópico

Após criar o agente, você pode adicionar tópicos, que representam ações executadas com base nas mensagens enviadas pelo usuário.

No menu do copiloto, acesse **Tópicos** e crie um novo.

Defina um **gatilho** relacionado a perguntas do usuário sobre um curso e crie uma resposta generativa informando locais onde ele poderá realizá-lo.

## 3. Personalizar mensagens de erro nos tópicos

Quando o usuário envia algo que não corresponde ao que o copiloto espera, é possível definir o comportamento padrão.

Nos próprios tópicos, existem as opções **Fallback** e **Melhora da conversa**:

- Em **Melhora da conversa**, a condição *“não está em branco”* permite executar uma ação e, em seguida, encerrar o tópico.
- Em **Todas as outras condições**, você pode configurar uma mensagem personalizada, como:  
  > "Desculpe, não foi possível encontrar a resposta que você esperava."

## 4. Ajustar a qualidade das respostas com IA generativa

Em **Propriedades** da opção **Criar respostas generativas**, é possível definir:

- A **fonte de conhecimento** utilizada  
- Se haverá **pesquisa na web**  
- Se a busca será feita **somente na base de conhecimento**  
- Se a IA pode utilizar seu **conhecimento geral**

Também é possível:

- Ajustar o **nível de moderação de conteúdo** (níveis mais baixos reduzem as chances de alucinações)
- Personalizar o **prompt** com variáveis ou instruções mais claras
