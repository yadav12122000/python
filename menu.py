import os
import subprocess as sp
import getpass

password=getpass.getpass("Enter your password : ")
pwd="arth"
if password!="arth":
        print("INCORRECT PASSWORD. TRY AGAIN ")
        exit()
print("CORRECT PASSWORD. PLZ COUNTINE:  ")


def hadoop():
    while True:
        os.system("clear")
        os.system("tput setaf 5")
        print("\t\t\t\t  HADOOP")
        print("\t\t\t =================")
        os.system('date')
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 3")
        print(""" 
        [WARNING]: Please ensure that you have already installed hadoop and jdk sofware. 
    Press 1: To use as a Client              Press 2: To use as a Namenode
    Press 3: To use as a Datanode            Press 4: To exit from hadoop menu.
    """)
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 2")
        ch=input("Enter your choice:")
        os.system("tput setaf 3")
        ch=int(ch)
        if ch==1:
            print("""You have to put ip address,block size,replication number in core-site.xml file.
            So I am opening the file....Plz enter""")
            input("Enter for editing the file:")
            os.system("vi /etc/hadoop/core-site.xml")
            os.system("hadoop dfsadmin -report")
            print("If you can see the report, you are ready to use HDFS cluster....")
            os.system("tput setaf 5")
            os.system("clear")
            print("""
            Press 1: To upload a file             Press 2: To remove the file
            Press 3: To read the file             Press 4: To go back to hadoop menu
            """)
            ch=input("Enter your choice:")
            ch=int(ch)
            if ch==1:
                filename=input("Enter the filename with ext. :")
                os.system("hadoop fs -put {} /".format(filename))
            elif ch==2:
                filename=input("Enter the filename with ext. :")
                os.system("hadoop fs -rm /{} ".format(filename))
            elif ch==3:
                filename=input("Enter the filename with ext. :")
                os.system("hadoop fs -cat /{} ".format(filename))
            elif ch==4:
                continue
            else:
                print("WRONG CHOICE")
        elif ch==2:
            print("Before starting the namenode you have to edit the core-site.xml and hdfs-site.xml files.So plz edit these....")
            input("Press enter for edit core-site.xml file....")
            os.system("vi /etc/hadoop/core-site.xml")
            input("Press enter for edit hdfs-site.xml file....")
            os.system("vi /etc/hadoop/hdfs-site.xml")
            print("Plz create the folder you entered in hdfs-site.xml file")
            os.system("tput setaf 7")
            folder=input("Enter the folder name:")
            os.system("mkdir /{}".format(folder))
            os.system("hadoop namenode -format")
            print("Starting namenode .......")
            os.system("hadoop-daemon.sh start namenode")
            input("Press enter for checking the service is started or not")
            os.system("jps")
            os.system("hadoop dfsadmin -report")
        elif ch==3:
            print("Before starting the datanode you have to edit the core-site.xml and hdfs-site.xml files.So plz edit these....")
            input("Press enter for edit core-site.xml file....")
            os.system("vi /etc/hadoop/core-site.xml")
            input("Press enter for edit hdfs-site.xml file....")
            os.system("vi /etc/hadoop/hdfs-site.xml")
            print("Plz create the folder you entered in hdfs-site.xml file")
            os.system("tput setaf 7")
            folder=input("Enter the folder name:")
            os.system("mkdir /{}".format(folder))
            print("Starting namenode .......")
            os.system("hadoop-daemon.sh start datanode")
            input("Press enter for checking the service is started or not")
            os.system("jps")
            os.system("hadoop dfsadmin -report")
        elif ch==4:
            return
        else:
            print("WRONG OPTION")
            
        os.system("tput setaf 2")
        input("Press enter for continue")



def package():
    while True:
        os.system("clear")
        os.system("tput setaf 5")
        print("\t\t\t PACKAGE STORE")
        print("\t\t\t =================")
        os.system('date')
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 3")
        print("""
    Press 1: To install any package                Press 2: To uninstall
    Press 3: To install python modules             Press 4: To uninstall python modules
    Press 5: To check the all python modules       Press 6: To install a third-party downloaded software
    Press 7: To check all the installed softwares. Press 8: To clear the package cache
    Press 9: To start or stop any service.         Press 10: To exit from package menu.
    """)
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 2")
        ch=input("Enter your choice:")
        os.system("tput setaf 3")
        ch=int(ch)
        if ch==1:
            package=input("Enter the package name:")
            os.system("yum install {}".format(package))
        elif ch==2:
            package=input("Enter the package name:")
            os.system("yum uninstall {}".format(package))
        elif ch==3:
            package=input("Enter the module name:")
            os.system("pip3 install {}".format(package))
        elif ch==4:
            package=input("Enter the module name:")
            os.system("pip3 uninstall {}".format(package))
        elif ch==5:
            os.system("pip3 list")
        elif ch==6:
            print("[WARNING] : Make sure you already download the software.") 
            package=input("Enter the complete package name:")
            os.system("rpm -ivh {}".format(package))
        elif ch==7:
            os.system("rpm -q -a")
        elif ch==8:
            os.system("yum clean packages")
        elif ch==9:
            servicename=input("Enter the service name:")
            state=input("Choose the state of the servie(start/stop/enable/disable):")
            print(f"Your service {servicename} is going to be {state}.") 
            os.system("systemctl {} {}".format(state,servicename))
        elif ch==10:
            return
        else:
            print("WRONG OPTION")
        os.system("tput setaf 2")
        input("Press enter for continue")

def network():
    while True:
        os.system("clear")
        os.system("tput setaf 5")
        print("\t\t\t\t NETWORK")
        print("\t\t\t ======================")
        os.system('date')
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 3")
        print("""
    Press 1: To ping with other system        Press 2: To display ip 
    Press 3: To capture network packets       Press 4: To check occupied ports
    Press 5: To get the ip address of any web Press 6: To remote login to other system
    Press 7: To upload any file via SSH       Press 8: To download any file via SSH
    Press 9: To go back to menu program
    """)
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 2")
        ch=input("Enter your choice:")
        os.system("tput setaf 3")
        ch=int(ch)
        if ch ==1:
            ip=input("Enter the ip address you want to ping..")
            os.system("ping -c 5 {}".format(ip))
        elif ch==2:
            os.system("ifconfig")
        elif ch==3:
            cardname=input("Enter the  network card name (enp0s3/eth0/others):")
            port=input("Enter the port number on which you want to capture:")
            os.system("tcpdump -i {} port {} -n".format(cardname,port))
        elif ch==4:
            os.system("netstat -tnlp")
        elif ch==5:
            website=input("Enter the website to see ip of site:")
            os.system("nslookup {}".format(website))
        elif ch==6:
            ip=input("Enter the ip of the system you want to login:")
            user=input("Enter the username of remote system:")
            os.system("ssh {}@{} ".format(user,ip))
        elif ch==7:
            filename=input("Enter the file with location.e.g.(/path/of/file/file.txt):")
            ip=input("Enter the ip of the remote system:")
            remoteposition=input("Enter the path where you want to upload(e.g./root/):")
            os.system("scp {} {}:{} ".format(filename,ip,remoteposition))
        elif ch==8:
            filename=input("Enter the file with location where you want to save.e.g.(/path/of/file/file.txt):")
            ip=input("Enter the ip of the remote system:")
            remoteposition=input("Enter the path where where you want to download(e.g./root/):")
            os.system("scp {} {}:{} ".format(ip,remoteposition,filename))
        elif ch==9:
            return
        else:
            print("WRONG OPTION")
        os.system("tput setaf 2")
        input("Press enter for continue")
def local():
    while True:
        os.system("clear")
        os.system("tput setaf 5")
        print("\t\t\t System automation by python")
        print("\t\t\t ======================")
        os.system('date')
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 3")
        print("""
        Press 1: To display the date       Press 2: To display the calender
    Press 3: To display the RAM info       Press 4: To clear the cache memory
    Press 5: To add a new user             Press 6: To remove the user
    Press 7: To start firefox              Press 8: To change the password of any user.
    Press 9: To check number of CPU's.     Press 10: To go back to menu.
    """)
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 2")
        ch=input("Enter your choice:")
        os.system("tput setaf 3")
        ch=int(ch)
        if ch==1:
            os.system("date")
        elif ch==2:
            os.system("cal")
        elif ch==3:
            os.system("free -m")
        elif ch==4:
            os.system("echo 3 > /proc/sys/vm/drop_caches")
        elif ch==5:
            user_name=input("Enter the new username")
            os.system("useradd {}".format(user_name))
        elif ch==6:
            user_name=input("Enter the new username")
            os.system("userdel {}".format(user_name))
        elif ch==7:
            os.system("firefox")
        elif ch==8:
            user=input("Enter the user name to change password:") 
            os.system("passwd {}".format(user))
        elif ch==9:
            os.system("lscpu")
        elif ch==10:
            return
        else: 
            print("option not supported")
        os.system("tput setaf 2")
        input("Enter for continue...")

def docker():
    while True:
        def list_container():
            return sp.getoutput("docker ps -a")
        def list_images():
            return sp.getoutput("docker images")
        def pull_image():
            image_name=input("Enter the image name:")
            return sp.getoutput("docker pull {} ".format(image_name))
        def start_cont():
            os_name=input("Enter the container name:")
            image_name=input("Enter the image name:")
            return sp.getoutput("docker run -dit --name {} {}".format(os_name,image_name)) 
        def stop_cont():
            os_name=input("Enter the container name:")
            return sp.getoutput("docker stop {}".format(os_name))
        def restart_cont():
            os_name=input("Enter the container name:")
            return sp.getoutput("docker start {}".format(os_name))
        os.system("clear") 
        os.system("tput setaf 5")
        print("\t\t\t Docker automation by python")
        print("\t\t\t ======================")
        os.system('date')
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 3")
        print("""
        Press 1: To list container                 Press 2: To list images
        Press 3: To pull images from docker hub    Press 4: To start a new container
        Press 5: To stop the container             Press 6: To restart the container
        Press 7: To go back to menu
        """)
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 2")
        ch=input("Enter your choice:")
        os.system("tput setaf 3")
        ch=int(ch)
        if ch==1:
            o1=list_container()
            print(o1)
        elif ch==2:
            o2=list_images()
            print(o2)
        elif ch==3:
            o3=pull_image()
            print(o3)
        elif ch==4:
            o4=start_cont()
            print(o4)
        elif ch==5:
            o5=stop_cont()
            print(o5)
        elif ch==6:
            o6=restart_cont()
            print(o6)
        elif ch==7:
            return
        else:
            print("option not supported")
        os.system("tput setaf 2")
        input("Enter for continue")

def lvm():
    while True:
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
            os.system("lvreduce --size {} {}".format(size,lv))
            os.system("resize2fs {}".format(lv))
        def reback():
            return 
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
        Press 17: To go back.
        """)
        os.system("tput setaf 7")
        print("\t ====================================================")
        os.system("tput setaf 2")
        ch=input("Enter your choice:")
        os.system("tput setaf 3")
        ch=int(ch)
        if ch==1:
            o1=disk_info()
            print(o1)
        elif ch==2:
            o2=make_part()
            print(o2)
        elif ch==3:
            o3=part_info()
            print(o3)
        elif ch==4:
            o4=format_part()
            print(o4)
        elif ch==5:
            o5=mount()
            print(o5)
        elif ch==6:
            o6=umount()
            print(o6)
        elif ch==7:
            o7=details()
            print(o7)
        elif ch==8:
            o8=resizing()
            print(o8)
        elif ch==9:
            create_pv()
        elif ch==10:
            disp_pv()
        elif ch==11:
            create_vg()
        elif ch==12:
            disp_vg()
        elif ch==13:
            create_lv()
        elif ch==14:
            disp_lv()
        elif ch==15:
            extend_size()
        elif ch==16:
            reduce_size()
        elif ch==17:
            return
        else:
            print("option not supported")
        os.system("tput setaf 2")
        input("Enter for continue")
def aws():
    os.system("clear")
    os.system("aws configure")
    while True:
        os.system("clear")
        os.system("tput bold")
        os.system("tput smul")
        print("AWS")
        os.system("tput sgr0")
        os.system("tput rmul")
        print("""\nPress a: create a key pair
Press b: ec2
Press c: ebs
Press d: Security Group
Press e: S3 bucket
Press f: Exit to main menu""")
        dc=input("Enter your choice : ")
        if dc=='a':
            key=input("Enter your key name:")
            os.system("aws create-key-pair --key-name {}".format(key))
        elif dc=='b':
            print("""\nPress a: Launching_ec2
Press b: Describe_ec2
Press c: Stoping_ec2
Press d: Starting_ec2
Press e: Terminating_ec2
Press f: Exit to AWS menu""")
            ec=input("Enter your choice : ")
            if ec == 'a' :
                ec2_image=input("Enter image id : ")
                print("Instance types \n t2.nano \t t2.micro \t t2.small \t t2.medium ")
                ec2_type=input("Enter instance type : ")
                ec2_security=input("Enter security group id : ")
                os.system("aws ec2 describe-key-pairs")
                ec2_key=input("Enter key name : ")
                ec2_count=input("Enter number of instances : ")
                os.system("aws ec2 run-instances   --security-group-ids   {}   --instance-type  {} --image-id {}   --key-name {}  --count {}".format(ec2_security,ec2_type,ec2_image,ec2_key,ec2_count))

            elif ec== 'b' :
                os.system("aws ec2 describe-instances")
            elif ec == 'c' :
                s_ec2=input("Enter the instance id :")
                os.system("aws ec2 stop-instances --instance-ids {}".format(s_ec2))
            elif ec == 'd' :
                s_ec2=input("Enter the instance id :")
                os.system("aws ec2 start-instances --instance-ids {}".format(s_ec2))
            elif ec == 'e' :
                s_ec2=input("Enter the instance id :")
                os.system("aws ec2 terminate-instances --instance-ids {}".format(s_ec2))
            elif ec == 'f':
                continue
            else :
                print("please enter correct optionn..")
        elif dc == 'c' :
            print("""\nPress a: Create_ebs-Storage
Press b: Describe_ebs
Press c: Attaching_ebs
Press d: Detach ebs
Press e: Deleting_ebs
Press f: Exit to AWS menu""")
            ebs=input("Enter your choice : ")
            if ebs == 'a' :
                size=input("Enter the size of the volume :")
                os.system("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone ap-south-1a".format(size))
            elif ebs == 'b':
                os.system("aws ec2 describe-volumes")
            elif ebs == 'c':
                v_id=input("Enter the id of the volume")
                e_id=input("Enter the id of the intance")
                os.system("aws ec2  attach-volume   --volume-id {}   --instance-id {}  --device /dev/sdh".format(v_id,e_id))
            elif ebs == 'd':
                v_id=input("Enter the volume id : ")
                os.system("aws ec2 detach-volume --force --volume-id {}".format(v_id))
            elif ebs == 'f':
                continue
            else :
                return

        elif dc == 'd':
            print("""\nPress a: Create Security Group
Press b: Describe Security Group
Press c: delete Security Group
Press d: Exit to AWS menu""")
            sg=input("Enter your choice : ")
            if sg == 'a' :
                name=input("Enter the name of the security group :")
                des=input("Enter description of the security group :")
                os.system("aws ec2 create-security-group --group-name {} --description {}".format(name,des))
            elif  sg == 'b':
                s_id=input("Enter the Security Group id :")
                os.system("aws ec2 describe-security-groups --group-id {}".format(s_id))
            elif sg == 'c':
                s_id=input("Enter the Security Group id :")
                os.system("aws ec2 delete-security-group --group-id {}".format(s_id))
            elif sg == 'd':
                continue
            else :
                return

        elif dc == 'e':
            print("""\nPress a: Creating s3 bucket
Press b: uploding content to s3
Press c: delete bucket
Press d: Exit to AWS menu""")
            s3=input("Enter your choice : ")
            if s3 == 'a' :
                b_name=input("Enter your bucket name : ")
                os.system("aws s3 mb s3://{} --region ap-south-1".format(b_name))
            elif s3 == 'b':
                location=input("Enter the location of the file :")
                bucket=input("Enter the bucket name :")
                img=input("Enter the image name")
                os.system("aws s3 cp /{} s3://{}/{} --acl public-read".format(location,bucket,img))
            elif s3 == 'c':
                bucket=input("Enter the bucket name :")
                region=input("Enter the region :")
                os.system("aws s3api delete-bucket --bucket {} --region {}".format(bucket,region))
            elif s3 == 'd':
                continue

        elif dc == 'f':
            return
        else:
            os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """)
        input("Press Enter to continue...")



def menu():
    os.system("clear")
    os.system("tput setaf 5")
    print("\t\t\t  Automation by python")
    print("\t\t\t ======================")
    os.system('date')
    os.system("tput setaf 7")
    print("\t ====================================================")
    os.system("tput setaf 3")
    print("""
    Press 1: To docker related tasks        Press 2: To lvm 
    Press 3: To aws related tasks           Press 4: To local operating system
    Press 5: To networking related          Press 6: To software and service related tasks
    Press 7: To hadoop related tasks        Press 8: to exit
    """)
    os.system("tput setaf 7")
    print("\t ====================================================")
    os.system("tput setaf 2")
    ch=input("Enter your choice:")
    os.system("tput setaf 3")
    ch=int(ch)
    if ch==1:
        docker()
    elif ch==2:
        lvm()
    elif ch==3:
        aws()
    elif ch==4:
        local()
    elif ch==5:
        network()
    elif ch==6:
        package()
    elif ch==7:
        hadoop()
    elif ch==8:
        os.system("tput setaf 7")
        exit()
    else:
        print("WRONG CHOICE")
 
while True:
    os.system("clear")
    menu()
    os.system("tput setaf 2")
    input("press enter for continue:")
    os.system("tput setaf 7")

