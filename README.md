
![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Chaturbate_logo.svg/2560px-Chaturbate_logo.svg.png)


# Member Info Web Backend

This project is a backend for the Chaturbate Member Info project

📚 Libs:
-
- Django
- Django Rest Framework
- Requests



## 👨🏻‍💻 How to install:

#### 1️. Create Virtual Environment
```bash
  python3 -m venv venv
```

#### 2️. Activate It
Mac OS \ Linux:
```bash
  source venv/bin/activate
```
Windows:
```bash
  source venv/Scripts/activate
```

#### 3️. Install Requirements
```bash
  pip install -r requirements.txt
```

#### 4️. Go to MemberInfoWeb:
```bash
  cd MemberInfoWeb
```

#### 5️. Make Migrations
```bash
  python manage.py makemigrations
```

#### 6️. Migrate It
```bash
  python manage.py migrate
```

#### 7️. Create Superuser
```bash
  python manage.py createsuperuser
```

#### 8️. Run Server
```bash
  python manage.py runserver
```
## 👾 Management Commands

There are some managerial commands in the project that are worth setting to auto-execute the system

### 1. License Update

At runtime, this script checks all license records and marks as inactive those that have expired, and marks the has_license field of linked users as False. If the license expiration date has been extended, the license is marked as active and has_license for the user is set to True

#### How to execute:
```bash
  python manage.pu update_licenses
```

### 2. Stop Inactive Poller Processes

At runtime it checks all records of running processes and tries to stop those whose updated_at field has not been updated for more than 10 minutes

#### How to execute:
```bash
  python manage.pu stop_inactive_poller_processes
```


## 💀 Support

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat-squeare&logo=telegram&logoColor=white)](https://t.me/ihatemylifebutiluvmoney)


## 🔗 My Links
[![portfolio](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/herbalsomml)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/herbalsomml)

