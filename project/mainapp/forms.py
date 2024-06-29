from django import forms

class receiverForm(forms.ModelForm):

      class Meta:
            fields = {'file'}
      
      def __init__(self, *args, **kwargs):
            super(receiverForm, self).__init__(*args, **kwargs)
            self.fields['file'].widget.attrs['class'] = 'form-class'
            self.fields['file'].widget.attrs['accept'] = '.csv, .txt'
