FROM python:latest
FROM gorialis/discord.py

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

COPY sleeps_til_bot.py .

CMD [ "python", "./sleeps_til_bot.py" ]
