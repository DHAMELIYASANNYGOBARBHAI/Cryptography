import base64
def base_dec(new_name):
    with open('s10.txt', "rb") as File:
        str1= (File.read())

    imgdata = base64.b64decode(str1)
    filename = "D:/Lecture e-books/Semester - 6/SC402-Crypto/Project/Project code/static/user_output/"+new_name
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
