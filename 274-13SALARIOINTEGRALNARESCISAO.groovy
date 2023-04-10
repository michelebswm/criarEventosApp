if (!TipoProcessamento.RESCISAO.equals(calculo.tipoProcessamento)) {
    suspender \"Este evento é calculado apenas em processamentos rescisórios\"
}
if (TipoMatricula.APOSENTADO.equals(matricula.tipo) || TipoMatricula.PENSIONISTA.equals(matricula.tipo)) {
    suspender \"Este cálculo não é executado para aposentados e pensionistas\"
}
if (!Funcoes.permitecalc13integral()) {
    suspender 'A matrícula não tem direito a receber décimo terceiro ou o seu período aquisitivo contém uma situação não permitida para o cálculo do evento'
}
if (Funcoes.dtrescisao()) {
    int avosAuxMat13 = Funcoes.avosAuxMat13()
    int avos13 = Funcoes.avos13(12) - avosAuxMat13
    if (avos13 <= 0) {
        suspender \"Não há avos adquiridos no período aquisitivo de décimo terceiro\"
    }
    double valorCalcFgts
    int avos13Fgts = Funcoes.avos13(12, true) - avosAuxMat13
    def vvar = Lancamentos.valor(evento)
    if (vvar >= 0) {
        valorCalculado = vvar
        valorCalcFgts = vvar * avos13Fgts / avos13
    } else {
        double salario = Funcoes.remuneracao(matricula.tipo).valor
        valorCalculado = salario * avos13 / 12
        valorCalcFgts = salario * avos13Fgts / 12
    }
    valorReferencia = avos13
    Bases.compor(valorCalcFgts, Bases.FGTS13)
    Bases.compor(valorCalculado,
            Bases.IRRF13,
            Bases.INSS13,
            Bases.PREVEST13,
            Bases.FUNDASS13,
            Bases.FUNDPREV13,
            Bases.FUNDFIN13)
}
