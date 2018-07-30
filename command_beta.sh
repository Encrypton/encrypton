###We will do it based on drive assignment, such as /dev/sdc1
#They must plug in the storage devices in the order that we state

#Command to encrypt
#First we must unmount with
umount /dev/sdc
#Then we encrypt with
cryptsetup --verbose -s 512 luksFormat /dev/sdc
#It will ask for a caps "YES" and then will ask for what password should be used, then asks to verify the password
