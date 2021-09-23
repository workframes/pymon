from pymon import pymon
import json

pymon = pymon()

SearchId = 1029025
UserId = 674068579

print(pymon.IdToName(SearchId))
print(pymon.ItemBestPrice(SearchId))
print(pymon.ItemRAP(SearchId))
print(pymon.ItemValue(SearchId))
print(pymon.LimitedCatalog("NAME"))
print(pymon.LimitedCatalog("ID"))
print(pymon.ItemDemand(SearchId))
print(pymon.ItemAcronym(SearchId))
print(pymon.ItemTrend(SearchId))
print(pymon.ItemProjectedCheck(SearchId))
print(pymon.LimitedCount())
print(pymon.ItemTotalCopies(SearchId))
print(pymon.ItemAvailableCopies(SearchId))
print(pymon.ItemPremiumCopies(SearchId))
print(pymon.ItemDeletedCopies(SearchId))
print(pymon.ItemOwnerCount(SearchId))
print(pymon.ItemPremiumOwnerCount(SearchId))
print(pymon.ItemHoardedCopies(SearchId))
print(pymon.ItemPercentHoarded(SearchId))
