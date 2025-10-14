from django.db import models

class Options(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FormField(models.Model):
    FIELD_TYPE = [
        ('text', 'Text'),
        ('email', 'Email'),
        ('number', 'Number'),
        ('password', 'Password'),
        ('date', 'Date'),
        ('checkbox', 'Checkbox'),
        ('radio', 'Radio'),
        ('select', 'Select'),
    ]
    # REMOVE THE COMMAS HERE!
    label = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    
    # REMOVE THE COMMAS HERE!
    field = models.CharField(max_length=20, choices=FIELD_TYPE)
    requiredYn = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='Y')
    errorMessage = models.CharField(max_length=255, blank=True, null=True)
    inline = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N')
    toasterMessage = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')], default='N')
    options = models.ManyToManyField(Options, related_name='form_fields')

    def __str__(self):
        return self.label