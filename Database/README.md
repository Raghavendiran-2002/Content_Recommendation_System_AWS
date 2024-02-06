# Content_Recommendation_System_AWS

## Setup AWS RDS (MYSQL) and insert data into DB

1. Fill up the following

   - DB instance identifier = YOUR DB NAME
   - Engine options - MySQL
   - Templates - Free Tier
   - Master username (DB-username) = admin
   - Master password (DB-password) = ""
   - Public access = Yes

2. Update Security Rule

   - add Inbound rules
     - CIDR blocks = 0.0.0.0/0
     - Type = MySQL/AURORA

3. Change .env.prod variables

   - DBUSER
   - DBPASS
   - DATABASE
   - DBHOST

4. run
   `python3 main.py`
