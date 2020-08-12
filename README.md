# ouvICEx
Sistema web de ouvidoria pra denúncias e reclamações aberto aos alunos do ICEx - Trabalho de Engenharia de Software

# Sprint Planning

### Apresentar o sistema

- Como usuário do sistema, eu gostaria de entender como o sistema funciona e qual o seu propósito. 

- Tarefas: 
    - Criar a página inicial contendo uma explicação do funcionamento do sistema e seu propósito; (Giovanna)
    - Criar o menu. (Giovanna)

### Postar sugestão, reclamação ou denúncias

- Como usuário do sistema, eu gostaria de poder fazer sugestões, reclamações ou denúncias, de forma anônima, ou não, e informar o departamento alvo do meu comentário.

- Tarefas:
    - Criar estrutura do banco de dados para armazenar os envios; (Ana)
    - Criar a tabela no banco com as seguintes colunas: postagem, data, departamento do denunciado, departamento do usuário, tag que identifica o contexto da denúncia e tag de situação da denúncia; (Ana)
    - Criar um formulário funcional para os envios. (Ana)

### Ter um histórico de todas postagens

- Como usuário do sistema, eu gostaria de ser capaz de ler e filtrar as postagens feitas.

- Tarefas:
    - Criar a página para exposição dos comentários; (Isadora)
    - Criar filtros específicos por data, departamento (denunciado e usuário), tipo e estado da postagem. (Isadora)

### Requisição de análise de dados

- Como usuário do sistema, eu gostaria de ser capaz de acessar gráficos e estatísticas relacionadas às denúncias enviadas. 

- Tarefas:
    - Criar a página para exposição das análises dos dados que inicialmente apresentará a análise sem filtros; (Igor)
    - Criação dos filtros para os comentários por determinadas tags. (Igor)


### Gerenciar as postagens 

- Como administrador do sistema, eu gostaria de poder atualizar a situação dos envios (resolvido ou não)

- Tarefas:
    - Criar a página de login do administrador; (Thiago)
    - Criar a página do administrador, que estará conectado ao banco de dados contendo as postagens; (Thiago)
    - Adicionar botão que marca as postagens como resolvidas ou não (Thiago)
    - Criar filtros específicos por data, departamento (denunciado e usuário), tipo e estado da postagem. (Isadora)
