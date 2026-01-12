from pydantic import BaseModel, Field

class ReviewModel(BaseModel):
    summary: str = Field(..., description="Provide a concise summary of the review in 2-3 sentences.")
    sentiment: str = Field(..., description="Determine the overall sentiment of the review as positive, negative, or neutral.")
    key_themes: list[str] = Field(..., description="Write down all the key themes discussed in the review in a list")
    pros: list[str] | None = Field(None, description="Write down all the pros inside a list")
    cons: list[str] | None = Field(None, description="Write down all the cons inside a list")
    name: str = Field(..., description="Write down the name of the reviewer")
    

review=ReviewModel(summary="I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.",
                   sentiment="positive",key_themes=["Powerful processor", "Long battery life", "Fast charging", "S-Pen integration", "200MP camera"],
                   pros=["Insanely powerful processor (great for gaming and productivity)", "Stunning 200MP camera with incredible zoom capabilities", "Long battery life with fast charging", "S-Pen support is unique and useful"],
                   cons=["Weight and size make it a bit uncomfortable for one-handed use", "Samsung’s One UI comes with bloatware", "$1,300 price tag is high"],
                   name="Nitish Singh");

print(review.model_dump_json(indent=4))
