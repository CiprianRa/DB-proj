from flask import Flask,render_template,jsonify,request,redirect,url_for,session
import cx_Oracle

app = Flask ( __name__ )

con=cx_Oracle.connect("bd111","bd111","bd-dc.cs.tuiasi.ro:1539/orcl")

@app.route ( "/" )
@app.route('/dirijori')
def dir():
    dirijori = []

    cur=con.cursor()
    cur.execute('select * from dirijori')
    for result in cur:
        dirijor={}
        dirijor['id_dirijor']=result[0]
        dirijor['nume']=result[1]
        dirijor['email']=result[2]
        dirijor['nr_de_telefon']=result[3]
        dirijori.append(dirijor)
    cur.close()
    return render_template('dirijori.html',dirijori=dirijori)

@app.route('/concerte')
def conc():
    concerte=[]

    cur=con.cursor()
    cur.execute('select * from concerte')
    for result in cur:
        concert={}
        concert['id_concert']=result[0]
        concert['nume_concert']=result[1]
        concert['data']=result[2]
        concert['oras']=result[3]
        concert['id_dirijor']=result[4]
        concerte.append(concert)
    cur.close()
    return render_template('concerte.html',concerte=concerte)

@app.route('/instrumente')
def inst():
    instrumente=[]

    cur=con.cursor()
    cur.execute('select * from instrumente')
    for result in cur:
        instrument={}
        instrument['id_instrument']=result[0]
        instrument['nume']=result[1]
        instrument['categorie']=result[2]
        instrumente.append(instrument)
    cur.close()
    return render_template('instrumente.html',instrumente=instrumente)

@app.route('/muzicieni')
def muz():
    muzicieni=[]

    cur=con.cursor()
    cur.execute('select * from muzicieni')
    for result in cur:
        muzician={}
        muzician['id_muzician']=result[0]
        muzician['nume']=result[1]
        muzician['nr_de_telefon']=result[2]
        muzician['email']=result[3]
        muzician['id_instrument']=result[4]
        muzicieni.append(muzician)
    cur.close()
    return render_template('muzicieni.html',muzicieni=muzicieni)

@app.route('/piese')
def pie():
    piese=[]

    cur=con.cursor()
    cur.execute('select * from piese')
    for result in cur:
        piesa={}
        piesa['id_piesa']=result[0]
        piesa['titlu_piesa']=result[1]
        piesa['numele_autorului']=result[2]
        piese.append(piesa)
    cur.close()
    return render_template('piese.html',piese=piese)

@app.route('/repertoriu')
def repertoriu():
    repertoriu=[]

    cur=con.cursor()
    cur.execute('select * from repertoriu')
    for result in cur:
        repert={}
        repert['id_concert']=result[0]
        repert['id_piesa']=result[1]
        repert['ordine_interpretare']=result[2]
        repertoriu.append(repert)
    cur.close()
    return render_template('repertoriu.html',repertoriu=repertoriu)

@app.route('/participari')
def participari():
    participari=[]

    cur=con.cursor()
    cur.execute('select * from participari')
    for result in cur:
        participare={}
        participare['id_muzician']=result[0]
        participare['id_concert']=result[1]
        participare['loc_scena']=result[2]
        participari.append(participare)
    cur.close()
    return render_template('participari.html',participari=participari)

@app.route('/addDirijor',methods=['GET','POST'])
def add_dir():
    error = None
    if request.method=='POST':
        dir=0
        cur=con.cursor()
        cur.execute('select max(id_dirijor) from dirijori')
        result = cur.fetchone()
        if result and result[0] is not None:
            dir = result[0]
        cur.close()
        dir+=1
        cur=con.cursor()
        values=[]
        values.append("'"+str(dir)+"'")
        values.append("'"+request.form['nume']+"'")
        values.append("'"+request.form['email']+"'")
        values.append("'"+request.form['nr_de_telefon']+"'")
        fields=['id_dirijor','nume','email','nr_de_telefon']
        query='INSERT INTO %s (%s) VALUES (%s)' % ('dirijori',','.join(fields),','.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/dirijori')
    else:
        error = 'Campul "nume" este obligatoriu.'
    return render_template('addDirijor.html', error=error)

@app.route('/delDirijor',methods=['GET','POST'])
def del_dir():
    id_dirijor=request.form['id_dirijor']
    cur=con.cursor()
    cur.execute('DELETE FROM repertoriu WHERE id_concert IN (SELECT id_concert FROM concerte WHERE id_dirijor = :id)',{'id': id_dirijor})
    cur.execute('DELETE FROM participari WHERE id_concert IN (SELECT id_concert FROM concerte WHERE id_dirijor = :id)',{'id': id_dirijor})
    cur.execute('DELETE FROM concerte WHERE id_dirijor = :id', {'id': id_dirijor})
    cur.execute('DELETE FROM dirijori WHERE id_dirijor = :id', {'id': id_dirijor})
    cur.execute('commit')
    return redirect('/dirijori')

@app.route('/editDirijor/<int:id_dirijor>',methods=['GET','POST'])
def edit_dir(id_dirijor):
    cur=con.cursor()
    cur.execute('select * from dirijori where id_dirijor=:id_dirijor',id_dirijor=id_dirijor)
    data = cur.fetchone()
    print(data)
    nume= data[1]
    email = data[2]
    nr_de_telefon = data[3]
    if request.method == 'POST':
        name=request.form['nume']
        email=request.form['email']
        nr_de_telefon=request.form['nr_de_telefon']
        #print(name)
        cur=con.cursor()
        cur.execute("UPDATE dirijori SET nume=: name,email=:email,nr_de_telefon=:nr_de_telefon WHERE id_dirijor=:dir",name=name,email=email,nr_de_telefon=nr_de_telefon,dir=id_dirijor)
        con.commit()
        return redirect(url_for('dir'))
    cur.close()
    return render_template('editDirijor.html',nume=nume,email=email,nr_de_telefon=nr_de_telefon,id_dirijor=id_dirijor)

@app.route('/getDirijor',methods=['POST'])
def get_dir():
    dir=request.form['id_dirijor']
    cur=con.cursor()
    cur.execute('select * from dirijori where id_dirijor='+dir)

    dirs=cur.fetchone()
    id_dirijor=dirs[0]
    cur.close()
    return redirect(url_for('edit_dir',id_dirijor=id_dirijor))


@app.route('/addMuzician',methods=['GET','POST'])
def add_muz():
    error = None
    cur = con.cursor()
    cur.execute('select * from instrumente')
    result = cur.fetchall()
    print(result)
    if request.method=='POST':
        muz=0
        cur.execute('select max(id_muzician) from muzicieni')
        result = cur.fetchone()
        if result and result[0] is not None:
            muz = result[0]
        cur.close()
        muz+=1
        cur=con.cursor()
        values=[]
        values.append("'"+str(muz)+"'")
        values.append("'"+request.form['nume']+"'")
        values.append("'"+request.form['nr_de_telefon']+"'")
        values.append("'"+request.form['email']+"'")
        values.append("'"+request.form['instrument']+"'")
        fields=['id_muzician','nume','nr_de_telefon','email','id_instrument']
        query='INSERT INTO %s (%s) VALUES (%s)' % ('muzicieni',','.join(fields),','.join(values))

        cur.execute(query)
        cur.close()
        con.commit()
        return redirect('/muzicieni')
    else:
        error = 'Campul "nume" este obligatoriu.'
    return render_template('addMuzician.html', instrumente=result, error=error)

@app.route('/delMuzician',methods=['GET','POST'])
def del_muz():
    id_muzician=request.form['id_muzician']
    cur=con.cursor()
    cur.execute('DELETE FROM participari WHERE id_muzician=:id',{'id': id_muzician})
    cur.execute('DELETE FROM muzicieni WHERE id_muzician = :id', {'id': id_muzician})
    cur.execute('commit')
    return redirect('/muzicieni')

@app.route('/editMuzician/<int:id_muzician>',methods=['GET','POST'])
def edit_muz(id_muzician):
    cur=con.cursor()
    cur.execute('select * from muzicieni where id_muzician=:id_muzician',id_muzician=id_muzician)
    data = cur.fetchone()
    print(data)
    nume= data[1]
    email = data[2]
    nr_de_telefon = data[3]
    id_instrument=data[4]
    if request.method == 'POST':
        name=request.form['nume']
        email=request.form['email']
        nr_de_telefon=request.form['nr_de_telefon']
        id_instrument=request.form['id_instrument']
        #print(name)
        cur=con.cursor()
        cur.execute("UPDATE muzicieni SET nume=: name,nr_de_telefon=:nr_de_telefon,email=:email,id_instrument=:id_instrument WHERE id_muzician=:muz",name=name,email=email,nr_de_telefon=nr_de_telefon,id_instrument=id_instrument,muz=id_muzician)
        con.commit()
        return redirect(url_for('muz'))
    cur.close()
    return render_template('editMuzician.html',nume=nume,nr_de_telefon=nr_de_telefon,email=email,id_instrument=id_instrument,id_muzician=id_muzician)

@app.route('/getMuzician',methods=['POST'])
def get_muz():
    muz=request.form['id_muzician']
    cur=con.cursor()
    cur.execute('select * from muzicieni where id_muzician='+muz)

    muzs=cur.fetchone()
    id_muzician=muzs[0]
    cur.close()
    return redirect(url_for('edit_muz',id_muzician=id_muzician))

@app.route('/addConcert',methods=['GET','POST'])
def add_conc():
    error = None
    cur = con.cursor()
    cur.execute('SELECT id_dirijor,nume FROM dirijori WHERE id_dirijor NOT IN (SELECT id_dirijor FROM concerte)')
    result = cur.fetchall()
    print(result)
    if request.method=='POST':
        conc=0
        cur.execute('select max(id_concert) from concerte')
        result = cur.fetchone()
        if result and result[0] is not None:
            conc = result[0]
        cur.close()
        conc+=1
        cur=con.cursor()
        values=[]
        values.append("'"+str(conc)+"'")
        values.append("'"+request.form['nume_concert']+"'")
        values.append("'"+request.form['data']+"'")
        values.append("'"+request.form['oras']+"'")
        values.append("'"+request.form['dirijor']+"'")
        print(values)

        fields=['id_concert','nume_concert','data','oras','id_dirijor']
        print(fields)
        cur.execute("INSERT INTO CONCERTE (id_concert,nume_concert,data,oras,id_dirijor) VALUES (:1,:2,TO_DATE(:3, 'YYYY-MM-DD' ),:4,:5)",(conc,request.form['nume_concert'],request.form['data'],request.form['oras'],request.form['dirijor']))


        cur.close()
        con.commit()
        return redirect('/concerte')
    else:
        error = 'Campul "nume" este obligatoriu.'
    return render_template('addConcert.html', dirijori=result, error=error)

@app.route('/delConcert',methods=['GET','POST'])
def del_conc():
    id_concert=request.form['id_concert']
    cur=con.cursor()
    cur.execute('DELETE FROM participari WHERE id_concert=:id',{'id': id_concert})
    cur.execute('DELETE FROM repertoriu WHERE id_concert = :id', {'id': id_concert})
    cur.execute('DELETE FROM concerte WHERE id_concert=:id',{'id':id_concert})
    cur.execute('commit')
    return redirect('/concerte')

@app.route('/addParticipare',methods=['GET','POST'])
def add_part():
    error = None
    if request.method=='POST':
        cur=con.cursor()
        values=[]
        values.append("'"+request.form['id_muzician']+"'")
        values.append("'"+request.form['id_concert']+"'")
        values.append("'"+request.form['loc_scena']+"'")

        fields=['id_muzician','id_concert','loc_scena']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('participari', ','.join(fields), ','.join(values))
        cur.execute(query)
        cur.close()
        con.commit()
        return redirect('/participari')
    else:
        error = 'Campul "nume" este obligatoriu.'
    return render_template('addParticipare.html', error=error)

@app.route('/addRepertoriu', methods=['GET', 'POST'])
def add_rep():
    error = None
    if request.method == 'POST':
        #print(request.form)  # Add this line to print the form data
        cur = con.cursor()
        values = []
        values.append("'" + request.form['id_concert'] + "'")
        values.append("'" + request.form['id_piesa'] + "'")
        values.append("'" + request.form['ordine_interpretare'] + "'")

        fields = ['id_concert', 'id_piesa', 'ordine_interpretare']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('repertoriu', ','.join(fields), ','.join(values))
        cur.execute(query)
        cur.close()
        con.commit()
        return redirect('/repertoriu')
    else:
        error = 'Campul "nume" este obligatoriu.'
    return render_template('addRepertoriu.html', error=error)


if __name__ == "__main__" :
    app.run (debug=True)
    con.close()