"""
Kaggle의 NLP competition EDA로 pandas, text data에 익숙해지기
- 링크 : https://www.kaggle.com/code/gunesevitan/nlp-with-disaster-tweets-eda-cleaning-and-bert

"""
# %%
import gc
import re
import string
import operator
from collections import defaultdict

import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import matplotlib.pyplot as plt
import seaborn as sns

import tokenization
from wordcloud import STOPWORDS

from sklearn.model_selection import StratifiedKFold, StratifiedShuffleSplit
from sklearn.metrics import precision_score, recall_score, f1_score

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.layers import Dense, Input, Dropout, GlobalAveragePooling1D
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, Callback

SEED = 1337

print('import done')

# %%
# reading files
df_train = pd.read_csv('../data/nlp-getting-started/train.csv', dtype={'id': np.int16, 'target': np.int8})
df_test = pd.read_csv('../data/nlp-getting-started/test.csv', dtype={'id': np.int16})

print('Training Set Shape = {}'.format(df_train.shape))
print('Training Set Memory Usage = {:.2f} MB'.format(df_train.memory_usage().sum() / 1024**2))
print('Test Set Shape = {}'.format(df_test.shape))
print('Test Set Memory Usage = {:.2f} MB'.format(df_test.memory_usage().sum() / 1024**2))


# %%
display(df_train.head())
print('test')
display(df_test.head())

# %%
print(df_train[missing_cols].isnull().sum().index)
print(df_train[missing_cols].isnull().sum().values)
# print(df_train['location'].isnull().sum())

# %%
## 1. Keyword and location

## 1.1 Missing Values

print(df_train['location'].isnull().sum())
print(df_train[df_train['keyword'].isnull()].count())

missing_cols = ['keyword', 'location']

fig, axes = plt.subplots(ncols=2, figsize=(17,4), dpi=100)

sns.barplot(x=df_train[missing_cols].isnull().sum().index, y=df_train[missing_cols].isnull().sum().values, ax=axes[0])
sns.barplot(x=df_test[missing_cols].isnull().sum().index, y=df_test[missing_cols].isnull().sum().values, ax=axes[1])

axes[0].set_ylabel('Missing Value Count', size=15, labelpad=20)
axes[0].tick_params(axis='x', labelsize=15)
axes[0].tick_params(axis='y', labelsize=15)
axes[1].tick_params(axis='x', labelsize=15)
axes[1].tick_params(axis='y', labelsize=15)

axes[0].set_title('Training Set', fontsize=13)
axes[1].set_title('Test Set', fontsize=13)

plt.show()

for df in [df_train, df_test]:
    for col in ['keyword', 'location']:
        df[col] = df[col].fillna(f'no_{col}')

# %%

## 1.2 Cardinality and Target Distribution
## 집합의 크기(Cardinality)
print(f'Number of unique values in keyword = {df_train["keyword"].nunique()} (Training) - {df_test["keyword"].nunique()} (Test)')
print(f'Number of unique values in location = {df_train["location"].nunique()} (Training) - {df_test["location"].nunique()} (Test)')


# %%
## 분포 확인(Target Distribution)
# hue를 추가하여 특정 데이터 별로 어떻게 다른지 확인 가능(카테고리형 범주여야 함. 갯수가 너무 많으면 안됨(하나의 값에 대해서 어떤 column이 어떤 값에 따라서 나뉘는 거임. 소수까지 되면 불가))
df_train['target_mean'] = df_train.groupby('keyword')['target'].transform('mean')

fig = plt.figure(figsize=(8, 72), dpi=100)

sns.countplot(y=df_train.sort_values(by='target_mean', ascending=False)['keyword'], hue=df_train.sort_values(by='target_mean', ascending=False)['target'])

plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=12)
plt.legend(loc=1)
plt.title('Target Distribution in Keywords')

plt.show()

df_train.drop(columns=['target_mean'], inplace=True)
# %%
## 2. Meta Features

## new column들을 추가하는 부분
## 기본적으로 text를 분석할 때, data science 에서는 통계적 특성을 파악하는 것이 필요함.
## 그러기 위해서 기본적으로 data들을 다양한 단위로 자르고 count 하는 과정이 필요한 듯

## word count
df_train['word_count'] = df_train['text'].apply(lambda x: len(str(x).split()))
df_test['word_count'] = df_train['text'].apply(lambda x: len(str(x).split()))

## unique_word_count
df_train['unique_word_count'] = df_train['text'].apply(lambda x: len(set(str(x).split())))
df_test['unique_word_count'] = df_test['text'].apply(lambda x: len(set(str(x).split())))

## stop_word_count
df_train['stop_word_count'] = df_train['text'].apply(lambda x:len([t for t in str(x).lower().split()if t in STOPWORDS]))
df_test['stop_word_count'] = df_test['text'].apply(lambda x:len([t for t in str(x).lower().split()if t in STOPWORDS]))

## url_count
df_train['url_count'] = df_train['text'].apply(lambda x:len([t for t in str(x).lower().split()if 'http' in t or 'https' in t]))
df_test['url_count'] = df_test['text'].apply(lambda x:len([t for t in str(x).lower().split()if 'http' in t or 'https' in t]))

## mean_word_length
df_train['mean_word_length']= df_train['text'].apply(lambda x: np.mean([len(t) for t in str(x).split()]))
df_test['mean_word_length']= df_test['text'].apply(lambda x: np.mean([len(t) for t in str(x).split()]))

## char_count
df_train['char_count'] = df_train['text'].apply(lambda x: len(str(x)))
df_test['char_count'] = df_test['text'].apply(lambda x: len(str(x)))

## punctuation_count
df_train['punctuation_count'] = df_train['text'].apply(lambda x: len([c for c in str(x) if c in string.punctuation]))
df_test['punctuation_count'] = df_test['text'].apply(lambda x: len([c for c in str(x) if c in string.punctuation]))

## hashtag_count
df_train['hashtag_count'] = df_train['text'].apply(lambda x: len([c for c in str(x) if c == '#']))
df_test['hashtag_count'] = df_test['text'].apply(lambda x: len([c for c in str(x) if c == '#']))

## mention_count
df_train['mention_count'] = df_train['text'].apply(lambda x: len([c for c in str(x) if c == '@']))
df_test['mention_count'] = df_test['text'].apply(lambda x: len([c for c in str(x) if c == '@']))

# %%
METAFEATURES = ['word_count', 'unique_word_count', 'stop_word_count', 'url_count', 'mean_word_length', 'char_count', 'punctuation_count', 'hashtag_count', 'mention_count']
DISASTER_TWEETS = df_train['target'] == 1

fig, axes = plt.subplots(ncols=2, nrows=len(METAFEATURES), figsize=(20,50), dpi=100) # ax를 통해 subplot에서의 위치를 정함

for i, feature in enumerate(METAFEATURES):
    sns.distplot(df_train.loc[~DISASTER_TWEETS][feature], label='Not Disaster', ax=axes[i][0], color='green') 
    sns.distplot(df_train.loc[DISASTER_TWEETS][feature], label='Disaster', ax=axes[i][0], color='red')

    sns.distplot(df_train[feature], label='Training', ax=axes[i][1])
    sns.distplot(df_test[feature], label='Test', ax=axes[i][1])

    for j in range(2):
        axes[i][j].set_xlabel('')
        axes[i][j].tick_params(axis='x', labelsize=12)
        axes[i][j].tick_params(axis='y', labelsize=12)
        axes[i][j].legend()

    axes[i][0].set_title(f'{feature} Target Distribution in Training Set', fontsize=13)
    axes[i][1].set_title(f'{feature} Training & Test Set Distribution', fontsize=13)

plt.show()

# %%

display(df_train['text'].head())
print(df_train['text'].apply(lambda x: len(str(x))).head())
print(df_test['text'].apply(lambda x: len(set(str(x).split()))).head())
print(df_train['text'].apply(lambda x:len([t for t in str(x).lower().split()if t in STOPWORDS])).head())
print(df_train['text'].apply(lambda x:len([t for t in str(x).lower().split()if 'http' in t or 'https' in t])).head())
print(df_train['text'].apply(lambda x: np.mean([len(t) for t in str(x).split()])).head())


# df_train.head()

# df_train.groupby('keyword')['target'].transform('mean').head()

# %%
