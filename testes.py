#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy

class Contrato(scrapy.Item):
    unidade_gestora =scrapy.Field()
    data_emissao =scrapy.Field()
    instrumento_contrato =scrapy.Field()
    numero_contrato =scrapy.Field()
    data_expiracao =scrapy.Field()
    tipo =scrapy.Field()
    fornecedor =scrapy.Field()
    cnpj_cpf =scrapy.Field()
    aditivo =scrapy.Field()
    processo =scrapy.Field()
    valor =scrapy.Field()

def first(sel, xpath):
    return sel.xpath(xpath).extract_first()


class VerificadordeSiteDaTransparencia(scrapy.Spider):
    name = 'verificador-de-site-da-transparencia'    
    start_urls =  ['http://200.217.192.171/pronimtb/index.asp?acao=1&item=1']

    custom_settings = {
        'DOWNLOAD_DELAY': 3,
    }

    def parse(self, response):
        #link_transparencia = response.xpath("//*").extract()
            # "//div/*/@href[contains(., 'transparencia')]") #funcionando 
             # u"//td/*[contains(., 'Administração')]").extract()
            #"//*/@href").extract()
       # self.log('RESULTADO: %s' % link_transparencia)
        # return scrapy.FormRequest.from_response(
        #     response,
        #     formdata={"cmbUnidadeLC": "DW_LC131_AG_0", "cmbDataVigenciaLC": "2015", "cmbUnidadeGestoraLC": "-1"},
        #     callback=self.coleta_contratos
        # )#"ASPSESSIONIDSQACDQRR": "GFEBGMGDPHHJHGBKNINAGHMG", 
        #session[0]: session[1].split(";")[0]
        session = response.headers.get("Set-Cookie").split("=") #não funciona pegando sessão por aqui, só pelo navegador
        #self.log(response.headers)
        cookies = {"ASPSESSIONIDSSBCCRRQ": "KAHHCIDAFEDEAOBEEJFJCFDD", "ckPatrimonioSituacaoBem":-1, "ckPatrimonioStatus":-1, "ckUnidadeGestoraLC":-1, "ckAno":"null", "ckExercicio":"null", "ckApresentarPor":0, "ckEmpenhoOrcamentario":1, "ckEmpenhoExtra":4, "ckEmpenhoResto":2, "ckEstado":-1, "ckMunicipio":-1, "ckDataFiltro":1, "ckCategoria":"null"}
        #self.log(cookies)
        return scrapy.FormRequest.from_response( #-> funcionou com sessão valida
            response,
            cookies = cookies,
            #""url"": "http://200.217.192.171/pronimtb/index.asp?acao=1&item=1",
            formname="frmFormulario",
            formdata={"hndAcao": "1", "hndItem": "1", "hndvisao": "1", "hndAPDtIni": "", "hndAPLotacao": "", "hndAPCargo": "", "hndAPNivel": "", "hndTipoEsportacaoDados": "", "cmbTipoEsportacaoDados": "2", "cmbUnidadeLC": "DW_LC131_AG_0", "txtNomePublicacoes": "", "cmbTemaPublicacoes": "", "hndAnoCargasPublicacoes": "", "cmbAnoCargasPublicacoes": "", "hndPeriodoPublicacao": "", "txtReferenciaDePublicacoes": "", "txtReferenciaAtePublicacoes": "", "cmbReferenciaDePublicacoes": "", "cmbReferenciaAtePublicacoes": "", "hndEntidadePublicacoes": "", "cmbEntidadePublicacoes": "", "cmbUnidadeGestoraPublicacoes": "", "hndDataVigenciaLC": "", "cmbDataVigenciaLC": "2015", "hndAno": "", "hndExercicio": "", "hndTipoMovimento": "", "cmbTipoMovimento": "0", "hndUnidadeGestoraLC": "CONSOLIDADA", "cmbUnidadeGestoraLC": "-1", "hndUnidadeCP": "SELECIONE", "cmbUnidadeCP": "", "txtNumeroContrato": "", "txtAnoContrato": "", "hndSitProcessoLicit": "", "cmbSitProcessoLicit": "", "txtNumeroProcesso": "", "txtAnoProcesso": "", "hndDataFiltro": "", "cmbDataFiltro": "1", "txtDataInicial": "", "txtDataFinal": "", "hndMesInicial": "SELECIONE", "cmbMesInicial": "", "hndMesFinal": "SELECIONE", "cmbMesFinal": "", "hndUnidadeGP": "", "hndVinculoGP": "SELECIONE", "cmbVinculoGP": "", "cmbDataGP": "", "hndUnidadeGestora": "SELECIONE", "cmbUnidadeGestora": "", "txtNomeFuncionario": "", "txtCargoFuncionario": "", "txtLotacaoFuncionario": "", "hndApresentarPorCP": "", "cmbApresentarPor": "0", "cmbEstoqueUnidadeCM": "", "hndEstoqueDataVigenciaLC": "SELECIONE", "cmbEstoqueDataVigenciaLC": "", "hndEstoqueUnidadeGestoraLC": "%0D%0A++++++++++++++++++++++++++++++++++++SELECIONE%0D%0A++++++++++++++++++++++++++++++++", "cmbEstoqueUnidadeGestoraLC": "", "hndEstoqueAlmoxarifado": "%0D%0A++++++++++++++++++++++++++++++++++++SELECIONE%0D%0A++++++++++++++++++++++++++++++++", "cmbEstoqueAlmoxarifado": "", "txtEstoqueLocalizacao": "", "txtEstoqueMaterial": "", "hndEstoqueMesInicial": "SELECIONE", "cmbEstoqueMesInicial": "", "hndEstoqueMesFinal": "SELECIONE", "cmbEstoqueMesFinal": "", "hndEstoqueTipoMovimento": "SELECIONE", "cmbEstoqueTipoMovimento": "-1", "txtEstoqueClassificacao": "", "cmbPatrimonioUnidadePP": "", "hndPatrimonioUnidadeGestoraLC": "%0D%0A++++++++++++++++++++++++++++++++++++SELECIONE%0D%0A++++++++++++++++++++++++++++++++", "cmbPatrimonioUnidadeGestoraLC": "", "txtPatrimonioDescricaoBem": "", "txtPatrimonioDataInicial": "", "txtPatrimonioDataFinal": "", "txtPatrimonioClassificacao": "", "txtPatrimonioLocalizacao": "", "hndPatrimonioSituacaoBem": "SELECIONE", "cmbPatrimonioSituacaoBem": "-1", "hndPatrimonioStatus": "SELECIONE", "cmbPatrimonioStatus": "-1", "hndPatrimonioTipoIngresso": "", "cmbPatrimonioTipoIngresso": "", "hndApresentarPorGP": "SELECIONE", "hndApresentar": "", "ckTipoGestaoPessoas": "-1", "txtLotacaoCargo": "", "ckEmpenhoOrcamentario": "1", "txtNomeFornecedor": "", "txtCPFCNPJFornecedor": "", "hndDiariasPassagens": "SELECIONE", "cmbDiariasPassagens": "", "txtEmpenho": "", "hndEstado": "", "cmbEstado": "-1", "hndMunicipio": "", "cmbMunicipio": "-1", "txtValorContratoInicial": "", "txtValorContratoFinal": "", "txtObjeto": "", "txtDescricaoProduto": "", "hndCategoria": "", "confirma": "Gerar"},
            #formdata={"cmbUnidadeLC": "DW_LC131_AG_0", "cmbDataVigenciaLC": "2015", "cmbUnidadeGestoraLC": "-1"},
            callback=self.coleta_contratos
        )
        #self.log(response.headers.getlist("Set-Cookie"))
        # return 

    def aguarde(self, response):
        yield scrapy.Request(response.url, self.coleta_contratos)


    # Pegando contratos de Itaperuna e salvando em json
    def coleta_contratos(self, response):
        self.log(response.text)
        linha = response.xpath("//tr[@id='tbTabela_parLinha1']")
        linhas = response.xpath("//table[@id='tbTabela']")

        contratos = []

        for index, cada_linha in enumerate(linhas.xpath("//table[@id='tbTabela']/tr")):
            if(index > 2):
                args = (index, cada_linha.extract())
                # self.log("Linha %d: %s" %args)

                parametros = []
                for index_2, cada_coluna in enumerate(cada_linha.xpath("td")):
                    parametros.append(cada_coluna.xpath("a/text()").extract())
                    args_2 = (index_2, parametros[index_2])
                    self.log("Coluna %d: %s" %args_2)

                if parametros:
                    contrato = Contrato()
                    contrato['unidade_gestora'] = parametros[0]
                    contrato['data_emissao'] = parametros[1]
                    contrato['instrumento_contrato'] = parametros[2]
                    contrato['numero_contrato'] = parametros[3]
                    contrato['data_expiracao'] = parametros[4]
                    contrato['tipo'] = parametros[5]
                    contrato['fornecedor'] = parametros[6]
                    contrato['cnpj_cpf'] = parametros[7]
                    contrato['aditivo'] = parametros[8]
                    contrato['processo'] = parametros[9]
                    contrato['valor'] = parametros[10]

                    yield contrato
                    contratos.append(contrato);
        # yield contratos
        # self.log(contratos)

        # for coluna in linha.xpath("//td/a/text()").extract():
        #     self.log("Coluna: %s" %coluna)

        #self.log(response.xpath("//tr[@id='tbTabela_parLinha1']/td[1]/a/text()").extract())


        return
# class YoutubeChannelLister(scrapy.Spider):
#     name = 'channel-lister'
#     youtube_channel = 'portadosfundos'
#     start_urls = ['https://www.youtube.com/user/%s/videos' % youtube_channel]

#     def parse(self, response):
#         for sel in response.css("ul#channels-browse-content-grid > li"):
#             yield {
#                 'link': response.urljoin(first(sel, './/h3/a/@href')),
#                 'title': first(sel, './/h3/a/text()'),
#                 'views': first(sel, ".//ul/li[1]/text()"),
#             }

            # scrapy runspider testes.py -o portadosfundos.csv

