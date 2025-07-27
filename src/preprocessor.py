import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def preprocess(text: str) -> List[str]:
    """
    1. Lowercase
    2. Remove non-alpha
    3. Tokenize
    4. Remove stopwords & short tokens
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = word_tokenize(text)
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]