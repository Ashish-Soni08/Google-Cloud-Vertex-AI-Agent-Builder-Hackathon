# Google-Cloud-Vertex-AI-Agent-Builder-Hackathon

organized by [GOOGLE AND DEVPOST](https://googlevertexai.devpost.com/).

Built a no/low-code conversational AI agent using [Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder?hl=en) that falls into the following category:

  ```markdown
Lifestyle Bot (improves health/wellness)
  ```

## Inspiration

**Mental health** is a complex issue and addressing mental health demands the highest level of attention and care. Unlike many other health concerns, mental health issues often intertwine with various aspects of an individual's life, including their social environment, personal experiences, and genetic predispositions. Additionally, the stigma surrounding mental health further complicates the matter, hindering individuals from seeking help and society from providing adequate support systems.

The main **goal** of this project is to `provide a support system for an individuals's mental well-being.`

**Generative AI** has ushered in a new era for chatbots, providing them with capabilities to engage users in more natural conversations. **Generative AI** models also known as **LLMs(Large Language Models)** have given us the opportunity to offer more personalized and foster more engaging interactions. But deploying these **LLMs** in consumer applications poses several challenges, including the need to add guardrails that prevent the model from generating undesirable responses. For example, `in the context of building an AI for mental health, then you don't want it to generate toxic answers that bring more mental distress or teach people to engage in behaviors harmful to oneself.`

## What it does

## How we built it

## Challenges we ran into

## Accomplishments that we're proud of

## What we learned

## Environment Setup

```bash
python -V
# Output -> Python 3.10.13
```

```bash
# create a environment named -> .wellness-ai-agent
python -m venv .wellness-ai-agent
```

```bash
# activate the environment
source .wellness-ai-agent/bin/activate
```

```bash
# Install packages to create a Jupyter Notebook kernel
pip install jupyter ipykernel
```

```bash
# add your virtual environment as a kernel
python -m ipykernel install --user --name=wellness-ai-agent --display-name="Py3.10-wellness-ai-agent"
```

```bash
# verify kernel installation
jupyter kernelspec list
```