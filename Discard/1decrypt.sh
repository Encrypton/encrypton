#!/bin/bash
#How to decrypt
echo "This works"
#We must completly remove the encryption since we need to access it on other de$
#How about we copy the encrypted data to local storage, then immidiatly format t$
#open the drive
sudo cryptsetup luksOpen /dev/sda decrypt_drive
#link it to a folder
mkdir -p /mnt/decrypt_drive
mount /dev/mapper/decrypt_drive /mnt/decrypt_drive
#copy all the files to local storage
mv -v /mnt/decrypt_drive/. /home/pi/decrypt_drive/
#format the flashdrive
umount /mnt/decrypt_drive/
cryptsetup luksClose /dev/mapper/decrypt_drive
mkfs.vfat -n 'decrypted' -I /dev/sdc1
#move the files back to the flashdrive
mkdir -p /mnt/decrypted
mount /dev/sdc1 /mnt/decrypted
mv -v /home/pi/decrypt_drive/. /mnt/decrypted/
#delete all of the folders that were created
umount /mnt/decrypted
rm -R /mnt/main_drive 
rm -R /mnt/decrypted
