from django import template

register = template.Library()

<<<<<<< HEAD

=======
>>>>>>> 2fc00f767cecb808a23904e47e76f3ebdab3771b
@register.filter
def get_at_index(list, index):
	return list[index]
