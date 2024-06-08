# sms_verification

[![LICENSE](https://img.shields.io/badge/LICENSE-GPL--3.0-green)](https://github.com/jadijadi/sms_serial_verification/blob/master/LICENSE) 
[![Requirements](https://img.shields.io/badge/Requirements-See%20Here-orange)](https://github.com/jadijadi/sms_serial_verification/blob/master/requirements.txt)
[![Todo](https://img.shields.io/badge/Todo-See%20Here-success)](https://github.com/jadijadi/sms_serial_verification/blob/master/TODO.md)

This project is done for Altech (Schneider Electric Iran) as an educational series. 

<div dir="rtl"> 
این پروژه ای است به سفارش آلتک (اشنایدر الکتریک ایران) برای سنجش صحت شماره سریال ها با پیامک. 
جادی پروژه رو ازشون قبول کرده به این شرط که همه مراحلش رو ضبط و منتشر کنه تا نمونه ای باشه از انجام یک پروژه واقعی توسط یک فریلنسر. در این پروژه از تکنولوژی های زیر استفاده می شه:

- پایتون
- فلسک
- ای پی آی های دریافت و ارسال اسمس از درگاه پیامک کاوه نگار
- پاس فندق
- مای اسکوئل


## How to run
1. Install python3, pip3, virtualenv, MySQL in your system.
2. Clone the project `git clone https://github.com/jadijadi/sms_serial_verification && cd sms_serial_verification`
3. in the app folder, rename the `config.py.sample` to `config.py` and do proper changes.
4. db configs are in config.py. Create the db and grant all access to the specified user with specified password.
5. Create a virtualenv named venv using `virtualenv -p python3 venv`
6. Connect to virtualenv using `source venv/bin/activate`
7. From the project folder, install packages using `pip install -r requirements.txt`
8. Now environment is ready. Run it by `python app/main.py`

## Example of creating db and granting access:

> Note: this is just a sample. You have to find your own systems commands.

```
CREATE DATABASE smsmysql;
USE smsmysql;
CREATE USER 'smsmysql'@'localhost' IDENTIFIED BY 'test' PASSWORD NEVER EXPIRE;
GRANT ALL PRIVILEGES ON smsmysql.* TO 'smsmysql'@'localhost';
```

