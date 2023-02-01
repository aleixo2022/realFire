import fdb

def conectar():
    # informações de conexão
    host = "10.255.255.115" #10.20.4.179"
    banco = "c:/BD/DESENVOLVIMENTO.FDB"#D:/Sys/Base/MILLENNIUM"
    usuario = "sysdba"
    senha = "masterkey"
    
    # criação da conexão
    con = fdb.connect(
        host=host,
        database=banco,
        user=usuario,
        password=senha
    )
    return con