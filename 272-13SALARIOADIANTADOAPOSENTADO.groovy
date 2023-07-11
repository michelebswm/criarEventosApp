if (!(TipoProcessamento.DECIMO_TERCEIRO_SALARIO.equals(calculo.tipoProcessamento) && SubTipoProcessamento.ADIANTAMENTO.equals(calculo.subTipoProcessamento))) {
    suspender \"O evento deve ser calculado apenas em processamentos de décimo terceiro (adiantamento)\"
}
if (!TipoMatricula.APOSENTADO.equals(matricula.tipo)) {
    suspender \"Este cálculo é executado apenas para aposentados\"
}
if (!Funcoes.recebeDecimoTerceiro()) {
    suspender \"O aposentado não tem direito a receber décimo terceiro\"
}
if (!periodoAquisitivoDecimoTerceiro.situacao.equals(SituacaoPeriodoAquisitivoDecimoTerceiro.EM_ANDAMENTO) && !periodoAquisitivoDecimoTerceiro.situacao.equals(SituacaoPeriodoAquisitivoDecimoTerceiro.ATRASADO)) {
    suspender \"O período aquisitivo de décimo terceiro já foi quitado ou está com situação diferente de 'Em andamento' ou 'Atrasado'\"
}
valorReferencia = Funcoes.avos13(12)
if (valorReferencia <= 0) {
    suspender \"Não há avos adquiridos no período aquisitivo de décimo terceiro\"
}
def vaux = Lancamentos.valor(evento)
if (vaux >= 0) {
    valorCalculado = vaux
} else {
    if (!evento.taxa || evento.taxa == 0) {
        suspender \"Para o cálculo do décimo terceiro adiantado de aposentados deve ser informada uma taxa e ela deve ser superior a zero\"
    }
    valorCalculado = aposentado.valorBeneficio * valorReferencia / 12 * evento.taxa / 100
}
