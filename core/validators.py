def validate_logo(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.svg', '.png', '.jpeg', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('We accept .svg, .png, .jpeg, .jpg.')
    
def validate_year_of_formation(value):
    import datetime
    from django.core.exceptions import ValidationError
    if value < 2003:
        raise ValidationError("You weren't even born!")
    elif value > datetime.date.today().year:
        raise ValidationError('You can come back when you really finish.')
    