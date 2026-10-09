from datetime import date, timedelta

dia = int(input('Digite o dia em que a última menstruação começou: '))
mes = int(input('Digite o mês: '))
ciclo = int(input('Quantos dias costuma durar o ciclo? (em geral, 28): '))

hoje = date.today()

ultima = date(hoje.year, mes, dia)
# Só pedimos dia e mês, então o ano é o atual. Se a data cair no futuro, ela é do ano passado (ex.: hoje é 5/1 e a última foi em 20/12).
if ultima > hoje:
    ultima = date(hoje.year - 1, mes, dia)
   
proxima = ultima + timedelta(days=ciclo)

if hoje <= proxima:
    faltam = (proxima - hoje).days
    print(f'A próxima menstruação deve vir em {proxima.strftime("%d/%m")} (faltam {faltam} dias).')
else:
    atraso = (hoje - proxima).days
    print(f'A menstruação está atrasada há {atraso} dias. Era esperada em {proxima.strftime("%d/%m")}.')
    