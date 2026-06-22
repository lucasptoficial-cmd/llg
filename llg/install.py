import os
import shutil

DESTINO = r"C:\LLG"

if not os.path.exists(DESTINO):
    os.makedirs(DESTINO)

shutil.copy("llg.exe", os.path.join(DESTINO, "llg.exe"))

print("LLG instalada em C:\\LLG")
input("Prima Enter para sair...")