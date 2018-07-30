###We will do it based on drive assignment, such as /dev/sdc1
#They must plug in the storage devices in the order that we state

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
sudo cryptsetup luksOpen /dev/sdb1 volume01
#link it to a folder
sudo mount /dev/mapper/volume01 /mnt/drive01
#copy all the files to local storage
cp -a /mtn/main_drive/. /dest/
#format the flashdrive
mkfs.vfat -n 'decrypted' -I /dev/sdb1
#move the files back to the flashdrive
cp -a /dest/. /media/root/decrypted
#delete all of the folders that were created
rm -R /mnt/main_drive 
rm -R /dev/mapper/main_drive

##Use https://www.loganmarchione.com/2015/05/encrypted-external-drive-with-luks/#Step_5_8211_Unlock_the_LUKS_device
#To find more data
