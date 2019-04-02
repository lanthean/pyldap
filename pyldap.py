#!/usr/bin/env python
#-*- coding:utf-8 -*-
###
# @Author   Martin Bortel <martin.bortel@mavenir.com>
# @Created  07/03/2019
# @Updated  07/03/2019
#
# @Package  
###

# Imports
ldap

## TODO
# place your code here (eg> class and function definitions),
# leave the definition of main() to the end of file (standard)

##
# @method main
# @uses - main method /always called first
def main():
    # this is the main function called when interpreting
    # use as interface
    print 'Hello world'

    try:
        dir(ldap)
        ldap.__dict__
    except Exception as e:
        print("Ldap issue")
        raise e

# boilerplate code to run the main function if it is not a import..
if __name__ == '__main__':
    main()
# EOF
###
