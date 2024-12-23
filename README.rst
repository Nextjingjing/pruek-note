============
pruek-note
============

django-note is a Django app to conduct web-based note. For saving note and query each note.


Quick start
-----------

1. Add "note" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "pruek_note",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("note/", include("pruek_note.urls")),

3. Run ``python manage.py migrate`` to create the models.


4. Visit the ``/note/`` URL to participate in the poll.