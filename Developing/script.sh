#!/bin/bash
###We will do it based on drive assignment, such as /dev/sdc1
#They must plug in the storage devices in the order that we state
sudo su
#Command to encrypt
#First we must unmount with
umount /dev/sdc
#Then we encrypt with
cryptsetup --verbose -s 512 luksFormat /dev/sdc
#It will ask for a caps "YES" and then will ask for what password should be used, then asks to verify the password

#How to decrypt
#We must completly remove the encryption since we need to access it on other devices
How about we copy the encrypted data to local storage, then immidiatly format the USB and copy the data over
#open the drive
sudo cryptsetup luksOpen /dev/sdb1 decrypt_drive
#link it to a folder
sudo mkdir -p /mnt/decrypt_drive
sudo mount /dev/mapper/decrypt_drive /mnt/decrypt_drive
#copy all the files to local storage
mv -v /mtn/decrypt_drive/. /home/pi/decrypt_drive/
#format the flashdrive
umount /mnt/decrypt_drive/
cryptsetup luksClose /dev/mapper/decrypt_drive
mkfs.vfat -n 'decrypted' -I /dev/sda1
#move the files back to the flashdrive
mkdir -p /mnt/decrypted
mount /dev/sda1 /mnt/decrypted
mv -v /home/pi/decrypt_drive/. /mnt/decrypted/
#delete all of the folders that were created
umount /mnt/decrypted
rm -R /mnt/main_drive 
rm -R /mnt/decrypted
rm -R /dev/mapper/main_drive

##Use https://www.loganmarchione.com/2015/05/encrypted-external-drive-with-luks/#Step_5_8211_Unlock_the_LUKS_device
#To find more data
