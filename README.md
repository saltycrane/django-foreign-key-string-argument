After creating some objects, the following produces an error:

    $ python
    Python 2.6.6 (r266:84292, Sep 15 2010, 16:22:56)
    [GCC 4.4.5] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from myapp1.models import Tim
    >>> tall = Tim.objects.all()
    >>> tall[0].model
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/eliot/.virtualenvs/foreign_key_string_argument/lib/python2.6/site-packages/django/db/models/fields/related.py", line 302, in __get__
        other_field = self.field.rel.get_related_field()
      File "/home/eliot/.virtualenvs/foreign_key_string_argument/lib/python2.6/site-packages/django/db/models/fields/related.py", line 773, in get_related_field
        data = self.to._meta.get_field_by_name(self.field_name)
    AttributeError: 'str' object has no attribute '_meta'
    >>>
