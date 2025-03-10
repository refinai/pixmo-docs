from datadreamer import DataDreamer
from datadreamer.llms import OpenAI
from datadreamer.steps import (
    Prompt,
    DataSource,
    DataFromAttributedPrompt,
)

with DataDreamer("./output"):
    # Load GPT-4
    gpt_4 = OpenAI(model_name="gpt-4")

    # Create prompts to generate attributes for movie reviews
    attribute_generation_prompts = DataSource(
        "Attribute Generation Prompts",
        data={
            "prompts": [
                "Generate the names of 10 movies released in theatres in the past, in a comma separated list.",
                "Generate 10 elements of a movie a reviewer might consider, in a comma separated list.",
                "Generate 10 adjectives that could describe a movie reviewer's style, in a comma separated list.",
            ],
        },
    )

    # Generate the attributes for movie reviews
    attributes = Prompt(
        "Generate Attributes",
        inputs={
            "prompts": attribute_generation_prompts.output["prompts"],
        },
        args={
            "llm": gpt_4,
        },
    ).output["generations"]

    # Generate movie reviews with varied attributes
    movie_reviews = (
        DataFromAttributedPrompt(
            "Generate Movie Reviews",
            args={
                "llm": gpt_4,
                "n": 1,
                "instruction": "Generate a few sentence {review_style} movie review about {movie_name} that focuses on {movie_element}.",
                "attributes": {
                    "movie_name": attributes[0].split(","),
                    "movie_element": attributes[1].split(","),
                    "review_style": attributes[2].split(","),
                },
            },
            outputs={"generations": "reviews"},
        )
        .select_columns(["reviews"])
        .shuffle()
    )

    movie_reviews.publish_to_hf_hub(
        "refine-ai/test",
    )