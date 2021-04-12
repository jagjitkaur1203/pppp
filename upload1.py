from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:/Users/Lenovo/Desktop/visual/demo/uploadphoto'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__,template_folder='template')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_PATH']=16 * 1024 * 1024




class StaffLoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    

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



















@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)