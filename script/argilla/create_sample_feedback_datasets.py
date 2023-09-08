import argilla as rg

print("step 1 - login")
rg.init(
    api_url="http://localhost:6900/",
    api_key="admin.apikey",
    workspace="admin"
)

print("step2 - create dataset")
dataset = rg.FeedbackDataset(
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

# create a single Feedback Record
record = rg.FeedbackRecord(
    fields={
        "question": "Why can camels survive long without water?",
        "answer": "Camels use the fat in their humps to keep them filled with energy and hydration for long periods of time."
    },
    metadata={"source": "encyclopedia"},
    external_id=None
)
dataset.add_records(record)

print("step3 - push to the platform argilla")
remote_dataset = dataset.push_to_argilla(name="my-dataset_test_12", workspace="admin")