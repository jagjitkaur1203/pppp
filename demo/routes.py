from flask import render_template,flash,redirect,url_for
from demo import app
from demo.forms import RegistrationForm, LoginForm, StaffLoginForm,CommentForm
from demo.model import StudentRegistration, Comment


@app.route('/')

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/about') 
def about():
    return render_template('about.html',title='About')

@app.route('/handbooks') 
def handbooks():
    return render_template('handbooks.html',title='handbooks')

@app.route('/eligibility') 
def eligibility():
    return render_template('eligibility.html',title='eligibility')

@app.route('/database') 
def database():
    return render_template('database.html',title='database')

@app.route('/register',methods=['GET','POST']) 
def register():
    form = RegistrationForm() 
    if form.validate_on_submit():
        flash(f'Hi, {form.username.data}!, Login Yourself', 'success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET','POST']) 
def login():
    form = LoginForm() 
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('eligibility'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html',title='Login',form=form)


@app.route('/stafflogin',methods=['GET','POST']) 
def stafflogin():
    form = StaffLoginForm() 
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('database'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('stafflogin.html',title='Login',form=form)

@app.route("/comment", methods=["GET", "POST"])
def comment_post():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data)
        db.session.add(comment)
        db.session.commit()
        flash("Your comment has been added to the post", "success")
        return redirect(url_for("home"))
    ''' post = Post.query.get_or_404(post_id)'''

    return render_template("comment.html", title="Comment Post", form=form)
