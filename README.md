## aiida-wait

This is a test AiiDA plugin that allows creating calculations which can be stopped manually. Its purpose it to be used in manual testing. 

The ``wait_for.sh`` script is the actual 'calculation': It waits until a ``stop`` file appears in the directory where it is executed.
