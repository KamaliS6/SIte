from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email, Length
from datetime import timedelta, datetime
from database import init_db, add_comment, get_all_comments
from flask_mail import Mail, Message
import os

# --- Flask setup ---
app = Flask(__name__)
app.secret_key = '876'
app.permanent_session_lifetime = timedelta(minutes=5)
csrf = CSRFProtect(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kamalileon111@gmail.com'         # your Gmail
app.config['MAIL_PASSWORD'] = 'gfye eblc yiio kxlef'    # your app password from Step 1
app.config['MAIL_DEFAULT_SENDER'] = 'kamalileon111@gmail.com'

mail = Mail(app)

# --- Contact Form (moved from forms.py) ---
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=5, max=1000)])
    submit = SubmitField('Send Message')

# --- Initialize database ---
if not os.path.exists('portfolio.db'):
    init_db()

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html', current_page=request.endpoint)

@app.route('/projects')
def projects():
    return render_template('projects.html', current_page=request.endpoint)

@app.route('/resume')
def resume():
    return render_template('resume.html', current_page=request.endpoint)

@app.route('/contact', methods=['GET'])
def contact():
    form = ContactForm()
    # It's good practice to load existing comments here for initial page load
    # or have a separate AJAX endpoint. Let's make a separate AJAX endpoint for clarity.
    return render_template('contact.html', form=form)

@app.route('/submit_message', methods=['POST'])
def submit_message():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # Save to DB
        add_comment(name, email, message)
        timestamp = datetime.now().strftime('%B %d, %Y')
        # Email content
        try:
            msg = Message(
                subject=f"{name} sent a message through your website",
                recipients=['kamalileon111@gmail.com'],  # Where the message gets sent
                body=f"From: {name}\n\nMessage: {message}\n\nSent on: {timestamp}"
            )
            mail.send(msg)
        except Exception as e:
            print("Email failed:", e)

        return jsonify({
            'success': True,
            'message': {
                'name': name,
                'email': email,
                'content': message,
                'timestamp': datetime.now().strftime('%B %d, %Y')
            }
        })

    return jsonify({'success': False, 'error': 'Invalid form data'}), 400


@app.route('/comments', methods=['GET'])
def comments():
    form = ContactForm()
    if form.validate_on_submit():
        add_comment(form.name.data, form.email.data, form.message.data)
        return jsonify({
            'success': True,
            'message': {
                'name': form.name.data,
                'email': form.email.data,
                'content': form.message.data,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        })

    return jsonify({'success': False, 'error': 'Invalid form data'}), 400

# --- Run app ---
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)



