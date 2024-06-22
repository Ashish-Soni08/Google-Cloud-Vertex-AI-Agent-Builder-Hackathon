# Gemini-API-Developer-Competition

organised by [Google](https://ai.google.dev/competition)

```markdown
Lifestyle Bot (improves health/wellness)
```

## Inspiration

**Mental health** is a complex issue and addressing mental health demands the highest level of attention and care. Unlike many other health concerns, mental health issues often intertwine with various aspects of an individual's life, including their social environment, personal experiences, and genetic predispositions. Additionally, the stigma surrounding mental health further complicates the matter, hindering individuals from seeking help and society from providing adequate support systems.

The main **goal** of this project is to `provide a support system for an individuals's mental well-being.`

**Generative AI** has ushered in a new era for chatbots, providing them with capabilities to engage users in more natural conversations. **Generative AI** models also known as **LLMs(Large Language Models)** have given us the opportunity to offer more personalized and foster more engaging interactions. But deploying these **LLMs** in consumer applications poses several challenges, including the need to add guardrails that prevent the model from generating undesirable responses. For example, `in the context of building an AI for mental health, then you don't want it to generate toxic answers that bring more mental distress or teach people to engage in behaviors harmful to oneself.`

## What it does

```markown
Mental Wellness Companion

This bot fosters emotional well-being by generating personalized affirmations, guided meditations, and mindfulness exercises based on the user's mood and current needs. 

```

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


```bash
# Install the gcloud CLI - https://cloud.google.com/sdk/docs/install#linux

# Determine Linux version
getconf LONG_BIT
# Output -> 64, therefore chose Linux 64-bit(Arm)

# Download the Linux archive file
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-478.0.0-linux-arm.tar.gz

# Extract the contents of the file
tar -xf google-cloud-cli-478.0.0-linux-arm.tar.gz

# Add gcloud CLI to path
./google-cloud-sdk/install.sh 

# Then open a new terminal so that changes can take effect

# Initialize gcloud CLI
./google-cloud-sdk/bin/gcloud init
```

```bash
# remove the tar file
 rm -rf google-cloud-cli-478.0.0-linux-arm.tar.gz
```

```bash
# Get sample cloud functions - https://cloud.google.com/functions/docs/tutorials/http
git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
```

````bash
# Set a default region for functions -> https://cloud.google.com/functions/docs/locations
gcloud config set functions/region europe-west3
# Output -> Updated property [functions/region].
```


```bash
# Deploying the Cloud Function -> https://cloud.google.com/functions/docs/tutorials/http
gcloud functions deploy python-http-function \
--gen2 \
--runtime=python310 \
--source=. \
--entry-point=hello_get \ 
--trigger-http
--allow-unauthenticated

# Notes: 
# - source: path to the directory where the .py file exists with the function you want to deploy

# Retrieve your functions's URL -> https://cloud.google.com/functions/docs/calling/http#url
gcloud functions describe python-http-function \
--gen2 \
--region=europe-west3 \
--format="value(serviceConfig.uri)"
# Output -> https://europe-west3-gcp-lablab-ai-hackathon.cloudfunctions.net/python-http-function


# Delete the Cloud Function
gcloud functions delete python-http-function --gen2 --region europe-west3 
```
