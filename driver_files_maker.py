import os

def drive_func():
  print("Hello in driver maker")
  type=input("enter driver name ")
  os.mkdir(type+'_driver')
  os.chdir('./'+type+'_driver')
  f1=open(type+'_config.h', 'w')
  f2=open(type+'_register.h', 'w')
  f3=open(type+'_private.h', 'w')
  f4=open(type+'_program.c', 'w')
  f5=open(type+'_main.c', 'w')
  f6=open(type+'_interface.h', 'w')
  f5.write('#include'+type+'BIT_Math.h\n')
  f4.write('#include'+type+'STD_TYPES.h\n')
  f4.write('#include'+type+'_config.h\n')
  f4.write('#include'+type+'_register.h\n')
  f4.write('#include'+type+'_private.h\n')
  f4.write('#include'+type+'_interface.h\n')
  
  f5.write('#include'+type+'BIT_Math.h\n')
  f4.write('#include'+type+'STD_TYPES.h\n')
  f5.write('#include'+type+'STD_TYPES.h\n')
  f5.write('#include'+type+'_interface.h\n')

  f1.close()
  f2.close()
  f3.close()
  f4.close()
  f5.close()
  f6.close()
  
drive_func()