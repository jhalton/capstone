from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
from app.models import Collection

def collection_name_exists(form, field):
    name = field.data
    collection = Collection.query.filter(Collection.name == name).first()
    if collection:
        raise ValidationError('A collection with this name already exists')

class CreateCollectionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField("Description")
