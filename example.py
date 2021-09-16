from pymon import pymon

pymon = pymon()

SearchId = 182774911

print({
    "Best Price: " + str(pymon.ItemBestPrice(SearchId)),
    "Recent Average Price: " + str(pymon.ItemRAP(SearchId)),
    "Value: " + str(pymon.ItemValue(SearchId)),
    "Demand: " + str(pymon.ItemDemand(SearchId)),
    "Total Copies: " + str(pymon.ItemTotalCopies(SearchId)),
    "Available Copies: " + str(pymon.ItemAvailableCopies(SearchId)),
    "Premium Copies: " + str(pymon.ItemPremiumCopies(SearchId)),
    "Deleted Copies: " + str(pymon.ItemDeletedCopies(SearchId)),
    "Owners: " + str(pymon.ItemOwnerCount(SearchId)),
    "Premium Owners: " + str(pymon.ItemPremiumOwnerCount(SearchId)),
    "Hoarded Copies: " + str(pymon.ItemHoardedCopies(SearchId)),
    "Percent Hoarded: " + str(pymon.ItemPercentHoarded(SearchId)),
})


