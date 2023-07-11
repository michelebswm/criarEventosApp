Funcoes.somenteFuncionarios()
if (!TipoProcessamento.RESCISAO.equals(calculo.tipoProcessamento)) {
    suspender \"Este evento é calculado apenas em processamentos rescisórios\"
}
if (!Funcoes.permitecalc13integral()) {
    suspender 'A matrícula não tem direito a receber décimo terceiro ou o seu período aquisitivo contém uma situação não permitida para o cálculo do evento'
}
int avos13
int avos13Fgts
double valBasePropCalc
double valBaseFgts
if (Funcoes.dtrescisao()) {
    def vvar = Lancamentos.valor(evento)
    if (vvar >= 0) {
        valBasePropCalc = vvar
        valorCalculado = valBasePropCalc
        valBaseFgts = vvar
    } else {
        int avosAuxMat13 = Funcoes.avosAuxMat13()
        avos13Fgts = Funcoes.avos13(12, true) - avosAuxMat13
        avos13 = Funcoes.avos13(12) - avosAuxMat13
        if (avos13 <= 0) {
            suspender \"Não há avos adquiridos no período aquisitivo de décimo terceiro\"
        }
        double base = Eventos.valor(276) + Eventos.valor(277) + Eventos.valor(278) //apenas para gerar dependência
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
        valBasePropCalc = mediaVantagem.calcular(periodoAtual, avos13)
        valorCalculado = valBasePropCalc
        valBaseFgts = (valBasePropCalc * 12 / avos13) * avos13Fgts / 12
    }
    valorReferencia = avos13
    Bases.compor(valorCalculado,
            Bases.IRRF13,
            Bases.INSS13,
            Bases.PREVEST13,
            Bases.FUNDASS13,
            Bases.FUNDPREV13,
            Bases.FUNDFIN13)
    Bases.compor(valBaseFgts, Bases.FGTS13)
    double valEsocialFgts = valBaseFgts - valBasePropCalc
    Bases.compor(valEsocialFgts, Bases.FGTS13AFASES)
}
