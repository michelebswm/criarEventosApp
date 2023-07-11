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
    double base = Eventos.valor(302) + Eventos.valor(303) + Eventos.valor(304) //apenas para gerar dependência
    if (Funcoes.dtrescisao()) {
        def periodoAtual
        PeriodosAquisitivosDecimoTerceiro.buscaPeriodosAquisitivosBySituacao(
                SituacaoPeriodoAquisitivoDecimoTerceiro.ATRASADO,
                SituacaoPeriodoAquisitivoDecimoTerceiro.EM_ANDAMENTO,
                SituacaoPeriodoAquisitivoDecimoTerceiro.QUITADO_PARCIALMENTE).each {
            periodovenc ->
                if (periodovenc.anoExercicio == Datas.ano(calculo.competencia)) {
                    periodoAtual = periodovenc
                }
        }
        valorCalculado = mediaVantagem.calcular(periodoAtual, avosAuxMat13)
    } else {
        valorCalculado = mediaVantagem.calcular(avosAuxMat13)
    }
}
valorReferencia = avosAuxMat13
Bases.compor(valorCalculado,
        Bases.IRRF13,
        Bases.INSS13,
        Bases.FGTS13,
        Bases.FUNDPREV13,
        Bases.FUNDFIN13)
