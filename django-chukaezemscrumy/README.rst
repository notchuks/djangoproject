=============================================================================
chukaezemscrumy
=============================================================================

chukaezemscrumy is a Django app created by twitter:@notchuks to learn django

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "chukaezemscrumy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('chukaezemscrumy/', include('chukaezemscrumy.urls')),

3. Run `python manage.py migrate` to create the chukaezemscrumy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/chukaezemscrumy/ to participate in the poll.