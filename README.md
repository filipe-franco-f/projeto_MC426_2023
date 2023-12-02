# Gerenciador de República
Repositório de atividades para o projeto da disciplina MC426 turma A (Engenharia de Software) da Unicamp, 2023, segundo semestre. O tema escolhido foi uma aplicação de gerenciamento de república.

# Equipe
* Filipe Franco Ferreira - 251027
* Arimã da Silva Alves Batista - 194347
* Gabriel Batista Moura - 216101
* Andre Rocco Drisostes - 194148

## Diagrama de Componentes - Modelo C4
![alt text](https://github.com/filipe-franco-f/projeto_MC426_2023/blob/Padr%C3%A3o-de-projeto-adotado/C4-nivel3.png)

## Componentes do Sistema
* Login

  Autenticação de usuário a partir de suas credenciais para acessar o sistema.

* Tarefas

  Componente pelo qual ol o usuário pode cadastrar para um usuário e marcar como concluído as tarefas

* Agendamento de Reunião

  Componente onde o usuário Requerer uma reunião aos outros usuários

* Notificação

  Local onde fica armazenado as atualizações de tarefas e agendamentos que  requerem a atenção do usuário   

* Menu

  Navegação entre os componentes do sistema

* Banco de dados

  Onde armazena as informações dos usuários
  
## Estilo

O principal estilo utilizado é o de Invocação Implícita, em que todos os usuários em uma mesma república servem como Publishers e Subscribers. Ao se cadastrarem em na mesa República, eles podem agendar reuniões e cadastrar ou cumprir tarefas, que serão ações notificadas aos outros usuários.

## Padrão de Projeto

O padrão mais adequado adotado pela equipe foi o [Mediador](https://refactoring.guru/design-patterns/mediator), tendo em vista centralizar as informações e dependências entre componentes numa única página (Menu Inicial).
