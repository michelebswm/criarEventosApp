if (!Funcoes.permiteCalculoAuxilioMaternidade()) {
    suspender 'A matrícula não tem direito a receber o abatimento salário maternidade'
}
if (!Funcoes.permitecalc13integral()) {
    suspender 'A matrícula não tem direito a receber décimo terceiro ou o seu período aquisitivo contém uma situação não permitida para o cálculo do evento'
}
int avosAuxMat13
def vvar = Lancamentos.valor(evento)
if (vvar >= 0) {
    valorCalculado = vvar
} else {
    if (!TipoProcessamento.RESCISAO.equals(calculo.tipoProcessamento) && !(TipoProcessamento.DECIMO_TERCEIRO_SALARIO.equals(calculo.tipoProcessamento) && SubTipoProcessamento.INTEGRAL.equals(calculo.subTipoProcessamento))) {
        suspender 'Este evento deve ser calculado apenas nos processamentos de rescisão e décimo terceiro (integral)'
    }
    avosAuxMat13 = Funcoes.avosAuxMat13()
    if (avosAuxMat13 <= 0) {
        suspender 'Não há avos de auxílio maternidade no período aquisitivo de décimo terceiro'
    }
    double salario = Funcoes.remuneracao(matricula.tipo).valor
    valorCalculado = salario * avosAuxMat13 / 12
}
valorReferencia = avosAuxMat13
Bases.compor(valorCalculado,
        Bases.IRRF13,
        Bases.INSS13,
        Bases.FGTS13,
        Bases.FUNDPREV13,
        Bases.FUNDFIN13)
