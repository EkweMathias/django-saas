from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from datetime import datetime 


class UniversityForm(forms.Form):
    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'university_id'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_fo'
        self.helper.add_input(Submit('submit', 'Submit'))
    
    SUBJECT_CHOICES =  (
        (1, 'Web Development'),
        (2, 'Systems Programming'),
        (3, 'Data Science')
    )
    
    name = forms.CharField()
    age = forms.IntegerField()
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    enroll_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}, format=r"%d/%m/%Y"))
    