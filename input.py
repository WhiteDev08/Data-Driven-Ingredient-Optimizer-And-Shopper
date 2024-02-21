from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
def ip1():
    llm = ChatOpenAI(openai_api_key="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")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class technical documentation writer."),
        ("user", "{input}")
    ])
    chain = prompt |llm
    ip1= ": for the dish given below , give me all ingredients one by one only with the name without giving options or any other unnecessary detail only with the ingredient name one by one seperated by comma in a single line. give me in the format of Sure, here are the ingredients for the dish:"
    user_ip=input()
    ingredients = chain.invoke({"input": user_ip+ip1}).content
    #print(ingredients)
    ingredients_1 = ingredients.split(':', 1)[-1].strip()
    lst = ingredients_1.split(',')
    return lst
