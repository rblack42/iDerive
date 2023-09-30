Project Documentation
#####################

Documenting any development project is an important task. Unfortunately, how to
document a project is not easy to figure out. In a |PY| project, many folks use
*Sphinx* and **autodoc** to generate documentation. If you examine a big
|PY| project, you discover that the **autodoc** generated
documentation relies on **docstring** comments embedded in the project source
code. This generates summary pages detailing how to use the components of the
project, but nothing about the theory behind each code component, unless that
information is embedded in the **docstrings** as well. 

Donald Knuth thought this approach to documentation was upside down. He
developed a different approach called *Literate Programming* where the primary
focus is on the documentation and the code is embedded in that documentation.
Of course you need a tool to extract the code from the documentation so it can
be processed normally.

*Literate Programming* never really took off, and it seems at odds with modern
programming practices used in source-code control systems like **git**. 

I write a lot of documentation aimed at students. These developers are just
learning how to build a project, and they need to understand how projects
evolve. The documents they need to read tell them how a serious project gets
set up and how the development tools are used to manage the their work. The level
of detail is much higher than what is needed for more routine development
projects.

While I like the ideas behind *Literate Programming* in that the documentation
and code are tied tightly together, maintaining that means that the developer
must update both parts at the same time. This *should* happen, but often does
not. This problem is not just an issue in *Literate Programming*! A classic
example is this:

..  code::  text

    # Set X to 3
    x = 2

Which is right? The comment or the code. I do know one thing. I do not trust
either at this point!

My Approach
***********


The documentation for this project is aimed at students with limited experience
in developing programs. The intended users of this project are probably
technical folks who spend most of their time working on the mathematics of a
problem, and not developing tools like this. Still, a subset of those folks do
write code, and I hope they might want to help extend this work and help me
improve things. 

The tools I will be using are these:

* **Git**  - manages both code and documentation
* **Sphinx** - All documentation is written in *reStructuredText and processed by *Sphinx*.
* **sphinx-autodoc** to document he actual project code.
* **PyTest** - unit testing is done using *PyTest* and supporting tools.

Initially, **docstrings** will be limited to basic descriptions of a component
and its parameters.
