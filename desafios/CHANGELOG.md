# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added descriptions.

### Changed

- Changed descriptions.

### Removed

- Removed descriptions.

## [1.0.0] 2025-09-26

### Added

- Metodo para despósito com verificação de valor para evitar entrada de valor negativo ou zero e aceita duas casas decimal.
- Função para saque com verificações de saldo, limite de operaçẽos de saque, limite de valor e valor mínimo para executar a operação.
- Função extrato para apresentar as operações realizadas e o saldo atual.

### Changed

- Alterado o escopo das operações, cada operação foi removido do main e passado para funções específicas para organizar o código.
- Alterado as variáveis isoladas para armazenar dados como saque, limite e extrato para um dict que organiza esses dados na variável conta.


[unreleased]: https://github.com/MuriloAM/trilha-python-dio/releases/tag/v1.0.0...HEAD
[1.0.0]: https://github.com/MuriloAM/trilha-python-dio/releases/tag/v1.0.0