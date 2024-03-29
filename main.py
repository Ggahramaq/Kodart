import discord
from datetime import datetime
from discord.ext import commands
from io import BytesIO
from discord.ui import Button, View, Modal
import sqlite3
import requests

conn = sqlite3.connect('update.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS updates (update_text TEXT)''')
conn.commit()


connn = sqlite3.connect('updates.db')
cn = connn.cursor()

cn.execute('''CREATE TABLE IF NOT EXISTS updates (updates TEXT)''')
connn.commit()


class SelectRules(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Правило №1",
                value="who_we_are",
                description="Покажет первое правило",
                emoji="<:00settings:1215000851597238342>"
            ),
            discord.SelectOption(
                label="Правило №2",
                value="expectations",
                description="Покажет второе правило",
                emoji="<:kodart:1215282442760355881>"
            ),
            discord.SelectOption(
                label="Правило №3",
                value="account_info",
                description="Покажет третье правило",
                emoji="<:starr:1215281872611975230>"
            ),
        ]

        super().__init__(
            placeholder="Выберите тему...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "who_we_are":
            em = discord.Embed(title="Правило №1", description="Вам нужно бежать.", color=discord.Colour.blurple(), timestamp=interaction.message.created_at)
            em.set_footer(text="Kodart | Firecat, Prosto S, lucky.snake, ggahramaq")
            await interaction.response.send_message(embed=em, ephemeral=True)
        elif self.values[0] == "expectations":
            em = discord.Embed(title="Правило №2", description="Вам нужно будет подбирать щит.", color=discord.Colour.blurple(), timestamp=interaction.message.created_at)
            em.set_footer(text="Kodart | Firecat, Prosto S, lucky.snake, ggahramaq")
            await interaction.response.send_message(embed=em, ephemeral=True)
        elif self.values[0] == "account_info":
            em = discord.Embed(title="Правило №3", description="Вам нужно будет избегать препятствий.", color=discord.Colour.blurple(), timestamp=interaction.message.created_at)
            em.set_footer(text="Kodart | Firecat, Prosto S, lucky.snake, ggahramaq")
            await interaction.response.send_message(embed=em, ephemeral=True)








class SelectCreators(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Ggahramaq",
                value="ggahramaq",
                description="Пайтон программист.",
                emoji="<a:chipi:1218879261314912278>"
            ),
            discord.SelectOption(
                label="Prosto S",
                value="prosto_s",
                description="3д дизайнер.",
                emoji="<:shock:1217841430110666752>"
            ),
            discord.SelectOption(
                label="Firecat",
                value="firecat",
                description="Крутой микрочелик-юнитиюэер.",
                emoji="<:firee:1217841342533861417>"
            ),
            discord.SelectOption(
                label="Lucky.snake",
                value="lucky_snake",
                description="Фронтенд и бэкенд разработчик.",
                emoji="🪐"
            ),
        ]

        super().__init__(
            placeholder="Выберите разработчика...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "ggahramaq":
            em = discord.Embed(title="Информация о пользователе **Ggahramaq**", description="<a:danceee:1218879327022743612>**Ggahramaq** - опытный программист, специализирующийся на языке **Python**. Обладает глубоким знанием различных фреймворков, включая **Django**, **Quart**, и особенно хорошо владеет фреймворком **Flask**. Кроме этого, он знает язык программирования **Javascript**, а также хорошо разбирается в фреймворке **Node.js**, он также разбирается в разных базы данных и умеет создавать Discord ботов.<a:danceee:1218879327022743612>", color=discord.Colour.blurple(), timestamp=interaction.message.created_at)
            em.set_footer(text="Kodart | Firecat, Prosto S, lucky.snake, ggahramaq")
            await interaction.response.send_message(embed=em, ephemeral=True)
        elif self.values[0] == "prosto_s":
            em = discord.Embed(title="Информация о пользователе **Prosto S**", description="<:shock:1217841430110666752>**Prosto S** - зовут Сергей, он делал 3d модели для игры **KodArt Runner**. Также он хороший майнкрафт строитель.<:shock:1217841430110666752>", color=discord.Colour.blurple(), timestamp=interaction.message.created_at)
            em.set_footer(text="Kodart | Firecat, Prosto S, lucky.snake, ggahramaq")
            await interaction.response.send_message(embed=em, ephemeral=True)
        elif self.values[0] == "firecat":
            em = discord.Embed(title="Информация о пользователе **Firecat**", description="<:firee:1217841342533861417>**Firecat** - зовут Ильяс. Ему 14 лет, учится в сфере IT более 4 лет. Пишет сайты на веб-конструкторе Tilda, делает игры на движке Unity.<:firee:1217841342533861417>", color=discord.Colour.blurple(), timestamp=interaction.message.created_at)
            em.set_footer(text="Kodart | Firecat, Prosto S, lucky.snake, ggahramaq")
            await interaction.response.send_message(embed=em, ephemeral=True)
        elif self.values[0] == "lucky_snake":
            em = discord.Embed(title="Информация о пользователе **Lucky_snake**", description="🪐**Lucky_Snake** - Веб-дизайнер. Фронт энд и бэк энд дизайнер. Делает сайт для игры **Kodart Runner**.🪐", color=discord.Colour.blurple(), timestamp=interaction.message.created_at)
            em.set_footer(text="Kodart | Firecat, Prosto S, lucky.snake, ggahramaq")
            await interaction.response.send_message(embed=em, ephemeral=True)

class CreatorsView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(SelectCreators())


class RulesView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(SelectRules())

class Review(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            discord.ui.InputText(
                style=discord.InputTextStyle.short,
                label="Оценка",
                required=True,
                placeholder="Введите вашу оценку(10/10)"
            ),
            discord.ui.InputText(
                style=discord.InputTextStyle.long,
                label="Отзыв",
                required=True,
                placeholder="Напишите отзыв о игре"
            ),
            *args,
            **kwargs,
        )
    
    async def callback(self, interaction: discord.Interaction):
        user_id = 906115102888046623
        userr = await bot.fetch_user(user_id)
        embed = discord.Embed(title="Новая Заявка!", description=f"{interaction.user.name} написал отзыв!", color=discord.Colour.blurple(), timestamp=interaction.message.created_at)
        embed.add_field(name="Оценка:", value=f"{self.children[0].value}<:starr:1215281872611975230>", inline=True)
        embed.add_field(name="Отзыв:", value=f"Отзыв: {self.children[1].value}<:kodart:1215282442760355881>", inline=True)
        embed.set_footer(text="Kodart | Firecat, Prosto S, lucky.snake, ggahramaq")
        embed.set_author(name=interaction.user)
        await userr.send(embed=embed)
        await interaction.response.send_message("Ваш отзыв был отправлен!", ephemeral=True)

class UpdatesSubmitView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.bot = bot
        self.value = None

    @discord.ui.button(label='Yes', style=discord.ButtonStyle.success)
    async def yes_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        channel_id = 1223219861426012200
        c.execute("SELECT update_text FROM updates")
        new_update_text = c.fetchone()[0]
        cn.execute("INSERT INTO updates (updates) VALUES (?)", (new_update_text,))
        connn.commit()
        channel = self.bot.get_channel(channel_id)
        button = Button(label="Оставить отзыв..", style=discord.ButtonStyle.grey, emoji="<:00settings:1215000851597238342>")
    
        async def button_callback(interaction):
            modal = Review(title="Отзыв") 
            await interaction.response.send_modal(modal)

        button.callback = button_callback

        view = View()
        view.add_item(button)
        view.timeout = None
        if channel:
            await channel.send(
f"""
# Произошло новое обновление в игре!

`{new_update_text}`
""", view=view)
        await interaction.response.send_message("Вы добавили новое обновление!")
            
        



    @discord.ui.button(label='Edit', style=discord.ButtonStyle.grey)
    async def edit_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        c.execute("SELECT update_text FROM updates")
        new_update_text = c.fetchone()[0]
        view = Update(title="Обновление", interaction=interaction, previous_input=new_update_text)
        await interaction.response.send_modal(view)


    @discord.ui.button(label='No', style=discord.ButtonStyle.danger)
    async def no_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.delete_original_response()


class Update(Modal):
    def __init__(self, interaction = discord.Interaction, previous_input=None, *args, **kwargs) -> None:
        super().__init__(
            discord.ui.InputText(
                style=discord.InputTextStyle.long,
                label="Обновление",
                required=True,
                placeholder="**Произошел новый багфиксинг**",
                value=previous_input,
            ),
            *args,
            **kwargs,
        )
    
    async def callback(self, interaction: discord.Interaction):
        c.execute("DELETE FROM updates")

        c.execute("INSERT INTO updates (update_text) VALUES (?)", (self.children[0].value,))
        conn.commit()

        embed = discord.Embed(title="Ваше обновление было написанно! Опубликовать?", description=
f"""
**Вот так выглядит ваш текст:**
`{self.children[0].value}`
""", color=discord.Colour.blurple(), timestamp=interaction.message.created_at)
        embed.set_footer(text="Kodart | Firecat, Prosto S, lucky.snake, ggahramaq")
        view = UpdatesSubmitView()
        await interaction.response.send_message(embed=embed, view=view)



class UpdatesView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Yes', style=discord.ButtonStyle.success)
    async def yes_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        modal = Update(title="Обновление")
        await interaction.response.send_modal(modal)

    @discord.ui.button(label='No', style=discord.ButtonStyle.danger)
    async def no_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.delete_original_response()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)
random_command = "helloworld"





@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    userr_id = 1042775942646485002
    userrr = await bot.fetch_user(userr_id)
    await userrr.send("**Команда `!kodartupdatescom` работает для вас!**")

@bot.slash_command()
async def rules(interaction):
    view = RulesView()
    await interaction.response.send_message(
"""
**Пожалуйста, выберите правило ниже.**
"""
, view=view)

@bot.command()
async def kodartupdatescom(ctx):
    allowed_user_id = 1042775942646485002  

    if ctx.author.id == allowed_user_id and isinstance(ctx.channel, discord.DMChannel):
        view = UpdatesView()
        await ctx.send("Вы хотите опубликовать новое обновление?",view=view)
    elif ctx.author.id != allowed_user_id:
        await ctx.send("У вас нет прав добавлять обновления!")
    else:
        await ctx.send("Эту команду можно запускать только в личных сообщениях.")




@bot.slash_command()
async def updates(ctx):
    connection = sqlite3.connect('updates.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM updates')
    updates = cursor.fetchall()

    if not updates:
        await ctx.response.send_message("Пока что нету никаких обновлений!")
        return

    number_emojis = {
        1: "<:onee:1218799891111739483> ",
        2: "<:twoo:1218799861407813672> ",
        3: "<:threee:1218799812443508783> ",
        4: "<:fourr:1218799754285158420>",
        5: "<:fivee:1218799706616893452> ",
        6: "<:sixx:1218799666104373318> ",
        7: "<:sevenn:1218799638237286501> ",
        8: "<:eightt:1218799581035364363> ",
        9: "<:ninee:1218799542183526490>",
        0: "<:zeroo:1218799917707821156> ",
    }

    embed = discord.Embed(title="Обновления", description="Все обновления которые произошли в игре:")

    for i, update in enumerate(updates, start=1):
        update_emoji = number_emojis[i % 10]  
        if i > 9:
            tens = i // 10
            ones = i % 10
            update_emoji = f"{number_emojis[tens]}{number_emojis[ones]}"  
        embed.add_field(name=f"Обновление {update_emoji}:", value=f"`{update[0]}`", inline=False) 

    await ctx.response.send_message(embed=embed)


@bot.slash_command()
async def info(ctx):
    view = CreatorsView()
    await ctx.response.send_message(
"""
**Создатели:**
1. <a:chipi:1218879261314912278> `Ggahramaq`<a:danceee:1218879327022743612>
2. <:shock:1217841430110666752>`Prosto S`<:shock:1217841430110666752>
3. <:firee:1217841342533861417>`Firecat`<:firee:1217841342533861417>
4. 🪐`Lucky.snake`🪐

**Подробнее о создателей ниже.**
"""
, view=view)





bot.run("pon!")
