# gittask
Master branch was empty. In the task it was asked to make PR for every feature branch and merge to master branch...
we believe that in task 1. result won't be visible without additional configs or restart of the system
task 3a - we are getting "ERROR! Syntax Error while loading YAML". There is an issue with YAML indentation. Additionally ansible playbook is trying to access passenger.conf file which is not in this folder but in 3b?!
task 3b - there is an issue with Xenial repo and key, they are not specified so installation does not go through for us. Additionally the naming of variables is messed up, you defined vars user, password and you try to use dbuser and dbpassword below
task 3c - we again had syntax error: apt: pkg=$item state=latest should be apt: pkg=$item state=latest (we used ansible 2.3.2.0, maybe you had another version...)
