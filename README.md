<div align='center'>

<img width="280" src="https://github.com/user-attachments/assets/1741e0bc-9b74-4e92-b4ad-36ce364a02ac" />

</div>

<div align = "center">

<p>

<a href="#descricao">Descrição</a> &#xa0; | &#xa0;
<a href="#erros">Erros</a> &#xa0; | &#xa0;
<a href="#arquitetura">Arquitetura</a> &#xa0; | &#xa0;
<a href="#testes">Testes</a> &#xa0; | &#xa0;
<a href="#referencias">Referências</a>

</p>

</div>

<div id = "descricao">

## :pushpin: Descrição ##

<p>

Esse é um repositório do Sistema Bancário, um projeto voltado para o processo seletivo para desenvolvedor pleno no Banco Itaú.

O objetivo desse projeto era identificar os erros que estão no [código principal][codigo_sistema_bancario] e propor as correções.

</p>

</div>

<div id = "erros">

## :warning: Erros ##

Todos os erros identificados:

* Linha 03 - erro de sintaxe da variável (saldo_ inicial)

```python
def __init__(self, saldo_inicial=0):
    self.saldo = saldo_ inicial  # erro 01
```

* Linha 06 - erro de lógica (depósito deveria somar o valor)

```python
def depositar(self, valor):
    self.saldo -= valor  # erro 02
```

* Linha 21 - erro de sintaxe (f-strings -> R${valor})

```python
destinatario.depositar(valor)
print(f"Transferência de R$(valor) realizada. Novo saldo: R${self.saldo}")  # erro 03
```

* Linha 52, 55, 58 e 61 - erro de lógica (o usuário deve escolher um valor entre 1 e 4, não A e D)

```python
if escolha == "A":  # erro 04
    valor_deposito = obtem_valor_input("Informe o valor a ser depositado na Conta 1: R$")
    conta1.depositar(valor_deposito)
elif escolha == "B":  # erro 05
    valor_saque = obter_valor_input("Informe o valor a ser sacado da Conta 1: R$")
    conta1.sacar(valor_saque)
elif escolha == "C":  # erro 06
    valor_transferencia = obter_valor_input("Informe o valor a ser transferido da Conta 1 para Conta 2: R$")
    conta1.transferir(conta2, valor_transferencia)
elif escolha == "D":  # erro 07
    break
```

* Linha 53 - erro de sintaxe da função (obtem_valor_input)

```python
if escolha == "A":
    valor_deposito = obtem_valor_input("Informe o valor a ser depositado na Conta 1: R$")  # erro 08
```

* Linha 54, 57 e 60 - é responsabilidade do banco realizar as transações e não da própria conta

```python
if escolha == "A":
    valor_deposito = obtem_valor_input("Informe o valor a ser depositado na Conta 1: R$")
    conta1.depositar(valor_deposito)  # "erro" 09
elif escolha == "B":
    valor_saque = obter_valor_input("Informe o valor a ser sacado da Conta 1: R$")
    conta1.sacar(valor_saque)  # "erro" 10
elif escolha == "C":
    valor_transferencia = obter_valor_input("Informe o valor a ser transferido da Conta 1 para Conta 2: R$")
    conta1.transferir(conta2, valor_transferencia)  # "erro" 11
elif escolha == "D":
    break
```

</div>

<div id = "arquitetura">

## :rocket: Arquitetura ##

<p>

A arquitetura utilizada nesse projeto foi a *Clean Architecture*. O objetivo era manter uma estrutura organizada e de fácil entendimento.

Com o desenvolvimento foi necessário o uso de entitdades modelo (MVC) para definir quais seriam as entidades do sistema e, com o objetivo
de explorar mais os conceitos de orientação a objetos, foi feito o uso de uma classe abstrata abordando o princípio de herança.

</p>

</div>

<div id = "testes">

## :computer: Testes ##

<p>

Para os casos de testes unitários foi utilizado o [*PyTest*][pytest].

Como o desenvolvimento dos testes para esse projeto não teve tanta complexidade, não houve necessidade de fazer uso de todas as das
funcionalidades do PyTest, como _Mock_ e _Fixture_, que são usadas frequentemente durtante o desenvolvimento na equipe.

</p>

</div>

<div id = "referencias">

## :key: Referências ##

Alguns locais de onde me baseei para realizar o projeto:

* [Naval Battle - Iuri Almeida][naval_battle]

:mag: &#xa0; Os ícones usados nesse README foram tirados desse [repositório][icones].

</div>

<!-- Links -->
[pytest]: https://docs.pytest.org/en/stable/
[icones]: https://gist.github.com/rxaviers/7360908
[naval_battle]: https://github.com/Iuri-Almeida/naval-battle
[codigo_sistema_bancario]: https://github.com/Iuri-Almeida/bank-system/blob/master/C%C3%B3digo%20Sistema%20Banc%C3%A1rio%20-%20Pyhton.txt