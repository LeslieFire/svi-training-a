#Heroku Guides
###Exporting remote database to local
1. On the terminal inside the heroku repo, type:

  ```heroku pg:backups capture```
  
  This will create a backup file for your heroku database normally named with the syntax similar to ```b001```. Sometimes it takes long to create the backup but you can just leave it and do something as the backup creation continues unless intentionally stopped with a heroku command (**ctrl-c** will only stop the monitoring).
2. On your terminal still inside the repo, type:

  ```heroku pg:backups public-url <name of backup. Something similar to b001>```
  
  This will give you a url of the backup db which when visited will automatically download the db to the local.
3. To restore the db in the local, first create a blank db and then on your terminal:

  ```pg_restore --verbose --clean --no-acl --no-owner -h localhost -U myuser -d <name of db> <name of file>```
  
  This will create the schema and the rows inside the blank db and there. You just successfully exported the remote heroku db to local.
