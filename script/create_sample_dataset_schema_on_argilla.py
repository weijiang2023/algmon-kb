import os
import argilla as rg

#print("step 0")
#set your variable here
#os.environ["ARGILLA_API_URL"] = "http://localhost:6900/"
#os.environ["ARGILLA_API_KEY"] = "admin.apikey"

print("step 1")
rg.init(
    api_url="http://localhost:6900/",
    api_key="admin.apikey",
    workspace="admin"
)

print("step2-1")
dataset = rg.FeedbackDataset(
    guidelines="Add some guidelines for the annotation team here.",
    fields=[
        rg.TextField(name="prompt", title="Human prompt"),
        rg.TextField(name="output", title="Generated output", use_markdown=True)
    ],
    questions =[
        rg.RatingQuestion(
            name="rating",
            title="Rate the quality of the response:",
            description="1 = very bad - 5= very good",
            required=True,
            values=[1,2,3,4,5]
        ),
        rg.TextQuestion(
            name="corrected-text",
            title="Provide a correction to the response:",
            required=False,
            use_markdown=True
        )
    ]
)
dataset.push_to_argilla(name="algmon_dataset_test_type_feedback", workspace="admin")

print("step2-2")
dataset2 = rg.FeedbackDataset(
    guidelines="Please, read the question carefully and try to answer it as accurately as possible.",
    fields=[
        rg.TextField(name="question"),
        rg.TextField(name="answer"),
    ],
    questions=[
        rg.RatingQuestion(
            name="answer_quality",
            description="How would you rate the quality of the answer?",
            values=[1, 2, 3, 4, 5],
        ),
        rg.TextQuestion(
            name="answer_correction",
            description="If you think the answer is not accurate, please, correct it.",
            required=False,
        ),
    ]
)
dataset2.push_to_argilla(name="algmon_dataset2_test_type_feedback", workspace="admin")