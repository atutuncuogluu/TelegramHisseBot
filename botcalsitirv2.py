import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Bot Tokenınızı Buraya Ekleyin
BOT_TOKEN = ''
TARGET_GROUP_ID = 0 

# Verileri Çeken Fonksiyon
def get_data():
    data = []
    current_entry = {}
    with open('veriler.txt', 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("Hisse: "):
                if current_entry:
                    data.append(current_entry)
                current_entry = {'Hisse': line.split('Hisse: ')[1]}
            elif current_entry:
                if line == "---------------------------------------":
                    data.append(current_entry)
                    current_entry = {}
                else:
                    key, value = line.split(': ')
                    current_entry[key] = value
    return data

def hisse(update, context):
    # Sadece hedeflenen gruptan gelen komutları işleyin
    if update.message.chat_id == TARGET_GROUP_ID:
        if context.args:
            hisse_adi = context.args[0]
            data = get_data()
            message = ''
            found = False
            for entry in data:
                if entry.get('Hisse') == hisse_adi:
                    found = True
                    message += f"{entry['Hisse']}:\n"
                    for key, value in entry.items():
                        if key != 'Hisse':
                            message += f"{key}: {value}\n"
                    message += "---------------------------------------\n"
            if found:
                # Kullanıcının ID'sini alın
                user_id = update.message.from_user.id
                # Kullanıcıya özel mesaj gönderin
                context.bot.send_message(chat_id=user_id, text=message)
                # Grup sohbetinde de yanıt verin
                #update.message.reply_text(message)
            else:
                update.message.reply_text(f"{hisse_adi} hissesi bulunamadı.")
        else:
            update.message.reply_text("Lütfen bir hisse adı belirtin. Örnek: /hisse AZTEK")
    else:
        # Hedeflenen grupta olmayan kullanıcılara cevap verme
        update.message.reply_text("Bu komutu kullanmak için yetkiniz yok.")

# Ana Fonksiyon
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('hisse', hisse, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()