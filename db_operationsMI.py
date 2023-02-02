import psycopg2
from psycopg2 import extras


def save_produto(PRODUTO,
    CUSTO, QUANTIDADE_CAIXA, CUSTO_FIXO, CONTROLA_PECA, CUSTO_MEDIO, FATOR_CA, UNIDADE_USO, FATOR_AU, DEPARTAMENTO, COLECAO, BAIXA_ESTOQUE_FICH,
    SUBST_ICMS, ICMS, AL_ICMS, IPI_INCIDE_ICMS, SIT_TRIB, MOEDA_COMPRA, LARGURA, AL_IPI, RED_ICMS, RED_IPI, DESCRICAO1, REFERENCIA,
    DESCRICAO2, PESO, GRUPO, TIPO, COD_PRODUTO, GRADE, DATA_ATUALIZACAO, DATA_CADASTRO, IPI, TIPO_PROD, CONTROLA_TAMANHO, UNIDADE_ARMAZEN,
    UNIDADE_COMPRA, CONTROLA_COR, CLASSIFICACAO_FIS, CONTROLA_ESTAMPA, ESTOQUE_MINIMO, PRECISAO, CONTROLA_LOTE, ESTOQUE_MAXIMO, INTEIRO,
    CURVA_ABC, CLASS_PROD, AL_ISS, WEB, PROMOCAO, EXCLUI_FIN, COD_PRODUTO2, MARCA, DIVISAO, CLIENTE, IBAMADO, COD_IBAMA, GRADE_FORN,
    PAIS, CATEGORIA, SUBCOLECAO, FORNECEDOR, INFLUI_MODELAGEM, DESCRICAO_SF, MOVIMENTA_PESO, FAIXA_PRECO, MODELO, MATERIAL, N_CONTRATO,
    PRODBASE, CODBASE, QUALIDADE, DATA_DISP, COD_NCM, APROVEITA_IPI, APROVEITA_ICMS, CENTRO_CUSTO_PAD, CC_RECEITA, CC_CUSTO, CC_DESPESA,
    CC_ESTOQUE, CC_RESERVA, CC_TERCEIROS, CC_BENEFICIAMENTO, CC_INVENTARIO, PCONTA, PRODUTO_CLASS_SEFAZ, SERVICO_SUJEITO_ICMS, SERVICO_SUJEITO_ISS,
    SERVICO_SUJEITO_IPI, CC_DEVVENDA, CC_DEVCOMPRA, BLOQUEIA_VENDA, DESCRICAO_ETIQ, DESCRICAO_TRADUZIDA, EMBALAGEM, CC_PRODUCAO, HORIZONTE_ESTOQ_PROJETADO,
    BLOQUEIA_PV, CLFIS, CC_COMISSAO_DESP, ESTILISTA, MODELISTA, COD_PRODUTO_FORNEC, CC_TRANSPORTE_DESP, STATUS, PRIORIDADE_GRUPO, CC_COMISSAO_DESP_FUN,
    DESCRICAO_ORIGINAL, ID_KIT, QT_KIT, CODIGO_ANVISA, DATA_ANVISA, DIAS_VALIDADE, NAO_INCIDE_PIS_COFINS, NAO_CONTROLA_ESTOQUE, LOCALEXEC,
    CODLS, GRAMASM2, LAVAGEM, INATIVO, CARTELA, ALTURA, COMPRIMENTO, COD_DES, KIT, PROFUNDIDADE, INDICADOR_PRODEPE, CODIGO_PRODEPE,
    PERFIL_IMPOSTO, PERCENTUAL_LICENCIAMENTO, NAO_CALCULA_COMISSAO, ORIGEM_PROD, PROPORCAO_PRECO, PERMITE_PEDIDO_SEM_ESTOQUE, LEAD_TIME_ENTREGA,
    PRE_VENDA, DATA_LANCAMENTO, QTDE_MAX_VENDA, CODIGO_YOUTUBE, COD_ISBN, EXIGE_RECEITA, CLASS_PROD_SPED, FCI_NUMERO, FCI_PERCENTUAL,
    APELIDO_COR, APELIDO_ESTAMPA, APELIDO_TAMANHO, MESES_GARANTIA, PERMITE_PRESENTE, TIPO_ISS, NAT_ISS, PRECO_AUTOMATICO, PRODUTO_VOLUME,
    NUMERO_VOLUME, TRANS_ID, PRAZO_LOTE_VENCIDO, URL_PRODUTO, QUANTIDADES_MULTIPLAS, ACRESCIMO_QUEBRA, ESTRATEGIA_ABASTECIMENTO, ADICIONA_LOTE_PROD_NFE,
    PRECO_PROPORCIONAL_CODBASE, CONFERENCIA_AUTOMATICA, FINALIZA_AUTO_TAREFA_SEPARACAO, CODBASE_COMPONENTE_KIT, GRUPO_SEPARACAO, ALTERNATIVO_PRODUTO_BASE,
    TABELA_MEDIDA, COD_MPN, CODLS_SP, COMPRADOR, GRADE_DISTRIBUICAO, FAIXA_VALOR, UNIDADE_TRIB, FATOR_TRIB, PEDIDOC_ORIGEM, UTILIZA_FIFO,
    PERMITE_LOTE_EMBRANCO, IBGE_MUNCODDV, COD_BENEF_FISCAL, UNIDADE_USO_OLD, UNIDADE_ARMAZEN_OLD, UNIDADE_COMPRA_OLD, CEST, WMS, PESO_BRUTO_MEDIO,
    COD_INF_NUTRICIONAL, COD_INF_EXTRAS, CODPRODANP, FORNECEDOR_JUST_IN_TIME, BLOQUEIA_PED_COMPRA, BLOQUEIA_COMPRA, DESCRICAO_NFE, ALTURA_REAL,
    LARGURA_REAL, COMPRIMENTO_REAL, PESO_REAL, QUANT_FECHA_VOLUME_WMS, ID_CLASS_PROD, UTILIZA_LOTE_COMERCIAL, DCRE, TIPO_EMBALAGEM, PERC_INC_ALTURA,
    EMPILHAMENTO_MAXIMO, MOVIMENTA_EST_VOLUME, VERSAO_VOLUME, CNAE_SERV, CODTRIBMUN):
     
    
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="newport",
            user="postgres",
            password="musica2000"
        )
        
        cursor = connection.cursor()
        
        postgreSQL_insert_query = """INSERT INTO PRODUTOS (PRODUTO,
    CUSTO, QUANTIDADE_CAIXA, CUSTO_FIXO, CONTROLA_PECA, CUSTO_MEDIO, FATOR_CA, UNIDADE_USO, FATOR_AU, DEPARTAMENTO, COLECAO, BAIXA_ESTOQUE_FICH,
    SUBST_ICMS, ICMS, AL_ICMS, IPI_INCIDE_ICMS, SIT_TRIB, MOEDA_COMPRA, LARGURA, AL_IPI, RED_ICMS, RED_IPI, DESCRICAO1, REFERENCIA,
    DESCRICAO2, PESO, GRUPO, TIPO, COD_PRODUTO, GRADE, DATA_ATUALIZACAO, DATA_CADASTRO, IPI, TIPO_PROD, CONTROLA_TAMANHO, UNIDADE_ARMAZEN,
    UNIDADE_COMPRA, CONTROLA_COR, CLASSIFICACAO_FIS, CONTROLA_ESTAMPA, ESTOQUE_MINIMO, PRECISAO, CONTROLA_LOTE, ESTOQUE_MAXIMO, INTEIRO,
    CURVA_ABC, CLASS_PROD, AL_ISS, WEB, PROMOCAO, EXCLUI_FIN, COD_PRODUTO2, MARCA, DIVISAO, CLIENTE, IBAMADO, COD_IBAMA, GRADE_FORN,
    PAIS, CATEGORIA, SUBCOLECAO, FORNECEDOR, INFLUI_MODELAGEM, DESCRICAO_SF, MOVIMENTA_PESO, FAIXA_PRECO, MODELO, MATERIAL, N_CONTRATO,
    PRODBASE, CODBASE, QUALIDADE, DATA_DISP, COD_NCM, APROVEITA_IPI, APROVEITA_ICMS, CENTRO_CUSTO_PAD, CC_RECEITA, CC_CUSTO, CC_DESPESA,
    CC_ESTOQUE, CC_RESERVA, CC_TERCEIROS, CC_BENEFICIAMENTO, CC_INVENTARIO, PCONTA, PRODUTO_CLASS_SEFAZ, SERVICO_SUJEITO_ICMS, SERVICO_SUJEITO_ISS,
    SERVICO_SUJEITO_IPI, CC_DEVVENDA, CC_DEVCOMPRA, BLOQUEIA_VENDA, DESCRICAO_ETIQ, DESCRICAO_TRADUZIDA, EMBALAGEM, CC_PRODUCAO, HORIZONTE_ESTOQ_PROJETADO,
    BLOQUEIA_PV, CLFIS, CC_COMISSAO_DESP, ESTILISTA, MODELISTA, COD_PRODUTO_FORNEC, CC_TRANSPORTE_DESP, STATUS, PRIORIDADE_GRUPO, CC_COMISSAO_DESP_FUN,
    DESCRICAO_ORIGINAL, ID_KIT, QT_KIT, CODIGO_ANVISA, DATA_ANVISA, DIAS_VALIDADE, NAO_INCIDE_PIS_COFINS, NAO_CONTROLA_ESTOQUE, LOCALEXEC,
    CODLS, GRAMASM2, LAVAGEM, INATIVO, CARTELA, ALTURA, COMPRIMENTO, COD_DES, KIT, PROFUNDIDADE, INDICADOR_PRODEPE, CODIGO_PRODEPE,
    PERFIL_IMPOSTO, PERCENTUAL_LICENCIAMENTO, NAO_CALCULA_COMISSAO, ORIGEM_PROD, PROPORCAO_PRECO, PERMITE_PEDIDO_SEM_ESTOQUE, LEAD_TIME_ENTREGA,
    PRE_VENDA, DATA_LANCAMENTO, QTDE_MAX_VENDA, CODIGO_YOUTUBE, COD_ISBN, EXIGE_RECEITA, CLASS_PROD_SPED, FCI_NUMERO, FCI_PERCENTUAL,
    APELIDO_COR, APELIDO_ESTAMPA, APELIDO_TAMANHO, MESES_GARANTIA, PERMITE_PRESENTE, TIPO_ISS, NAT_ISS, PRECO_AUTOMATICO, PRODUTO_VOLUME,
    NUMERO_VOLUME, TRANS_ID, PRAZO_LOTE_VENCIDO, URL_PRODUTO, QUANTIDADES_MULTIPLAS, ACRESCIMO_QUEBRA, ESTRATEGIA_ABASTECIMENTO, ADICIONA_LOTE_PROD_NFE,
    PRECO_PROPORCIONAL_CODBASE, CONFERENCIA_AUTOMATICA, FINALIZA_AUTO_TAREFA_SEPARACAO, CODBASE_COMPONENTE_KIT, GRUPO_SEPARACAO, ALTERNATIVO_PRODUTO_BASE,
    TABELA_MEDIDA, COD_MPN, CODLS_SP, COMPRADOR, GRADE_DISTRIBUICAO, FAIXA_VALOR, UNIDADE_TRIB, FATOR_TRIB, PEDIDOC_ORIGEM, UTILIZA_FIFO,
    PERMITE_LOTE_EMBRANCO, IBGE_MUNCODDV, COD_BENEF_FISCAL, UNIDADE_USO_OLD, UNIDADE_ARMAZEN_OLD, UNIDADE_COMPRA_OLD, CEST, WMS, PESO_BRUTO_MEDIO,
    COD_INF_NUTRICIONAL, COD_INF_EXTRAS, CODPRODANP, FORNECEDOR_JUST_IN_TIME, BLOQUEIA_PED_COMPRA, BLOQUEIA_COMPRA, DESCRICAO_NFE, ALTURA_REAL,
    LARGURA_REAL, COMPRIMENTO_REAL, PESO_REAL, QUANT_FECHA_VOLUME_WMS, ID_CLASS_PROD, UTILIZA_LOTE_COMERCIAL, DCRE, TIPO_EMBALAGEM, PERC_INC_ALTURA,
    EMPILHAMENTO_MAXIMO, MOVIMENTA_EST_VOLUME, VERSAO_VOLUME, CNAE_SERV, CODTRIBMUN) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
     
        record_to_insert = (PRODUTO,CUSTO,QUANTIDADE_CAIXA,CUSTO_FIXO,CONTROLA_PECA,CUSTO_MEDIO,FATOR_CA,UNIDADE_USO,FATOR_AU,DEPARTAMENTO,COLECAO,
                        BAIXA_ESTOQUE_FICH,SUBST_ICMS,ICMS,AL_ICMS,IPI_INCIDE_ICMS,SIT_TRIB,MOEDA_COMPRA,LARGURA,AL_IPI,RED_ICMS,RED_IPI,DESCRICAO1,
                        REFERENCIA,DESCRICAO2,PESO,GRUPO,TIPO,COD_PRODUTO,GRADE,DATA_ATUALIZACAO,DATA_CADASTRO,IPI,TIPO_PROD,CONTROLA_TAMANHO,
                        UNIDADE_ARMAZEN,UNIDADE_COMPRA,CONTROLA_COR,CLASSIFICACAO_FIS,CONTROLA_ESTAMPA,ESTOQUE_MINIMO,PRECISAO,CONTROLA_LOTE,
                        ESTOQUE_MAXIMO,INTEIRO,CURVA_ABC,CLASS_PROD,AL_ISS,WEB,PROMOCAO,EXCLUI_FIN,COD_PRODUTO2,MARCA,DIVISAO,CLIENTE,IBAMADO,
                        COD_IBAMA,GRADE_FORN,PAIS,CATEGORIA,SUBCOLECAO,FORNECEDOR,INFLUI_MODELAGEM,DESCRICAO_SF,MOVIMENTA_PESO,FAIXA_PRECO,MODELO,
                        MATERIAL,N_CONTRATO,PRODBASE,CODBASE,QUALIDADE,DATA_DISP,COD_NCM,APROVEITA_IPI,APROVEITA_ICMS,CENTRO_CUSTO_PAD,CC_RECEITA,
                        CC_CUSTO,CC_DESPESA,CC_ESTOQUE,CC_RESERVA,CC_TERCEIROS,CC_BENEFICIAMENTO,CC_INVENTARIO,PCONTA,PRODUTO_CLASS_SEFAZ,
                        SERVICO_SUJEITO_ICMS,SERVICO_SUJEITO_ISS,SERVICO_SUJEITO_IPI,CC_DEVVENDA,CC_DEVCOMPRA,BLOQUEIA_VENDA,DESCRICAO_ETIQ,
                        DESCRICAO_TRADUZIDA,EMBALAGEM,CC_PRODUCAO,HORIZONTE_ESTOQ_PROJETADO,BLOQUEIA_PV,CLFIS,CC_COMISSAO_DESP,ESTILISTA,
                        MODELISTA,COD_PRODUTO_FORNEC,CC_TRANSPORTE_DESP,STATUS,PRIORIDADE_GRUPO,CC_COMISSAO_DESP_FUN,DESCRICAO_ORIGINAL,
                        ID_KIT,QT_KIT,CODIGO_ANVISA,DATA_ANVISA,DIAS_VALIDADE,NAO_INCIDE_PIS_COFINS,NAO_CONTROLA_ESTOQUE,LOCALEXEC,CODLS,GRAMASM2,
                        LAVAGEM,INATIVO,CARTELA,ALTURA,COMPRIMENTO,COD_DES,KIT,PROFUNDIDADE,INDICADOR_PRODEPE,CODIGO_PRODEPE,PERFIL_IMPOSTO,
                        PERCENTUAL_LICENCIAMENTO,NAO_CALCULA_COMISSAO,ORIGEM_PROD,PROPORCAO_PRECO,PERMITE_PEDIDO_SEM_ESTOQUE,LEAD_TIME_ENTREGA,
                        PRE_VENDA,DATA_LANCAMENTO,QTDE_MAX_VENDA,CODIGO_YOUTUBE,COD_ISBN,EXIGE_RECEITA,CLASS_PROD_SPED,FCI_NUMERO,FCI_PERCENTUAL,
                        APELIDO_COR,APELIDO_ESTAMPA,APELIDO_TAMANHO,MESES_GARANTIA,PERMITE_PRESENTE,TIPO_ISS,NAT_ISS,PRECO_AUTOMATICO,PRODUTO_VOLUME,
                        NUMERO_VOLUME,TRANS_ID,PRAZO_LOTE_VENCIDO,URL_PRODUTO,QUANTIDADES_MULTIPLAS,ACRESCIMO_QUEBRA,ESTRATEGIA_ABASTECIMENTO,
                        ADICIONA_LOTE_PROD_NFE,PRECO_PROPORCIONAL_CODBASE,CONFERENCIA_AUTOMATICA,FINALIZA_AUTO_TAREFA_SEPARACAO,CODBASE_COMPONENTE_KIT,
                        GRUPO_SEPARACAO,ALTERNATIVO_PRODUTO_BASE,TABELA_MEDIDA,COD_MPN,CODLS_SP,COMPRADOR,GRADE_DISTRIBUICAO,FAIXA_VALOR,UNIDADE_TRIB,
                        FATOR_TRIB,PEDIDOC_ORIGEM,UTILIZA_FIFO,PERMITE_LOTE_EMBRANCO,IBGE_MUNCODDV,COD_BENEF_FISCAL,UNIDADE_USO_OLD,UNIDADE_ARMAZEN_OLD,
                        UNIDADE_COMPRA_OLD,CEST,WMS,PESO_BRUTO_MEDIO,COD_INF_NUTRICIONAL,COD_INF_EXTRAS,CODPRODANP,FORNECEDOR_JUST_IN_TIME,
                        BLOQUEIA_PED_COMPRA,BLOQUEIA_COMPRA,DESCRICAO_NFE,ALTURA_REAL,LARGURA_REAL,COMPRIMENTO_REAL,PESO_REAL,QUANT_FECHA_VOLUME_WMS,
                        ID_CLASS_PROD,UTILIZA_LOTE_COMERCIAL,DCRE,TIPO_EMBALAGEM,PERC_INC_ALTURA,EMPILHAMENTO_MAXIMO,MOVIMENTA_EST_VOLUME,VERSAO_VOLUME,
                        CNAE_SERV,CODTRIBMUN,)
         
    
        cursor.execute(postgreSQL_insert_query, record_to_insert)
        connection.commit()
        print("Dados inseridos com sucesso!")
    except(Exception, psycopg2.Error) as error:
        print("Error ao inserir dados da tabela produtos do millennium no Postgres[Produtos]", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Consulta finalizada com sucesso!")
   
def check_produto_exists(produto):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="newport",
            user="postgres",
            password="musica2000"
        )
        
        cursor = connection.cursor()
        print(produto)
        postgresSQL_select_query = """select PRODUTO,
        CUSTO, QUANTIDADE_CAIXA, CUSTO_FIXO, CONTROLA_PECA, CUSTO_MEDIO, FATOR_CA, UNIDADE_USO, FATOR_AU, DEPARTAMENTO, COLECAO, BAIXA_ESTOQUE_FICH,
        SUBST_ICMS, ICMS, AL_ICMS, IPI_INCIDE_ICMS, SIT_TRIB, MOEDA_COMPRA, LARGURA, AL_IPI, RED_ICMS, RED_IPI, DESCRICAO1, REFERENCIA,
        DESCRICAO2, PESO, GRUPO, TIPO, COD_PRODUTO, GRADE, DATA_ATUALIZACAO, DATA_CADASTRO, IPI, TIPO_PROD, CONTROLA_TAMANHO, UNIDADE_ARMAZEN,
        UNIDADE_COMPRA, CONTROLA_COR, CLASSIFICACAO_FIS, CONTROLA_ESTAMPA, ESTOQUE_MINIMO, PRECISAO, CONTROLA_LOTE, ESTOQUE_MAXIMO, INTEIRO,
        CURVA_ABC, CLASS_PROD, AL_ISS, WEB, PROMOCAO, EXCLUI_FIN, COD_PRODUTO2, MARCA, DIVISAO, CLIENTE, IBAMADO, COD_IBAMA, GRADE_FORN,
        PAIS, CATEGORIA, SUBCOLECAO, FORNECEDOR, INFLUI_MODELAGEM, DESCRICAO_SF, MOVIMENTA_PESO, FAIXA_PRECO, MODELO, MATERIAL, N_CONTRATO,
        PRODBASE, CODBASE, QUALIDADE, DATA_DISP, COD_NCM, APROVEITA_IPI, APROVEITA_ICMS, CENTRO_CUSTO_PAD, CC_RECEITA, CC_CUSTO, CC_DESPESA,
        CC_ESTOQUE, CC_RESERVA, CC_TERCEIROS, CC_BENEFICIAMENTO, CC_INVENTARIO, PCONTA, PRODUTO_CLASS_SEFAZ, SERVICO_SUJEITO_ICMS, SERVICO_SUJEITO_ISS,
        SERVICO_SUJEITO_IPI, CC_DEVVENDA, CC_DEVCOMPRA, BLOQUEIA_VENDA, DESCRICAO_ETIQ, DESCRICAO_TRADUZIDA, EMBALAGEM, CC_PRODUCAO, HORIZONTE_ESTOQ_PROJETADO,
        BLOQUEIA_PV, CLFIS, CC_COMISSAO_DESP, ESTILISTA, MODELISTA, COD_PRODUTO_FORNEC, CC_TRANSPORTE_DESP, STATUS, PRIORIDADE_GRUPO, CC_COMISSAO_DESP_FUN,
        DESCRICAO_ORIGINAL, ID_KIT, QT_KIT, CODIGO_ANVISA, DATA_ANVISA, DIAS_VALIDADE, NAO_INCIDE_PIS_COFINS, NAO_CONTROLA_ESTOQUE, LOCALEXEC,
        CODLS, GRAMASM2, LAVAGEM, INATIVO, CARTELA, ALTURA, COMPRIMENTO, COD_DES, KIT, PROFUNDIDADE, INDICADOR_PRODEPE, CODIGO_PRODEPE,
        PERFIL_IMPOSTO, PERCENTUAL_LICENCIAMENTO, NAO_CALCULA_COMISSAO, ORIGEM_PROD, PROPORCAO_PRECO, PERMITE_PEDIDO_SEM_ESTOQUE, LEAD_TIME_ENTREGA,
        PRE_VENDA, DATA_LANCAMENTO, QTDE_MAX_VENDA, CODIGO_YOUTUBE, COD_ISBN, EXIGE_RECEITA, CLASS_PROD_SPED, FCI_NUMERO, FCI_PERCENTUAL,
        APELIDO_COR, APELIDO_ESTAMPA, APELIDO_TAMANHO, MESES_GARANTIA, PERMITE_PRESENTE, TIPO_ISS, NAT_ISS, PRECO_AUTOMATICO, PRODUTO_VOLUME,
        NUMERO_VOLUME, TRANS_ID, PRAZO_LOTE_VENCIDO, URL_PRODUTO, QUANTIDADES_MULTIPLAS, ACRESCIMO_QUEBRA, ESTRATEGIA_ABASTECIMENTO, ADICIONA_LOTE_PROD_NFE,
        PRECO_PROPORCIONAL_CODBASE, CONFERENCIA_AUTOMATICA, FINALIZA_AUTO_TAREFA_SEPARACAO, CODBASE_COMPONENTE_KIT, GRUPO_SEPARACAO, ALTERNATIVO_PRODUTO_BASE,
        TABELA_MEDIDA, COD_MPN, CODLS_SP, COMPRADOR, GRADE_DISTRIBUICAO, FAIXA_VALOR, UNIDADE_TRIB, FATOR_TRIB, PEDIDOC_ORIGEM, UTILIZA_FIFO,
        PERMITE_LOTE_EMBRANCO, IBGE_MUNCODDV, COD_BENEF_FISCAL, UNIDADE_USO_OLD, UNIDADE_ARMAZEN_OLD, UNIDADE_COMPRA_OLD, CEST, WMS, PESO_BRUTO_MEDIO,
        COD_INF_NUTRICIONAL, COD_INF_EXTRAS, CODPRODANP, FORNECEDOR_JUST_IN_TIME, BLOQUEIA_PED_COMPRA, BLOQUEIA_COMPRA, DESCRICAO_NFE, ALTURA_REAL,
        LARGURA_REAL, COMPRIMENTO_REAL, PESO_REAL, QUANT_FECHA_VOLUME_WMS, ID_CLASS_PROD, UTILIZA_LOTE_COMERCIAL, DCRE, TIPO_EMBALAGEM, PERC_INC_ALTURA,
        EMPILHAMENTO_MAXIMO, MOVIMENTA_EST_VOLUME, VERSAO_VOLUME, CNAE_SERV, CODTRIBMUN from produtos where produto = %s"""
        
        cursor.execute(postgresSQL_select_query, (produto,))
        records = cursor.fetchall()
        
        if len(records) > 0:
            return True
        else:
            return False
    except(Exception, psycopg2.Error) as error:
        print("Não foi possível consultar o id Produto do banco de dados MIllennium", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("2ª consulta no postgres encerrada com sucesso!")
        
