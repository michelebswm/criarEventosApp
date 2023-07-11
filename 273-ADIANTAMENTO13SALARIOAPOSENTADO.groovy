if (!(TipoProcessamento.DECIMO_TERCEIRO_SALARIO.equals(calculo.tipoProcessamento) && SubTipoProcessamento.INTEGRAL.equals(calculo.subTipoProcessamento))) {
    suspender \"Este evento deve ser calculado apenas no processamento de décimo terceiro (integral)\"
}
if (!TipoMatricula.APOSENTADO.equals(matricula.tipo)) {
    suspender \"Este cálculo é executado apenas para aposentados\"
}
if (!Funcoes.recebeDecimoTerceiro()) {
    suspender \"O aposentado não tem direito a receber décimo terceiro\"
}
if (!Funcoes.permitecalc13integral()) {
    suspender \"O período aquisitivo de décimo terceiro já foi quitado para o aposentados\"
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
        suspender \"No ano exercício de '${ano}' calculado, não há período aquisitivo de décimo terceiro com o status 'Quitado parcialmente' para realizar o desconto de décimo terceiro adiantado ou de desconto de décimo terceiro devido reversão da cessação\"
    }
    def movimentacoesAdiantamento = null
    periodo.movimentacoesByMotivo(MotivoMovimentacaoPeriodoAquisitivoDecimoTerceiro.ADIANTAMENTO_DECIMO_TERCEIRO)
            .each{ mov -> movimentacoesAdiantamento = mov }
    if (movimentacoesAdiantamento == null) {
        suspender \"Não há adiantamentos lançados ou cessações revertidas no período aquisitivo de décimo terceiro do ano exercício de '${ano}'\"
    }
    double valorAdiantado = periodo.totalMovimentacoesByMotivo(MotivoMovimentacaoPeriodoAquisitivoDecimoTerceiro.ADIANTAMENTO_DECIMO_TERCEIRO)
    if (valorAdiantado <= 0) {
        suspender \"Não há valores de décimo terceiro lançados no período aquisitivo do ano exercício de '${ano}' referentes a adiantamentos lançados ou cessações revertidas\"
    }
    valorCalculado = valorAdiantado
}
valorCalculado -= Funcoes.buscaValorEvento13SalarioIntegralAdiantado()
