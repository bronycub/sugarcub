from   django.core.exceptions   import ValidationError
from   django.utils.deconstruct import deconstructible
from   django.utils.translation import gettext_lazy as _
from   django.core              import validators


@deconstructible
class SkypeValidator:
    message = _('Enter a valid URL.')
    code = 'invalid'

    def __call__(self, value):
        if not value.startswith('skype:'):
            raise ValidationError(self.message, code=self.code)


@deconstructible
class UrlValidator:
    message = _('Enter a valid URL.')
    code = 'invalid'
    validators = [validators.URLValidator(), validators.EmailValidator(), SkypeValidator()]

    def __call__(self, value):
        def apply_validator(value):
            def _apply_validator(validator):
                try:
                    validator(value)
                except ValidationError as e:
                    skype_failed = True

            return _apply_validator


        if any(map(apply_validator(value), self.validators)):
            raise ValidationError(self.message, code=self.code)


