> # `pymon` - [Rolimons](https://www.rolimons.com/) API Wrapper

## Description
This module allows you to fetch Item data, Example: RAP, Value, Graphs, ETC. `pymon` interacts with the websites private API to extract data.

## Table Of Contents
- [Items](#items)
    - [ItemBestPrice](#itembestprice)
    - [ItemRAP](#itemrap)
    - [ItemValue](#itemvalue)
    - [ItemDemand](#itemdemand)
    - [ItemTotalCopies](#itemtotalcopies)
    - [ItemAvailableCopies](#itemavailablecopies)
    - [ItemPremiumCopies](#itempremiumcopies)
    - [ItemDeletedCopies](#itemdeletedcopies)
    - [ItemOwnerCount](#itemownercount)
    - [ItemPremiumOwnerCount](#itempremiumownercount)
    - [ItemHoardedCopies](#itemhoardedcopies)
    - [ItemPercentHoarded](#itempercenthoarded)
- [Players](#players)
    - [PlayerAssets](#playerassets)    


## Installation

To pip install `pymon` from github:

```bash
pip install git+https://github.com/workframes/pymon.git
```
or
```bash
pip3 install git+https://github.com/workframes/pymon.git
```

> ## **Items**
### ItemBestPrice

```py
from pymon import pymon
pymon = pymon()

pymon.ItemBestPrice(ItemID)
```
### ItemRAP

```py
from pymon import pymon
pymon = pymon()

pymon.ItemRAP(ItemID)
```
### ItemValue

```py
from pymon import pymon
pymon = pymon()

pymon.ItemValue(ItemID)
```
### ItemDemand

```py
from pymon import pymon
pymon = pymon()

pymon.ItemDemand(ItemID)
```
### ItemTotalCopies

```py
from pymon import pymon
pymon = pymon()

pymon.ItemTotalCopies(ItemID)
```
### ItemAvailableCopies

```py
from pymon import pymon
pymon = pymon()

pymon.ItemAvailableCopies(ItemID)
```
### ItemPremiumCopies

```py
from pymon import pymon
pymon = pymon()

pymon.ItemPremiumCopies(ItemID)
```
### ItemDeletedCopies

```py
from pymon import pymon
pymon = pymon()

pymon.ItemDeletedCopies(ItemID)
```
### ItemOwnerCount

```py
from pymon import pymon
pymon = pymon()

pymon.ItemOwnerCount(ItemID)
```
### ItemPremiumOwnerCount

```py
from pymon import pymon
pymon = pymon()

pymon.ItemPremiumOwnerCount(ItemID)
```
### ItemHoardedCopies

```py
from pymon import pymon
pymon = pymon()

pymon.ItemHoardedCopies(ItemID)
```
### ItemPercentHoarded

```py
from pymon import pymon
pymon = pymon()

pymon.ItemPercentHoarded(ItemID)
```
> ## **Players**
### PlayerAssets

```py
from pymon import pymon
pymon = pymon()

print(pymon.PlayerAssets(UserId))
```
