from   django.core.urlresolvers import reverse, resolve
import pytest

skipNotFinishedYet = pytest.mark.skipif(True, reason = 'not implemented')


class UnitTestUtilsMixin(object):
    ''' Regroup utilities functions for django unittests '''

    def assert_url_matches_view(self, view, expected_url, url_name,
                                url_args=None, url_kwargs=None, urlconf=None):
        '''
        Assert a view's url is correctly configured
        Check the url_name reverses to give a correctly formated expected_url.
        Check the expected_url resolves to the expected view.
        '''

        reversed_url = reverse(
            url_name,
            urlconf=urlconf,
            args=url_args,
            kwargs=url_kwargs,
        )
        self.assertEqual(reversed_url, expected_url)

        resolved_view = resolve(expected_url, urlconf=urlconf).func
        if hasattr(resolved_view, 'cls'):
            self.assertEqual(resolved_view.cls, view)
        else:
            self.assertEqual(resolved_view.__name__, view.__name__)
