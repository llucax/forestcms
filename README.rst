
===========
|ForestCMS|
===========

|ForestCMS| stands for "Filesystem_-Oriented reST_ CMS_" (or
"Filesystem_-Oriented reStructuredText_ `Content Management System`_" for long
;).

It's a `Web CMS`_ inspired in the ideas brought by the Hooks_ PHP_ framework
for content managements and it's intended to make easy to publish contents in
a filesystem_-oriented way (i.e. use the hierarchical nature of the filesystem_
to build a tree-like content database). This makes very easy to manage contents
without a web interface (by just editing files in the filesystem_). A web
interface can come in the future, though, it just have to manage files in the
filesystem_ instead of rows in a relational database.

|ForestCMS| is written in Python_, and the content is written in
reStructuredText_ instead of HTML_. Why? Just because reStructuredText_ is
great for writing content, and if you *really* need to do some nasty HTML_
tricks, you can always use the `raw directive`_.



Quick Test
==========

If you want to quickly try ForestCMS just run::

        python fcms.py

And point your browser to http://localhost:8000/README to see this very same
file rendered as HTML_.



.. |ForestCMS| replace:: **ForestCMS**

.. _PHP: http://www.php.net/
.. _Python: http://www.python.org/
.. _reStructuredText:
.. _reST: http://docutils.sourceforge.net/rst.html
.. _Hooks: http://hooks.gforge.lug.fi.uba.ar/hooks/docs/html/
.. _HTML: http://en.wikipedia.org/wiki/HTML
.. _Filesystem: http://en.wikipedia.org/wiki/Filesystem
.. _Content Management System:
.. _CMS: http://en.wikipedia.org/wiki/Content_Management_System
.. _Web CMS: http://en.wikipedia.org/wiki/Web_Content_Management_System
.. _raw directive: http://docutils.sourceforge.net/docs/ref/rst/directives.html#raw-data-pass-through

