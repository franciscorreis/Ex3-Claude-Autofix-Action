# Requisitos — Validação de Password

## Contexto

Esta funcionalidade faz parte do módulo de registo e autenticação de utilizadores.
Antes de criar a conta, o sistema deve validar que a password cumpre os critérios mínimos de segurança.

## Requisitos

A password deve cumprir **todos** os seguintes critérios:

- Mínimo de **8 caracteres**
- Pelo menos **1 letra maiúscula** (A-Z)
- Pelo menos **1 letra minúscula** (a-z)
- Pelo menos **1 carácter especial** (ex: `!`, `@`, `#`, `$`, ...)

## Exemplos

| Password       | Válida? | Motivo                          |
|----------------|---------|---------------------------------|
| `abc123`       | Não     | 6 caracteres, sem maiúscula nem especial |
| `Abc123`       | Não     | 6 caracteres, sem especial      |
| `Abc123!`      | Não     | 7 caracteres                    |
| `Abc1234!`     | Sim     | 8 caracteres, cumpre tudo       |
| `Segura@2024`  | Sim     | 11 caracteres, cumpre tudo      |
