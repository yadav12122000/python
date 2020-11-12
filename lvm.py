import os
import subprocess as sp

def lvm():
    def disk_info():
        return sp.getoutput("fdisk -l")
    def make_part():
        disk_name = input("Enter the complete disk name for e.g. /dev/sdb: ")
        return os.system("fdisk {} ".format(disk_name))
    def part_info():
        d_name = input("Enter the disk name:")
        return os.system("fdisk -l {}".format(d_name))
    def format_part():
        part=input("Enter the partition name(e.g. /dev/sdb1): ")
        return os.system("mkfs.ext4 {}".format(part))
    def mount():
        folder_name=input("Enter the folder name on which you want to mount the partition. ")
        part_name = input("Enter the formatted partition full name: ")
        return os.system("mount {} {}".format(part_name,folder_name))
    def umount():
        folder_name=input("Enter the folder name on which you want to unmount the partition. ")
        part_name = input("Enter the partition full name: ")
        return os.system("umount {} {}".format(part_name,folder_name))
    def details():
        return os.system("df -h")
    def resizing():
        print("Before resizing the partition,please make sure that you already unmount the partition.")
        part_name=input("Enter the unmounted partition name:")
        size = input("Enter the desired size of partition [e.g. 3G](should be less than max size of the disk):")
    def create_pv():
        disk_name=input("Enter the disk name :")
        return os.system("pvcreate {}".format(disk_name))
    def disp_pv():
        disk_name=input("Enter the disk name :")
        return os.system("pvdisplay {}".format(disk_name))
    def create_vg():
        pv1=input("Enter 1st PV name:")
        pv2=input("Enter 2nd PV name:")
        vg=input("Enter the name of the VG:")
        return os.system("vgcreate {} {} {}".format(pv1,pv2,vg))
    def disp_vg():
        vg=input("Enter the VG name:")
        return os.system("vgdisplay {}".format(vg))
    def create_lv():
        size=input("Enter the size of the Logical volume(e.g. 8G):")
        vg=input("Enter the name of the VG:")
        lv=input("Enter the name of the Logical volume:")
        return os.system("lvcreate --size {} --name {} {}".format(size,lv,vg))
    def disp_lv():
        lv=input("Enter the name of the Logical volume:")
        vg=input("Enter the name of the VG:")
        return os.system("lvdisplay {}/{}".format(vg,lv))
    def extend_size():
        lv=input("Enter the name of the Logical volume:")
        size=input("How much size you want to extend(e.g. 8G):")
        os.system("lvextend --size +{} {}".format(size,lv))
        os.system("resize2fs {}".format(lv))
    def reduce_size():
        lv=input("Enter the name of the Logical volume:")
        size=input("How much size you want to reduce(e.g. 8G):")
        os.system("lvreduce --size -{} {}".format(size,lv))
        os.system("resize2fs {}".format(lv))
    def reback():
        exit()
    os.system("clear")
    os.system("tput setaf 5")
    print("\t\t\t LVM automation by python")
    print("\t\t\t ======================")
    os.system('date')
    os.system("tput setaf 7")
    print("\t ====================================================")
    os.system("tput setaf 3")
    print("""
    Press 1: To get all the harddisks information.
    Press 2: To create partition.
    Press 3: To get all partitions information in one disk.
    Press 4: To format the partition.
    Press 5: To mount the partition to the directory.
    Press 6: To unmount the partition.
    Press 7: To get details of size and mount point of the disk.
    Press 8: To resize the partition(Partition should be unmounted)
    Press 9: To create Physical volume(PV).
    Press 10: To display PV information.
    Press 11: To create Volume Group(VG).
    Press 12: To display VG information.
    Press 13: To create logical volume(LV).
    Press 14: To display LV information.
    Press 15: To extend the size of LV's.
    Press 16: To reduce the size of LV's.
    Press 17: To exit.
    """)
    os.system("tput setaf 7")
    print("\t ====================================================")
    os.system("tput setaf 2")
    ch=input("Enter your choice:")
    os.system("tput setaf 3")

    if int(ch)==1:
        o1=disk_info()
        print(o1)
    elif int(ch)==2:
        o2=make_part()
        print(o2)
    elif int(ch)==3:
        o3=part_info()
        print(o3)
    elif int(ch)==4:
        o4=format_part()
        print(o4)
    elif int(ch)==5:
        o5=mount()
        print(o5)
    elif int(ch)==6:
        o6=umount()
        print(o6)
    elif int(ch)==7:
        o7=details()
        print(o7)
    elif int(ch)==8:
        o8=resizing()
        print(o8)
    elif int(ch)==9:
        create_pv()
    elif int(ch)==10:
        disp_pv()
    elif int(ch)==11:
        create_vg()
    elif int(ch)==12:
        disp_vg()
    elif int(ch)==13:
        create_lv()
    elif int(ch)==14:
        disp_lv()
    elif int(ch)==15:
        extend_size()
    elif int(ch)==16:
        reduce_size()
    elif int(ch)==17:
        os.system("tput setaf 7")
        reback()
    else:
        print("option not supported")
while True:
    os.system("clear")
    lvm()
    input("press enter for continue:")
    os.system("tput setaf 7")

