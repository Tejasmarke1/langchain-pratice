from langchain_google_genai import ChatGoogleGenerativeAI as gemini
from pydantic import BaseModel, Field, conlist
from typing import Optional, Literal, List

from dotenv import load_dotenv

load_dotenv()

model=gemini(model="gemini-2.5-flash",temperature=0)


class ReviewModel(BaseModel):
    key_themes: List[str]=Field(description="write down all the key themes discussed in the review in a list")
    summary:str=Field(description="Provide a concise summary of the review in 2-3 sentences.")
    sentiment:Literal["positive","negative","neutral"]=Field(description="Determine the overall sentiment of the review as positive, negative, or neutral.")
    pros:Optional[List[str]]=Field(default=None,description="Write down all the pros inside a list")
    cons:Optional[List[str]]=Field(default=None,description="Write down all the cons inside a list")
    name:Optional[str]=Field(default=None,description="write down the name of the reviewer")
    

    
structured_output=model.with_structured_output(ReviewModel)
result=structured_output.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh""")


print(result)
print(result.summary)
print(result.sentiment)

