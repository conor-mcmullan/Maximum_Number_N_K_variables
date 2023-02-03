# Maximum_Number_N_K_variables

## Goal
Return the maximum value possible given two integer variables N & K.
The idea is to extract the maximum value of K that can be treated as any "unit type" (hundreds, tens, units) when being added to any "unit type" of N.

## Assumptions
N & K are integer values.
Return type is Integer.
Return value will always be bigger than N if K > 0.
Not all of K remaining has to be used.
Larger K value does not always cause a substancly increase to N. 
K is more important to the increase in value than N.

## Limitations
N = [100...999]
K = [0...30]

## Example
N = 260
K = 10

Taking 2, 6, 0 from the N variable. 

2 Hundreds
6 Tens
0 Units

What needs to be done is apply what of K can make N reach max without going bust.

Of K 7 can be applied to 2, there remains 3, this can be applied to 6 this leaves K at 0 and therefore nothing gets added to 0. 

Result = 990
