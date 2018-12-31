Document Repository
===================

Using this restructured text format allows us to routinely present the document repository as structurred html, bundle it as a pdf 'book' or output it as an 'epub' for offline use on tabs or smart phones.

Maintaining it on a managed 'point of truth' such as a git repository (e.g. on github) allows us to keep a definitive canonical collection of signed club documents.

Management
----------

This documentation is a collection of `restructured text files`_ organized with `Sphinx`_ for delivery on site as html
or output as a pdf or other electronic publication.

It is maintained as a git repository on github so that changes may be managed through pull requests. A webhook will be
used to automatically update the website when the master branch is updated. Badges or links may also allow access to
new drafts or upcoming versions.

To work with the documentation, you currently need a local installation and
familiarity with:

 - `Git`_
 - `restructured text files`_
 - `Sphinx`_


For the most part, authoring the documentation only needs minimal knowledge of `Sphinx`_. The ``django devdoc`` command
handles building the documentation.

See a quick `cheat sheet
<http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_ or review the existing
documentation source by clicking the "Show Source" button.


.. _Sphinx: http://sphinx-doc.org/
.. _Git: https://try.github.io/levels/1/challenges/1
.. _restructured text files: http://docutils.sourceforge.net/docs/user/rst/quickstart.html
.. _Django documentation: https://docs.djangoproject.com/en/dev/internals/contributing/writing-documentation/
