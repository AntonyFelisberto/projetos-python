import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, ConceptsOptions, RelationsOptions, EmotionOptions, EntitiesOptions, SentimentOptions,SemanticRolesOptions

natural_language_understanding_v1 = NaturalLanguageUnderstandingV1(
    username="",
    password="",
    version=""
)

response = natural_language_understanding_v1.analize(
    text="who is the president of brazil",
    features=Features(
        concepts=ConceptsOptions(),
        emotion=EmotionOptions(),
        entities=EntitiesOptions(),
        sentiment=SentimentOptions()
    )
)
print(json.dumps(response,indent=2))

response = natural_language_understanding_v1.analize(
    text="who is the president of brazil",
    features=Features(
        relations=RelationsOptions(),
        concepts=ConceptsOptions(),
        emotion=EmotionOptions(),
        entities=EntitiesOptions(),
        semantic_roles=SemanticRolesOptions(),
        sentiment=SentimentOptions()
    )
)
print(json.dumps(response,indent=2))