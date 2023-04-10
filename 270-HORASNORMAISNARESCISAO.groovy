Funcoes.somenteFuncionarios()
if (!TipoProcessamento.RESCISAO.equals(calculo.tipoProcessamento)) {
    suspender \"Este evento é calculado apenas em processamentos rescisórios\"
}
if (TipoAdmissao.TRANSFERENCIA.equals(funcionario.tipoAdmissao)) {
    suspender \"Este cálculo não é executado para funcionários recebidos por transferência\"
}
if (Funcoes.acumula(1, TipoValor.CALCULADO, calculo.competencia, calculo.competencia, TipoProcessamento.MENSAL) > 0) {
    suspender \"As horas normais da competência já foram calculadas em folhas anteriores do processamento mensal\"
}
def vaux = Lancamentos.valor(evento)
if (vaux >= 0) {
    valorReferencia = vaux
} else {
    def diastrab = Funcoes.diastrab()
    def horastrab = Funcoes.cnvdpbase(diastrab)
    def compoemes = Lancamentos.valorComposicaoMes()
    vaux = horastrab - compoemes
    if (vaux < 0) {
        vaux = 0
    }
    valorReferencia = vaux
}
def salario = funcionario.salario
if (salario <= 0) {
    suspender \"Não há valor de salário para o funcionário na competência\"
}
vaux = Funcoes.calcprop(salario, vaux)
valorCalculado = vaux.round(2)
if (valorCalculado > 0) {
    Bases.compor(salario, Bases.HORAEXTRA)
    Bases.compor(valorReferencia, Bases.PAGAPROP)
    Bases.compor(valorCalculado,
            Bases.SALBASE,
            Bases.PERIC,
            Bases.SIND,
            Bases.FGTS,
            Bases.IRRF,
            Bases.INSS,
            Bases.PREVEST,
            Bases.FUNDASS,
            Bases.FUNDOPREV,
            Bases.COMPHORAMES,
            Bases.FUNDFIN)
}
