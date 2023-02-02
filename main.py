from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
import logging


logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)


@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultGif(
               id="Gif01",
               gif_url="https://media.giphy.com/media/5zkHGrgdd5Hu6DsYuj/giphy.gif",
               thumb_url="https://media.giphy.com/media/5zkHGrgdd5Hu6DsYuj/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif02",
               gif_url="https://media.giphy.com/media/I6n8YSKRIJqPwGll4n/giphy.gif",
               thumb_url="https://media.giphy.com/media/I6n8YSKRIJqPwGll4n/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif03",
               gif_url="https://media.giphy.com/media/cmIu5BPKV0PtMLmMxi/giphy.gif",
               thumb_url="https://media.giphy.com/media/cmIu5BPKV0PtMLmMxi/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif04",
               gif_url="https://media.giphy.com/media/CqHVEMYCED7oKQeE6K/giphy.gif",
               thumb_url="https://media.giphy.com/media/CqHVEMYCED7oKQeE6K/giphy.gif",
            ),
             types.InlineQueryResultGif(
               id="Gif05",
               gif_url="https://media.giphy.com/media/bcrOR2stk6tKIxqPOZ/giphy.gif",
               thumb_url="https://media.giphy.com/media/bcrOR2stk6tKIxqPOZ/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif06",
               gif_url="https://media.giphy.com/media/xL7PDV9frcudO/giphy.gif",
               thumb_url="https://media.giphy.com/media/xL7PDV9frcudO/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif07",
               gif_url="https://media.giphy.com/media/eoxomXXVL2S0E/giphy.gif",
               thumb_url="https://media.giphy.com/media/eoxomXXVL2S0E/giphy.gif",
            ),
             types.InlineQueryResultGif(
               id="Gif08",
               gif_url="https://media.giphy.com/media/dEdmW17JnZhiU/giphy.gif",
               thumb_url="https://media.giphy.com/media/dEdmW17JnZhiU/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif09",
               gif_url="https://media.giphy.com/media/pPhyAv5t9V8djyRFJH/giphy.gif",
               thumb_url="https://media.giphy.com/media/pPhyAv5t9V8djyRFJH/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif10",
               gif_url="https://media.giphy.com/media/xCRPMY7xfof3W/giphy.gif",
               thumb_url="https://media.giphy.com/media/xCRPMY7xfof3W/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif11",
               gif_url="https://media.giphy.com/media/IpKxfPy33hMRy/giphy.gif",
               thumb_url="https://media.giphy.com/media/IpKxfPy33hMRy/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif12",
               gif_url="https://media.giphy.com/media/Zq91mkPoj5e5PWpXNb/giphy.gif",
               thumb_url="https://media.giphy.com/media/Zq91mkPoj5e5PWpXNb/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif13",
               gif_url="https://media.giphy.com/media/d3mlE7uhX8KFgEmY/giphy.gif",
               thumb_url="https://media.giphy.com/media/d3mlE7uhX8KFgEmY/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif14",
               gif_url="https://media.giphy.com/media/GeimqsH0TLDt4tScGw/giphy.gif",
               thumb_url="https://media.giphy.com/media/GeimqsH0TLDt4tScGw/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif15",
               gif_url="https://media.giphy.com/media/l41lVsYDBC0UVQJCE/giphy.gif",
               thumb_url="https://media.giphy.com/media/l41lVsYDBC0UVQJCE/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif16",
               gif_url="https://media.giphy.com/media/S3Ot3hZ5bcy8o/giphy.gif",
               thumb_url="https://media.giphy.com/media/S3Ot3hZ5bcy8o/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif17",
               gif_url="https://media.giphy.com/media/cF7QqO5DYdft6/giphy.gif",
               thumb_url="https://media.giphy.com/media/cF7QqO5DYdft6/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif18",
               gif_url="https://media.giphy.com/media/wcjtdRkYDK0sU/giphy.gif",
               thumb_url="https://media.giphy.com/media/wcjtdRkYDK0sU/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif19",
               gif_url="https://media.giphy.com/media/kFT7uQIOOUjNHWwhQV/giphy.gif",
               thumb_url="https://media.giphy.com/media/kFT7uQIOOUjNHWwhQV/giphy.gif",
            ),
            types.InlineQueryResultGif(
               id="Gif20",
               gif_url="https://media.giphy.com/media/yJFeycRK2DB4c/giphy.gif",
               thumb_url="https://media.giphy.com/media/yJFeycRK2DB4c/giphy.gif",
            ),


        ]
    )






executor.start_polling(dp, skip_updates=True)