from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/Encryption') 
def encrypt():
    return render_template('Encryption.html')


@app.route('/Decryption')
def decrypt():
    return render_template('Decryption.html')


@app.route('/Encryption', methods=['POST'])
def getdata_enc():
    import os
    source_name = request.form['source_name']  #INPUT MAIN IMAGE
    p = int(request.form['prime_1'])
    q = int(request.form['prime_2'])
    cover_name = request.form['cover_name']    #ANOTHER DUPLICATE INPUT
    new_img_name = request.form['new_name']    #INPUT+DUPLIACET=NEW

    import base_enc
    base_enc.base_enc(source_name)

    import rsa_enc
    rsa_enc.call_rsa('s.txt', p, q)

    import stego_enc
    cover_name = os.path.dirname(os.path.abspath(__file__))+'/static/coverimages/'+cover_name
    stego_enc.encode(cover_name, new_img_name)
    return render_template('thank.html')

@app.route('/Decryption', methods=['POST'])
def getdata_dec():
    cover_name = request.form['cover_name']
    p = int(request.form['prime_1'])
    q = int(request.form['prime_2'])
    new_cover_name = request.form['new_cover_name']

    import stego_dec
    stego_dec.decode(cover_name)

    import rsa_dec
    rsa_dec.rsa_dec(p,q)

    '''import base_dec
    base_dec.base_dec(new_cover_name)'''

    return render_template('thank.html')


if __name__ == '__main__':
    app.run(debug=True)
