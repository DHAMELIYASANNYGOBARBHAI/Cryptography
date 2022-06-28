import base64
import os
def base_enc(source_name):
    file_name = os.path.dirname(os.path.abspath(__file__))+'/static/user_input/'+source_name
    with open(file_name, "rb") as File:
        str1 = base64.b64encode(File.read())
    filename = 's.txt'
    with open(filename, 'wb') as f:
        f.write(str1)
        f.close()