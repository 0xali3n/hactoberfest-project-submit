from django import template
register = template.Library()

def lookup(mylist, value):
    return mylist.append(value)