
from stegano import lsb

hide=lsb.hide("name of image","Message to be encrypted")
hide.save("Name of encrypted file")

text=lsb.reveal("Name of encrypted file/image")
print(text)