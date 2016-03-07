# VNIXSPQR
Displays Unix time - in Roman numerals. Readably.

If this was done in the usual fashion, a Unix timestamp would be about 1.4 million Ms and then a few other numerals.

This would obviously not be useful or readable.

Solution: Break the timestamp into triads, zero padded at the left. This not only allows the epoch to stand alone, it has the useful property of making sure that we do not have to deal with four digit Arabic numbers (since traditional Roman numerals lack the ability to express numbers greater than 4999 without repeating M a lot). So:
  * Unix: (00)1 457 379 747
  * VNIX: I·CDLVII·CCCLXXX·CCXVIII

The NVMERVMROMANVMSVM function, which converts an Arabic number to Roman numerals, is fully general and should do the M thing as above if it is fed anything large, but it is implemented naively from scratch so I have no idea if the algorithm is in any way optimal. I'm not exactly displeased with it, though, and it was fun to write.

The source code is as Latinate as I am able to make it within the frameworks of Python. Yes, this is silly, but if you're reading the source code for this and you were somehow still under the impression that anything about it was not silly, well, perhaps you should go have a beer with Pontius Pilate and his very good friend Biggus Dickus.
