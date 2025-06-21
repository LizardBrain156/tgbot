from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🤔 Кто я вообще такой?")],
        [KeyboardButton("💘 Как я вижу любовь и отношения?")],
        [KeyboardButton("🤓 Чем я люблю заниматься?")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Привет! 👋🏻\nРад, что смог тебя заинтересовать.\n\nО чём ты хотела бы почитать?",
        reply_markup=reply_markup
    )

    inline_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("📩 Написать мне", url="https://t.me/the_darkest1")]
    ])
    await update.message.reply_text("Или, если ты уже узнала всё, что хотела, жми сюда:", reply_markup=inline_markup)

async def general_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Меня зовут Сергей, мне 31 год. Я живу в небольшом городке под названием Сланцы в Ленинградской области. На данный момент я пытаюсь вкатиться в IT, в направление QA, если точнее. Мои субъективные плюсы и минусы:

➕ Весьма умён. Много знаю, многое умею, быстро соображаю.
➕ Говорят, у меня приятный голос.
➕ Не курю, равнодушен к алкоголю, вещества не пробовал и не хочу.
➕ Спокойный характер, без эмоциональных качелей, истерик и рукоприкладства.
➕ Исключительно верен, никогда не изменял.

➖ Внешне неказист (т.н. скошенный подбородок меня сильно портит, а на исправление я пока не заработал).
➖ Слабо приспособлен к жизни. Просто не испытываю к ней такой тяги, как большинство людей, поэтому не привык прилагать для выживания больше усилий, чем минимально необходимо. Так что я далёк от вершин богатства, статуса или на что там принято дрочить...
""")


async def love_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Я считаю любовь и отношения главным в жизни. Всё остальное подчинено им.

Я хочу проводить максимально возможное количество времени вместе, занимаясь вещами, которые мы оба любим. Всегда быть друг за друга горой, что бы ни случилось — в горе и в радости, в болезни и в здравии. Любить друг друга просто потому что ты — это ты, а я — это я.

Я искренне убеждён, что в жизни у каждого человека может быть лишь одно дело, которому он исключительно предан и которому отдаёт всего себя. Для многих это работа, для кого-то известность, для кого-то дети. Вариантов много, но мой — любовь, и от тебя я ожидаю того же.
"""
    )


async def hobbies_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Я чилловый домосед, который ценит покой и уют, так что и увлечения у меня соответствующие:
        
🎮 Моё главное хобби вот уже 20 с лишним лет — компьютерные игры. Я люблю серьёзные сюжетные игры, с хорошо прописанным миром, историей и персонажами. Очень ценю, когда у выбора есть ощутимые последствия. Хорошими примерами будут Ведьмак, Mass Effect, серия Метро 2033, Baldur's Gate.

🎲 Я вообще игрок, люблю играть практически во всё, во что можно играть. Карты, настолки, покидать дротики, покатать шары...

📽️ Ещё я люблю проводить время за просмотром фильмов и сериалов. Люблю научную фантастику, криминальные и военные драмы. Аниме не смотрю, как-то не заходит.

🤓 А ещё я очень люблю узнавать новое, поэтому часто смотрю документалки и ролики на тему истории и естественных наук.
"""
    )


async def contact_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        ""
    )

TOKEN = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^🤔 Кто я вообще такой\\?$"), general_info))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^💘 Как я вижу любовь и отношения\\?$"), love_info))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^🤓 Чем я люблю заниматься\\?$"), hobbies_info))

app.run_polling()
