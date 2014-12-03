from sugarcub import settings

def custom_fields(request):
	''' Provides a list of fields custom for each association '''
	return {'association_name': settings.ASSOCIATION_NAME}

def humanitarian_actions(request):
	''' provides the next humanitarian actions for the footer '''
	return {'next_humanitarian_action': 'test'}
