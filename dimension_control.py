import os
import re
import sys


def dir_up(second_path):
    points = os.listdir(second_path)
    for point in points:
        point = os.path.join(second_path, point)
        if os.path.isdir(point):
            dir_up(point)
            if not os.listdir(point):
                os.rmdir(point)
        if os.path.isfile(point):
            file_up(point)

def file_up(point):
    file_from = point
    print('from:',file_from)
    if sys_type == 'win':
        file_to = root_path+'\\'+point.split(root_path+'\\')[1].replace('\\',replace_sample)
    elif sys_type == 'linux':
        file_to = root_path++'/'+point.split(root_path+'/')[1].replace('/',replace_sample)
    else:
        print('Wrong sysinfo!!')
    print('to  :',file_to)
    os.rename(file_from,file_to)

def file_down(point):
    file_from = point
    print('From:',file_from)
    if sys_type == 'win':
        file_to = root_path+point.split(root_path)[1].replace(replace_sample,'\\')
    elif sys_type == 'linux':
        file_to = root_path + point.split(root_path)[1].replace(replace_sample, '/')
    else:
        print('Wrong sysinfo!!')
    print('To  :',file_to)
    if not os.path.isdir(os.path.dirname(file_to)):
        print(os.path.dirname(file_to),'need to mk')
        os.makedirs(os.path.dirname(file_to))
    os.rename(file_from,file_to)




if __name__ == '__main__':
    sys_type = ''
    if os.path.isdir('c:\\'):
        sys_type = 'win'
        print('sys:win')
    elif os.path.isdir('/'):
        sys_type = 'linux'
        print('sys:linux')
    else:
        print('Wrong sysinfo!!')

    replace_sample = '--'
    command_recive = sys.argv
    command_num = len(command_recive)
    if command_num >1 :
        if command_recive[1] in ['h','help','-h','-help','--help']:
            print('Usage: ./dimension_control.py root [command] [re1] [re2]\n'
                  'commands: \n'
                  '     up/u : do Up\n'
                  '     down/d :do Down \n'
                  '     replace/r : Replace name with re\n')
        else:
            root_path = command_recive[1]
            root_path = os.path.abspath(root_path)
            if root_path == 'aa':
                root_path = 'D:\\0-Storage\\京阿尼-desktop\\'
            # print('root_path = ', root_path)
            if command_num > 2 :
                if os.path.isdir(root_path):
                    print('path selected as ',root_path,',marching on!\n')
                    if command_recive[2] in ['up','u']:
                        for point in os.listdir(root_path):
                            point = os.path.join(root_path,point)
                            if os.path.isdir(point):
                                dir_up(point)
                                if not os.listdir(point):
                                    os.rmdir(point)
                            if os.path.isfile(point):
                                # file_up(point)
                                pass
                        print('Work Done')

                    elif command_recive[2] in ['down','d']:
                        for point in os.listdir(root_path):
                            point = os.path.join(root_path, point)
                            file_down(point)
                        print('Work Done')

                    elif command_recive[2] in ['replace','r']:
                        if command_num > 3 :
                            re1 = command_recive[3]
                            print(re1)
                            if command_num > 4:
                                re2 = command_recive[4]
                            else:
                                re2 = ''
                            for point in os.listdir(root_path):
                                point = os.path.join(root_path, point)
                                file_from = point
                                print('From:', file_from)
                                file_to = root_path + re.sub(re1,re2,point.split(root_path)[1])
                                print('To  :', file_to)
                                os.rename(file_from,file_to)
                            print('Work Done')
                        else:
                            print('No re recived ,Abourting!!')
                    else:
                        print('Wrong command,Abourting!!')
                else:
                    print("It's not a path,abourting!!")
            else:
                print('Got no command ,Abourting!!')
    else:
        print('Usage: ./dimension_control.py root [command] [re1] [re2]')
