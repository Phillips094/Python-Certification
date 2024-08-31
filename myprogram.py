#import function from mymodule.py file
from mymodule import my_func

my_func()



#import module from MyMainPackage directory

from MyMainPackage import some_main_script

some_main_script.report_main()



#import module from MyMainPackage/SubPackage directory

from MyMainPackage.SubPackage import mysubscript

mysubscript.sub_report()




#import a specific function from MyMainPackage/SubPackage/mysubscript directory

from MyMainPackage.SubPackage.mysubscript import sub_report

sub_report()