if (!TipoProcessamento.RESCISAO.equals(calculo.tipoProcessamento)) {
    suspender \"Este evento é calculado apenas em processamentos rescisórios\"
}
if (TipoMatricula.APOSENTADO.equals(matricula.tipo) || TipoMatricula.PENSIONISTA.equals(matricula.tipo)) {
    suspender \"Este cálculo não é executado para aposentados e pensionistas\"
}
if (!Funcoes.permitecalc13integral()) {
    suspender 'A matrícula não tem direito a receber décimo terceiro ou o seu período aquisitivo contém uma situação não permitida para o cálculo do evento'
}
def vaux = Lancamentos.valor(evento)
if (vaux >= 0) {
    valorCalculado = vaux
} else {
    def ano = Funcoes.anoExercicio13()
    def periodo = null
    PeriodosAquisitivosDecimoTerceiro
            .buscaPeriodosAquisitivosBySituacao(SituacaoPeriodoAquisitivoDecimoTerceiro.QUITADO_PARCIALMENTE)
                .each{ p -> if (p.anoExercicio == ano) {
                    periodo = p
                }
            }
    if (periodo == null) {
        suspender \"No ano exercício de '${ano}' calculado, não há período aquisitivo de décimo terceiro com o status 'Quitado parcialmente' para realizar o desconto de décimo terceiro adiantado\"
    }
    def movimentacoesAdiantamento = null
    periodo.movimentacoesByMotivo(MotivoMovimentacaoPeriodoAquisitivoDecimoTerceiro.ADIANTAMENTO_DECIMO_TERCEIRO, MotivoMovimentacaoPeriodoAquisitivoDecimoTerceiro.ADIANTAMENTO_FERIAS)
            .each{ mov -> movimentacoesAdiantamento = mov }
    if (movimentacoesAdiantamento == null) {
        suspender \"Não há adiantamentos lançados no período aquisitivo de décimo terceiro do ano exercício de '${ano}'\"
    }
    double valorAdiantado = periodo.totalMovimentacoesByMotivo(MotivoMovimentacaoPeriodoAquisitivoDecimoTerceiro.ADIANTAMENTO_DECIMO_TERCEIRO) + periodo.totalMovimentacoesByMotivo(MotivoMovimentacaoPeriodoAquisitivoDecimoTerceiro.ADIANTAMENTO_FERIAS)
    if (valorAdiantado <= 0) {
        suspender \"Não há valores de adiantamentos de décimo terceiro lançados no período aquisitivo do ano exercício de '${ano}' para o cálculo\"
    }
    valorCalculado = valorAdiantado
}
if (Eventos.valor(274) > 0 && !folha.calculoVirtual) {
    Bases.compor(valorCalculado, Bases.FGTS13)
}
