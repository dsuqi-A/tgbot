from bot import logger, safone_api

class Safone:
    async def safone_ai(msg):
        chatgpt_res = None
        bard_res = None
        chatbot_res = None
        try:
            chatgpt_res = await safone_api.chatgpt(msg)
        except Exception as e:
            logger.error(f"Error ChatGPT: {e}")
            try:
                bard_res = await safone_api.bard(msg)
            except Exception as e:
                logger.error(f"Error Bard: {e}")
                try:
                    chatbot_res = await safone_api.chatbot(msg)
                except Exception as e:
                    logger.error(f"Error Chatbot: {e}")
        return chatgpt_res, bard_res, chatbot_res


    async def webshot(url):
        try:
            res = await safone_api.webshot(url)
            return res
        except Exception as e:
            logger.error(f"Error Webshot: {e}")


    async def imagine(prompt):
        try:
            res = await safone_api.imagine(prompt)
            res = res[0]
            return res
        except Exception as e:
            logger.error(f"Error imagine: {e}")

            
