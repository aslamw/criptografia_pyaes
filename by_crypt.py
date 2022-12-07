import os
import pyaes

## abrir o arquivo a ser criptografado

file_name = input("digite um o nome do arquivo Ex:.teste.txt _>>")
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"testemarcosw9000"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".crypt"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
