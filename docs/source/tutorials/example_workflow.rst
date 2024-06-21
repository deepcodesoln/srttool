Example Workflow
================

If you have a collection of SRT files, for example in ``/my/srt/files``,
converting them to a frequency list can be done via:

.. code-block:: text

   python3 srttool.py to_dialog --srt_dir /my/srt/files dialog_out
   python3 srttool.py ginza_wrapper --dialog_dir dialog_out json_out
   python3 srttool.py word_frequency json_out frequency_list.txt

This workflow assumes you have the
`ginza <https://github.com/megagonlabs/ginza>`_ tool installed.
