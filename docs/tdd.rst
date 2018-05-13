
.. tdd

Test Driven Development (TDD)
=============================

The goal of every programmer is to write high quality code. 

I think every programmer will agree that some form of testing is required to make high quality code possible.

TDD is one approach to testing that has many devoted followers, and for good reason, there are measurable benefits to it.

There are plenty of books about TDD and plenty of advanced topics to learn. Anyone interested in learning the smart patterns, tricks and rules of thumb that can make TDD better should certainly do so, but I think any common sense application of the simple TDD steps will result in cleaner, simpler code that just works and can be proven to work.

A simple understanding is all that's required to benefit from TDD.

Developer TDD Methodology
-------------------------

The basic steps of TDD are as follows::
    
    1) Write a test
        - It will fail because the production code doesn't support it
    2) See it fail
        - To prove the test procedure is working, you must see it fail
    3) See it pass
        - Write production code until it passes
        - All tests must pass or the production code is wrong
    4) Refactor all the code
        - This is a good point to clean up tests and production code
    5) Go to step 1
    
This is sometimes summarized as::

    Red - Green - Refactor
       or
    Fail - Pass - Refactor

Add Another D (TDDD)
--------------------

It seems like the documentation is too often an afterthought in program development. I recommend that you add another D to TDD and make it **Test Driven Documented Development**.

Test Driven Documented Development (TDDD)
-----------------------------------------

Instead of delaying all the documentation for the end of the project, use the mantra::

    Red - Green - Refactor - Document 
       or
    Fail - Pass - Refactor - Document 
    
If you keep your *RST* files up to date as you develop, the documentation will be much higher quality and will likely even help you remember what you did at some critical future moment. More importantly, your good documentation will make a better first impression on those considering using your code.

If you are serious about open source and helping others, then being serious about good documentation must also be a priority.


Tk_Nosy TDD Methodology
-----------------------

Tk_Nosy takes the "Red - Green - Refactor" mantra literally.

When a new failing test is written, as soon as the file is saved, Tk_Nosy will show a Red bar and describe the nature of the Fail. 

As soon as new production code is added and the file is saved, Tk_Nosy will run nosetests on the project. When all tests pass, a Green bar indicates the Pass.

During the Refactor step, any time either the test files or production files are saved, Tk_Nosy will run nosetests, watching for regression errors during the code cleanup phase.

The Documentation step (hopefully you are using TDDD), is not currently being supported by Tk_Nosy. That is no excuse to ignore keeping the *RST* files up to date, however.

.. todo:: Write **tk_Sphinxy** to watch *RST* files, run sphinx when they change and launch or refresh system browser

