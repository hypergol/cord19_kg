# Cord19Kg

The goal of this project is to create a knowledge graph of medical entities and phrases and create an embedding for it with node2vec using gensim's word2vec/corpus_file facility. I will heavily use [Sujit Pal](https://github.com/sujitpal)'s previous work.

Information on the data 

-   [https://github.com/allenai/cord19](https://github.com/allenai/cord19)
-   [https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html)
-   [https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/discussion/137474](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/discussion/137474)
-   [https://github.com/sujitpal/saturn-scispacy/tree/master/notebooks/full](https://github.com/sujitpal/saturn-scispacy/tree/master/notebooks/full)
-   [https://registry.opendata.aws/cord-19/](https://registry.opendata.aws/cord-19/)
-   [https://github.com/allenai/cord19](https://github.com/allenai/cord19)

Hypergol commands used to generate code:

```
python -m hypergol.cli.create_project Cord19Kg
python -m hypergol.cli.create_data_model RawMetadata cordUid:str:id sha:str sourceX:List[str] title:str doi:str pmcid:str pubmedId:str license:str abstract:str publishTime:str authors:str journal:str magId:str whoCovidenceId:str arxivId:str pdfJsonFiles:str pmcJsonFiles:str url:str s2Id:str
python -m hypergol.cli.create_data_model RawData cordUid:str:id "data:List[str]" rawMetadata:RawMetadata

python3 -m hypergol.cli.create_task CreateRawMetadata --source
python3 -m hypergol.cli.create_task CreateRawData RawMetadata RawData
python3 -m hypergol.cli.create_pipeline CreateSchema CreateMetadata CreateSchema RawMetadata RawData
```

Generated datamodel (from the JSONs with Genson):

```
x python -m hypergol.cli.create_data_model Location postCode:str settlement:str region:str country:str addrLine:str postBox:str --force
x python -m hypergol.cli.create_data_model Affiliation laboratory:str institution:str location:Location --force
x python -m hypergol.cli.create_data_model Author first:str "middle:List[str]" last:str suffix:str affiliation:Affiliation email:str --force
x python -m hypergol.cli.create_data_model Metadata title:str "authors:List[Author]" --force

x python -m hypergol.cli.create_data_model CiteSpan start:int end:int text:str "refId:List[str]" --force
x python -m hypergol.cli.create_data_model RefSpan start:int end:int text:str "refId:List[str]" --force

x python -m hypergol.cli.create_data_model Abstract text:str "citeSpans:List[CiteSpan]" "refSpans:List[RefSpan]" section:str --force
x python -m hypergol.cli.create_data_model BodyText text:str "citeSpans:List[CiteSpan]" "refSpans:List[RefSpan]" section:str --force
x python -m hypergol.cli.create_data_model BackMatter text:str "citeSpans:List[CiteSpan]" "refSpans:List[RefSpan]" section:str --force

x python -m hypergol.cli.create_data_model OtherId "DOI:List[str]" "arXiv:List[str]" "PMID:List[str]" "PMCID:List[str]" --force
x python -m hypergol.cli.create_data_model BibEntry refId:str title:str "authors:List[Author]" "year:List[int]" venue:str volume:str issn:str pages:str otherIds:OtherId bibEntryId:str --force
x python -m hypergol.cli.create_data_model RefEntry text:str latex:null type:str refEntryId:str html:str --force

x python -m hypergol.cli.create_data_model Article paperId:str metadata:Metadata "abstract:List[Abstract]" "bodyText:List[BodyText]" "bibEntries:List[BibEntry]" "refEntries:List[RefEntry]" "backMatter:List[BackMatter]" --force
```

Actual datamodel 

```
python -m hypergol.cli.create_data_model Article articleId:str:id paperId:str title:str "authors:List[str]" "DOI:List[str]" "arXiv:List[str]" "PMID:List[str]" "PMCID:List[str]" "year:List[int]" --force
python -m hypergol.cli.create_data_model Paragraph articleId:str:id paragraphId:int:id text:str citations:List[str] --force
python -m hypergol.cli.create_data_model ArticleText articleId:str:id article:Article "paragraphs:List[Paragraph]" --force
python -m hypergol.cli.create_data_model Document documentId:int:id "tokens:List[str]" "labels:List[str]" --force
```


Download the data from AI2 (check their site above for the latest version):

```
wget https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases/cord-19_2020-12-13.tar.gz
tar -zxvf cord-19_2020-12-13.tar.gz 
tar -zxvf document_parses.tar.gz
```

This project was generated with the Hypergol framework

Please see documentation for instructions: [https://hypergol.readthedocs.io/en/latest/](https://hypergol.readthedocs.io/en/latest/)

### Initialise git

Hypergol is heavily integrated with git, all projects must be in a git repository to ensure code and data lineage (to record which data was created by which version of the code).

Initialise git with:

```git init .```

Create the first commit (datasets record the last commit when they are created and without this there is nothing to record):

```git commit -m "First Commit!"```

The project now (and any time a file is changed but the change is not committed to the repo) is in a "dirty" stage. If you run a pipeline or train a model, the last commit will be recorded but that commit will not represent the code that is running! Add changes and commit:

```
git add .
git commit -m "All the files!"
```

If there are files that shouldn't be checked in ever to git they should be to the `.gitignore` file before `git add .`

Alternatively individual files can be added to git with `git add <filename>`.

### Make the virtual environment

Having dedicated virtual environment fully described by the projects `requirements.txt` is the recommended practice. Don't forget to `deactivate` the current virtual environment! Files from the environment are included in the projects `.gitignore` file and will ignored by git.

```
deactivate
./make_venv.sh
source .venv/bin/activate
```


### How to list existing Datasets (in Jupyter)

```
from hypergol import HypergolProject
project = HypergolProject(
    projectDirectory='<project_directory>/cord19_kg',
    dataDirectory='<data_directory>'
)
project.list_datasets(pattern='.*', asCode=True);
```

This will list all existing datasets that matches `pattern` as self contained executable code.


### How to start Tensorboard

It is recommended to start it in a screen session (`screen -S tensorboard`) so you can close the terminal window or if you disconnect from a remote Linux machine (reconnect with `screen -x tensorboard`). In the project directory:

```
screen -S tensorboard
source .venv/bin/activate
tensorboard --logdir=<data_directory>/cord19_kg/tensorboard/
```


### How to train your model

After implementing all components and required functions:

```
./train_cord19_kg.sh
```

This will execute the model manager's run() function with the prescribed schedule (training steps, evaluation steps, etc.). Training can be stopped with Ctrl-C, this will won't result in the corruption of the output dataset (datasets must be closed properly to generate their chk file after they are read only). This is possible because the entire training happen in a `try/finally` block.

### How to serve your model

In the generated `models/serve_cord19_kg.py` function specify the directory of the model to be served at:

```
MODEL_DIRECTORY = '<data_directory>/cord19_kg/<branch>/models/<ModelName>/<epoch_number>'
```

then start serving with (port and host can be set in the shell script):

```
./serve_cord19_kg.sh
```


### How to call your model from python with requests

```
import requests
response = json.loads(requests.get('http://0.0.0.0:8000', headers={'accept': 'application/json'}).text)
modelLongName = response['model']
```

This allows to verify if indeed the intended model is served. The generated training script sets training day and the commit hash at that point to be part of the long name and to ensure that the exact conditions of training are available at serving. Long name should be used in logging to identify which model created an output. From v0.0.10 the long name is returned in the header of the response of `/output` endpoint as well in the `x-model-long-name` field.

To get the response of the model to a list of objects, see example below. Replace `ExampleOutput` with the correct output type and load a dataset into `ds`, use `list_datasets` from above to do this.

```
sys.path.insert(0, '<project_directory>/cord19_kg')
import requests
from itertools import islice

from data_models.example_output import ExampleOutput


with ds.open('r') as dsr:
    values = [value.to_data() for value in islice(dsr, 10)]


response = requests.post(
    'http://0.0.0.0:8000/output',
    headers={
        'accept': 'application/json',
        'Content-Type': 'application/json',
    },
    data=json.dumps(values)
)
outputs = [ExampleOutput.from_data(v) for v in json.loads(response.text)]
modelLongName = response.headers['x-model-long-name']
```

It is not recommended to do large scale evaluation through the API as the overhead per object is too high and it is single threaded.
