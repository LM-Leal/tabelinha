# Tabelinha

Programa de terminal em Python que estima a data da próxima menstruação e avisa se ela está atrasada.

A pessoa informa o dia em que a última menstruação começou e quanto dura o ciclo. O programa compara com a data de hoje e responde quantos dias faltam ou há quantos dias está atrasada.

## Exemplo de uso

```
Digite o dia em que a última menstruação começou: 20
Digite o mês: 9
Quantos dias costuma durar o ciclo? (em geral, 28): 28
A próxima menstruação deve vir em 18/10 (faltam 9 dias).
```

```
Digite o dia em que a última menstruação começou: 1
Digite o mês: 9
Quantos dias costuma durar o ciclo? (em geral, 28): 28
A menstruação está atrasada há 10 dias. Era esperada em 29/09.
```

## Como rodar

Precisa do Python 3 instalado. Não usa nenhuma biblioteca externa.

```
python ciclo.py
```

## Como funciona

1. Monta a data da última menstruação com o dia e o mês digitados e o ano atual.
2. Soma a duração do ciclo a essa data para chegar à data esperada.
3. Compara a data esperada com hoje: se ainda não chegou, mostra quantos dias faltam; se já passou, mostra o atraso.

Tudo com o módulo `datetime`, que já cuida de meses com 30 ou 31 dias e de anos bissextos.

### A virada do ano

Como a pessoa digita só dia e mês, o programa assume o ano atual. Isso quebrava em janeiro: se hoje é 5/1 e a última menstruação foi em 20/12, a data montada ficava em dezembro do ano *seguinte*, e o programa dizia que faltavam 377 dias.

A correção: se a data montada cair depois de hoje, ela só pode ser do ano anterior. Testei fixando a data de hoje em 5/1/2027 para simular o caso.

## Aviso

O cálculo é uma estimativa baseada na média do ciclo. Não substitui acompanhamento médico e **não serve como método contraceptivo**.

## Próximos passos

- [ ] Validar a entrada (hoje, digitar uma letra ou uma data impossível, como 31/02, encerra o programa com erro)
- [ ] Salvar o histórico de ciclos num arquivo CSV
- [ ] Calcular a duração média do ciclo a partir do histórico, em vez de pedir esse número
- [ ] Mostrar a janela fértil estimada

## Tecnologias

- Python 3
- Módulo `datetime` (biblioteca padrão)