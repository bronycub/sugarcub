from django.core.exceptions import ImproperlyConfigured
from crispy_forms           import helper, layout


class FormHelperMixin:
    '''
    Custom Form that allows to attach a crispy-forms FormHelper class,
    that will modify in some way the rendering of the layout.

    Example::

        FooForm(FormHelperMixin, form.ModelForm):
            class Meta:
                model = FooModel
                helper_class = FooFormHelper
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if hasattr(self.Meta, "helper_class"):
            helper_class = getattr(self.Meta, "helper_class")
            kwargs = self.get_helper_kwargs()
            self.helper = helper_class(self, **kwargs)
        else:
            raise ImproperlyConfigured(
                "{0} is missing a 'helper_class' meta attribute.".format(
                    self.__class__.__name__))

    def get_helper_kwargs(self):
        '''
        Get all helper attributes from class Meta by stripping them of
        `helper_` part of attribute string

        :return: dict with helper kwargs
        '''

        kwargs = {}
        for attr, value in self.Meta.__dict__.items():
            if attr.startswith("helper_") and attr != "helper_class":
                new_attr = attr.split("_", 1)[1]
                kwargs[new_attr] = value
        return kwargs


class BootstrapFormHelper(helper.FormHelper):
    '''
    Setup helper to a classic bootstrap form
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_class = 'col-lg-3'
        self.field_class = 'col-lg-9'


class PartialFormHelper(BootstrapFormHelper):
    '''
    Used to create partial forms, designed to be used along others form.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form_tag = False


class SubmitFormHelper(BootstrapFormHelper):
    '''
    Add a submit button
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.layout.append(
            layout.Div(
                layout.Submit('save', 'Submit'),
                css_class='col-lg-offset-2',
            ),
        )
