# mojteposudu_bot

## Info
Bot made to control sequence of homework, for you and your neighbours

## Usage
you need to have file configs.py, which will contain
`
users = [['name', telegram_user_id],...]
BOT_ID = your_bot_id
cleaningwork = ['name of clean routine'...] # len(cleaningwork) == len(users)
`

then launch launching.py

## Dependencies
aiogram
apscheduler