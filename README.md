# Oficina de Refatoração

## Descrição do problema

Uma empresa chamada _Unstrict_ performou bem no ano de 2019, conseguiu
angariar mais contratos de projetos de software e gostaria de iniciar
o desenvolvimento de seus próprios produtos.

Para isso a _Unstrict_ precisava melhorar seu processo de contratação
de novos funcionários. Uma parte que consume um bom tempo do processo é
a filtragem de currículo.

Um dos colaboradores teve a ideia de criar um _filtro de currículos_ para
as vagas python da empresa. O programa, apesar de simples, já trouxe um
certo ganho de tempo no processo.

### Filtro de Curriculum Vitae

O _Filtro de Curriculum Vitae_ faz o seguinte processamento:

1. Baixa uma lista de currículos em PDF de um endereço na web com o formato:

http://host/curriculos/<email-do-candidato>.pdf

2. Lê todo o texto do documento

3. Busca um número de telefone no texto

4. Busca a palavra "python" no código

5. Se não encontra o telefone ou a palavra python no projeto, o candidato
é descartado

6. Retorna na saída do programa uma lista de e-mails

## Novos requisitos!

A _Unstrict_ recebeu alguns currículos de menores de idade, essas pessoas
devem ser descartadas.

A empresa também abriu uma vaga de desenvolvimento Elixir.

E não é mais necessário ter um telefone para contato, apenas o e-mail
é o suficiente.

### O Desafio

Não é possível adicionar esses novos comportamentos no código que existe
sem alterá-lo. Refatore o código que existe para que isso seja possível,
depois altere os comportamentos descritos.
