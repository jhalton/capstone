from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Optional
from app.models import Collection

def collection_name_exists(form, field):
    name = field.data
    collection_id = form.collection_id.data

    if collection_id:
        existing_collection = Collection.query.filter(
            Collection.name == name,
            Collection.id != collection_id
        ).first()
        if existing_collection:
            raise ValidationError("A collection with that name already exists")
        else:
            existing_collection = Collection.query.filter_by(name=name).first()
            if existing_collection:
                raise ValidationError("A collection with that name already exists")


    # collection = Collection.query.filter(Collection.name == name).first()
    # if collection:
    #     raise ValidationError('A collection with this name already exists')

class CreateCollectionForm(FlaskForm):
    collection_id = IntegerField("Collection ID", validators=[Optional()])
    name = StringField('Name', validators=[DataRequired("Collection name is required"), collection_name_exists])
    description = StringField("Description")
