SRT Schema
==========

``srttool`` expects the following schema for SRT files:

.. code-block:: text

   line_no
   timestamp
   text
   <new line>

``line_no`` is a positive integer, for example ``1``.

``timestamp`` is the to and from timestamp. Individual timestamps are formatted
as ``hh:mm:ss,ms``, for example ``00:00:05,123``. The entire line is formatted
as ``hh:mm:ss,ms --> hh:mm:ss,ms``.

``text`` is the subtitle text for the element bound by the timestamps, for
example ``nani nani nani``. ``text`` can be multiple lines.

``<new line>`` is a single ``\n`` character indicating the end of the subtitle
element above it.

All lines must end with a ``\n``. This tool is not currently tested on Windows
and so may not work correctly with lines ending with ``\r\n``.
