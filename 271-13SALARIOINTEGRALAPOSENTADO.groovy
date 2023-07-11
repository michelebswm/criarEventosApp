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
    suspender \"O período aquisitivo de décimo terceiro já foi quitado para o aposentado\"
}
valorReferencia = Funcoes.avos13(12)
if (valorReferencia <= 0) {
    suspender \"Não há avos adquiridos no período aquisitivo de décimo terceiro\"
}
def vvar = Lancamentos.valor(evento)
if (vvar >= 0) {
    valorCalculado = vvar
} else {
    valorCalculado = aposentado.valorBeneficio * valorReferencia / 12
}
Bases.compor(valorCalculado,
            Bases.IRRF13,
            Bases.INSS13,
            Bases.PREVEST13,
            Bases.FUNDASS13,
            Bases.FUNDPREV13,
            Bases.FUNDFIN13,
            Bases.PAISIR13SA)
