
# Start the program
Go into the root directory and enter
`docker-compose up`

You can connect to 
* The server at localhost:8080
* The database at localhost:81, which already contains a username "test".
* The client at localhost:3000

The docker container of the server may be exited if the database is not ready. To run it:
`docker start ayomi_server_1`