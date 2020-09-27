class BioForm(FlaskForm):
    bio = TextAreaField('Write A Short Bio About You...')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    blog = TextAreaField('Write a Blog...')
    submit = SubmitField('submit')