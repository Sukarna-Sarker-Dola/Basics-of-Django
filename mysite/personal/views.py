from django.shortcuts import render
from personal.models import Question

# Create your views here.
def home_screen_view(request):
	context = {}
# 	context['some_string'] = 'this is some strings that i am passing to the view'
# 	context['some_number'] = 12345

# 	list_of_values = [] #this is a list
# 	list_of_values.append("first entry")
# 	list_of_values.append("2nd entry")
# 	list_of_values.append("3rd entry")
# 	list_of_values.append("4th entry")
# 	context['list_of_values'] = list_of_values
	questions = Question.objects.all()
	context['questions'] = questions

	return render(request, "personal/home.html", context)