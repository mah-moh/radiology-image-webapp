from app import *
from .models import *
from .middlewares import *

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if session['user']:
            user = User.query.filter_by(id=session['user']).first()
            return redirect('/home')
    except:
        if request.method == 'POST':
            email = request.form.get("email")
            password = request.form.get("password")
            user = User.query.filter_by(email=email).first()
            if user.email == email and bcrypt.check_password_hash(user.password, password):
                session['user'] = user.id
                return redirect('/home')
        return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        password = request.form.get("password")
        hashed_pw = bcrypt.generate_password_hash(password)

        user = User(fname=fname, lname=lname, email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect('/')

    return render_template("register.html")

@app.route('/home', methods=['POST', 'GET'])
def home(): 
    try:
        if session['user']:
            user = User.query.filter_by(id=session['user']).first()
            file_paths = Filepath.query.filter_by(user_id=session['user']).all() # query filepaths
            return render_template("home.html", name=user.fname, file_paths=file_paths) # passing file_paths as a list
    except:
        flash("You have to login first!")
        return redirect("/")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                user = User.query.filter_by(id=session['user']).first()
                filepath = Filepath(path=file.filename, owener=user) #adding file name to db
                db.session.add(filepath)
                db.session.commit()
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                return redirect('/home')
    return render_template('upload.html')